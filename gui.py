# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri May 17 09:18:58 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(669, 340)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.serverInput = QtGui.QLineEdit(self.groupBox)
        self.serverInput.setObjectName(_fromUtf8("serverInput"))
        self.gridLayout_2.addWidget(self.serverInput, 0, 1, 1, 1)
        self.serverPortInput = QtGui.QSpinBox(self.groupBox)
        self.serverPortInput.setMinimumSize(QtCore.QSize(100, 0))
        self.serverPortInput.setMaximum(63535)
        self.serverPortInput.setProperty("value", 995)
        self.serverPortInput.setObjectName(_fromUtf8("serverPortInput"))
        self.gridLayout_2.addWidget(self.serverPortInput, 0, 2, 1, 1)
        self.protocolComboBox = QtGui.QComboBox(self.groupBox)
        self.protocolComboBox.setObjectName(_fromUtf8("protocolComboBox"))
        self.protocolComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.protocolComboBox, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.usernameInput = QtGui.QLineEdit(self.groupBox_2)
        self.usernameInput.setObjectName(_fromUtf8("usernameInput"))
        self.gridLayout.addWidget(self.usernameInput, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.passwordInput = QtGui.QLineEdit(self.groupBox_3)
        self.passwordInput.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordInput.setObjectName(_fromUtf8("passwordInput"))
        self.gridLayout_3.addWidget(self.passwordInput, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.folderLabel = QtGui.QLabel(self.groupBox_4)
        self.folderLabel.setText(_fromUtf8(""))
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.horizontalLayout.addWidget(self.folderLabel)
        self.selectFolderButton = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectFolderButton.sizePolicy().hasHeightForWidth())
        self.selectFolderButton.setSizePolicy(sizePolicy)
        self.selectFolderButton.setMinimumSize(QtCore.QSize(100, 0))
        self.selectFolderButton.setObjectName(_fromUtf8("selectFolderButton"))
        self.horizontalLayout.addWidget(self.selectFolderButton)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.beginButton = QtGui.QPushButton(self.centralwidget)
        self.beginButton.setCheckable(True)
        self.beginButton.setObjectName(_fromUtf8("beginButton"))
        self.verticalLayout_7.addWidget(self.beginButton)
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.verticalLayout_7.addWidget(self.statusLabel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mail attachment downloader", None))
        self.groupBox.setTitle(_translate("MainWindow", "Server", None))
        self.serverInput.setText(_translate("MainWindow", "pop.gmail.com", None))
        self.protocolComboBox.setItemText(0, _translate("MainWindow", "pop3 ssl", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Username", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Password", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Destination folder", None))
        self.selectFolderButton.setText(_translate("MainWindow", "Select folder", None))
        self.beginButton.setText(_translate("MainWindow", "Begin", None))

import resources_rc
