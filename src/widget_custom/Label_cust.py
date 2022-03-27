import mimetypes

from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel


class DropLabel(QLabel):

    new_ico = Signal(object)
    clicked = Signal()

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)

    def is_url_image(self, url):
        mimetype, encoding = mimetypes.guess_type(url)
        return (mimetype and mimetype.startswith('image'))

    def mousePressEvent(self, event):
        self.clicked.emit()

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        url = data.urls()[0].toLocalFile()
        if self.is_url_image(url):
            self.setPixmap(QPixmap(url))
            self.new_ico.emit(url)
        else:

            self.new_ico.emit(None)
        event.acceptProposedAction()
