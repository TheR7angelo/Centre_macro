from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ComboBox.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
            bg=Rgb().th2(),
            bg_hover=Rgb().th2(),
            fg=Rgb().th3(),

            border=(StyleBase().border(),)*4,
            border_hover=(StyleBase().border(),)*4,
            border_rgb=Rgb().th1(),
            border_hover_rgb=Rgb().th1(),

            img_rgb="th3"

        )
    def tr(self):
        Build(
            *self.wgs,

            edit=True,
            cursor=Cur().souris_main(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_selection=Rgb().th3(),
            fg=Rgb().th3(),
            fg_selection=Rgb().th1(),
        )
    def font(self, font=vb_wg.FONT):
        Build(
            *self.wgs,
            font=font
        )
