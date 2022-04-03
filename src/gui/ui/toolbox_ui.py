# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolbox.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ToolBoxUi(object):
    def setupUi(self, ToolBoxUi):
        if not ToolBoxUi.objectName():
            ToolBoxUi.setObjectName(u"ToolBoxUi")
        ToolBoxUi.resize(446, 791)
        self.vlay_main = QVBoxLayout(ToolBoxUi)
        self.vlay_main.setSpacing(0)
        self.vlay_main.setObjectName(u"vlay_main")
        self.vlay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(ToolBoxUi)
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
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.fr_body = QFrame(self.fr_main)
        self.fr_body.setObjectName(u"fr_body")
        self.vlay_body = QVBoxLayout(self.fr_body)
        self.vlay_body.setSpacing(0)
        self.vlay_body.setObjectName(u"vlay_body")
        self.vlay_body.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_body.addItem(self.verticalSpacer)


        self.vlay_fr_main.addWidget(self.fr_body)


        self.vlay_main.addWidget(self.fr_main)


        self.retranslateUi(ToolBoxUi)

        QMetaObject.connectSlotsByName(ToolBoxUi)
    # setupUi

    def retranslateUi(self, ToolBoxUi):
        pass
    # retranslateUi

