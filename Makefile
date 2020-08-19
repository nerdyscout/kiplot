#!/usr/bin/make
PY_COV=python3-coverage
PYTEST=pytest-3
REFDIR=tests/reference/
REFILL=tests/board_samples/zone-refill.kicad_pcb
CWD := $(abspath $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST))))))
USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)

ifneq ("$(wildcard *.yaml)","")
$(error Move away any config file)
endif

ifneq ("$(wildcard *.sch)","")
$(error Move away any schematic file)
endif

ifneq ("$(wildcard tests/board_samples/bom.xml-bak*)","")
$(error Revert tests/board_samples/bom.xml-bak)
endif

deb:
	perl debian/make_postinst.pl > debian/postinst
	chmod +x debian/postinst
	fakeroot dpkg-buildpackage -uc -b

lint: doc
	# flake8 --filename is broken
	ln -sf src/kiplot kiplot.py
	ln -sf src/kibot kibot.py
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --statistics
	rm kiplot.py
	rm kibot.py

test_tmp: lint
	$(PY_COV) erase
	$(PYTEST)
	$(PY_COV) report

test: lint
	rm -rf output
	rm -f example.kiplot.yaml
	rm -f example.kibot.yaml
	$(PY_COV) erase
	$(PYTEST) --test_dir output
	$(PY_COV) report
	$(PY_COV) html
	x-www-browser htmlcov/index.html

test_docker_local:
	rm -rf output
	$(PY_COV) erase
	# Run in the same directory to make the __pycache__ valid
	# Also change the owner of the files to the current user (we run as root like in GitHub)
	docker run --rm -v $(CWD):$(CWD) --workdir="$(CWD)" setsoft/kicad_auto_test:latest \
		/bin/bash -c "flake8 . --count --statistics ; pytest-3 --test_dir output ; chown -R $(USER_ID):$(GROUP_ID) output/ tests/board_samples/"
	$(PY_COV) report
	$(PY_COV) html
	x-www-browser htmlcov/index.html

docker_shell:
	docker run  -it --rm -v $(CWD):$(CWD) --workdir="$(CWD)" \
	-v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$(DISPLAY) \
	--user $(USER_ID):$(GROUP_ID) \
	--volume="/etc/group:/etc/group:ro" \
	--volume="/etc/passwd:/etc/passwd:ro" \
	--volume="/etc/shadow:/etc/shadow:ro" \
	--volume="/home/$(USER):/home/$(USER):rw" \
	setsoft/kicad_auto_test:latest /bin/bash

single_test:
	rm -rf pp
	-$(PYTEST) --log-cli-level debug -k "$(SINGLE_TEST)" --test_dir pp
	@echo "********************" Output
	@cat pp/*/output.txt
	@echo "********************" Error
	@cat pp/*/error.txt
	@rm -f tests/input_samples/bom.ini

single_tests:
	rm -rf pp
	# 12 threads, for a 6 core CPU w/HT. Almost 4 times faster for BoM tests.
	-$(PYTEST) -n 12 --log-cli-level debug -k "$(SINGLE_TEST)" --test_dir pp
	@rm -f tests/input_samples/bom.ini

deb_clean:
	fakeroot debian/rules clean

gen_ref:
	# Reference outputs, must be manually inspected if regenerated
	cp -a $(REFILL).refill $(REFILL)
	src/kibot -c tests/yaml_samples/pdf_zone-refill.kibot.yaml -b tests/board_samples/zone-refill.kicad_pcb -d $(REFDIR)
	src/kibot -c tests/yaml_samples/print_pcb_zone-refill.kibot.yaml -b tests/board_samples/zone-refill.kicad_pcb -d $(REFDIR)
	cp -a $(REFILL).ok $(REFILL)

doc:
	make -C docs

py_build:
	python3 setup.py sdist bdist_wheel

pypi_upload: py_clean py_build
	python3 -m twine upload dist/*

py_clean:
	@rm -rf .pybuild build dist kibot.egg-info

.PHONY: deb deb_clean lint test test_local gen_ref doc py_build pypi_upload py_clean
