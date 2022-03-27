from PySide6.QtWidgets import QAbstractItemView


class DragDropMode:

    def no_drag(self): return QAbstractItemView.NoDragDrop
    def drag_only(self): return QAbstractItemView.DragOnly
    def drop_only(self): return QAbstractItemView.DropOnly
    def drag_and_drop(self): return QAbstractItemView.DragDrop
    def internal_move(self): return QAbstractItemView.InternalMove
