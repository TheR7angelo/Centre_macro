from src import *
from src.gui.dlg.RgbBox.RgbDlg import RgbDlg


class RgbBox:
    def __init__(
            self,
            width=750,
            height=550,
            opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, title, rgb, ico, ico_rgb, txt_ok, txt_cancel):
        rgb_dlg = RgbDlg(
            title=title,
            rgb=rgb,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        rgb_dlg.exec()
        return rgb_dlg.return_rgb if rgb_dlg.response else False


    def GET(
            self,
            title="RGB",
            rgb=None,
            ico=Img().info(),
            ico_rgb="th3",
            txt_ok="Ok",
            txt_cancel="Annuler"
    ):
        return self._rtn(
            title=title,
            rgb=rgb,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel
        )
