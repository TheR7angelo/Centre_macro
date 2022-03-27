from PySide6 import QtWidgets


class InsertPolicy:

    def no_insert(self): return QtWidgets.QComboBox.NoInsert
    def insert_top(self): return QtWidgets.QComboBox.InsertAtTop
    def insert_bottom(self): return QtWidgets.QComboBox.InsertAtBottom
    def insert_current(self): return QtWidgets.QComboBox.InsertAtCurrent
    def insert_after_current(self): return QtWidgets.QComboBox.InsertAfterCurrent
    def insert_before_current(self): return QtWidgets.QComboBox.InsertBeforeCurrent
    def insert_alphabetically(self): return QtWidgets.QComboBox.InsertAlphabetically
