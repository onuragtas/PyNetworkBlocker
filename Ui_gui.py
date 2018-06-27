# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/onuragtas/Workspace/arPython/gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(563, 332)
        self.ifaceButton = QtWidgets.QPushButton(Dialog)
        self.ifaceButton.setGeometry(QtCore.QRect(10, 210, 251, 27))
        self.ifaceButton.setObjectName("ifaceButton")
        self.devicesList = QtWidgets.QListWidget(Dialog)
        self.devicesList.setGeometry(QtCore.QRect(300, 10, 256, 251))
        self.devicesList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.devicesList.setObjectName("devicesList")
        self.devicesButton = QtWidgets.QPushButton(Dialog)
        self.devicesButton.setGeometry(QtCore.QRect(310, 270, 251, 27))
        self.devicesButton.setObjectName("devicesButton")
        self.arpButton = QtWidgets.QPushButton(Dialog)
        self.arpButton.setGeometry(QtCore.QRect(310, 300, 121, 27))
        self.arpButton.setObjectName("arpButton")
        self.ifaceList = QtWidgets.QListWidget(Dialog)
        self.ifaceList.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.ifaceList.setObjectName("ifaceList")
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(436, 300, 121, 27))
        self.stop.setObjectName("stop")

        self.retranslateUi(Dialog)
        self.ifaceButton.clicked.connect(Dialog.show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyNetworkBlocker"))
        self.ifaceButton.setText(_translate("Dialog", "Search Interfaces"))
        self.devicesButton.setText(_translate("Dialog", "Ağdaki Cihazları Ara"))
        self.arpButton.setText(_translate("Dialog", "Engelle"))
        self.stop.setText(_translate("Dialog", "Durdur"))

