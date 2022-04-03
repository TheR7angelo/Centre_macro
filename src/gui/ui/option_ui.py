# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'option.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Option(object):
    def setupUi(self, Option):
        if not Option.objectName():
            Option.setObjectName(u"Option")
        Option.resize(972, 625)
        self.glay_main = QGridLayout(Option)
        self.glay_main.setSpacing(0)
        self.glay_main.setObjectName(u"glay_main")
        self.glay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Option)
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
        self.hlay_opt_body = QHBoxLayout(self.fr_body)
        self.hlay_opt_body.setSpacing(0)
        self.hlay_opt_body.setObjectName(u"hlay_opt_body")
        self.hlay_opt_body.setContentsMargins(1, -1, 1, -1)
        self.trw_option = QTreeWidget(self.fr_body)
        self.trw_option.headerItem().setText(0, "")
        QTreeWidgetItem(self.trw_option)
        QTreeWidgetItem(self.trw_option)
        QTreeWidgetItem(self.trw_option)
        self.trw_option.setObjectName(u"trw_option")

        self.hlay_opt_body.addWidget(self.trw_option)

        self.stk_option = QStackedWidget(self.fr_body)
        self.stk_option.setObjectName(u"stk_option")
        self.pg_opt_configs = QWidget()
        self.pg_opt_configs.setObjectName(u"pg_opt_configs")
        self.vlay_pg_opt_configs = QVBoxLayout(self.pg_opt_configs)
        self.vlay_pg_opt_configs.setSpacing(10)
        self.vlay_pg_opt_configs.setObjectName(u"vlay_pg_opt_configs")
        self.vlay_pg_opt_configs.setContentsMargins(10, 20, 10, 10)
        self.fcb_opt_ft_font = QFontComboBox(self.pg_opt_configs)
        self.fcb_opt_ft_font.setObjectName(u"fcb_opt_ft_font")

        self.vlay_pg_opt_configs.addWidget(self.fcb_opt_ft_font)

        self.fr_opt_cfg_opacity = QFrame(self.pg_opt_configs)
        self.fr_opt_cfg_opacity.setObjectName(u"fr_opt_cfg_opacity")
        self.hlay_opt_fr_opt_cfg_opacity = QHBoxLayout(self.fr_opt_cfg_opacity)
        self.hlay_opt_fr_opt_cfg_opacity.setSpacing(10)
        self.hlay_opt_fr_opt_cfg_opacity.setObjectName(u"hlay_opt_fr_opt_cfg_opacity")
        self.hlay_opt_fr_opt_cfg_opacity.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_cfg_opacity = QLabel(self.fr_opt_cfg_opacity)
        self.lb_opt_cfg_opacity.setObjectName(u"lb_opt_cfg_opacity")

        self.hlay_opt_fr_opt_cfg_opacity.addWidget(self.lb_opt_cfg_opacity)

        self.sb_opt_cfg_opacity = QSpinBox(self.fr_opt_cfg_opacity)
        self.sb_opt_cfg_opacity.setObjectName(u"sb_opt_cfg_opacity")

        self.hlay_opt_fr_opt_cfg_opacity.addWidget(self.sb_opt_cfg_opacity)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_opt_fr_opt_cfg_opacity.addItem(self.horizontalSpacer_7)


        self.vlay_pg_opt_configs.addWidget(self.fr_opt_cfg_opacity)

        self.fr_opt_cfg_autoclose = QFrame(self.pg_opt_configs)
        self.fr_opt_cfg_autoclose.setObjectName(u"fr_opt_cfg_autoclose")
        self.glay_fr_opt_cfg_autoclose = QGridLayout(self.fr_opt_cfg_autoclose)
        self.glay_fr_opt_cfg_autoclose.setSpacing(5)
        self.glay_fr_opt_cfg_autoclose.setObjectName(u"glay_fr_opt_cfg_autoclose")
        self.glay_fr_opt_cfg_autoclose.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_cfg_autoclose = QLabel(self.fr_opt_cfg_autoclose)
        self.lb_opt_cfg_autoclose.setObjectName(u"lb_opt_cfg_autoclose")

        self.glay_fr_opt_cfg_autoclose.addWidget(self.lb_opt_cfg_autoclose, 1, 0, 1, 1)

        self.lb_opt_cfg_debug = QLabel(self.fr_opt_cfg_autoclose)
        self.lb_opt_cfg_debug.setObjectName(u"lb_opt_cfg_debug")

        self.glay_fr_opt_cfg_autoclose.addWidget(self.lb_opt_cfg_debug, 0, 0, 1, 1)

        self.ck_opt_cfg_autoclose = QCheckBox(self.fr_opt_cfg_autoclose)
        self.ck_opt_cfg_autoclose.setObjectName(u"ck_opt_cfg_autoclose")

        self.glay_fr_opt_cfg_autoclose.addWidget(self.ck_opt_cfg_autoclose, 1, 1, 1, 1)

        self.ck_opt_cfg_debug = QCheckBox(self.fr_opt_cfg_autoclose)
        self.ck_opt_cfg_debug.setObjectName(u"ck_opt_cfg_debug")

        self.glay_fr_opt_cfg_autoclose.addWidget(self.ck_opt_cfg_debug, 0, 1, 1, 1)

        self.lb_opt_cfg_ui_pin = QLabel(self.fr_opt_cfg_autoclose)
        self.lb_opt_cfg_ui_pin.setObjectName(u"lb_opt_cfg_ui_pin")

        self.glay_fr_opt_cfg_autoclose.addWidget(self.lb_opt_cfg_ui_pin, 2, 0, 1, 1)

        self.ck_opt_cfg_ui_pin = QCheckBox(self.fr_opt_cfg_autoclose)
        self.ck_opt_cfg_ui_pin.setObjectName(u"ck_opt_cfg_ui_pin")

        self.glay_fr_opt_cfg_autoclose.addWidget(self.ck_opt_cfg_ui_pin, 2, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_fr_opt_cfg_autoclose.addItem(self.horizontalSpacer_10, 0, 2, 3, 1)


        self.vlay_pg_opt_configs.addWidget(self.fr_opt_cfg_autoclose)

        self.fr_opt_cfg_resize = QFrame(self.pg_opt_configs)
        self.fr_opt_cfg_resize.setObjectName(u"fr_opt_cfg_resize")
        self.glay_fr_opt_cfg_resize = QGridLayout(self.fr_opt_cfg_resize)
        self.glay_fr_opt_cfg_resize.setSpacing(5)
        self.glay_fr_opt_cfg_resize.setObjectName(u"glay_fr_opt_cfg_resize")
        self.glay_fr_opt_cfg_resize.setContentsMargins(5, 5, 5, 5)
        self.lb_opt_cfg_resize = QLabel(self.fr_opt_cfg_resize)
        self.lb_opt_cfg_resize.setObjectName(u"lb_opt_cfg_resize")

        self.glay_fr_opt_cfg_resize.addWidget(self.lb_opt_cfg_resize, 0, 0, 1, 1)

        self.ck_opt_cfg_resize = QCheckBox(self.fr_opt_cfg_resize)
        self.ck_opt_cfg_resize.setObjectName(u"ck_opt_cfg_resize")

        self.glay_fr_opt_cfg_resize.addWidget(self.ck_opt_cfg_resize, 0, 1, 1, 1)

        self.lb_opt_cfg_resize_width = QLabel(self.fr_opt_cfg_resize)
        self.lb_opt_cfg_resize_width.setObjectName(u"lb_opt_cfg_resize_width")

        self.glay_fr_opt_cfg_resize.addWidget(self.lb_opt_cfg_resize_width, 1, 0, 1, 1)

        self.lb_opt_cfg_resize_height = QLabel(self.fr_opt_cfg_resize)
        self.lb_opt_cfg_resize_height.setObjectName(u"lb_opt_cfg_resize_height")

        self.glay_fr_opt_cfg_resize.addWidget(self.lb_opt_cfg_resize_height, 2, 0, 1, 1)

        self.sb_opt_cfg_resize_width = QSpinBox(self.fr_opt_cfg_resize)
        self.sb_opt_cfg_resize_width.setObjectName(u"sb_opt_cfg_resize_width")

        self.glay_fr_opt_cfg_resize.addWidget(self.sb_opt_cfg_resize_width, 1, 1, 1, 1)

        self.sb_opt_cfg_resize_height = QSpinBox(self.fr_opt_cfg_resize)
        self.sb_opt_cfg_resize_height.setObjectName(u"sb_opt_cfg_resize_height")

        self.glay_fr_opt_cfg_resize.addWidget(self.sb_opt_cfg_resize_height, 2, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_fr_opt_cfg_resize.addItem(self.horizontalSpacer_11, 0, 2, 3, 1)


        self.vlay_pg_opt_configs.addWidget(self.fr_opt_cfg_resize)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_configs.addItem(self.verticalSpacer_14)

        self.stk_option.addWidget(self.pg_opt_configs)
        self.pg_opt_themes = QWidget()
        self.pg_opt_themes.setObjectName(u"pg_opt_themes")
        self.vlay_pg_opt_themes = QVBoxLayout(self.pg_opt_themes)
        self.vlay_pg_opt_themes.setSpacing(10)
        self.vlay_pg_opt_themes.setObjectName(u"vlay_pg_opt_themes")
        self.vlay_pg_opt_themes.setContentsMargins(10, 20, 10, 10)
        self.cb_opt_tm_theme = QComboBox(self.pg_opt_themes)
        self.cb_opt_tm_theme.setObjectName(u"cb_opt_tm_theme")

        self.vlay_pg_opt_themes.addWidget(self.cb_opt_tm_theme)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_themes.addItem(self.verticalSpacer_15)

        self.hlay_opt_tm_colors = QHBoxLayout()
        self.hlay_opt_tm_colors.setSpacing(0)
        self.hlay_opt_tm_colors.setObjectName(u"hlay_opt_tm_colors")
        self.pb_opt_tm_th1 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_th1.setObjectName(u"pb_opt_tm_th1")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_th1)

        self.pb_opt_tm_th2 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_th2.setObjectName(u"pb_opt_tm_th2")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_th2)

        self.pb_opt_tm_th3 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_th3.setObjectName(u"pb_opt_tm_th3")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_th3)

        self.pb_opt_tm_bn1 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_bn1.setObjectName(u"pb_opt_tm_bn1")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_bn1)

        self.pb_opt_tm_bn2 = QPushButton(self.pg_opt_themes)
        self.pb_opt_tm_bn2.setObjectName(u"pb_opt_tm_bn2")

        self.hlay_opt_tm_colors.addWidget(self.pb_opt_tm_bn2)


        self.vlay_pg_opt_themes.addLayout(self.hlay_opt_tm_colors)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_themes.addItem(self.verticalSpacer_16)

        self.stk_option.addWidget(self.pg_opt_themes)
        self.pg_opt_infos = QWidget()
        self.pg_opt_infos.setObjectName(u"pg_opt_infos")
        self.vlay_pg_opt_infos = QVBoxLayout(self.pg_opt_infos)
        self.vlay_pg_opt_infos.setSpacing(0)
        self.vlay_pg_opt_infos.setObjectName(u"vlay_pg_opt_infos")
        self.vlay_pg_opt_infos.setContentsMargins(10, 20, 10, 10)
        self.lb_opt_info_nom = QLabel(self.pg_opt_infos)
        self.lb_opt_info_nom.setObjectName(u"lb_opt_info_nom")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_nom)

        self.verticalSpacer_17 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pg_opt_infos.addItem(self.verticalSpacer_17)

        self.lb_opt_info_desc = QLabel(self.pg_opt_infos)
        self.lb_opt_info_desc.setObjectName(u"lb_opt_info_desc")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_desc)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_pg_opt_infos.addItem(self.verticalSpacer_18)

        self.lb_opt_info_auteur = QLabel(self.pg_opt_infos)
        self.lb_opt_info_auteur.setObjectName(u"lb_opt_info_auteur")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_auteur)

        self.lb_opt_info_version = QLabel(self.pg_opt_infos)
        self.lb_opt_info_version.setObjectName(u"lb_opt_info_version")

        self.vlay_pg_opt_infos.addWidget(self.lb_opt_info_version)

        self.stk_option.addWidget(self.pg_opt_infos)

        self.hlay_opt_body.addWidget(self.stk_option)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_opt_bottom = QFrame(self.fr_main)
        self.fr_opt_bottom.setObjectName(u"fr_opt_bottom")
        self.hlay_opt_bottom = QHBoxLayout(self.fr_opt_bottom)
        self.hlay_opt_bottom.setSpacing(2)
        self.hlay_opt_bottom.setObjectName(u"hlay_opt_bottom")
        self.hlay_opt_bottom.setContentsMargins(0, 2, 1, 1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_opt_bottom.addItem(self.horizontalSpacer)

        self.pb_opt_appliquer = QPushButton(self.fr_opt_bottom)
        self.pb_opt_appliquer.setObjectName(u"pb_opt_appliquer")

        self.hlay_opt_bottom.addWidget(self.pb_opt_appliquer)

        self.pb_opt_ok = QPushButton(self.fr_opt_bottom)
        self.pb_opt_ok.setObjectName(u"pb_opt_ok")

        self.hlay_opt_bottom.addWidget(self.pb_opt_ok)


        self.vlay_fr_main.addWidget(self.fr_opt_bottom)


        self.glay_main.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Option)

        self.stk_option.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Option)
    # setupUi

    def retranslateUi(self, Option):

        __sortingEnabled = self.trw_option.isSortingEnabled()
        self.trw_option.setSortingEnabled(False)
        ___qtreewidgetitem = self.trw_option.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Option", u"Configs", None));
        ___qtreewidgetitem1 = self.trw_option.topLevelItem(1)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Option", u"Th\u00e8mes", None));
        ___qtreewidgetitem2 = self.trw_option.topLevelItem(2)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Option", u"Infos", None));
        self.trw_option.setSortingEnabled(__sortingEnabled)

        self.lb_opt_cfg_opacity.setText(QCoreApplication.translate("Option", u"Opacit\u00e9 ", None))
        self.lb_opt_cfg_autoclose.setText(QCoreApplication.translate("Option", u"Auto close : ", None))
        self.lb_opt_cfg_debug.setText(QCoreApplication.translate("Option", u"Debug : ", None))
        self.lb_opt_cfg_ui_pin.setText(QCoreApplication.translate("Option", u"ToolBox Pin :", None))
        self.lb_opt_cfg_resize.setText(QCoreApplication.translate("Option", u"Manuel : ", None))
        self.lb_opt_cfg_resize_width.setText(QCoreApplication.translate("Option", u"Largeur : ", None))
        self.lb_opt_cfg_resize_height.setText(QCoreApplication.translate("Option", u"Hauteur : ", None))
        self.pb_opt_tm_th1.setText(QCoreApplication.translate("Option", u"TH1", None))
        self.pb_opt_tm_th2.setText(QCoreApplication.translate("Option", u"TH2", None))
        self.pb_opt_tm_th3.setText(QCoreApplication.translate("Option", u"TH3", None))
        self.pb_opt_tm_bn1.setText(QCoreApplication.translate("Option", u"BN1", None))
        self.pb_opt_tm_bn2.setText(QCoreApplication.translate("Option", u"BN2", None))
        pass
    # retranslateUi

