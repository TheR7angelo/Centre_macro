from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.DateEdit.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs, margin=((vb_wg.HEIGHT - vb_wg.IMG_HEIGHT) / 2, 0, (vb_wg.HEIGHT - vb_wg.IMG_HEIGHT) / 2, 0)):
        self.wgs = wgs
        self.margin = margin

    def th(self):
        Build(
            *self.wgs,

            img=Img().calendrier(),
            img_hover=Img().calendrier(),
            img_rgb="",
            img_hover_rgb="",
            img_margin=self.margin,
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_selection=Rgb().th3(),
            fg=Rgb().th3(),
            fg_selection=Rgb().th1(),

            img=Img().calendrier(),
            img_hover=Img().calendrier(),
            img_rgb="",
            img_hover_rgb="",
            img_margin=self.margin,
        )
