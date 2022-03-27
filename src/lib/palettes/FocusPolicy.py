from PySide6.QtCore import Qt


class FocusPolicy:

    def no_focus(self): return Qt.NoFocus
    def tab_focus(self): return Qt.TabFocus
    def click_focus(self): return Qt.ClickFocus
    def strong_focus(self): return Qt.StrongFocus
    def wheel_focus(self): return Qt.WheelFocus
