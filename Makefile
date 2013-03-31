all: gui resource_rc.py

gui:
	pyuic4 -o gui.py gui.ui

resource_rc.py:
	pyrcc4 -o resources_rc.py resources.qrc
