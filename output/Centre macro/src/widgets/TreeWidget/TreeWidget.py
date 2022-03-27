from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TreeWidget.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            bg_header=Rgb().th3(),
            fg_header=Rgb().th1(),
        )
    def tr(self):
        bd_item = (0, 0, 0, 2)

        Build(
            *self.wgs,

            scroll_h=Scroll().off(),
            scroll_v=Scroll().off(),

            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().bn1(),

            border_item=bd_item,
            border_item_hover=bd_item,
            border_item_checked=bd_item,
            border_item_checked_hover=bd_item,
            border_item_rgb=Rgb().th2(),
            border_item_hover_rgb=Rgb().th3(),
            border_item_checked_rgb=Rgb().bn1(),
            border_item_checked_hover_rgb=Rgb().bn1(),

            radius_item=(0,) * 4
        )
    def option(self):
        bd_gen = (0, 0, 2, 0)
        bd_item = (0, 0, 0, 2)

        Build(
            *self.wgs,

            width=Dim().h5(),

            scroll_h=Scroll().off(),
            scroll_v=Scroll().off(),

            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().tr(),
            bg_item_checked_hover=Rgb().tr(),
            bg_header=Rgb().th1(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().bn1(),
            fg_header=Rgb().th1(),

            border=bd_gen,
            border_hover=bd_gen,
            border_rgb=Rgb().th2(),
            border_hover_rgb=Rgb().th2(),
            border_item=bd_item,
            border_item_hover=bd_item,
            border_item_checked=bd_item,
            border_item_checked_hover=bd_item,
            border_item_rgb=Rgb().th2(),
            border_item_hover_rgb=Rgb().th3(),
            border_item_checked_rgb=Rgb().bn1(),
            border_item_checked_hover_rgb=Rgb().bn1(),

            radius_item=(0,) * 4
        )
