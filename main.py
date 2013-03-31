#!python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui
from MainWindow import MainWindow
import delegate

import sys
if hasattr(sys, 'setdefaultencoding'):
    import locale
    loc = locale.getdefaultlocale()
    if loc[1]:
        encoding = loc[1]
        sys.setdefaultencoding(encoding)


def main():
    app = QtGui.QApplication(sys.argv)
    guiDelegate = delegate.GuiDelegate()
    window = MainWindow(guiDelegate=guiDelegate)
    guiDelegate.set_main_window(window)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
