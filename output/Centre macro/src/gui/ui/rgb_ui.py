# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rgb.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Rgb(object):
    def setupUi(self, Rgb):
        if not Rgb.objectName():
            Rgb.setObjectName(u"Rgb")
        Rgb.resize(783, 348)
        self.glay_main = QGridLayout(Rgb)
        self.glay_main.setSpacing(0)
        self.glay_main.setObjectName(u"glay_main")
        self.glay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Rgb)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(self.fr_main)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.lb_mt_ico = QLabel(self.fr_menu_top)
        self.lb_mt_ico.setObjectName(u"lb_mt_ico")

        self.hlay_menu_top.addWidget(self.lb_mt_ico)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.fr_body = QFrame(self.fr_main)
        self.fr_body.setObjectName(u"fr_body")
        self.vlay_rgb_body = QVBoxLayout(self.fr_body)
        self.vlay_rgb_body.setSpacing(0)
        self.vlay_rgb_body.setObjectName(u"vlay_rgb_body")
        self.vlay_rgb_body.setContentsMargins(20, 0, 20, 0)
        self.glay_rgb = QGridLayout()
        self.glay_rgb.setObjectName(u"glay_rgb")
        self.glay_rgb.setHorizontalSpacing(20)
        self.glay_rgb.setVerticalSpacing(0)
        self.le_rgb_hex = QLineEdit(self.fr_body)
        self.le_rgb_hex.setObjectName(u"le_rgb_hex")

        self.glay_rgb.addWidget(self.le_rgb_hex, 1, 3, 1, 1)

        self.fr_rgb_colors = QFrame(self.fr_body)
        self.fr_rgb_colors.setObjectName(u"fr_rgb_colors")
        self.vlay_fr_rgb_colors = QVBoxLayout(self.fr_rgb_colors)
        self.vlay_fr_rgb_colors.setSpacing(0)
        self.vlay_fr_rgb_colors.setObjectName(u"vlay_fr_rgb_colors")
        self.vlay_fr_rgb_colors.setContentsMargins(0, 0, 0, 0)

        self.glay_rgb.addWidget(self.fr_rgb_colors, 3, 3, 8, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_rgb.addItem(self.verticalSpacer_14, 0, 0, 1, 4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_rgb.addItem(self.horizontalSpacer_10, 3, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glay_rgb.addItem(self.verticalSpacer_11, 11, 0, 1, 4)

        self.sb_rgb_blue = QSpinBox(self.fr_body)
        self.sb_rgb_blue.setObjectName(u"sb_rgb_blue")

        self.glay_rgb.addWidget(self.sb_rgb_blue, 9, 2, 1, 1)

        self.lb_rgb_blue = QLabel(self.fr_body)
        self.lb_rgb_blue.setObjectName(u"lb_rgb_blue")

        self.glay_rgb.addWidget(self.lb_rgb_blue, 9, 0, 1, 1)

        self.sb_rgb_green = QSpinBox(self.fr_body)
        self.sb_rgb_green.setObjectName(u"sb_rgb_green")

        self.glay_rgb.addWidget(self.sb_rgb_green, 6, 2, 1, 1)

        self.lb_rgb_red = QLabel(self.fr_body)
        self.lb_rgb_red.setObjectName(u"lb_rgb_red")

        self.glay_rgb.addWidget(self.lb_rgb_red, 3, 0, 1, 1)

        self.lb_rgb_green = QLabel(self.fr_body)
        self.lb_rgb_green.setObjectName(u"lb_rgb_green")

        self.glay_rgb.addWidget(self.lb_rgb_green, 6, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_rgb.addItem(self.horizontalSpacer_12, 9, 1, 1, 1)

        self.sd_rgb_red = QSlider(self.fr_body)
        self.sd_rgb_red.setObjectName(u"sd_rgb_red")
        self.sd_rgb_red.setOrientation(Qt.Horizontal)

        self.glay_rgb.addWidget(self.sd_rgb_red, 4, 0, 1, 3)

        self.sd_rgb_green = QSlider(self.fr_body)
        self.sd_rgb_green.setObjectName(u"sd_rgb_green")
        self.sd_rgb_green.setOrientation(Qt.Horizontal)

        self.glay_rgb.addWidget(self.sd_rgb_green, 7, 0, 1, 3)

        self.sb_rgb_red = QSpinBox(self.fr_body)
        self.sb_rgb_red.setObjectName(u"sb_rgb_red")

        self.glay_rgb.addWidget(self.sb_rgb_red, 3, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_rgb.addItem(self.verticalSpacer_12, 8, 0, 1, 3)

        self.sd_rgb_blue = QSlider(self.fr_body)
        self.sd_rgb_blue.setObjectName(u"sd_rgb_blue")
        self.sd_rgb_blue.setOrientation(Qt.Horizontal)

        self.glay_rgb.addWidget(self.sd_rgb_blue, 10, 0, 1, 3)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_rgb.addItem(self.verticalSpacer_13, 5, 0, 1, 3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_rgb.addItem(self.horizontalSpacer_11, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_rgb.addItem(self.verticalSpacer, 2, 3, 1, 1)


        self.vlay_rgb_body.addLayout(self.glay_rgb)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_rgb_bottom = QFrame(self.fr_main)
        self.fr_rgb_bottom.setObjectName(u"fr_rgb_bottom")
        self.hlay_rgb_bottom = QHBoxLayout(self.fr_rgb_bottom)
        self.hlay_rgb_bottom.setSpacing(2)
        self.hlay_rgb_bottom.setObjectName(u"hlay_rgb_bottom")
        self.hlay_rgb_bottom.setContentsMargins(0, 2, 1, 1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_rgb_bottom.addItem(self.horizontalSpacer)

        self.pb_rgb_ok = QPushButton(self.fr_rgb_bottom)
        self.pb_rgb_ok.setObjectName(u"pb_rgb_ok")

        self.hlay_rgb_bottom.addWidget(self.pb_rgb_ok)

        self.pb_rgb_annuler = QPushButton(self.fr_rgb_bottom)
        self.pb_rgb_annuler.setObjectName(u"pb_rgb_annuler")

        self.hlay_rgb_bottom.addWidget(self.pb_rgb_annuler)


        self.vlay_fr_main.addWidget(self.fr_rgb_bottom)


        self.glay_main.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Rgb)

        QMetaObject.connectSlotsByName(Rgb)
    # setupUi

    def retranslateUi(self, Rgb):
        pass
    # retranslateUi

