from PySide6 import QtWidgets, QtGui


class Shadow:
    def __init__(self, rgb=(0, 0, 0)):
        self.rgb = rgb

    def glow(self, wg):
        shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(*self.rgb, 255))
        shadow.setOffset(0, 0)
        return shadow
    def perspective(self, wg):
        shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
        shadow.setBlurRadius(6)
        shadow.setColor(QtGui.QColor(*self.rgb, 150))
        shadow.setOffset(3, 3)
        return shadow
    def ombre_portee(self, wg):
        shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
        shadow.setBlurRadius(12)
        shadow.setColor(QtGui.QColor(*self.rgb, 150))
        shadow.setOffset(0, 0)
        return shadow
