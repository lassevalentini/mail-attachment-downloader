# -*- coding: utf-8 -*-

from PyQt4 import Qt,QtGui
from gui import Ui_MainWindow
import os
#~ from pprint import pprint


class MainWindow(QtGui.QMainWindow):

    def __init__(self, guiDelegate):
        QtGui.QMainWindow.__init__(self)

        self.is_fetching = False

        self.guiDelegate = guiDelegate

        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self._connectSignals()


    def _connectSignals(self):
        self.connect(self.ui.selectFolderButton, Qt.SIGNAL("clicked()"), self._folderButtonClicked)
        self.connect(self.ui.beginButton, Qt.SIGNAL("clicked()"), self._beginButtonClicked)
        # self.connect(self.ui.influenceLevelCombo, Qt.SIGNAL("currentIndexChanged(int)"), self._influenceLevelChanged)
        # self.connect(self.ui.attributeFileButton, Qt.SIGNAL("clicked()"), self._attributeFileButtonClicked)
        # self.connect(self.ui.calculateButton, Qt.SIGNAL("clicked()"), self._calculateButtonClicked)


    def _beginButtonClicked(self):
        if not self.is_fetching:
            self.ui.beginButton.setText("Stop")
            self.ui.beginButton.setDown(True)
            self.guiDelegate.begin_fetching()
        else:
            self.ui.beginButton.setText("Begin")
            self.ui.beginButton.setDown(False)
            self.guiDelegate.stop_fetching()

        self.is_fetching = not self.is_fetching


    def _folderButtonClicked(self):
        # folder_path = QtGui.QFileDialog.getOpenFileName(self, "Select file", ".", "*")
        folder_path = QtGui.QFileDialog.getExistingDirectory(self, "Select folder")
        print folder_path
        if folder_path:
            self.ui.folderLabel.setText(unicode(folder_path))
            self.guiDelegate.set_destination_folder(folder_path)


    def reset(self, status=""):
        self.ui.beginButton.setText("Begin")
        self.ui.beginButton.setDown(False)
        self.ui.statusLabel.setText(status)
