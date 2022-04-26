from PySide6 import QtWidgets, QtCore


class DateDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent=None, input_format="yyyy-MM-dd", output_format="dd/MM/yyyy"):
        super(DateDelegate, self).__init__(parent)
        self.input_format = input_format
        self.output_format = output_format

    def createEditor(self, parent, option, index):
        widget = QtWidgets.QDateEdit(parent)
        widget.setCalendarPopup(True)
        return widget

    def setEditorData(self, editor, index):
        if isinstance(editor, QtWidgets.QDateEdit):
            dt_str = index.data(QtCore.Qt.EditRole)
            if dt_str == "" or dt_str is None:
                dt = QtCore.QDate().currentDate().toPython()
            else:
                dt = QtCore.QDate().fromString(dt_str, self.input_format).toPython()
            editor.setDate(dt)
            return
        super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QtWidgets.QDateEdit):
            dt = editor.date().toString(self.input_format)
            model.setData(index, dt, QtCore.Qt.EditRole)
            return
        super().setModelData(editor, model, index)

    def displayText(self, value, locale):
        return QtCore.QDate().fromString(value, self.input_format).toString(self.output_format)

class FloatDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent=None, decimal=1, step=0.1):
        super(FloatDelegate, self).__init__(parent)
        self.decimal = decimal
        self.step = step

    def createEditor(self, parent, option, index):
        widget = QtWidgets.QDoubleSpinBox(parent)
        widget.setDecimals(self.decimal)
        widget.setSingleStep(self.step)
        return widget

class ReadOnlyDelegate(QtWidgets.QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        return