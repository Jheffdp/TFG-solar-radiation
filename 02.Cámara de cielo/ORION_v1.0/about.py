#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from ui_py_files.about_ui import Ui_about


class dialog_about(QtWidgets.QDialog):

    def __init__(self):
        super(dialog_about, self).__init__()
        self.ui = Ui_about()
        self.ui.setupUi(self)

        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))

        pixmap_logo = QtGui.QPixmap('img/logo.png')
        self.ui.logo.setPixmap(pixmap_logo)
        self.ui.logo.setScaledContents(True)

        pixmap_logo_app = QtGui.QPixmap('img/logo_app.png')
        self.ui.logo_app.setPixmap(pixmap_logo_app)
        self.ui.logo_app.setScaledContents(True)
