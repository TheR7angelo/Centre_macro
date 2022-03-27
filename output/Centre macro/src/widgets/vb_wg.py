from src.config.config import Configue
from src.lib.palettes import *


########################
##     DIMENSIONS     ##
########################
WIDTH = None
HEIGHT = Dim().h9()

####################
##     POLICE     ##
####################
FONT = Configue().cfg["config"]["font"]
FONT_SIZE = Font().h4()
FONT_SIZE_HD = Font().h3()

########################
##     PARAMETRES     ##
########################
BUTTON_SYMBOLS = ButtonSymbols().plus_minus()
DRAG_DROP_MODE = DragDropMode().no_drag()
DROP_ACTION = DropAction().move()
EDIT = False
FOCUS_POLICY = FocusPolicy().strong_focus()
FLOW = Flow().top_to_bottom()
FRAME_SHAPE = FrameShape().no_frame()
FRAME_SHADOW = FrameShadow().plain()
INSERT_POLICY = InsertPolicy().insert_bottom()
MAX_VISIBLE_ITEMS = 10
MAX_LENGTH = 32767
PROGRESS_FORMAT = ProgressFormat().percentage()
SELECTION_BEHAVIOR = SelectionBehavior().row()
SELECTION_MODE = SelectionMode().single()
TEXT_VISIBLE = True
VALUE_MIN = 0
VALUE_MAX = 100
VALUE_STEP = 1
PAGE_STEP = 10
TEXT_FORMAT = TextFormat().plain()
TICK_POSITION = TickPosition().no()
TICK_INTERVAL = 0
WORD_WRAP = True

#####################
##     CURSEUR     ##
#####################
CUR = Cur().Arrow()
CUR_MAIN = Cur().main()
CUR_VIEW = Cur().souris_main()
CUR_VIEWPORT = Cur().Cross()
CUR_LE = Cur().ibeam()

######################
##     COULEURS     ##
######################
# BG
BG = Rgb().th3()
BG_ALTERNATE = Rgb().th2()
BG_HOVER = Rgb().th3()
BG_CHECKED = Rgb().th1()
BG_CHECKED_HOVER = Rgb().th1()
BG_INDETERMINATE = Rgb().th2()
BG_INDETERMINATE_HOVER = Rgb().th2()
BG_PRESSED = Rgb().th3()
BG_CHECKED_PRESSED = Rgb().th1()
BG_SELECTION = Rgb().th1()
# BG item
BG_ITEM = Rgb().th3()
BG_ITEM_HOVER = Rgb().th3()
BG_ITEM_CHECKED = Rgb().th1()
BG_ITEM_CHECKED_HOVER = Rgb().th1()
# BG Autres
BG_CHUNK = Rgb().th2()
BG_CHUNK_HOVER = Rgb().bn1()
BG_GROOVE = Rgb().th3()
BG_GROOVE_HOVER = Rgb().th3()
BG_GROOVE_PRESSED = Rgb().th3()
BG_HANDLE = Rgb().th2()
BG_HANDLE_HOVER = Rgb().th2()
BG_HANDLE_PRESSED = Rgb().bn1()
BG_SEPARATOR = Rgb().bn1()

# FG
FG = Rgb().th1()
FG_HOVER = Rgb().bn1()
FG_CHECKED = Rgb().th3()
FG_CHECKED_HOVER = Rgb().bn1()
FG_INDETERMINATE = Rgb().th3()
FG_INDETERMINATE_HOVER = Rgb().th1()
FG_PRESSED = Rgb().bn1()
FG_CHECKED_PRESSED = Rgb().bn2()
FG_SELECTION = Rgb().th3()
FG_PLACEHOLDER = Rgb().th2()
# FG item
FG_ITEM = Rgb().th1()
FG_ITEM_HOVER = Rgb().bn1()
FG_ITEM_CHECKED = Rgb().th3()
FG_ITEM_CHECKED_HOVER = Rgb().bn1()

# Autres
GRIDLINE = Rgb().th2()

####################
##     IMAGES     ##
####################
# Check
IMG_UNCHECK = Img().check0()
IMG_UNCHECK_HOVER = Img().check0()
IMG_CHECK = Img().check2()
IMG_CHECK_HOVER = Img().check2()
IMG_INDETERMINATE = Img().check1()
IMG_INDETERMINATE_HOVER = Img().check1()
IMG_UNROLL = Img().fleche_bottom()
IMG_UNROLL_HOVER = Img().fleche_bottom()
# Check RGB
IMG_UNCHECK_RGB = "th2"
IMG_UNCHECK_HOVER_RGB = "bn1"
IMG_CHECK_RGB = "th2"
IMG_CHECK_HOVER_RGB = "bn1"
IMG_INDETERMINATE_RGB = "th3"
IMG_INDETERMINATE_HOVER_RGB = "th1"
IMG_UNROLL_RGB = "th2"
IMG_UNROLL_HOVER_RGB = "bn1"

# Fleches
IMG_UP = Img().plus()
IMG_DOWN = Img().moins()
IMG_RIGHT = Img().fleche_droite()
IMG_LEFT = Img().fleche_gauche()
# Fleches RGB
IMG_UP_RGB = "th2"
IMG_UP_HOVER_RGB = "bn1"
IMG_DOWN_RGB = "th2"
IMG_DOWN_HOVER_RGB = "bn1"
IMG_RIGHT_RGB = "th3"
IMG_RIGHT_HOVER_RGB = "bn1"
IMG_LEFT_RGB = "th3"
IMG_LEFT_HOVER_RGB = "bn1"

# img dim
img_width = HEIGHT * StyleBase().x_ico()
IMG_WIDTH = HEIGHT * StyleBase().X_ICO()
img_height = HEIGHT * StyleBase().x_ico()
IMG_HEIGHT = HEIGHT * StyleBase().X_ICO()

#####################
##     BORDURE     ##
#####################
BORDER_WIDTH = (0,) * 4
BORDER_STYLE = "solid"
BORDER_RGB = Rgb().tr()

###################
##     RAYON     ##
###################
RADIUS_SIZE = 3
RADIUS = (RADIUS_SIZE,) * 4

####################
##     SCROLL     ##
####################
SCROLL_BG = Rgb().th1()
SCROLL_WIDTH = 10
SCROLL_HEIGHT = 10

SCROLL_HANDLE_BG = Rgb().th3()
SCROLL_HANDLE_BG_HOVER = Rgb().th3()
SCROLL_HANDLE_FG = Rgb().th2()
SCROLL_HANDLE_FG_HOVER = Rgb().bn1()
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20

SCROLL_H = Scroll().need()
SCROLL_V = Scroll().need()
HEADER_H = True
HEADER_V = True
