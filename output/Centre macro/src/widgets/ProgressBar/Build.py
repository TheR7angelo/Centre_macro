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
            progress_format=vb_wg.PROGRESS_FORMAT,
            text_visible=vb_wg.TEXT_VISIBLE,
            value_min=vb_wg.VALUE_MIN,
            value_max=vb_wg.VALUE_MAX,

            # Curseur
            cursor=Cur().Arrow(),

            # Couleurs BG
            bg=vb_wg.BG,
            bg_chunk=vb_wg.BG_CHUNK,
            bg_chunk_hover=vb_wg.BG_CHUNK_HOVER,
            # Couleurs FG
            fg=vb_wg.FG,

            # Positions WG
            padding=(0,) * 4,

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
            radius_chunk=vb_wg.RADIUS
    ):
        """
        *Align: QtCore.Qt : Align().%nomAlign() \n
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *FocusPolicy: QtCore.Qt : FocusPolicy().%nomFocus \n
        *Font: int() : Font().%nomFont() \n
        *ProgressFormat: str() : ProgressFormat().%nomProgress() \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param font: str()
        :param font_size: *Font
        :param align_horizontal: *Align
        :param align_vertical: *Align
        :param progress_format: *ProgressFormat
        :param text_visible: bool()
        :param value_min: int()
        :param value_max: int()
        :param cursor: *Cur
        :param bg: *RgbBox
        :param bg_chunk: *RgbBox
        :param bg_chunk_hover: *RgbBox
        :param fg: *RgbBox
        :param padding: *Tuple
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param radius: *Tuple
        :param radius_chunk: *Tuple
        """

        style = f"""
                /* PROGRESSBAR */
                QProgressBar {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}

                /* PROGRESS */
                QProgressBar::chunk {{
                background-color: rgba{bg_chunk};
                border-top-right-radius: {radius_chunk[0]}px;
                border-top-left-radius: {radius_chunk[1]}px;
                border-bottom-right-radius: {radius_chunk[2]}px;
                border-bottom-left-radius: {radius_chunk[3]}px;
                }}
                QProgressBar::chunk:hover {{
                background-color: rgba{bg_chunk_hover};
                }}

                /* BORDURES */
                .QProgressBar {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                }}
                .QProgressBar:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QProgressBar {{
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
            wg.setFormat(progress_format)
            wg.setTextVisible(text_visible)
            wg.setMinimum(value_min)
            wg.setMaximum(value_max)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
