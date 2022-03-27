from src import *
from src.gui.dlg.MsgBox.MsgDlg import MsgDlg


class MsgBox:
    def __init__(
            self,
            width=650,
            height=250,
            opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, title, msg, ico, ico_rgb, txt_ok):
        msg_dlg = MsgDlg(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        msg_dlg.exec()


    def INFO(
            self,
            title="INFO",
            msg="",
            ico=Img().info(),
            ico_rgb="th3",
            txt_ok="Ok"
    ):
        self._rtn(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok
        )
    def ALERTE(
            self,
            title="ALERTE",
            msg="",
            ico=Img().alerte(),
            ico_rgb="th3",
            txt_ok="Ok"
    ):
        self._rtn(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok
        )
