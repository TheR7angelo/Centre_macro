from PySide6.QtWidgets import QAbstractItemView


class SelectionMode:

    def no(self): return QAbstractItemView.NoSelection
    def single(self): return QAbstractItemView.SingleSelection
    def multi(self): return QAbstractItemView.MultiSelection
    def extended(self): return QAbstractItemView.ExtendedSelection
    def contiguous(self): return QAbstractItemView.ContiguousSelection
