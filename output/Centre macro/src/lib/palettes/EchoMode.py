from PySide6.QtWidgets import QLineEdit


class EchoMode:

    def normal(self): return QLineEdit.Normal
    def no(self): return QLineEdit.NoEcho
    def password(self): return QLineEdit.Password
    def password_on_edit(self): return QLineEdit.PasswordEchoOnEdit
