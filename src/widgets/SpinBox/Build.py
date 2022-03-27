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
            accelerated=True,
            align_horizontal=Align().center_horizontal(),
            align_vertical=Align().center_vertical(),
            button_symbols=vb_wg.BUTTON_SYMBOLS,
            focus_policy=vb_wg.FOCUS_POLICY,
            frame=False,
            value_min=vb_wg.VALUE_MIN,
            value_max=vb_wg.VALUE_MAX,
            value_step=vb_wg.VALUE_STEP,
            prefix="",
            suffix="",

            # Curseur
            cursor=vb_wg.CUR,
            cursor_le=vb_wg.CUR_LE,

            # Couleurs BG
            bg=vb_wg.BG,
            bg_selection=vb_wg.BG_SELECTION,
            # Couleurs FG
            fg=vb_wg.FG,
            fg_selection=vb_wg.FG_SELECTION,

            # Images
            img_up=vb_wg.IMG_UP,
            img_up_hover=vb_wg.IMG_UP,
            img_down=vb_wg.IMG_DOWN,
            img_down_hover=vb_wg.IMG_DOWN,
            # Images RGB
            img_up_rgb=vb_wg.IMG_UP_RGB,
            img_up_hover_rgb=vb_wg.IMG_UP_HOVER_RGB,
            img_down_rgb=vb_wg.IMG_DOWN_RGB,
            img_down_hover_rgb=vb_wg.IMG_DOWN_HOVER_RGB,
            # Images DIM
            img_up_width=10,
            img_up_height=10,
            img_down_width=10,
            img_down_height=10,
            # Images positions
            img_up_pos=(3, 0, 3, 0),
            img_down_pos=(0, 3, 3, 0),

            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
    ):
        """
        *Align: QtCore.Qt : Align().%nomAlign() \n
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *ButtonSymbols: QtWidgets.QAbstractSpinBox : ButtonSymbols().%nomBouton() \n
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
        :param accelerated: bool()
        :param align_horizontal: *Align
        :param align_vertical: *Align
        :param button_symbols: *ButtonSymbols
        :param focus_policy: *FocusPolicy
        :param frame: bool()
        :param value_min: int()
        :param value_max: int()
        :param value_step: int()
        :param prefix: str()
        :param suffix: str()
        :param cursor: *Cur
        :param cursor_le: *Cur
        :param bg: *RgbBox
        :param bg_selection: *RgbBox
        :param fg: *RgbBox
        :param fg_selection: *RgbBox
        :param img_up: *Img
        :param img_up_hover: *Img
        :param img_down: *Img
        :param img_down_hover: *Img
        :param img_up_rgb: *Img
        :param img_up_hover_rgb: *Img
        :param img_down_rgb: *Img
        :param img_down_hover_rgb: *Img
        :param img_up_width: *Dim
        :param img_up_height: *Dim
        :param img_down_width: *Dim
        :param img_down_height: *Dim
        :param img_up_pos: *Tuple
        :param img_down_pos: *Tuple
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param radius: *Tuple
        """
        
        style = f"""
                /* SPINBOX */
                QSpinBox, QDoubleSpinBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection}
                }}

                QSpinBox::up-button, QDoubleSpinBox::up-button  {{
                subcontrol-position: top right;
                top: {img_up_pos[0]}px;
                bottom: {img_up_pos[1]}px;
                right: {img_up_pos[2]}px;
                left: {img_up_pos[3]}px;
                image: url({f"{img_up}{img_up_rgb}.svg"});
                width: {img_up_width}px;
                height: {img_up_height}px;
                }}
                QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover  {{
                image: url({f"{img_up_hover}{img_up_hover_rgb}.svg"});
                }}

                QSpinBox::down-button, QDoubleSpinBox::down-button  {{
                subcontrol-position: bottom right;
                top: {img_down_pos[0]}px;
                bottom: {img_down_pos[1]}px;
                right: {img_down_pos[2]}px;
                left: {img_down_pos[3]}px;
                image: url({f"{img_down}{img_down_rgb}.svg"});
                width: {img_down_width}px;
                height: {img_down_height}px;
                }}
                QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover  {{
                image: url({f"{img_down_hover}{img_down_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QSpinBox, .QDoubleSpinBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QSpinBox:hover, .QDoubleSpinBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QSpinBox, .QDoubleSpinBox {{
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
            wg.setAccelerated(accelerated)
            wg.setAlignment(align_horizontal | align_vertical)
            wg.setButtonSymbols(button_symbols)
            wg.setFocusPolicy(focus_policy)
            wg.setFrame(frame)
            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)
            wg.setPrefix(prefix)
            wg.setSuffix(suffix)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))
            wg.lineEdit().setCursor(Functions().SET_CURSOR(cursor_le))

            # Style
            wg.setStyleSheet(style)
