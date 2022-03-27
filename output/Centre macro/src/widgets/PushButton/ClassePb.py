from PySide6 import QtCore

from src.build.mods.Functions import Functions


class ClassePb:
    def __init__(
            self,
            wg,
            dim_ico,
            DIM_ICO,
            img,
            img_hover,
            img_uncheck,
            img_uncheck_hover,
            img_check,
            img_check_hover,
            img_rgb,
            img_hover_rgb,
            img_uncheck_rgb,
            img_uncheck_hover_rgb,
            img_check_rgb,
            img_check_hover_rgb,
    ):
        self.wg = wg
        self.dim_ico = dim_ico
        self.DIM_ICO = DIM_ICO
        self.img = img
        self.img_hover = img_hover
        self.img_uncheck = img_uncheck
        self.img_uncheck_hover = img_uncheck_hover
        self.img_check = img_check
        self.img_check_hover = img_check_hover
        self.img_rgb = img_rgb
        self.img_hover_rgb = img_hover_rgb
        self.img_uncheck_rgb = img_uncheck_rgb
        self.img_uncheck_hover_rgb = img_uncheck_hover_rgb
        self.img_check_rgb = img_check_rgb
        self.img_check_hover_rgb = img_check_hover_rgb

    def ENT_CHECK(self, event):
        if self.wg.isEnabled():
            if not self.wg.isChecked():
                Functions().SET_ICON(wg=self.wg, img=self.img_uncheck_hover + self.img_uncheck_hover_rgb, dim=self.dim_ico)
            else:
                Functions().SET_ICON(wg=self.wg, img=self.img_check_hover + self.img_check_hover_rgb, dim=self.dim_ico)
    def LVE_CHECK(self, event):
        if self.wg.isEnabled():
            if not self.wg.isChecked():
                Functions().SET_ICON(wg=self.wg, img=self.img_uncheck + self.img_uncheck_rgb, dim=self.dim_ico)
            else:
                Functions().SET_ICON(wg=self.wg, img=self.img_check + self.img_check_rgb, dim=self.dim_ico)
    def MP_CHECK(self, event):
        if self.wg.isEnabled():
            if not self.wg.isChecked():
                self.wg.setChecked(True)
                Functions().SET_ICON(wg=self.wg, img=self.img_check_hover + self.img_check_hover_rgb, dim=self.dim_ico)
            else:
                self.wg.setChecked(False)
                Functions().SET_ICON(wg=self.wg, img=self.img_uncheck_hover + self.img_uncheck_hover_rgb, dim=self.dim_ico)


    def ENT_ICO(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            Functions().SET_ICON(wg=self.wg, img=self.img + self.img_hover_rgb, dim=self.dim_ico)
    def LVE_ICO(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            Functions().SET_ICON(wg=self.wg, img=self.img + self.img_rgb, dim=self.dim_ico)
    def MP_ICO(self, event):
        if self.wg.isChecked() and self.wg.isEnabled():
            self.wg.setChecked(False)
            Functions().SET_ICON(wg=self.wg, img=self.img + self.img_rgb, dim=self.dim_ico)
        elif not self.wg.isChecked() and self.wg.isEnabled():
            self.wg.setChecked(True)
            Functions().SET_ICON(wg=self.wg, img=self.img + self.img_hover_rgb, dim=self.dim_ico)

    def ENT_ZOOM(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            self.wg.setIconSize(QtCore.QSize(self.DIM_ICO, self.DIM_ICO))
    def LVE_ZOOM(self, event):
        if not self.wg.isChecked() and self.wg.isEnabled():
            self.wg.setIconSize(QtCore.QSize(self.dim_ico, self.dim_ico))

"""
if self.wg.isEnabled():
    if not self.wg.isChecked():
        pass
    else:
        pass
"""