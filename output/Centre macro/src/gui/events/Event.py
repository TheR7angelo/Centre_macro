from PySide6 import QtCore, QtWidgets, QtGui

from src.build.mods import Functions
from src.config.config import Configue
from src.lib.globals import v_gb
from src.lib.palettes import *


class Event:
    def __init__(self, ui):
        self.ui = ui
        self.margin = v_gb.MARGIN_APP

    def _e_center_screen(self):
        """Permet de centrer la fenêtre."""
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.ui.frameGeometry()
        geo.moveCenter(center)
        self.ui.move(geo.topLeft())

    #####

    def e_agrandir(self):
        """Permet d'agrandir la fenêtre"""
        if self.ui.windowState() == QtCore.Qt.WindowMaximized:
            self.ui.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
            self.margin = v_gb.MARGIN_APP
            self.ui.win_state = QtCore.Qt.WindowNoState
            self.ui.e_resize_screen()
            self._e_center_screen()
        else:
            self.ui.vlay_main.setContentsMargins(0, 0, 0, 0)
            self.margin = 0
            self.ui.win_state = QtCore.Qt.WindowMaximized

        self.ui.setWindowState(self.ui.win_state)
    def e_reduire(self):
        """Permet de réduire la fenêtre"""
        self.ui.setWindowState(QtCore.Qt.WindowMinimized)
        self.ui.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
        self.margin = v_gb.MARGIN_APP
    def e_cacher(self):
        """Permet de cacher la fenêtre"""
        if Configue().cfg["var"]["debug"]: return self.ui.e_quitter()
        self.ui.hide()
        self._e_center_screen()

    #####

    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and self.margin < verif_height < Dim().h9()+self.margin and self.ui.windowState() != QtCore.Qt.WindowMaximized:
            self.ui.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseDoubleClickEvent(self, event):
        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and self.margin < verif_height < Dim().h9()+self.margin:
            self.e_agrandir()
            event.accept()
    def mouseMoveEvent(self, event):
        def act_move(event):
            self.ui.move(self.ui.pos() + event.globalPosition().toPoint() - self.ui.dragPos)
            self.ui.dragPos = event.globalPosition().toPoint()
            event.accept()

        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and self.margin < verif_height < Dim().h9()+self.margin and self.ui.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= self.margin:
            self.ui.setCursor(Functions().SET_CURSOR(Cur().agrandir()))
        else:
            self.ui.setCursor(Functions().SET_CURSOR(Cur().Arrow()))

        try:
            if event.buttons() == QtCore.Qt.LeftButton and self.margin < verif_height < Dim().h9()+self.margin and self.ui.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and self.margin < verif_height < Dim().h9()+self.margin and self.ui.windowState() == QtCore.Qt.WindowMaximized:
                self.ui.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
                self.margin = v_gb.MARGIN_APP
                self.ui.setWindowState(QtCore.Qt.WindowNoState)
                self.ui.win_state = QtCore.Qt.WindowNoState
                act_move(event)
        except AttributeError: pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        verif_height = cur.pos().y() - self.ui.pos().y()
        if Dim().h9() + self.margin > verif_height > self.margin >= cur.pos().y() and self.ui.windowState() != QtCore.Qt.WindowMaximized:
            self.ui.setCursor(Functions().SET_CURSOR(Cur().Arrow()))
            self.e_agrandir()
            event.accept()
