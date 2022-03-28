# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

from src.widget_custom.Label_cust import DropLabel

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(852, 725)
        self.vlay_main = QVBoxLayout(main)
        self.vlay_main.setSpacing(0)
        self.vlay_main.setObjectName(u"vlay_main")
        self.vlay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(main)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(self.fr_main)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_menu_top.sizePolicy().hasHeightForWidth())
        self.fr_menu_top.setSizePolicy(sizePolicy)
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.lb_mt_ico = QLabel(self.fr_menu_top)
        self.lb_mt_ico.setObjectName(u"lb_mt_ico")

        self.hlay_menu_top.addWidget(self.lb_mt_ico)

        self.wg_mt_blank = QWidget(self.fr_menu_top)
        self.wg_mt_blank.setObjectName(u"wg_mt_blank")

        self.hlay_menu_top.addWidget(self.wg_mt_blank)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_option = QPushButton(self.fr_menu_top)
        self.pb_mt_option.setObjectName(u"pb_mt_option")

        self.hlay_menu_top.addWidget(self.pb_mt_option)

        self.pb_mt_reduire = QPushButton(self.fr_menu_top)
        self.pb_mt_reduire.setObjectName(u"pb_mt_reduire")

        self.hlay_menu_top.addWidget(self.pb_mt_reduire)

        self.pb_mt_agrandir = QPushButton(self.fr_menu_top)
        self.pb_mt_agrandir.setObjectName(u"pb_mt_agrandir")

        self.hlay_menu_top.addWidget(self.pb_mt_agrandir)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.fr_body = QFrame(self.fr_main)
        self.fr_body.setObjectName(u"fr_body")
        self.fr_body.setFrameShape(QFrame.StyledPanel)
        self.fr_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.list_menu = QListWidget(self.fr_body)
        self.list_menu.setObjectName(u"list_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.list_menu.sizePolicy().hasHeightForWidth())
        self.list_menu.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.list_menu)

        self.stackedWidget = QStackedWidget(self.fr_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_logiciel = QWidget()
        self.page_logiciel.setObjectName(u"page_logiciel")
        self.verticalLayout_2 = QVBoxLayout(self.page_logiciel)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_logiciel)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 574, 665))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_logiciel_titre = QLabel(self.scrollAreaWidgetContents)
        self.lb_logiciel_titre.setObjectName(u"lb_logiciel_titre")
        sizePolicy.setHeightForWidth(self.lb_logiciel_titre.sizePolicy().hasHeightForWidth())
        self.lb_logiciel_titre.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.lb_logiciel_titre)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_logiciel)
        self.page_helper = QWidget()
        self.page_helper.setObjectName(u"page_helper")
        self.stackedWidget.addWidget(self.page_helper)
        self.page_editeur = QWidget()
        self.page_editeur.setObjectName(u"page_editeur")
        self.verticalLayout_7 = QVBoxLayout(self.page_editeur)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_4 = QSpacerItem(20, 303, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pb_addApp_edit = QPushButton(self.page_editeur)
        self.pb_addApp_edit.setObjectName(u"pb_addApp_edit")

        self.gridLayout_5.addWidget(self.pb_addApp_edit, 0, 0, 1, 1)

        self.pb_addVer_edit = QPushButton(self.page_editeur)
        self.pb_addVer_edit.setObjectName(u"pb_addVer_edit")

        self.gridLayout_5.addWidget(self.pb_addVer_edit, 0, 1, 1, 1)

        self.pb_addHelp_edit = QPushButton(self.page_editeur)
        self.pb_addHelp_edit.setObjectName(u"pb_addHelp_edit")

        self.gridLayout_5.addWidget(self.pb_addHelp_edit, 0, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 302, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_editeur)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.verticalLayout_11 = QVBoxLayout(self.page_admin)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_6 = QSpacerItem(20, 303, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pb_addAuteur_admin = QPushButton(self.page_admin)
        self.pb_addAuteur_admin.setObjectName(u"pb_addAuteur_admin")

        self.gridLayout_6.addWidget(self.pb_addAuteur_admin, 0, 3, 1, 1)

        self.pb_addVer_admin = QPushButton(self.page_admin)
        self.pb_addVer_admin.setObjectName(u"pb_addVer_admin")

        self.gridLayout_6.addWidget(self.pb_addVer_admin, 0, 1, 1, 1)

        self.pb_addApp_admin = QPushButton(self.page_admin)
        self.pb_addApp_admin.setObjectName(u"pb_addApp_admin")

        self.gridLayout_6.addWidget(self.pb_addApp_admin, 0, 0, 1, 1)

        self.pb_addHelper_admin = QPushButton(self.page_admin)
        self.pb_addHelper_admin.setObjectName(u"pb_addHelper_admin")

        self.gridLayout_6.addWidget(self.pb_addHelper_admin, 0, 2, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_6)

        self.verticalSpacer_7 = QSpacerItem(20, 302, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

        self.stackedWidget.addWidget(self.page_admin)
        self.page_ajout_app = QWidget()
        self.page_ajout_app.setObjectName(u"page_ajout_app")
        self.verticalLayout_5 = QVBoxLayout(self.page_ajout_app)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_ajout_app)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_addApp_titre = QLabel(self.frame)
        self.lb_addApp_titre.setObjectName(u"lb_addApp_titre")

        self.verticalLayout_6.addWidget(self.lb_addApp_titre)

        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.lb_icon_new = DropLabel(self.frame)
        self.lb_icon_new.setObjectName(u"lb_icon_new")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_icon_new.sizePolicy().hasHeightForWidth())
        self.lb_icon_new.setSizePolicy(sizePolicy2)
        self.lb_icon_new.setMinimumSize(QSize(232, 232))
        self.lb_icon_new.setMaximumSize(QSize(232, 232))
        self.lb_icon_new.setStyleSheet(u".QLabel{\n"
"background-color: rgb(85, 255, 0);\n"
"}")

        self.verticalLayout_1.addWidget(self.lb_icon_new, 0, Qt.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pb_ico = QPushButton(self.frame)
        self.pb_ico.setObjectName(u"pb_ico")

        self.horizontalLayout_3.addWidget(self.pb_ico)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_1.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_new_ap_val = QPushButton(self.frame)
        self.pb_new_ap_val.setObjectName(u"pb_new_ap_val")

        self.gridLayout_2.addWidget(self.pb_new_ap_val, 8, 1, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 3, 1, 1)

        self.text_desc = QTextEdit(self.frame)
        self.text_desc.setObjectName(u"text_desc")
        self.text_desc.setUndoRedoEnabled(True)
        self.text_desc.setTabStopDistance(20.000000000000000)

        self.gridLayout_2.addWidget(self.text_desc, 5, 1, 1, 4)

        self.num_ver = QDoubleSpinBox(self.frame)
        self.num_ver.setObjectName(u"num_ver")
        self.num_ver.setDecimals(1)
        self.num_ver.setMinimum(0.100000000000000)
        self.num_ver.setMaximum(99999999.000000000000000)
        self.num_ver.setSingleStep(0.010000000000000)

        self.gridLayout_2.addWidget(self.num_ver, 2, 1, 1, 2)

        self.cb_auteur = QComboBox(self.frame)
        self.cb_auteur.setObjectName(u"cb_auteur")

        self.gridLayout_2.addWidget(self.cb_auteur, 3, 1, 1, 2)

        self.line_ap = QLineEdit(self.frame)
        self.line_ap.setObjectName(u"line_ap")

        self.gridLayout_2.addWidget(self.line_ap, 0, 1, 1, 4)

        self.text_chang = QTextEdit(self.frame)
        self.text_chang.setObjectName(u"text_chang")

        self.gridLayout_2.addWidget(self.text_chang, 7, 1, 1, 4)

        self.lb_desc_ap = QLabel(self.frame)
        self.lb_desc_ap.setObjectName(u"lb_desc_ap")

        self.gridLayout_2.addWidget(self.lb_desc_ap, 5, 0, 1, 1)

        self.lb_auteur_ap = QLabel(self.frame)
        self.lb_auteur_ap.setObjectName(u"lb_auteur_ap")

        self.gridLayout_2.addWidget(self.lb_auteur_ap, 3, 0, 1, 1)

        self.lb_chang_ap = QLabel(self.frame)
        self.lb_chang_ap.setObjectName(u"lb_chang_ap")

        self.gridLayout_2.addWidget(self.lb_chang_ap, 7, 0, 1, 1)

        self.lb_ver_ap = QLabel(self.frame)
        self.lb_ver_ap.setObjectName(u"lb_ver_ap")

        self.gridLayout_2.addWidget(self.lb_ver_ap, 2, 0, 1, 1)

        self.pb_ap_selector = QPushButton(self.frame)
        self.pb_ap_selector.setObjectName(u"pb_ap_selector")

        self.gridLayout_2.addWidget(self.pb_ap_selector, 0, 0, 1, 1)

        self.lb_nom_ap = QLabel(self.frame)
        self.lb_nom_ap.setObjectName(u"lb_nom_ap")

        self.gridLayout_2.addWidget(self.lb_nom_ap, 1, 0, 1, 1)

        self.line_ap_nom = QLineEdit(self.frame)
        self.line_ap_nom.setObjectName(u"line_ap_nom")

        self.gridLayout_2.addWidget(self.line_ap_nom, 1, 1, 1, 4)

        self.lb_stock = QLabel(self.frame)
        self.lb_stock.setObjectName(u"lb_stock")

        self.gridLayout_2.addWidget(self.lb_stock, 4, 0, 1, 1)

        self.cb_stock = QComboBox(self.frame)
        self.cb_stock.setObjectName(u"cb_stock")

        self.gridLayout_2.addWidget(self.cb_stock, 4, 1, 1, 3)


        self.verticalLayout_6.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_ajout_app)
        self.page_change_ver = QWidget()
        self.page_change_ver.setObjectName(u"page_change_ver")
        self.verticalLayout_8 = QVBoxLayout(self.page_change_ver)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lb_changeVer_titre = QLabel(self.page_change_ver)
        self.lb_changeVer_titre.setObjectName(u"lb_changeVer_titre")

        self.verticalLayout_8.addWidget(self.lb_changeVer_titre)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_list_app = QLabel(self.page_change_ver)
        self.lb_list_app.setObjectName(u"lb_list_app")

        self.verticalLayout_4.addWidget(self.lb_list_app)

        self.cb_list_app_ver = QComboBox(self.page_change_ver)
        self.cb_list_app_ver.setObjectName(u"cb_list_app_ver")

        self.verticalLayout_4.addWidget(self.cb_list_app_ver)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.lb_app_ver_add = QLabel(self.page_change_ver)
        self.lb_app_ver_add.setObjectName(u"lb_app_ver_add")
        self.lb_app_ver_add.setMinimumSize(QSize(232, 232))
        self.lb_app_ver_add.setMaximumSize(QSize(232, 232))
        self.lb_app_ver_add.setFrameShape(QFrame.Box)

        self.horizontalLayout_4.addWidget(self.lb_app_ver_add)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_old_ver = QLabel(self.page_change_ver)
        self.lb_old_ver.setObjectName(u"lb_old_ver")

        self.gridLayout_3.addWidget(self.lb_old_ver, 0, 0, 2, 3)

        self.lb_change_old_ver = QLabel(self.page_change_ver)
        self.lb_change_old_ver.setObjectName(u"lb_change_old_ver")

        self.gridLayout_3.addWidget(self.lb_change_old_ver, 2, 0, 1, 1)

        self.text_old_chang = QTextEdit(self.page_change_ver)
        self.text_old_chang.setObjectName(u"text_old_chang")

        self.gridLayout_3.addWidget(self.text_old_chang, 3, 1, 1, 2)

        self.lb_correct_old = QLabel(self.page_change_ver)
        self.lb_correct_old.setObjectName(u"lb_correct_old")

        self.gridLayout_3.addWidget(self.lb_correct_old, 3, 0, 1, 1)

        self.num_old_ver = QDoubleSpinBox(self.page_change_ver)
        self.num_old_ver.setObjectName(u"num_old_ver")
        self.num_old_ver.setDecimals(1)
        self.num_old_ver.setMinimum(0.100000000000000)
        self.num_old_ver.setMaximum(99999999.000000000000000)
        self.num_old_ver.setSingleStep(0.010000000000000)

        self.gridLayout_3.addWidget(self.num_old_ver, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 2, 2, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_correct_new = QLabel(self.page_change_ver)
        self.lb_correct_new.setObjectName(u"lb_correct_new")

        self.gridLayout_4.addWidget(self.lb_correct_new, 4, 0, 1, 1)

        self.lb_new_ver = QLabel(self.page_change_ver)
        self.lb_new_ver.setObjectName(u"lb_new_ver")

        self.gridLayout_4.addWidget(self.lb_new_ver, 0, 0, 2, 3)

        self.num_new_ver = QDoubleSpinBox(self.page_change_ver)
        self.num_new_ver.setObjectName(u"num_new_ver")
        self.num_new_ver.setDecimals(1)
        self.num_new_ver.setMinimum(0.100000000000000)
        self.num_new_ver.setMaximum(99999999.000000000000000)
        self.num_new_ver.setSingleStep(0.010000000000000)

        self.gridLayout_4.addWidget(self.num_new_ver, 3, 1, 1, 1)

        self.text_new_chang = QTextEdit(self.page_change_ver)
        self.text_new_chang.setObjectName(u"text_new_chang")

        self.gridLayout_4.addWidget(self.text_new_chang, 4, 1, 1, 2)

        self.lb_change_new_ver = QLabel(self.page_change_ver)
        self.lb_change_new_ver.setObjectName(u"lb_change_new_ver")

        self.gridLayout_4.addWidget(self.lb_change_new_ver, 3, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 3, 2, 1, 1)

        self.pb_ap_selector_ver = QPushButton(self.page_change_ver)
        self.pb_ap_selector_ver.setObjectName(u"pb_ap_selector_ver")

        self.gridLayout_4.addWidget(self.pb_ap_selector_ver, 2, 0, 1, 1)

        self.line_ap_ver = QLineEdit(self.page_change_ver)
        self.line_ap_ver.setObjectName(u"line_ap_ver")

        self.gridLayout_4.addWidget(self.line_ap_ver, 2, 1, 1, 2)


        self.verticalLayout_8.addLayout(self.gridLayout_4)

        self.pb_new_ver_val = QPushButton(self.page_change_ver)
        self.pb_new_ver_val.setObjectName(u"pb_new_ver_val")

        self.verticalLayout_8.addWidget(self.pb_new_ver_val)

        self.stackedWidget.addWidget(self.page_change_ver)
        self.page_ajout_helper = QWidget()
        self.page_ajout_helper.setObjectName(u"page_ajout_helper")
        self.stackedWidget.addWidget(self.page_ajout_helper)
        self.page_ajout_auteur = QWidget()
        self.page_ajout_auteur.setObjectName(u"page_ajout_auteur")
        self.verticalLayout_10 = QVBoxLayout(self.page_ajout_auteur)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lb_auteur_titre = QLabel(self.page_ajout_auteur)
        self.lb_auteur_titre.setObjectName(u"lb_auteur_titre")

        self.verticalLayout_9.addWidget(self.lb_auteur_titre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lb_auteur_name_add = QLabel(self.page_ajout_auteur)
        self.lb_auteur_name_add.setObjectName(u"lb_auteur_name_add")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_auteur_name_add)

        self.ln_auteur_name_add = QLineEdit(self.page_ajout_auteur)
        self.ln_auteur_name_add.setObjectName(u"ln_auteur_name_add")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ln_auteur_name_add)

        self.lb_auteur_alias_add = QLabel(self.page_ajout_auteur)
        self.lb_auteur_alias_add.setObjectName(u"lb_auteur_alias_add")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_auteur_alias_add)

        self.ln_auteur_alias_add = QLineEdit(self.page_ajout_auteur)
        self.ln_auteur_alias_add.setObjectName(u"ln_auteur_alias_add")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ln_auteur_alias_add)

        self.lb_auteur_mail_add = QLabel(self.page_ajout_auteur)
        self.lb_auteur_mail_add.setObjectName(u"lb_auteur_mail_add")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_auteur_mail_add)

        self.ln_auteur_mail_add = QLineEdit(self.page_ajout_auteur)
        self.ln_auteur_mail_add.setObjectName(u"ln_auteur_mail_add")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ln_auteur_mail_add)


        self.verticalLayout_9.addLayout(self.formLayout)

        self.pb_auteur_add_valide = QPushButton(self.page_ajout_auteur)
        self.pb_auteur_add_valide.setObjectName(u"pb_auteur_add_valide")

        self.verticalLayout_9.addWidget(self.pb_auteur_add_valide)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.stackedWidget.addWidget(self.page_ajout_auteur)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_menu_bottom = QFrame(self.fr_main)
        self.fr_menu_bottom.setObjectName(u"fr_menu_bottom")
        sizePolicy.setHeightForWidth(self.fr_menu_bottom.sizePolicy().hasHeightForWidth())
        self.fr_menu_bottom.setSizePolicy(sizePolicy)
        self.hlay_menu_bottom = QHBoxLayout(self.fr_menu_bottom)
        self.hlay_menu_bottom.setSpacing(0)
        self.hlay_menu_bottom.setObjectName(u"hlay_menu_bottom")
        self.hlay_menu_bottom.setContentsMargins(0, 0, 0, 0)
        self.lb_mb_version = QLabel(self.fr_menu_bottom)
        self.lb_mb_version.setObjectName(u"lb_mb_version")

        self.hlay_menu_bottom.addWidget(self.lb_mb_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_bottom.addItem(self.horizontalSpacer_4)


        self.vlay_fr_main.addWidget(self.fr_menu_bottom)


        self.vlay_main.addWidget(self.fr_main)


        self.retranslateUi(main)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        self.lb_logiciel_titre.setText(QCoreApplication.translate("main", u"Macro", None))
        self.pb_addApp_edit.setText(QCoreApplication.translate("main", u"Ajouter une application", None))
        self.pb_addVer_edit.setText(QCoreApplication.translate("main", u"Ajouter une version", None))
        self.pb_addHelp_edit.setText(QCoreApplication.translate("main", u"Ajouter un helper", None))
        self.pb_addAuteur_admin.setText(QCoreApplication.translate("main", u"Ajouter un auteur", None))
        self.pb_addVer_admin.setText(QCoreApplication.translate("main", u"Ajouter une version", None))
        self.pb_addApp_admin.setText(QCoreApplication.translate("main", u"Ajouter une application", None))
        self.pb_addHelper_admin.setText(QCoreApplication.translate("main", u"Ajouter un helper", None))
        self.lb_addApp_titre.setText(QCoreApplication.translate("main", u"Ajout d'une application", None))
        self.lb_icon_new.setText("")
        self.pb_ico.setText(QCoreApplication.translate("main", u"Icon", None))
        self.pb_new_ap_val.setText(QCoreApplication.translate("main", u"Enregistrer", None))
        self.text_desc.setMarkdown("")
        self.text_desc.setHtml(QCoreApplication.translate("main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lb_desc_ap.setText(QCoreApplication.translate("main", u"Description", None))
        self.lb_auteur_ap.setText(QCoreApplication.translate("main", u"Auteur", None))
        self.lb_chang_ap.setText(QCoreApplication.translate("main", u"Correctif", None))
        self.lb_ver_ap.setText(QCoreApplication.translate("main", u"Version", None))
        self.pb_ap_selector.setText(QCoreApplication.translate("main", u"Application", None))
        self.lb_nom_ap.setText(QCoreApplication.translate("main", u"Nom", None))
        self.lb_stock.setText(QCoreApplication.translate("main", u"Stokage", None))
        self.lb_changeVer_titre.setText(QCoreApplication.translate("main", u"Changer la version d'une application", None))
        self.lb_list_app.setText(QCoreApplication.translate("main", u"Liste d'application", None))
        self.lb_app_ver_add.setText(QCoreApplication.translate("main", u"TextLabel", None))
        self.lb_old_ver.setText(QCoreApplication.translate("main", u"Ancienne version", None))
        self.lb_change_old_ver.setText(QCoreApplication.translate("main", u"Version", None))
        self.lb_correct_old.setText(QCoreApplication.translate("main", u"Correctif", None))
        self.lb_correct_new.setText(QCoreApplication.translate("main", u"Correctif", None))
        self.lb_new_ver.setText(QCoreApplication.translate("main", u"Nouvelle version", None))
        self.lb_change_new_ver.setText(QCoreApplication.translate("main", u"Version", None))
        self.pb_ap_selector_ver.setText(QCoreApplication.translate("main", u"Application", None))
        self.pb_new_ver_val.setText(QCoreApplication.translate("main", u"Valider", None))
        self.lb_auteur_titre.setText(QCoreApplication.translate("main", u"Ajout d'un auteur", None))
        self.lb_auteur_name_add.setText(QCoreApplication.translate("main", u"GID :", None))
        self.lb_auteur_alias_add.setText(QCoreApplication.translate("main", u"Alias :", None))
        self.lb_auteur_mail_add.setText(QCoreApplication.translate("main", u"Adresse mail :", None))
        self.pb_auteur_add_valide.setText(QCoreApplication.translate("main", u"Ajouter", None))
        pass
    # retranslateUi

