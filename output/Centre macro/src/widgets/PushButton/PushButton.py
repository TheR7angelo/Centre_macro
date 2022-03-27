from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.PushButton.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
            width=Dim().h6(),

            border=(StyleBase().border(),)*4,
            border_rgb=Rgb().th2(),

            border_hover=(2,) * 4,
            border_hover_rgb=Rgb().th2()
        )
    def th2(self):
        Build(
            *self.wgs,

            border=(StyleBase().border(),) * 4,
            border_rgb=Rgb().th2(),

            border_hover=(2,) * 4,
            border_hover_rgb=Rgb().th2()
        )
    def tr(self):
        bg = Rgb().tr()
        
        Build(
            *self.wgs,
            
            bg=bg,
            bg_hover=bg,
            bg_checked=bg,
            bg_checked_hover=bg,
            bg_pressed=bg,
            bg_checked_pressed=bg,
            fg=Rgb().th3(),
            fg_checked=Rgb().bn1(),
        )

######################
##     MENU TOP     ##
######################
class menu_top:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            img=Img().main(),
            img_rgb="th2",
            ):
        Build(
            *self.wgs,
            pb_type="zoom",
            width=Dim().h9() * 1.2,
            cursor=Cur().souris_main(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_checked=Rgb().tr(),
            bg_checked_hover=Rgb().tr(),
            bg_pressed=Rgb().tr(),
            fg_checked=Rgb().th3(),
            img=img,
            img_rgb=img_rgb,
        )

    def option(self):
        self.rtn(
            img=Img().option()
        )
    def reduire(self):
        self.rtn(
            img=Img().reduire(),
            img_rgb="bn1"
        )
    def agrandir(self):
        self.rtn(
            img=Img().agrandir(),
            img_rgb="th3"
        )
    def quitter(self):
        self.rtn(
            img=Img().quitter(),
            img_rgb="bn2"
        )


#################
##     TXT     ##
#################
class Txt:
    def __init__(self, *wgs):
        self.wgs = wgs

    def txt(self):
        bd_gen = (StyleBase().border(),) * 4
        bd_rgb = Rgb().th3()

        Build(
            *self.wgs,
            bg=Rgb().th1(),
            fg=Rgb().th3(),
            bg_hover=Rgb().th3(),
            fg_hover=Rgb().th1(),
            bg_pressed=Rgb().th3(),
            bg_checked=Rgb().th3(),
            fg_checked=Rgb().th1(),
            bg_checked_hover=Rgb().th1(),
            fg_checked_hover=Rgb().th3(),
            bg_checked_pressed=Rgb().th1(),
            border=bd_gen,
            border_hover=bd_gen,
            border_checked=bd_gen,
            border_checked_hover=bd_gen,
            border_rgb=bd_rgb,
            border_hover_rgb=bd_rgb,
            border_checked_rgb=bd_rgb,
            border_checked_hover_rgb=bd_rgb,
        )
    def inv(self):
        bd_gen = (StyleBase().border(),) * 4
        bd_rgb = Rgb().th3()

        Build(
            *self.wgs,
            bg=Rgb().th3(),
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=Rgb().th3(),
            bg_pressed=Rgb().th1(),
            bg_checked=Rgb().th1(),
            fg_checked=Rgb().th3(),
            bg_checked_hover=Rgb().th3(),
            fg_checked_hover=Rgb().th1(),
            bg_checked_pressed=Rgb().th3(),
            border=bd_gen,
            border_hover=bd_gen,
            border_checked=bd_gen,
            border_checked_hover=bd_gen,
            border_rgb=bd_rgb,
            border_hover_rgb=bd_rgb,
            border_checked_rgb=bd_rgb,
            border_checked_hover_rgb=bd_rgb,
        )


#################
##     DLG     ##
#################
class Dlg:
    def __init__(self, *wgs):
        self.wgs = wgs

    def ok(self):
        bd_gen = (StyleBase().border(),) * 4
        rgb_gen = Rgb().bn1()

        Build(
            *self.wgs,
            width=Dim().h6(),
            height=None,
            bg=Rgb().th1(),
            fg=rgb_gen,
            bg_hover=rgb_gen,
            fg_hover=Rgb().th1(),
            bg_pressed=rgb_gen,
            fg_pressed=Rgb().th1(),
            border=bd_gen,
            border_hover=bd_gen,
            border_checked=bd_gen,
            border_checked_hover=bd_gen,
            border_rgb=rgb_gen,
            border_hover_rgb=rgb_gen,
            border_checked_rgb=rgb_gen,
            border_checked_hover_rgb=rgb_gen,
        )
    def ok_inv(self):
        bd_gen = (StyleBase().border(),) * 4
        rgb_gen = Rgb().bn1()

        Build(
            *self.wgs,
            width=Dim().h6(),
            height=None,
            bg=rgb_gen,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=rgb_gen,
            bg_pressed=Rgb().th1(),
            fg_pressed=rgb_gen,
            border=bd_gen,
            border_hover=bd_gen,
            border_checked=bd_gen,
            border_checked_hover=bd_gen,
            border_rgb=rgb_gen,
            border_hover_rgb=rgb_gen,
            border_checked_rgb=rgb_gen,
            border_checked_hover_rgb=rgb_gen,
        )
    def nok(self):
        bd_gen = (StyleBase().border(),) * 4
        rgb_gen = Rgb().bn2()

        Build(
            *self.wgs,
            width=Dim().h6(),
            height=None,
            bg=Rgb().th1(),
            fg=rgb_gen,
            bg_hover=rgb_gen,
            fg_hover=Rgb().th1(),
            bg_pressed=rgb_gen,
            fg_pressed=Rgb().th1(),
            border=bd_gen,
            border_hover=bd_gen,
            border_checked=bd_gen,
            border_checked_hover=bd_gen,
            border_rgb=rgb_gen,
            border_hover_rgb=rgb_gen,
            border_checked_rgb=rgb_gen,
            border_checked_hover_rgb=rgb_gen,
        )
    def nok_inv(self):
        bd_gen = (StyleBase().border(),) * 4
        rgb_gen = Rgb().bn2()

        Build(
            *self.wgs,
            width=Dim().h6(),
            height=None,
            bg=rgb_gen,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=rgb_gen,
            bg_pressed=Rgb().th1(),
            fg_pressed=rgb_gen,
            border=bd_gen,
            border_hover=bd_gen,
            border_checked=bd_gen,
            border_checked_hover=bd_gen,
            border_rgb=rgb_gen,
            border_hover_rgb=rgb_gen,
            border_checked_rgb=rgb_gen,
            border_checked_hover_rgb=rgb_gen,
        )


###################
##     PLEIN     ##
###################
class plein:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().tr(),
            height=Dim().h5(),

            border_gen=(0, )*4,
            border_gen_rgb=Rgb().tr(),
            cursor=Cur().main()
            ):
        Build(
            *self.wgs,
            height=height,
            cursor=cursor,

            bg=bg_gen,
            bg_hover=bg_gen,
            bg_checked=bg_gen,
            bg_checked_hover=bg_gen,
            bg_pressed=bg_gen,
            bg_checked_pressed=bg_gen,
            fg=fg_gen,
            fg_hover=fg_gen,
            fg_checked=fg_gen,
            fg_checked_hover=fg_gen,
            fg_pressed=fg_gen,
            fg_checked_pressed=fg_gen,
            border=border_gen,
            border_hover=border_gen,
            border_checked=border_gen,
            border_checked_hover=border_gen,
            border_rgb=border_gen_rgb,
            border_hover_rgb=border_gen_rgb,
            border_checked_rgb=border_gen_rgb,
            border_checked_hover_rgb=border_gen_rgb,

            radius=(0, )*4
        )

    def th1(self):
        self.rtn(
            bg_gen=Rgb().th1(),
            fg_gen=Rgb().th3(),
            border_gen=(StyleBase().border(),) * 4,
            border_gen_rgb=Rgb().th2(),
        )
    def th2(self):
        self.rtn(
            bg_gen=Rgb().th2(),
            fg_gen=Rgb().th3(),
        )
    def th3(self):
        self.rtn(
            bg_gen=Rgb().th3(),
            fg_gen=Rgb().th1(),
        )
    def bn1(self):
        self.rtn(
            bg_gen=Rgb().bn1(),
            fg_gen=Rgb().th3(),
        )
    def bn2(self):
        self.rtn(
            bg_gen=Rgb().bn2(),
            fg_gen=Rgb().th3(),
        )
