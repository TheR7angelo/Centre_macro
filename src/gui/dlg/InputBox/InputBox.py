from src import *
from src.gui.dlg.InputBox.InputDlg import InputDlg


class InputBox:
    def __init__(
            self,
            width=650,
            height=250,
            opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, title, msg, ico, ico_rgb, txt_ok, txt_cancel):
        input_dlg = InputDlg(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        input_dlg.exec()
        return input_dlg.input_txt if input_dlg.input_txt != "" else False


    def TXT(
            self,
            title="INPUT",
            msg="Tapez votre texte",
            ico=Img().info(),
            ico_rgb="th3",
            txt_ok="Ok",
            txt_cancel="Annuler"
    ):
        return self._rtn(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel
        )
