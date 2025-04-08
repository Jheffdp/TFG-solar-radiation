#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import utils as util
from ui_py_files.config_default_ui import Ui_Dialog


class dialog_config_defaults(QtWidgets.QDialog):

    def __init__(self):
        super(dialog_config_defaults, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.saved.setHidden(True)
        """ Load defaults input in all fields """
        lat, lon, elev, img_path, img_h, img_w, azimut_matrix, zenit_matrix = util.read_default_input()

        # ========== Latitude input field ==========
        self.ui.latitude.setValue(lat)

        # ========== Longitude input field ==========
        self.ui.longitude.setValue(lon)

        # ========== Elevation input field ==========
        self.ui.elevation.setValue(elev)

        # ========== Path images input field ==========
        self.ui.images_path.setText(img_path)

        # ========== Image height input field ==========
        self.ui.height_img.setValue(img_h)

        # ========== Image width input field ==========
        self.ui.width_img.setValue(img_w)

        # ========== Azimuth matrix input field ==========
        self.ui.input_azimut.setText(azimut_matrix)

        # ========== Zenith matrix input field ==========
        self.ui.input_zenit.setText(zenit_matrix)

        # =============== Select azimuth and zenith matrix file path ===============
        self.ui.input_azimut_btn.clicked.connect(
            lambda: self.input_matrix(title="Select azimuth file path", files_name="Numpy files(*.npy)", ext=".npy",
                                      url_field=self.ui.input_azimut.setText))
        self.ui.input_zenit_btn.clicked.connect(
            lambda: self.input_matrix(title="Select zenith file path", files_name="Numpy files(*.npy)", ext=".npy",
                                      url_field=self.ui.input_zenit.setText))

        # =============== Select images file path ===============
        self.ui.images_path_btn.clicked.connect(
            lambda: self.img_path(path_field=self.ui.images_path.setText)
        )

        # =============== Save data ===============
        self.ui.save_btn.clicked.connect(lambda: self.write_inputs())

        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))

    def write_inputs(self):
        self.ui.saved.setHidden(True)
        lat = self.ui.latitude.value()
        lon = self.ui.longitude.value()
        elev = self.ui.elevation.value()
        img_h = self.ui.height_img.value()
        img_w = self.ui.width_img.value()
        img_path = self.ui.images_path.text()
        azimut_path = self.ui.input_azimut.text()
        zenit_path = self.ui.input_zenit.text()

        file = open("data/default_input.dat", "w")
        file.write(str(lat) + ";" + str(lon) + ";" + str(elev) + ";" + str(img_path) + ";" + str("{:.0f}").format(
            img_h) + ";" + str("{:.0f}").format(img_w) + ";" + str(azimut_path) + ";" + str(zenit_path))
        file.close()
        self.ui.saved.setHidden(False)

    """ Select input matrix files, is used for:
        - Identify stars (Automatic mode)
        - Calculate FOV matrix

        Receive:
            title : string
                Title for window
            files_name : string
                Type file to filter
            ext : string
                File extension
            url_field : self.ui 
                Widget with the file path   

        Return:
            Widget with file path
    """

    def input_matrix(self, title, files_name, ext, url_field):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setNameFilter(files_name)
        dialog.setDefaultSuffix(ext)
        directory = dialog.getOpenFileName(caption=title, filter=files_name)
        dst = (directory[0])
        url_field(str(dst))

    """ Select images folder is used for: Identify stars manual and automatic mode """

    def img_path(self, path_field):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        directory = dialog.getExistingDirectory(caption="Select images folder")
        dst = (str(directory) + "/")
        path_field(dst)
