# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rep.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Rep(object):
    def setupUi(self, Rep):
        if not Rep.objectName():
            Rep.setObjectName(u"Rep")
        Rep.resize(773, 261)
        self.glay_main = QGridLayout(Rep)
        self.glay_main.setSpacing(0)
        self.glay_main.setObjectName(u"glay_main")
        self.glay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Rep)
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
        self.vlay_rep_body = QVBoxLayout(self.fr_body)
        self.vlay_rep_body.setSpacing(0)
        self.vlay_rep_body.setObjectName(u"vlay_rep_body")
        self.vlay_rep_body.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_rep_body.addItem(self.verticalSpacer_2)

        self.lb_rep_text = QLabel(self.fr_body)
        self.lb_rep_text.setObjectName(u"lb_rep_text")

        self.vlay_rep_body.addWidget(self.lb_rep_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_rep_body.addItem(self.verticalSpacer)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_rep_bottom = QFrame(self.fr_main)
        self.fr_rep_bottom.setObjectName(u"fr_rep_bottom")
        self.hlay_rep_bottom = QHBoxLayout(self.fr_rep_bottom)
        self.hlay_rep_bottom.setSpacing(2)
        self.hlay_rep_bottom.setObjectName(u"hlay_rep_bottom")
        self.hlay_rep_bottom.setContentsMargins(0, 2, 1, 1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_rep_bottom.addItem(self.horizontalSpacer)

        self.pb_rep_ok = QPushButton(self.fr_rep_bottom)
        self.pb_rep_ok.setObjectName(u"pb_rep_ok")

        self.hlay_rep_bottom.addWidget(self.pb_rep_ok)

        self.pb_rep_annuler = QPushButton(self.fr_rep_bottom)
        self.pb_rep_annuler.setObjectName(u"pb_rep_annuler")

        self.hlay_rep_bottom.addWidget(self.pb_rep_annuler)


        self.vlay_fr_main.addWidget(self.fr_rep_bottom)


        self.glay_main.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Rep)

        QMetaObject.connectSlotsByName(Rep)
    # setupUi

    def retranslateUi(self, Rep):
        pass
    # retranslateUi

