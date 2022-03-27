from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import rgb_ui
from src.gui.events.Event import Event


class RgbDlg(rgb_ui.Ui_Rgb, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
    response = False
    return_rgb = (0, 0, 0)

    def __init__(
            self,
            title,
            rgb,
            ico,
            ico_rgb,
            txt_ok,
            txt_cancel,
            width,
            height,
            opacity,
    ):
        super(RgbDlg, self).__init__()

        self.title = title
        self.rgb = (0, 0, 0) if rgb is None else rgb
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
        # Fenetre
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
        self.glay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QFrame ###
        Frame_cust.Menu(self.fr_menu_top).top()
        Frame_cust.Cadre(self.fr_main).th2()
        Frame_cust.Dlg(self.fr_body).th(rgb=Rgb().th1())
        Frame_cust.Menu(self.fr_rgb_bottom).bottom_dlg()
        Frame_cust.Base(self.fr_rgb_colors).th()
        ### /QFrame ###


        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_custom(img=self.ico, img_rgb=self.ico_rgb)
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_rgb_red, self.lb_rgb_green, self.lb_rgb_blue, font_size=Font().h4()).tr()
        ### /QLabel ###


        ### QPushButton ###
        PushButton.Dlg(self.pb_rgb_ok).ok()
        PushButton.Dlg(self.pb_rgb_annuler).nok_inv()
        PushButton.menu_top(self.pb_mt_quitter).quitter()
        ### /QPushButton ###


        ### QSpinBox ###
        SpinBox.Dlg(self.sb_rgb_red, self.sb_rgb_green, self.sb_rgb_blue).rgb()
        ### /QSpinBox ###


        ### QSlider ###
        Slider.Base(self.sd_rgb_red, self.sd_rgb_green, self.sd_rgb_blue).rgb()
        ### /QSlider ###


        ### QText ###
        LineEdit.Base(self.le_rgb_hex).rgb_hex()
        ### /QText ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=Cur().souris()))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
        self.lb_mt_nom.setText(self.title)

        # Message
        self.lb_rgb_red.setText("ROUGE")
        self.lb_rgb_green.setText("VERT")
        self.lb_rgb_blue.setText("BLEU")

        # pb dlg
        self.pb_rgb_ok.setText(self.txt_ok)
        self.pb_rgb_annuler.setText(self.txt_cancel)
        self.pb_rgb_annuler.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # Slider
        self.sd_rgb_red.valueChanged.connect(lambda: self.a_set_sb_val())
        self.sd_rgb_green.valueChanged.connect(lambda: self.a_set_sb_val())
        self.sd_rgb_blue.valueChanged.connect(lambda: self.a_set_sb_val())
        # Spin box
        self.sb_rgb_red.valueChanged.connect(lambda: self.a_set_sd_val())
        self.sb_rgb_green.valueChanged.connect(lambda: self.a_set_sd_val())
        self.sb_rgb_blue.valueChanged.connect(lambda: self.a_set_sd_val())
        # hex
        self.le_rgb_hex.textEdited.connect(lambda: self.a_set_rgb_val_hex())

        # pb dlg
        self.pb_rgb_ok.clicked.connect(lambda: self.f_ok())
        self.pb_rgb_annuler.clicked.connect(lambda: self.close())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        # Frame colors
        self.fr_rgb_colors.setFixedWidth(250)

        # slider / spin box
        self.sd_rgb_red.setValue(1)
        self.sd_rgb_red.setValue(0)

        self.sd_rgb_red.setValue(self.rgb[0])
        self.sd_rgb_green.setValue(self.rgb[1])
        self.sd_rgb_blue.setValue(self.rgb[2])
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


    #####################
    ##     ACTIONS     ##
    #####################
    def _a_set_fr_color(self):
        rgb = self.sd_rgb_red.value(), self.sd_rgb_green.value(), self.sd_rgb_blue.value()
        rgba = rgb + (255, )

        rgb_red_1 = 0, rgb[1], rgb[2], 255
        rgb_red_2 = 255, rgb[1], rgb[2], 255

        rgb_green_1 = rgb[0], 0, rgb[2], 255
        rgb_green_2 = rgb[0], 255, rgb[2], 255

        rgb_blue_1 = rgb[0], rgb[1], 0, 255
        rgb_blue_2 = rgb[0], rgb[1], 255, 255

        self.le_rgb_hex.setText(Functions().RGB_HEX(rgb=rgb))

        Frame_cust.palette_rgb(self.fr_rgb_colors, rgb=rgba)
        Slider.Base(self.sd_rgb_red).rgb(rgb=rgba, rgb_1=rgb_red_1, rgb_2=rgb_red_2)
        Slider.Base(self.sd_rgb_green).rgb(rgb=rgba, rgb_1=rgb_green_1, rgb_2=rgb_green_2)
        Slider.Base(self.sd_rgb_blue).rgb(rgb=rgba, rgb_1=rgb_blue_1, rgb_2=rgb_blue_2)
    #####
    def a_set_sb_val(self):
        self.sb_rgb_red.setValue(self.sd_rgb_red.value())
        self.sb_rgb_green.setValue(self.sd_rgb_green.value())
        self.sb_rgb_blue.setValue(self.sd_rgb_blue.value())

        self._a_set_fr_color()
    def a_set_sd_val(self):
        self.sd_rgb_red.setValue(self.sb_rgb_red.value())
        self.sd_rgb_green.setValue(self.sb_rgb_green.value())
        self.sd_rgb_blue.setValue(self.sb_rgb_blue.value())
    def a_set_rgb_val_hex(self):
        hex_colors = self.le_rgb_hex.text()

        try: rgb = Functions().HEX_RGB(hex_colors=hex_colors)
        except: return

        if len(rgb) == 3:
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            self.sb_rgb_red.setValue(red)
            self.sb_rgb_green.setValue(green)
            self.sb_rgb_blue.setValue(blue)

            self.sd_rgb_red.setValue(red)
            self.sd_rgb_green.setValue(green)
            self.sd_rgb_blue.setValue(blue)
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def f_ok(self):
        self.response = True
        self.return_rgb = self.sd_rgb_red.value(), self.sd_rgb_green.value(), self.sd_rgb_blue.value()
        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################
