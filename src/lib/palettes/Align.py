from PySide6.QtCore import Qt


class Align:

    def center(self): return Qt.AlignCenter
    def center_horizontal(self): return Qt.AlignHCenter
    def center_vertical(self): return Qt.AlignVCenter
    def top(self): return Qt.AlignTop
    def bottom(self): return Qt.AlignBottom
    def right(self): return Qt.AlignRight
    def left(self): return Qt.AlignLeft
