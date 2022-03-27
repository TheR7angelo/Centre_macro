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

            # Paramètres
            focus_policy=vb_wg.FOCUS_POLICY,
            value_min=vb_wg.VALUE_MIN,
            value_max=vb_wg.VALUE_MAX,
            value_step=vb_wg.VALUE_STEP,
            page_step=vb_wg.PAGE_STEP,
            tick_position=vb_wg.TICK_POSITION,
            tick_interval=vb_wg.TICK_INTERVAL,

            # Curseur
            cursor=vb_wg.CUR,
            
            # Couleurs BG
            bg=vb_wg.BG,
            bg_groove=vb_wg.BG_GROOVE,
            bg_groove_2=None,
            bg_groove_hover=vb_wg.BG_GROOVE_HOVER,
            bg_groove_hover_2=None,
            bg_groove_pressed=vb_wg.BG_GROOVE_PRESSED,
            bg_groove_pressed_2=None,
            bg_handle=vb_wg.BG_HANDLE,
            bg_handle_hover=vb_wg.BG_HANDLE_HOVER,
            bg_handle_pressed=vb_wg.BG_HANDLE_PRESSED,
            gradient=((0,) * 4),
            
            # Dimensions WG
            width_groove=Dim().h9(),
            height_groove=Dim().h9(),
            width_handle_h=Dim().h9(),
            height_handle_h=Dim().h9(),
            width_handle_v=Dim().h9(),
            height_handle_v=Dim().h9(),
            
            # Positions WG
            margin_handle_h=(0,) * 4,
            margin_handle_v=(0,) * 4,
            
            # Bordures
            border=vb_wg.BORDER_WIDTH,
            border_style=vb_wg.BORDER_STYLE,
            border_rgb=vb_wg.BORDER_RGB,
            # Bordures hover
            border_hover=vb_wg.BORDER_WIDTH,
            border_hover_style=vb_wg.BORDER_STYLE,
            border_hover_rgb=vb_wg.BORDER_RGB,
            # Bordures slider
            border_groove=vb_wg.BORDER_WIDTH,
            border_groove_style=vb_wg.BORDER_STYLE,
            border_groove_rgb=vb_wg.BORDER_RGB,
            # Bordures slider h
            border_handle_h=vb_wg.BORDER_WIDTH,
            border_handle_h_style=vb_wg.BORDER_STYLE,
            border_handle_h_rgb=vb_wg.BORDER_RGB,
            # Bordures slider v
            border_handle_v=vb_wg.BORDER_WIDTH,
            border_handle_v_style=vb_wg.BORDER_STYLE,
            border_handle_v_rgb=vb_wg.BORDER_RGB,

            # Rayons
            radius=vb_wg.RADIUS,
            radius_groove_h=vb_wg.RADIUS,
            radius_groove_v=vb_wg.RADIUS,
            radius_handle_h=vb_wg.RADIUS,
            radius_handle_v=vb_wg.RADIUS,
    ):
        """
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *Cur: list() : Cur().%nomCurseur() \n
        *Dim: int() : Dim().%nomDim() \n
        *FocusPolicy: QtCore.Qt : FocusPolicy().%nomFocus \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *TickPosition: QtWidgets.QSlider : TickPosition().%nomTickPosition() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs: Widgets séparés par ","
        :param width: *Dim
        :param height: *Dim
        :param focus_policy: *FocusPolicy
        :param value_min: int()
        :param value_max: int()
        :param value_step: int()
        :param page_step: int()
        :param tick_position: *TickPosition
        :param tick_interval: int()
        :param cursor: *Cur
        :param bg: *RgbBox
        :param bg_groove: *RgbBox
        :param bg_groove_2: *RgbBox
        :param bg_groove_hover: *RgbBox
        :param bg_groove_hover_2: *RgbBox
        :param bg_groove_pressed: *RgbBox
        :param bg_groove_pressed_2: *RgbBox
        :param bg_handle: *RgbBox
        :param bg_handle_hover: *RgbBox
        :param bg_handle_pressed: *RgbBox
        :param gradient: *RgbBox
        :param width_groove: int()
        :param height_groove: int()
        :param width_handle_h: int()
        :param height_handle_h: int()
        :param width_handle_v: int()
        :param height_handle_v: int()
        :param margin_handle_h: *Tuple
        :param margin_handle_v: *Tuple
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_hover: *Tuple
        :param border_hover_style: *Border_Style
        :param border_hover_rgb: *RgbBox
        :param border_groove: *Tuple
        :param border_groove_style: *Border_Style
        :param border_groove_rgb: *RgbBox
        :param border_handle_h: *Tuple
        :param border_handle_h_style: *Border_Style
        :param border_handle_h_rgb: *RgbBox
        :param border_handle_v: *Tuple
        :param border_handle_v_style: *Border_Style
        :param border_handle_v_rgb: *RgbBox
        :param radius: *Tuple
        :param radius_groove_h: *Tuple
        :param radius_groove_v: *Tuple
        :param radius_handle_h: *Tuple
        :param radius_handle_v: *Tuple
        """

        style = f"""
                /* SLIDER  */
                QSlider {{
                background-color: rgba{bg};
                }}

                /* BARRE_H */
                QSlider::groove:horizontal {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                height: {height_groove}px;
                border-top-right-radius: {radius_groove_h[0]}px;
                border-top-left-radius: {radius_groove_h[1]}px;
                border-bottom-right-radius: {radius_groove_h[2]}px;
                border-bottom-left-radius: {radius_groove_h[3]}px;
                border-top: {border_groove[0]}px {border_groove_style} rgba{border_groove_rgb};
                border-bottom: {border_groove[1]}px {border_groove_style} rgba{border_groove_rgb};
                border-right: {border_groove[2]}px {border_groove_style} rgba{border_groove_rgb};
                border-left: {border_groove[3]}px {border_groove_style} rgba{border_groove_rgb};
                }}
                QSlider::groove:horizontal:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:horizontal:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}

                /* CURSEUR_H */
                QSlider::handle:horizontal {{
                background-color: rgba{bg_handle};
                width: {width_handle_h}px;
                height: {height_handle_h}px;
                border-top-right-radius: {radius_handle_h[0]}px;
                border-top-left-radius: {radius_handle_h[1]}px;
                border-bottom-right-radius: {radius_handle_h[2]}px;
                border-bottom-left-radius: {radius_handle_h[3]}px;
                margin-top: {margin_handle_h[0]}px;
                margin-bottom: {margin_handle_h[1]}px;
                margin-right: {margin_handle_h[2]}px;
                margin-left: {margin_handle_h[3]}px;
                border-top: {border_handle_h[0]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-bottom: {border_handle_h[1]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-right: {border_handle_h[2]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-left: {border_handle_h[3]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                }}
                QSlider::handle:horizontal:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:horizontal:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}

                /* BARRE_V */
                QSlider::groove:vertical {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                width: {width_groove}px;
                border-top-right-radius: {radius_groove_v[0]}px;
                border-top-left-radius: {radius_groove_v[1]}px;
                border-bottom-right-radius: {radius_groove_v[2]}px;
                border-bottom-left-radius: {radius_groove_v[3]}px;
                border-top: {border_groove[0]}px {border_groove_style} rgba{border_groove_rgb};
                border-bottom: {border_groove[1]}px {border_groove_style} rgba{border_groove_rgb};
                border-right: {border_groove[2]}px {border_groove_style} rgba{border_groove_rgb};
                border-left: {border_groove[3]}px {border_groove_style} rgba{border_groove_rgb};
                }}
                QSlider::groove:vertical:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:vertical:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}

                /* CURSEUR_V */
                QSlider::handle:vertical {{
                background-color: rgba{bg_handle};
                width: {width_handle_v}px;
                height: {height_handle_v}px;
                border-top-right-radius: {radius_handle_v[0]}px;
                border-top-left-radius: {radius_handle_v[1]}px;
                border-bottom-right-radius: {radius_handle_v[2]}px;
                border-bottom-left-radius: {radius_handle_v[3]}px;
                margin-top: {margin_handle_v[0]}px;
                margin-bottom: {margin_handle_v[1]}px;
                margin-right: {margin_handle_v[2]}px;
                margin-left: {margin_handle_v[3]}px;
                border-top: {border_handle_v[0]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-bottom: {border_handle_v[1]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-right: {border_handle_v[2]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-left: {border_handle_v[3]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                }}
                QSlider::handle:vertical:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:vertical:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}

                /* BORDURES */
                .QSlider {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QSlider:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}

                /* RAYONS */
                .QSlider {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Paramètres
            wg.setFocusPolicy(focus_policy)
            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)
            wg.setPageStep(page_step)
            wg.setTickPosition(tick_position)
            wg.setTickInterval(tick_interval)
            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
