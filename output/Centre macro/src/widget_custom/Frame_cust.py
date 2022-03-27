from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame
from src.widgets.Frame import Frame

from src import Rgb


class Button_frame(QFrame):

    clicked = Signal()

    def __init__(self, *args, **kwargs):
        # super(Button_frame, self).__init__(parent)
        QFrame.__init__(self, *args, **kwargs)

        style = Frame.button.retour(self).replace(".QFrame", ".Button_frame")

        self.setStyleSheet(style)

        # print(Frame.button.retour(self))

    def mousePressEvent(self, event):
        self.clicked.emit()
