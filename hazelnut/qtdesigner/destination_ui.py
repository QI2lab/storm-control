# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'destination.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(654, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 220))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 220))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.shareButton = QtWidgets.QRadioButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shareButton.sizePolicy().hasHeightForWidth())
        self.shareButton.setSizePolicy(sizePolicy)
        self.shareButton.setText("")
        self.shareButton.setChecked(False)
        self.shareButton.setObjectName("shareButton")
        self.horizontalLayout.addWidget(self.shareButton)
        self.shareGroupBox = QtWidgets.QGroupBox(Dialog)
        self.shareGroupBox.setObjectName("shareGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.shareGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.directoryButton = QtWidgets.QPushButton(self.shareGroupBox)
        self.directoryButton.setObjectName("directoryButton")
        self.verticalLayout.addWidget(self.directoryButton)
        self.horizontalLayout.addWidget(self.shareGroupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sftpButton = QtWidgets.QRadioButton(Dialog)
        self.sftpButton.setText("")
        self.sftpButton.setChecked(True)
        self.sftpButton.setObjectName("sftpButton")
        self.horizontalLayout_2.addWidget(self.sftpButton)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.addressLabel = QtWidgets.QLabel(self.groupBox)
        self.addressLabel.setObjectName("addressLabel")
        self.gridLayout.addWidget(self.addressLabel, 0, 0, 1, 1)
        self.addressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.gridLayout.addWidget(self.addressLineEdit, 0, 1, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(self.groupBox)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 0, 1, 1)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.gridLayout.addWidget(self.usernameLineEdit, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.shareGroupBox.setTitle(_translate("Dialog", "Local Share"))
        self.directoryButton.setText(_translate("Dialog", "NA"))
        self.groupBox.setTitle(_translate("Dialog", "SFTP"))
        self.addressLabel.setText(_translate("Dialog", "Address"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))

