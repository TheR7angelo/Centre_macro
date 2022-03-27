from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import toolbox_ui


class ToolBoxUi(toolbox_ui.Ui_ToolBoxUi, QtWidgets.QDialog):
    def __init__(self):
        super(ToolBoxUi, self).__init__()

        self.width = 300
        self.height = 600
        self.opacity = 1

        self.INIT()

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)

        if Configue().cfg["var"]["toolbox_pin"]:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        else:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGraphicsEffect(Shadow().ombre_portee(self))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    def IN_SETUP_UI(self):
        ### Ui ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QFrame ###
        Frame.ToolBox(self.fr_main)
        Frame.Menu(self.fr_menu_top).top()
        Frame.Dlg(self.fr_body).th(rgb=Rgb().th1())
        ### /QFrame ###


        ### QPushButton ###
        PushButton.menu_top(self.pb_mt_quitter).quitter()
        ### /QPushButton ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=Cur().Arrow()))
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.hide())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_SETUP_UI()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()
    ############################
    ##    /INITIALISATION     ##
    ############################
