from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TableWidget.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            bg_corner=Rgb().th1(),

            border=(StyleBase().border(),) * 4,
            border_rgb=Rgb().th3(),
        )
    def tr(self):
        Build(
            *self.wgs,

            header_h=False,
            header_v=False,

            bg_corner=Rgb().th1(),
            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().th3(),
            bg_item_checked_hover=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().th1(),
        )
