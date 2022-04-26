import sys
from PySide6 import QtSql, QtWidgets, QtCore


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(':memory:')

    if not db.open():
        print('could not open')
        return False

    query = QtSql.QSqlQuery()

    query.exec_("create table sportsmen(id int primary key, "
                "firstname varchar(20), lastname varchar(20))")

    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
    return db


class Table(QtSql.QSqlTableModel):
    def __init__(self):
        super(Table, self).__init__()
        self.setTable("sportsmen")
        self.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)

        self.database().driver().notification[
            str, QtSql.QSqlDriver.NotificationSource, "QVariant"
        ].connect(self.onNotification)
        self.database().driver().subscribeToNotification("sportsmen")

    @QtCore.Slot(str, QtSql.QSqlDriver.NotificationSource, "QVariant")
    def onNotification(self, name, source, payload):
        print(name, source, payload)


def addrow():
    print(model.rowCount())
    record = model.record()
    model.insertRecord(-1, record)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    db = createDB()

    model = Table()
    view = QtWidgets.QTableView()
    view.setModel(model)
    model.select()

    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view)

    button = QtWidgets.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtWidgets.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.show()
    sys.exit(app.exec_())