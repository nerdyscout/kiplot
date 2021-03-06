"""
Tests of SVG format.

For debug information use:
pytest-3 --log-cli-level debug
"""

import os
import sys
# Look for the 'utils' module from where the script is running
prev_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if prev_dir not in sys.path:
    sys.path.insert(0, prev_dir)
# Utils import
from utils import context


PS_DIR = 'SVG'


def test_svg():
    prj = 'simple_2layer'
    ctx = context.TestContext('test_svg', prj, 'svg', PS_DIR)
    ctx.run()

    f_cu = ctx.get_gerber_filename('F_Cu', '.svg')
    f_fab = ctx.get_gerber_filename('F_Fab', '.svg')
    ctx.expect_out_file(f_cu)
    ctx.expect_out_file(f_fab)
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()


def test_svg_all():
    prj = 'simple_2layer'
    ctx = context.TestContext('test_svg_all', prj, 'svg_all', PS_DIR)
    ctx.run()

    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()


def test_svg_selected():
    prj = 'simple_2layer'
    ctx = context.TestContext('test_svg_selected', prj, 'svg_selected', PS_DIR)
    ctx.run()

    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()


def test_svg_copper_and_user():
    prj = 'good-project'
    ctx = context.TestContext('test_svg_copper_and_user', prj, 'svg_copper_and_user', PS_DIR)
    ctx.run()

    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()


def test_svg_copper_and_draw():
    prj = 'good-project'
    ctx = context.TestContext('test_svg_copper_and_draw', prj, 'svg_copper_and_draw', PS_DIR)
    ctx.run()

    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    # This name is selected manually:
    ctx.expect_out_file(ctx.get_gerber_filename('Dwgs_User', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()


def test_svg_copper_and_cmt():
    prj = 'good-project'
    ctx = context.TestContext('SVGCopperCmt', prj, 'svg_copper_and_cmt', PS_DIR)
    ctx.run()

    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()


def test_svg_anchor():
    prj = 'good-project'
    ctx = context.TestContext('test_svg_anchor', prj, 'svg_anchor', PS_DIR)
    ctx.run(extra=['SVG'])

    assert ctx.search_err(r"- 'SVG files' \(SVG\) \[svg\]")
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()


def test_svg_technical():
    prj = 'good-project'
    ctx = context.TestContext('test_svg_technical', prj, 'svg_technical', PS_DIR)
    ctx.run()

    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()
