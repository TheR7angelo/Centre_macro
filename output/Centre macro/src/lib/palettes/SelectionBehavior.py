from PySide6.QtWidgets import QAbstractItemView


class SelectionBehavior:

    def item(self): return QAbstractItemView.SelectItems
    def row(self): return QAbstractItemView.SelectRows
    def column(self): return QAbstractItemView.SelectColumns
