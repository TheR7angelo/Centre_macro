from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import input_ui
from src.gui.events.Event import Event


class InputDlg(input_ui.Ui_Input, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
    input_txt = ""

    def __init__(
            self,
            title,
            msg,
            ico,
            ico_rgb,
            txt_ok,
            txt_cancel,
            width,
            height,
            opacity,
    ):
        super(InputDlg, self).__init__()

        self.title = title
        self.msg = msg
        self.ico = ico
        self.ico_rgb = ico_rgb
        self.txt_ok = txt_ok
        self.txt_cancel = txt_cancel
        self.width = width
        self.height = height
        self.opacity = opacity

        self.INIT()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre ###
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
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
        Frame_cust.Menu(self.fr_menu_top).top()
        Frame_cust.Cadre(self.fr_main).th2()
        Frame_cust.Dlg(self.fr_body).th(rgb=Rgb().th1())
        Frame_cust.Menu(self.fr_input_bottom).bottom_dlg()
        ### /QFrame ###


        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_custom(img=self.ico, img_rgb=self.ico_rgb)
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_input_text).tr()
        ### /QLabel ###


        ### QPushButton ###
        PushButton.Dlg(self.pb_input_ok).ok()
        PushButton.Dlg(self.pb_input_annuler).nok_inv()
        PushButton.menu_top(self.pb_mt_quitter).quitter()
        ### /QPushButton ###


        ### QText ###
        LineEdit.Base(self.le_input_text).th()
        ### /QText ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=Cur().souris()))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
        self.lb_mt_nom.setText(self.title)

        # Message
        self.lb_input_text.setText(f"{self.msg}: ")
        self.le_input_text.setPlaceholderText(f"{self.msg}...")

        # pb dlg
        self.pb_input_ok.setText(self.txt_ok)
        self.pb_input_annuler.setText(self.txt_cancel)
        self.pb_input_annuler.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_input_ok.clicked.connect(lambda: self.f_ok())
        self.pb_input_annuler.clicked.connect(lambda: self.close())
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


    #######################
    ##     FONCTIONS     ##
    #######################
    def f_ok(self):
        self.input_txt = self.le_input_text.text()
        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################
