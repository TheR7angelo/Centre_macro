from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TextEdit.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            height=Dim().h6(),

            scroll_handle_bg=Rgb().th2(),
            scroll_handle_bg_hover=Rgb().th2(),
            scroll_handle_fg=Rgb().bn1(),
            scroll_handle_fg_hover=Rgb().bn1(),

            bg=Rgb().th2(),
            fg=Rgb().th3(),

            border=(StyleBase().border(),)* 4,
            border_hover=(StyleBase().border(),)* 4,
            border_rgb=Rgb().th1(),
            border_hover_rgb=Rgb().th1(),
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb().tr(),
            fg=Rgb().th3()
        )
