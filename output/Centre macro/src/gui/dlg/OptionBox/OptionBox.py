from src import *
from src.gui.dlg.OptionBox.OptionDlg import OptionDlg


class OptionBox:
    def __init__(self,
                 fen_main,
                 width=850,
                 height=600,
                 opacity=1
                 ):
        self.fen_main = fen_main
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, title, msg, ico, ico_rgb, txt_apply, txt_ok):
        opt = OptionDlg(
            fen_main=self.fen_main,
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_apply=txt_apply,
            txt_ok=txt_ok,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        opt.exec()


    def MAIN(self, title="OPTION", msg="", ico=Img().info(), ico_rgb="th3", txt_apply="Appliquer", txt_ok="Ok"):
        return self._rtn(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_apply=txt_apply,
            txt_ok=txt_ok
        )
