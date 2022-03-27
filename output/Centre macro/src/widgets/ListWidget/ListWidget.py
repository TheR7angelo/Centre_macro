from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ListWidget.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            fg_item_checked=Rgb().bn1(),

            border=(StyleBase().border(),)*4,
            border_rgb=Rgb().th3()
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().bn1(),

            radius_item=(0,)*4
        )

class Test:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
            border=(0, 0, 2, 0),
            border_hover=(0, 0, 2, 0),
            border_rgb=Rgb().th2(),
            border_hover_rgb=Rgb().th2(),

            width=Dim().h5(),
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
            fg_item=Rgb().th1(),
            fg_item_checked=Rgb().bn1(),

            width=Dim().h5(),
            radius_item=(0,)*4
        )
