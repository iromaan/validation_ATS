# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Rentgen\enter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setModal(False)
        self.oneButton = QtWidgets.QPushButton(Menu)
        self.oneButton.setGeometry(QtCore.QRect(100, 220, 121, 51))
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(Menu)
        self.twoButton.setGeometry(QtCore.QRect(290, 220, 141, 51))
        self.twoButton.setObjectName("twoButton")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Dialog"))
        self.oneButton.setText(_translate("Menu", "Одна рентгенограмма"))
        self.twoButton.setText(_translate("Menu", "Группа рентгенограмм"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui =  Ui_Menu()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
