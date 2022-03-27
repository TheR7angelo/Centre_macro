from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ScrollArea.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self, bg=Rgb().th3()):
        Build(
            *self.wgs,

            bg=bg,
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb().tr()
        )
