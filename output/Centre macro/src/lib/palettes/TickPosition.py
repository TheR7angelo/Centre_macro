from PySide6.QtWidgets import QSlider


class TickPosition:

    def no(self): return QSlider.NoTicks
    def above(self): return QSlider.TicksAbove
    def left(self): return QSlider.TicksLeft
    def below(self): return QSlider.TicksBelow
    def right(self): return QSlider.TicksRight
    def both_sides(self): return QSlider.TicksBothSides
