from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.CheckBox.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs, margin=(0, 0, 0, (vb_wg.HEIGHT-(vb_wg.HEIGHT*StyleBase().x_ico()))/2)):
        self.wgs = wgs
        self.margin = margin

    def th(self):
        Build(
            *self.wgs,

            img_margin=self.margin,
        )
    def tr(self, bg=Rgb().tr(), fg=Rgb().th3()):
        Build(
            *self.wgs,

            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_indeterminate=bg,
            bg_indeterminate_hover=bg,
            fg=fg,
            fg_checked=fg,
            fg_indeterminate=fg,
            fg_indeterminate_hover=Rgb().th2(),

            img_indeterminate_rgb="th3",
            img_indeterminate_hover_rgb="th2",
            img_margin=self.margin,
        )
