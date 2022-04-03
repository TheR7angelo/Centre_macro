# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(768, 449)
        self.vlay_main = QVBoxLayout(SplashScreen)
        self.vlay_main.setSpacing(0)
        self.vlay_main.setObjectName(u"vlay_main")
        self.vlay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(SplashScreen)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(5, 0, 5, 5)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_fr_main.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_description = QLabel(self.fr_main)
        self.lb_description.setObjectName(u"lb_description")

        self.gridLayout.addWidget(self.lb_description, 1, 1, 1, 1)

        self.lb_titre = QLabel(self.fr_main)
        self.lb_titre.setObjectName(u"lb_titre")

        self.gridLayout.addWidget(self.lb_titre, 0, 1, 1, 1)

        self.lb_ico = QLabel(self.fr_main)
        self.lb_ico.setObjectName(u"lb_ico")

        self.gridLayout.addWidget(self.lb_ico, 0, 0, 2, 1)


        self.vlay_fr_main.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_fr_main.addItem(self.verticalSpacer_2)

        self.lb_chargement = QLabel(self.fr_main)
        self.lb_chargement.setObjectName(u"lb_chargement")

        self.vlay_fr_main.addWidget(self.lb_chargement)

        self.pg_chargement = QProgressBar(self.fr_main)
        self.pg_chargement.setObjectName(u"pg_chargement")
        self.pg_chargement.setValue(0)

        self.vlay_fr_main.addWidget(self.pg_chargement)


        self.vlay_main.addWidget(self.fr_main)


        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        pass
    # retranslateUi

