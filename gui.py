# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Mar 31 10:58:00 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(696, 318)
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
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.serverInput = QtGui.QLineEdit(self.groupBox)
        self.serverInput.setObjectName(_fromUtf8("serverInput"))
        self.gridLayout_2.addWidget(self.serverInput, 0, 0, 1, 1)
        self.serverPortInput = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverPortInput.sizePolicy().hasHeightForWidth())
        self.serverPortInput.setSizePolicy(sizePolicy)
        self.serverPortInput.setObjectName(_fromUtf8("serverPortInput"))
        self.gridLayout_2.addWidget(self.serverPortInput, 0, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
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
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
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
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.selectFolderButton = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectFolderButton.sizePolicy().hasHeightForWidth())
        self.selectFolderButton.setSizePolicy(sizePolicy)
        self.selectFolderButton.setMinimumSize(QtCore.QSize(160, 0))
        self.selectFolderButton.setObjectName(_fromUtf8("selectFolderButton"))
        self.horizontalLayout.addWidget(self.selectFolderButton)
        self.folderLabel = QtGui.QLabel(self.groupBox_4)
        self.folderLabel.setText(_fromUtf8(""))
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.horizontalLayout.addWidget(self.folderLabel)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.beginButton = QtGui.QPushButton(self.centralwidget)
        self.beginButton.setObjectName(_fromUtf8("beginButton"))
        self.verticalLayout_7.addWidget(self.beginButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mail attachment downloader", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.serverPortInput.setText(QtGui.QApplication.translate("MainWindow", "110", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Destination folder", None, QtGui.QApplication.UnicodeUTF8))
        self.selectFolderButton.setText(QtGui.QApplication.translate("MainWindow", "Select folder", None, QtGui.QApplication.UnicodeUTF8))
        self.beginButton.setText(QtGui.QApplication.translate("MainWindow", "Begin", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc