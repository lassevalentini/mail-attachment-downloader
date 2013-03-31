# -*- coding: utf-8 -*-

import maildaemon
# from pprint import pprint


class GuiDelegate(object):
    def __init__(self, main_window=None):
        self.main_window = main_window

    def set_main_window(self, window):
        self.main_window = window

    def set_destination_folder(self, folder_path):
        self.folder_path = folder_path

    def begin_fetching(self):
        if self.maildaemon is not None:
            self.maildaemon = maildaemon.Maildaemon()
        self.maildaemon.start()

    def stop_fetching(self):
        if self.maildaemon is not None:
            self.maildaemon.stop()
