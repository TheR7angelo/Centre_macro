import datetime

from PySide6 import QtCore

from src.build.mods import Functions
from src.lib.palettes import *
from src.widgets import vb_wg


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=vb_wg.WIDTH,
            height=vb_wg.HEIGHT,

            # Police
            font=vb_wg.FONT,
            font_size=vb_wg.FONT_SIZE,

            # Paramètres
            align_horizontal=Align().center_horizontal(),
            align_vertical=Align().center_vertical(),
            button_symbols=vb_wg.BUTTON_SYMBOLS,
            calendar_popup=True,
            focus_policy=vb_wg.FOCUS_POLICY,

            # Curseur
            cursor=Cur().souris_main(),

            # Couleurs BG
            bg=vb_wg.BG,
            bg_hover=vb_wg.BG_HOVER,
            bg_selection=vb_wg.BG_SELECTION,
            bg_item=vb_wg.BG_ITEM,
            bg_item_hover=vb_wg.BG_ITEM_HOVER,
            bg_header=Rgb().th2(),
            bg_header_hover=Rgb().th2(),
            bg_mois=Rgb().th2(),
            # Couleurs FG
            fg=vb_wg.FG,
            fg_hover=vb_wg.FG_HOVER,
            fg_selection=vb_wg.FG_SELECTION,
            fg_item=vb_wg.FG_ITEM,
            fg_item_hover=vb_wg.FG_ITEM_HOVER,
            fg_header=Rgb().th1(),
            fg_header_hover=Rgb().bn1(),
            fg_mois=Rgb().th1(),

            # Images
            img=vb_wg.IMG_UNROLL,
            img_hover=vb_wg.IMG_UNROLL_HOVER,
            img_right=vb_wg.IMG_RIGHT,
            img_left=vb_wg.IMG_LEFT,
            # Images RGB
            img_rgb=vb_wg.IMG_UNROLL_RGB,
            img_hover_rgb=vb_wg.IMG_UNROLL_HOVER_RGB,
            img_right_rgb=vb_wg.IMG_RIGHT_RGB,
            img_left_rgb=vb_wg.IMG_LEFT_RGB,
            # Images DIM
            img_width=vb_wg.img_width,
            img_height=vb_wg.img_height,
            # Images positions
            img_margin=(0,) * 4,

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures jours
            border_day_size=(StyleBase().border(), )*4,
            border_day_style=vb_wg.BORDER_STYLE,
            border_day_rgb=vb_wg.FG_HOVER,
            # Bordures mois
            border_month_size=(0, StyleBase().border(), 0, 0),
            border_month_style=vb_wg.BORDER_STYLE,
            border_month_rgb=vb_wg.FG_HOVER,

            # Rayons
            radius=vb_wg.RADIUS,
    ):
        """
        *Align: QtCore.Qt : Align().%nomAlign() \n
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *ButtonSymbols: QtWidgets.QAbstractSpinBox : ButtonSymbols().%nomBoutons() \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *FocusPolicy: QtCore.Qt : FocusPolicy().%nomFocus \n
        *Font: int() : Font().%nomFont() \n
        *Img: str() : Img().%nomImage() \n
        *Img_rgb: str() : th1 | th2 | th3 | bn1 | bn2 \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param font: str()
        :param font_size: *Font
        :param align_horizontal: *Align
        :param align_vertical: *Align
        :param button_symbols: *ButtonSymbols
        :param calendar_popup: bool()
        :param focus_policy: *FocusPolicy
        :param cursor: *Cur
        :param bg: *RgbBox
        :param bg_hover: *RgbBox
        :param bg_selection: *RgbBox
        :param bg_item: *RgbBox
        :param bg_item_hover: *RgbBox
        :param bg_header: *RgbBox
        :param bg_header_hover: *RgbBox
        :param bg_mois: *RgbBox
        :param fg: *RgbBox
        :param fg_hover: *RgbBox
        :param fg_selection: *RgbBox
        :param fg_item: *RgbBox
        :param fg_item_hover: *RgbBox
        :param fg_header: *RgbBox
        :param fg_header_hover: *RgbBox
        :param fg_mois: *RgbBox
        :param img: *Img
        :param img_hover: *Img
        :param img_right: *Img
        :param img_left: *Img
        :param img_rgb: *Img_rgb
        :param img_hover_rgb: *Img_rgb
        :param img_right_rgb: *Img_rgb
        :param img_left_rgb: *Img_rgb
        :param img_width: *Dim
        :param img_height: *Dim
        :param img_margin: *Tuple
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param border_day_size: *Tuple
        :param border_day_style: *Border_Style
        :param border_day_rgb: *RgbBox
        :param border_month_size: *Tuple
        :param border_month_style: *Border_Style
        :param border_month_rgb: *RgbBox
        :param radius: *Tuple
        """

        style = f"""
                /* WIDGET */
                QDateEdit {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
                QDateEdit:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* IMG CALENDRIER */
                QDateEdit::drop-down {{
                image: url({f"{img}{img_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                margin-top: {img_margin[0]}px;
                margin-bottom: {img_margin[1]}px;
                margin-right: {img_margin[2]}px;
                margin-left: {img_margin[3]}px;
                }}
                QDateEdit::drop-down:hover {{
                image: url({f"{img_hover}{img_hover_rgb}.svg"});
                }}

                /* WIDGETS */
                QCalendarWidget QWidget {{
                alternate-background-color: rgba{bg_mois};
                color: rgba{fg_mois};
                }}

                /* TOOL BUTTON */
                QCalendarWidget QToolButton {{
                font-size: {font_size}px;
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                }}
                QCalendarWidget QToolButton:hover {{
                background-color: rgba{bg_header_hover};
                color: rgba{fg_header_hover};
                }}

                /* FLECHE GAUCHE DROITE */
                QToolButton#qt_calendar_nextmonth  {{
                qproperty-icon: url({f"{img_right}{img_right_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}
                QToolButton#qt_calendar_prevmonth {{
                qproperty-icon: url({f"{img_left}{img_left_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}

                /* MENU DEROULANT */
                QCalendarWidget QMenu {{
                width: 150px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                }}

                /* SPIN BOX */
                QCalendarWidget QSpinBox {{
                width: 60px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}

                /* JOURS */
                QCalendarWidget QAbstractItemView {{
                font-size: {font_size}px;
                font-family: {font};
                outline: 0px;
                }}
                QCalendarWidget QAbstractItemView:enabled {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                selection-background-color: rgba{fg_item};
                selection-color: rgba{bg_item};
                }}
                QCalendarWidget QWidget::item:hover, QCalendarWidget QWidget::item:selected {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_month_size[0]}px {border_month_style} rgba{border_month_rgb};
                border-bottom: {border_month_size[1]}px {border_month_style} rgba{border_month_rgb};
                border-right: {border_month_size[2]}px {border_month_style} rgba{border_month_rgb};
                border-left: {border_month_size[3]}px {border_month_style} rgba{border_month_rgb};
                }}
                QCalendarWidget QAbstractItemView::item:hover, QCalendarWidget QAbstractItemView::item:selected {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_day_size[0]}px {border_day_style} rgba{border_day_rgb};
                border-bottom: {border_day_size[1]}px {border_day_style} rgba{border_day_rgb};
                border-right: {border_day_size[2]}px {border_day_style} rgba{border_day_rgb};
                border-left: {border_day_size[3]}px {border_day_style} rgba{border_day_rgb};
                }}

                /* BARRE HAUT */
                QCalendarWidget QWidget#qt_calendar_navigationbar {{
                background-color: rgba{bg_header};
                }}

                /* BORDURES */
                QDateEdit {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                QDateEdit:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                QDateEdit {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setAlignment(align_horizontal | align_vertical)
            wg.setButtonSymbols(button_symbols)
            wg.setCalendarPopup(calendar_popup)
            wg.setFocusPolicy(focus_policy)

            dateDuJour = datetime.datetime.now().strftime("%Y_%m_%d").split("_")
            QdateDuJour = QtCore.QDate(int(dateDuJour[0]), int(dateDuJour[1]), int(dateDuJour[2]))
            wg.setDateTime(QtCore.QDateTime(QdateDuJour, QtCore.QTime(0, 0, 0)))
            wg.setDate(QdateDuJour)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))
            wg.lineEdit().setCursor(Functions().SET_CURSOR(vb_wg.CUR_LE))
            wg.calendarWidget().setCursor(Functions().SET_CURSOR(vb_wg.CUR_VIEW))

            # Style
            wg.setStyleSheet(style)
