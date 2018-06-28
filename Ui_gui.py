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
        Dialog.resize(316, 295)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.devicesList = QtWidgets.QListWidget(Dialog)
        self.devicesList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.devicesList.setObjectName("devicesList")
        self.gridLayout.addWidget(self.devicesList, 0, 1, 1, 1)
        self.devicesButton = QtWidgets.QPushButton(Dialog)
        self.devicesButton.setObjectName("devicesButton")
        self.gridLayout.addWidget(self.devicesButton, 1, 1, 1, 1)
        self.arpButton = QtWidgets.QPushButton(Dialog)
        self.arpButton.setObjectName("arpButton")
        self.gridLayout.addWidget(self.arpButton, 2, 1, 1, 1)
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 3, 0, 1, 1)
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 3, 1, 1, 1)
        self.ifaceButton = QtWidgets.QPushButton(Dialog)
        self.ifaceButton.setObjectName("ifaceButton")
        self.gridLayout.addWidget(self.ifaceButton, 2, 0, 1, 1)
        self.ifaceList = QtWidgets.QListWidget(Dialog)
        self.ifaceList.setObjectName("ifaceList")
        self.gridLayout.addWidget(self.ifaceList, 0, 0, 2, 1)

        self.retranslateUi(Dialog)
        self.ifaceButton.clicked.connect(Dialog.show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyNetworkBlocker"))
        self.devicesButton.setText(_translate("Dialog", "Ağdaki Cihazları Ara"))
        self.arpButton.setText(_translate("Dialog", "Engelle"))
        self.status.setText(_translate("Dialog", "Status:"))
        self.stop.setText(_translate("Dialog", "Durdur"))
        self.ifaceButton.setText(_translate("Dialog", "Search Interfaces"))

