from PySide6.QtWidgets import QTextEdit


class AutoFormating:

    def none(self): return QTextEdit.AutoNone
    def bullet_list(self): return QTextEdit.AutoBulletList
    def all(self): return QTextEdit.AutoAll
