#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from ui_py_files.help_auto_ui import Ui_help_auto
from ui_py_files.help_center_ui import Ui_help_center
from ui_py_files.help_check_ui import Ui_help_check
from ui_py_files.help_fov_ui import Ui_help_fov
from ui_py_files.help_manual_ui import Ui_help_manual_2


class help_manual(QtWidgets.QDialog):

    def __init__(self):
        super(help_manual, self).__init__()
        self.ui = Ui_help_manual_2()
        self.ui.setupUi(self)
        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))


class help_auto(QtWidgets.QDialog):

    def __init__(self):
        super(help_auto, self).__init__()
        self.ui = Ui_help_auto()
        self.ui.setupUi(self)
        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))


class help_center(QtWidgets.QDialog):

    def __init__(self):
        super(help_center, self).__init__()
        self.ui = Ui_help_center()
        self.ui.setupUi(self)
        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))


class help_fov(QtWidgets.QDialog):

    def __init__(self):
        super(help_fov, self).__init__()
        self.ui = Ui_help_fov()
        self.ui.setupUi(self)
        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))


class help_check(QtWidgets.QDialog):

    def __init__(self):
        super(help_check, self).__init__()
        self.ui = Ui_help_check()
        self.ui.setupUi(self)
        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))
