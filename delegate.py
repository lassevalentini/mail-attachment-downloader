# -*- coding: utf-8 -*-

import maildaemon
# from pprint import pprint


class GuiDelegate(object):
    def __init__(self, main_window=None):
        self.main_window = main_window
        self.maildaemon = None
        self.folder_path = "./"

    def set_main_window(self, window):
        self.main_window = window

    def set_destination_folder(self, folder_path):
        self.folder_path = folder_path

    def begin_fetching(self):
        if self.maildaemon is None:
            ui = self.main_window.ui
            self.maildaemon = maildaemon.Maildaemon(protocol=str(ui.protocolComboBox.currentText()),
                                                    server=str(ui.serverInput.text()),
                                                    port=int(ui.serverPortInput.text()),
                                                    username=unicode(ui.usernameInput.text()),
                                                    password=unicode(ui.passwordInput.text()),
                                                    destination=unicode(self.folder_path),
                                                    error_handler=self.main_window.reset)
            self.maildaemon.start()



    def stop_fetching(self):
        if self.maildaemon is not None:
            self.maildaemon.stop()
        self.maildaemon = None
        self.main_window.reset()

    def exit(self):
        if self.maildaemon is not None:
            self.maildaemon.stop()
