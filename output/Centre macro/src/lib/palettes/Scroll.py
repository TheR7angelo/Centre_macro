from PySide6.QtCore import Qt


class Scroll:

    def need(self): return Qt.ScrollBarAsNeeded
    def on(self): return Qt.ScrollBarAlwaysOn
    def off(self): return Qt.ScrollBarAlwaysOff
