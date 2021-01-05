# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Rentgen\two.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_two(object):
    def setupUi(self, Dialog):
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(40, 60, 421, 311))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 61, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 410, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        """
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Результат:"))
        self.pushButton.setText(_translate("Dialog", "Сохранить результаты"))
        self.pushButton_2.setText(_translate("Dialog", "Выход"))
        """
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui =  Ui_two()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
