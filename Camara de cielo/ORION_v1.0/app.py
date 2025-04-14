#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

import os
import shutil
import sys
from pathlib import Path
from time import perf_counter

import PyQt5
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from scipy.integrate import dblquad
import about
import config_default
import convert_npy
import help
import rename_images
import utils
import utils_plots
from ui_py_files.main_window_w import Ui_MainWindow

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.fspath(
    Path(PyQt5.__file__).resolve().parent / "Qt5" / "plugins"
)


if not os.path.exists("data"):
    os.mkdir("data")
if not os.path.exists("data/tmp"):
    os.mkdir("data/tmp")


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)

        """ Load stars name in all combos """
        for star in utils.read_all_stars():
            self.ui.stars.addItem(star)
            self.ui.stars_auto.addItem(star)
            self.ui.stars_util.addItem(star)

        """ Menu Bar actions """
        # ========== About Menu ==========
        self.ui.actionAbout.triggered.connect(lambda: about.dialog_about().show())

        # ========== Tools Menu ==========
        # ========== Load defaults ==========
        self.ui.actionLoad_default_inputs.triggered.connect(lambda: self.load_default())

        # ========== Open config default dialog ==========
        self.ui.actionConfig_defaults_inputs.triggered.connect(
            lambda: config_default.dialog_config_defaults().show()
        )

        # ========== Open convert npy files dialog ==========
        self.ui.actionConvert_npy_files.triggered.connect(
            lambda: convert_npy.dialog_convert().show()
        )

        # ========== Open rename images dialog ==========
        self.ui.actionRename_images_for_input.triggered.connect(
            lambda: rename_images.rename_images().show()
        )

        """ Identify stars (manual mode) - Buttons and actions """
        # ========== Hidden fields and buttons ==========
        self.ui.add_btn.setHidden(True)
        self.ui.remove_btn.setHidden(True)
        self.ui.finish_btn.setHidden(True)
        self.ui.label_points.setHidden(True)
        self.ui.label_date.setHidden(True)
        self.ui.finish.setHidden(True)
        self.ui.info.setHidden(True)

        # ========== Enter image path ==========
        self.ui.images_path_btn.clicked.connect(
            lambda: self.img_path(path_field=self.ui.images_path.setText)
        )

        # ========== Select path to save star data output file ==========
        self.ui.save_file_btn.clicked.connect(
            lambda: self.filesaved(
                title="Save star data",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.save_file.setText,
            )
        )

        # ========== Check all input data and start stars selection ==========
        self.ui.start_btn.clicked.connect(lambda: self.check_identify())

        # ========== Add selected point to data ==========
        self.ui.add_btn.clicked.connect(lambda: self.add())

        # ========== Ignore selected point ==========
        self.ui.remove_btn.clicked.connect(lambda: self.remove())

        # ========== Finish the points selection ==========
        self.ui.finish_btn.clicked.connect(lambda: self.finish())

        # ========== Show help ==========
        self.ui.help_manual.clicked.connect(lambda: help.help_manual().show())

        """ Identify stars (automatic mode) - Buttons and actions """
        # ========== Hidden fields and buttons ==========
        self.ui.add_btn_auto.setHidden(True)
        self.ui.remove_btn_auto.setHidden(True)
        self.ui.finish_btn_auto.setHidden(True)
        self.ui.label_points_auto.setHidden(True)
        self.ui.label_date_auto.setHidden(True)
        self.ui.finish_auto.setHidden(True)
        self.ui.info_auto.setHidden(True)

        # ========== Select enter custom matrix in automatic mode ==========
        self.ui.input_matrix.clicked.connect(lambda: self.enable_input_matrix_auto())

        # ========== Select use initial default matrix ==========
        self.ui.default_matrix.clicked.connect(
            lambda: self.enable_input_default_matrix()
        )

        # ========== Select images path ==========
        self.ui.images_path_btn_auto.clicked.connect(
            lambda: self.img_path(path_field=self.ui.images_path_auto.setText)
        )

        # ========== Select save file url ==========
        self.ui.save_file_btn_auto.clicked.connect(
            lambda: self.filesaved(
                title="Save star data",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.save_file_auto.setText,
            )
        )

        # ========== Select input azimuth matrix file ==========
        self.ui.input_azimut_btn_auto.clicked.connect(
            lambda: self.input_matrix(
                title="Input azimuth matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.input_azimut_auto.setText,
            )
        )

        # ========== Select input zenith matrix file ==========
        self.ui.input_zenit_btn_auto.clicked.connect(
            lambda: self.input_matrix(
                title="Input zenith matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.input_zenit_auto.setText,
            )
        )

        # ========== Check all input data and start stars automatic selection ==========
        self.ui.start_btn_auto.clicked.connect(lambda: self.check_identify_auto())

        # ========== Add selected point to data ==========
        self.ui.add_btn_auto.clicked.connect(lambda: self.add())

        # ========== Ignore selected point ==========
        self.ui.remove_btn_auto.clicked.connect(lambda: self.remove())

        # ========== Finish the points selection ==========
        self.ui.finish_btn_auto.clicked.connect(lambda: self.finish())

        # ========== Show help ==========
        self.ui.help_auto.clicked.connect(lambda: help.help_auto().show())

        """ Calculate center and  azimuth and zenith matrix - Buttons and actions """
        # ========== Hidden fields and buttons ==========
        self.ui.progressBar_fov.setHidden(True)
        self.ui.verticalWidget_center.setHidden(True)

        # ========== Select input stars npy data files ==========
        self.ui.input_files_btn.clicked.connect(lambda: self.stars_npy_files())

        # ========== Select path to save azimuth matrix ==========
        self.ui.save_azimut_btn.clicked.connect(
            lambda: self.filesaved(
                title="Save azimuth matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.save_azimut.setText,
            )
        )

        # ========== Select path to save zenith matrix ==========
        self.ui.save_zenit_btn.clicked.connect(
            lambda: self.filesaved(
                title="Save zenith matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.save_zenit.setText,
            )
        )

        # ========== Check input data and calculate center and azimuth, zenith matrix
        self.ui.calculate_btn.clicked.connect(lambda: self.check_calculate_center())

        # ========== Show help ==========
        self.ui.help_center.clicked.connect(lambda: help.help_center().show())

        """ Calculate FOV - Buttons and actions"""
        # ========== Hidden fields and buttons ==========
        self.ui.progressBar.setHidden(True)
        self.ui.stop_fov.setHidden(True)

        # ========== Select input azimuth matrix file ==========
        self.ui.input_azimut_btn.clicked.connect(
            lambda: self.input_matrix(
                title="Input azimuth matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.input_azimut_fov.setText,
            )
        )

        # ========== Select input zenith matrix file ==========
        self.ui.input_zenit_btn.clicked.connect(
            lambda: self.input_matrix(
                title="Input zenith matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.input_zenit_fov.setText,
            )
        )

        # ========== Select path to save FOV matrix file ==========
        self.ui.save_fov_btn.clicked.connect(
            lambda: self.filesaved(
                title="Save FOV matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.save_fov.setText,
            )
        )

        # ========== Check input data and calculate FOV matrix ==========
        self.ui.calculate_fov_btn.clicked.connect(lambda: self.check_calculate_fov())

        # ========== FOV stop calculation ==========
        self.ui.stop_fov.clicked.connect(lambda: self.finish())

        # ========== Show help ==========
        self.ui.help_fov.clicked.connect(lambda: help.help_fov().show())

        # ========== Initialize status for add, remove and stop buttons for selected points ==========
        self.btn2pushed = False
        self.radio = 0
        self.check_data = []

        """ Check Calibration - Buttons and actions """
        # ========== Hidden fields and buttons ==========
        self.ui.progressBar_util.setHidden(True)
        self.ui.info_util_check.setHidden(True)

        # ========== Set images path ==========
        self.ui.images_path_btn_util.clicked.connect(
            lambda: self.img_path(path_field=self.ui.images_path_util.setText)
        )

        # ========== Set azimuth matrix path ==========
        self.ui.input_azimut_btn_util.clicked.connect(
            lambda: self.input_matrix(
                title="Input azimuth matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.input_azimut_util.setText,
            )
        )

        # ========== Set azimuth matrix path ==========
        self.ui.input_zenit_btn_util.clicked.connect(
            lambda: self.input_matrix(
                title="Input zenith matrix",
                files_name="Numpy files(*.npy)",
                ext=".npy",
                url_field=self.ui.input_zenit_util.setText,
            )
        )

        # ========== Check imput data and run check calibration ==========
        self.ui.check_btn.clicked.connect(lambda: self.check_utilities())

        # ========== Save check calibration data ==========
        self.ui.save_check_data.clicked.connect(lambda: self.save_check_data())

        # ========== Show help ==========
        self.ui.help_check.clicked.connect(lambda: help.help_check().show())

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            "Window Close",
            "Are you sure you want to close the application?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            shutil.rmtree("data/tmp", ignore_errors=True)
        else:
            event.ignore()

    """ Show messages errors for input data check
        Receive:
            text_header : string
                Window header text
            text_body : string
                Body text message error              
    """

    def msgBox(self, text_title, text_header, text_body):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(text_header)
        msg.setInformativeText(text_body)
        msg.setWindowTitle(text_title)
        msg.exec_()

    """ Load defaults input in all fields """

    def load_default(self):
        (
            lat,
            lon,
            elev,
            img_path,
            img_h,
            img_w,
            azimut_matrix,
            zenit_matrix,
        ) = utils.read_default_input()

        # ========== Latitude inputs fields ==========
        self.ui.latitude.setValue(lat)
        self.ui.latitude_auto.setValue(lat)
        self.ui.latitude_util.setValue(lat)

        # ========== Longitude inputs fields ==========
        self.ui.longitude.setValue(lon)
        self.ui.longitude_auto.setValue(lon)
        self.ui.longitude_util.setValue(lon)

        # ========== Elevation inputs fields ==========
        self.ui.elevation.setValue(elev)
        self.ui.elevation_auto.setValue(elev)
        self.ui.elevation_util.setValue(elev)

        # ========== Path images inputs fields ==========
        self.ui.images_path.setText(img_path)
        self.ui.images_path_auto.setText(img_path)
        self.ui.images_path_util.setText(img_path)

        # ========== Image height input field ==========
        self.ui.height_img.setValue(img_h)

        # ========== Image width input field ==========
        self.ui.width_img.setValue(img_w)

        # ========== Azimuth matrix input field ==========
        self.ui.input_azimut_fov.setText(azimut_matrix)
        self.ui.input_azimut_util.setText(azimut_matrix)
        self.ui.input_azimut_auto.setText(azimut_matrix)

        # ========== Zenith matrix input field ==========
        self.ui.input_zenit_fov.setText(zenit_matrix)
        self.ui.input_zenit_util.setText(zenit_matrix)
        self.ui.input_zenit_auto.setText(zenit_matrix)

    # ========== Enable or Disable widgets when any action still running ==========
    def control_widget(self, status):
        self.ui.manual_widget.setEnabled(status)
        self.ui.auto_widget.setEnabled(status)
        self.ui.center_widget.setEnabled(status)
        self.ui.fov_widget.setEnabled(status)
        self.ui.check_widget.setEnabled(status)

    """ Check all input fields and show message error """

    # ========== Identify star (manual mode) ==========
    def check_identify(self):
        execute = True
        text_title = "Error with input data"
        if self.ui.latitude.value() == 0:
            self.msgBox(text_title, "Latitude = 0", "Please set the camera latitude")
            execute = False
        else:
            if self.ui.longitude.value() == 0:
                self.msgBox(
                    text_title, "Longitude = 0", "Please set the camera longitude"
                )
                execute = False
            else:
                if self.ui.elevation.value() == 0:
                    self.msgBox(
                        text_title, "Elevation = 0", "Please set the camera elevation"
                    )
                    execute = False
                else:
                    if self.ui.stars.currentText() == "":
                        self.msgBox(
                            text_title, "Error with star name", "Please select the star"
                        )
                        execute = False
                    else:
                        if self.ui.images_path.text() == "":
                            self.msgBox(
                                text_title,
                                "Error with the images path",
                                "Please set the images folder path",
                            )
                            self.img_path(path_field=self.ui.images_path.setText)
                            execute = False
                        else:
                            if self.ui.save_file.text() == "":
                                self.msgBox(
                                    text_title,
                                    "Error with the generated file path",
                                    "Please set the generated file folder path",
                                )
                                self.filesaved(
                                    title="Save star data",
                                    files_name="Numpy files(*.npy)",
                                    ext=".npy",
                                    url_field=self.ui.save_file.setText,
                                )
                                execute = False
        if execute:
            files = utils.read_img_path(self.ui.images_path.text())
            if len(files) == 0:
                self.msgBox(
                    text_title="Images error",
                    text_header="No images found",
                    text_body="Cannot find images with the necessary format in the selected directory",
                )
            else:
                self.identify_star()

    # ========== Identify star (automatic mode) ==========
    def check_identify_auto(self):
        execute = True
        text_title = "Error with input data"
        if self.ui.latitude_auto.value() == 0:
            self.msgBox(text_title, "Latitude = 0", "Please set the camera latitude")
            execute = False
        else:
            if self.ui.longitude_auto.value() == 0:
                self.msgBox(
                    text_title, "Longitude = 0", "Please set the camera longitude"
                )
                execute = False
            else:
                if self.ui.elevation_auto.value() == 0:
                    self.msgBox(
                        text_title, "Elevation = 0", "Please set the camera elevation"
                    )
                    execute = False
                else:
                    if self.ui.stars_auto.currentText() == "":
                        self.msgBox(
                            text_title, "Error with star name", "Please select the star"
                        )
                        execute = False
                    else:
                        if self.ui.images_path_auto.text() == "":
                            self.msgBox(
                                text_title,
                                "Error with the images path",
                                "Please set the images folder path",
                            )
                            self.img_path(path_field=self.ui.images_path_auto.setText)
                            execute = False
                        else:
                            if self.ui.save_file_auto.text() == "":
                                self.msgBox(
                                    text_title,
                                    "Error with the generated file path",
                                    "Please set the generated file folder path",
                                )
                                self.filesaved(
                                    title="Save star data",
                                    files_name="Numpy files(*.npy)",
                                    ext=".npy",
                                    url_field=self.ui.save_file_auto.setText,
                                )
                                execute = False
                            else:
                                if self.radio == 0:
                                    self.msgBox(
                                        text_title,
                                        "Error with the input files",
                                        "Please select the matrix to use",
                                    )
                                    execute = False
                                else:
                                    if self.radio == 1:
                                        if self.ui.input_azimut_auto.text() == "":
                                            self.msgBox(
                                                text_title,
                                                "Error with the input files",
                                                "Please set the azimuth matrix path",
                                            )
                                            self.input_matrix(
                                                title="Input azimuth matrix",
                                                files_name="Numpy files(*.npy)",
                                                ext=".npy",
                                                url_field=self.ui.input_azimut_auto.setText,
                                            )
                                            execute = False
                                        else:
                                            if self.ui.input_zenit_auto.text() == "":
                                                self.msgBox(
                                                    text_title,
                                                    "Error with the input files",
                                                    "Please set the zenith matrix path",
                                                )
                                                self.input_matrix(
                                                    title="Input zenith matrix",
                                                    files_name="Numpy files(*.npy)",
                                                    ext=".npy",
                                                    url_field=self.ui.input_zenit_auto.setText,
                                                )
                                                execute = False
        if execute:
            files = utils.read_img_path(self.ui.images_path_auto.text())
            if len(files) == 0:
                self.msgBox(
                    text_title="Images error",
                    text_header="No images found",
                    text_body="Cannot find images with the necessary format in the selected directory",
                )
            else:
                self.automated_search()

    # ========== Calculate center and azimuth, zenith matrix ==========
    def check_calculate_center(self):
        execute = True
        text_tile = "Error with input data"
        if self.ui.width_img.value() == 0:
            self.msgBox(
                text_tile, "Error with image dimensions", "0 is not valid for width"
            )
            execute = False
        else:
            if self.ui.height_img.value() == 0:
                self.msgBox(
                    text_tile,
                    "Error with image dimensions",
                    "0 is not valid for height",
                )
                execute = False
            else:
                if self.ui.input_list_star.count() == 0:
                    self.msgBox(
                        text_tile, "Error with inputs files", "No found npy files"
                    )
                    execute = False
        if execute:
            self.calculate_center()

    # ========== Calculate FOV ==========
    def check_calculate_fov(self):
        execute = True
        text_tile = "Error with input data"
        if self.ui.input_azimut_fov.text() == "":
            self.msgBox(
                text_tile,
                "Error with calibration matrix",
                "Please select a valid azimuth matrix",
            )
            execute = False
        else:
            if self.ui.input_zenit_fov.text() == "":
                self.msgBox(
                    text_tile,
                    "Error with calibration matrix",
                    "Please select a valid zenith matrix",
                )
                execute = False
            else:
                if self.ui.save_fov.text() == "":
                    self.msgBox(
                        text_tile,
                        "Error with output file",
                        "Please set the file path to save FOV matrix",
                    )
                    execute = False
        if execute:
            self.calculate_fov()

    # ========== Calibration Check ==========
    def check_utilities(self):
        execute = True
        text_title = "Error with input data"
        if self.ui.latitude_util.value() == 0:
            self.msgBox(text_title, "Latitude = 0", "Please set the camera latitude")
            execute = False
        else:
            if self.ui.longitude_util.value() == 0:
                self.msgBox(
                    text_title, "Longitude = 0", "Please set the camera longitude"
                )
                execute = False
            else:
                if self.ui.elevation_util.value() == 0:
                    self.msgBox(
                        text_title, "Elevation = 0", "Please set the camera elevation"
                    )
                    execute = False
                else:
                    if self.ui.stars_util.currentText() == "":
                        self.msgBox(
                            text_title, "Error with star name", "Please select the star"
                        )
                        execute = False
                    else:
                        if self.ui.images_path_util.text() == "":
                            self.msgBox(
                                text_title,
                                "Error with the images path",
                                "Please set the images folder path",
                            )
                            self.img_path(path_field=self.ui.images_path_util.setText)
                            execute = False
                        else:
                            if self.ui.input_azimut_util.text() == "":
                                self.msgBox(
                                    text_title,
                                    "Error with the input files",
                                    "Please set the azimuth matrix path",
                                )
                                self.input_matrix(
                                    title="Input azimuth matrix",
                                    files_name="Numpy files(*.npy)",
                                    ext=".npy",
                                    url_field=self.ui.input_azimut_util.setText,
                                )
                                execute = False
                            else:
                                if self.ui.input_zenit_util.text() == "":
                                    self.msgBox(
                                        text_title,
                                        "Error with the input files",
                                        "Please set the zenith matrix path",
                                    )
                                    self.input_matrix(
                                        title="Input zenith matrix",
                                        files_name="Numpy files(*.npy)",
                                        ext=".npy",
                                        url_field=self.ui.input_zenit_util.setText,
                                    )
                                    execute = False
        if execute:
            files = utils.read_img_path(self.ui.images_path_util.text())
            if len(files) == 0:
                self.msgBox(
                    text_title="Images error",
                    text_header="No images found",
                    text_body="Cannot find images with the necessary format in the selected directory",
                )
            else:
                self.check_calibration()

    # ========== Enable the input matrix ==========
    def enable_input_matrix_auto(self):
        self.radio = 1
        self.ui.label_azimut_auto.setEnabled(True)
        self.ui.label_zenit_auto.setEnabled(True)
        self.ui.input_azimut_auto.setEnabled(True)
        self.ui.input_zenit_auto.setEnabled(True)
        self.ui.input_azimut_btn_auto.setEnabled(True)
        self.ui.input_zenit_btn_auto.setEnabled(True)
        self.ui.label_gap_auto.setEnabled(False)
        self.ui.label_extreme_auto.setEnabled(False)
        self.ui.initial_gap.setEnabled(False)
        self.ui.zen_extreme.setEnabled(False)

    # ========== Enable default matrix ==========
    def enable_input_default_matrix(self):
        self.radio = 2
        self.ui.label_gap_auto.setEnabled(True)
        self.ui.label_extreme_auto.setEnabled(True)
        self.ui.initial_gap.setEnabled(True)
        self.ui.zen_extreme.setEnabled(True)
        self.ui.label_azimut_auto.setEnabled(False)
        self.ui.label_zenit_auto.setEnabled(False)
        self.ui.input_azimut_auto.setEnabled(False)
        self.ui.input_zenit_auto.setEnabled(False)
        self.ui.input_azimut_btn_auto.setEnabled(False)
        self.ui.input_zenit_btn_auto.setEnabled(False)

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
        dst = directory[0]
        url_field(str(dst))

    """ Select path to save npy files, is used for:
        - Identify stars (Manual mode)
        - Identify stars (Automatic mode)
        - Calculate center and azimuth, zenith matrix
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

    def filesaved(self, title, files_name, ext, url_field):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setNameFilter(files_name)
        dialog.setDefaultSuffix(ext)
        directory = dialog.getSaveFileName(caption=title, filter=files_name)
        dst = str(directory[0])
        ext = dst.split(".")
        if len(ext) != 2:
            url_field(dst + str(".npy"))
        else:
            if ext[1] == "npy":
                url_field(dst)
            else:
                url_field(ext[0] + ".npy")

    """ Save data for calibration check"""

    def save_check_data(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        directory = dialog.getSaveFileName(
            caption="Save output data", filter="All files(*)"
        )
        dst = str(directory[0])
        if dst != "":
            np.savetxt(
                dst,
                np.c_[self.check_data],
                header="azimuth zenith distance",
                fmt=["%.3f", "%.3f", "%.8f"],
            )

    """ Select images folder is used for: Identify stars manual and automatic mode """

    def img_path(self, path_field):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        directory = dialog.getExistingDirectory(caption="Select images folder")
        dst = str(directory) + "/"
        path_field(dst)

    """ Select list stars files data for calculate center and azimuth, zenith matrix """

    def stars_npy_files(self):
        self.ui.input_list_star.clear()
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setNameFilter("Numpy files(*.npy)")
        dialog.setDefaultSuffix(".npy")
        directory = dialog.getOpenFileNames(
            caption="Select npy stars files", filter="Numpy files(*.npy)"
        )
        for dst in directory[0]:
            self.ui.input_list_star.addItem(str(dst))
        self.input_stars = directory[0]

    """ Controls for image loop in Identify star manual and automatic mode """

    def add(self):
        self.btn2pushed = True
        self.message = 0

    def remove(self):
        self.btn2pushed = True
        self.message = 1

    def finish(self):
        self.btn2pushed = True
        self.message = 3

    """Automatic search for stars based on azimuth and zenith matrices
    or extreme zenith and image offset from north. The results are save in npy file for calculate center and
    generate azimuth and zenith calibartion matrix.
        Receive:
            lat_ : float
                Camera latitude
            lon_ : float
                Camera longitude
            elev_ : float
                Elevation over sea level
            star_ : string
                Selected star name
            path_ : str
                Images path
            Custom matrix
                azimut_matrix : str
                    Custom azimuth matrix path
                zenit_matrix : str
                    Custom zenith matrix path
            Default matrix
                initial_gap : float
                    Initial gap for north
                zen_extreme : float
                    Maximum zenith on image
        Return:
            results : npy file
                File with star azimuth, zenith and x, y position
    """

    def automated_search(self):
        # ========== Disable buttons and widget==========
        self.btn2pushed = False
        self.control_widget(False)
        self.ui.finish_btn_auto.setEnabled(False)
        self.ui.add_btn_auto.setHidden(False)
        self.ui.remove_btn_auto.setHidden(False)
        self.ui.info_auto.setHidden(False)

        # ========== Get input data ==========
        lon_ = self.ui.longitude_auto.value()
        lat_ = self.ui.latitude_auto.value()
        elev_ = self.ui.elevation_auto.value()
        star_ = self.ui.stars_auto.currentText()
        path = self.ui.images_path_auto.text()

        # ========== Find the star with custom matrix ==========
        if self.radio == 1:
            azimut_matrix = np.load(self.ui.input_azimut_auto.text())
            zenit_matrix = np.load(self.ui.input_zenit_auto.text())

        else:
            # ========== Find the star with initial gap and extreme zenith ==========
            if self.radio == 2:
                initial_gap = self.ui.initial_gap.value()
                zen_extreme = self.ui.zen_extreme.value()
                img_h, img_w = utils.image_size(path)
                azimut_matrix, zenit_matrix = utils.initial_matrix(
                    img_h, img_w, initial_gap, zen_extreme
                )

        results = []
        selected_points = []
        removed_points = []
        i = 0
        e = 0

        # ========== Get a list with all image in folder path ==========
        files = utils.read_img_path(path)

        for fichero in files:
            zenit_star, azimut_star = utils.get_star(
                name=star_,
                lat_=lat_,
                date_=utils.get_date_img(fichero),
                lon_=lon_,
                elev_=elev_,
            )
            if zenit_star < 83:
                self.ui.finish_auto.setHidden(True)

                # ========== Read image as grayscale mode ==========
                img = cv2.imread(str(path) + str(fichero), 0)

                # ========== Get image size ==========
                img_h, img_w = np.shape(img)
                max_dim = np.max((img_h, img_w))

                # ========== Check radio button for custom or default and define region for find max bright point ==========
                # ========== Find the star with custom matrix ==========
                if self.radio == 1:
                    plus_width = int(np.ceil(max_dim / 100))
                    plus_height = int(np.ceil(max_dim / 100))
                else:
                    # ========== Find the star with initial gap and extreme zenith ==========
                    if self.radio == 2:
                        plus_width = int(np.ceil(max_dim / 50))
                        plus_height = int(np.ceil(max_dim / 50))

                # ========== Get pixel position by azimuth and zenith matrix ==========
                input_coord = utils.select_pixel(
                    azimut_star,
                    zenit_star,
                    np.array(azimut_matrix),
                    np.array(zenit_matrix),
                )

                # ========== Select a region to find the maximum bright pixel and get the position ==========
                imCrop = img[
                    int(input_coord[1]) - plus_width : int(input_coord[1]) + plus_width,
                    int(input_coord[0] - plus_height) : int(
                        input_coord[0] + plus_height
                    ),
                ]
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(imCrop)
                coord = (
                    maxLoc[0] + (input_coord[0] - plus_height),
                    maxLoc[1] + input_coord[1] - plus_width,
                )
                coord_region = (maxLoc[0], maxLoc[1])

                # ========== Draw a circle in select region and image ==========
                image_region = cv2.circle(imCrop, coord_region, 8, (255, 0, 0), 2)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                if len(image_region) != 0:
                    cv2.imwrite(
                        "data/tmp/tmp.png",
                        cv2.cvtColor(image_region, cv2.COLOR_GRAY2RGB),
                    )
                if len(selected_points) > 0:
                    for point in selected_points:
                        image_result = cv2.circle(img, point, 4, (0, 255, 0), 2)
                if len(removed_points) > 0:
                    for del_point in removed_points:
                        image_result = cv2.circle(img, del_point, 4, (12, 12, 205), 2)
                image_result = cv2.circle(img, coord, 10, (0, 134, 211), 2)

                # ========== Show selected region and image ==========
                pixmap_region = QtGui.QPixmap("data/tmp/tmp.png")
                size = image_result.shape
                step = image_result.size / size[0]
                qformat = QtGui.QImage.Format_Indexed8
                if len(size) == 3:
                    if size[2] == 4:
                        qformat = QtGui.QImage.Format_RGBA8888
                    else:
                        qformat = QtGui.QImage.Format_RGB888
                img = QtGui.QImage(image_result, size[1], size[0], step, qformat)
                img = img.rgbSwapped()

                # ========== Data to add at the output file ==========
                results_to_add = (coord[0], coord[1], zenit_star, azimut_star)
                point = (coord[0], coord[1])

                # ========== Show information data and image with selection ==========
                self.ui.date_auto.setText(str(utils.get_date_img(fichero)))
                self.ui.img_height_info_auto.setText(str(img_h))
                self.ui.img_width_info_auto.setText(str(img_w))
                self.ui.azimut_info_auto.setText(str(round(azimut_star, 2)))
                self.ui.zenit_info_auto.setText(str(round(zenit_star, 2)))
                self.ui.selected_points_auto.setText(str(len(selected_points)))
                self.ui.region_img_auto.setPixmap(pixmap_region)
                self.ui.region_img_auto.setScaledContents(True)
                self.ui.show_image_auto.setPixmap(
                    QtGui.QPixmap.fromImage(img).scaled(
                        841,
                        561,
                        QtCore.Qt.KeepAspectRatio,
                        QtCore.Qt.SmoothTransformation,
                    )
                )
                cv2.destroyAllWindows()

                # ========== Set visible and enabled buttons ==========
                self.ui.add_btn_auto.setHidden(False)
                self.ui.remove_btn_auto.setHidden(False)
                self.ui.finish_btn_auto.setHidden(False)
                self.ui.label_date_auto.setHidden(False)
                self.ui.label_points_auto.setHidden(False)
                self.ui.finish_btn_auto.setEnabled(True)

                # ========== Control for add, remove and finish buttons ==========
                while self.btn2pushed != True:
                    QtWidgets.QApplication.processEvents()

                # ========== Add point ==========
                if self.message == 0:
                    selected_points.append(point)
                    results.append(results_to_add)
                self.btn2pushed = False

                # ========== Add point ==========
                if self.message == 1:
                    removed_points.append(point)
                self.btn2pushed = False

                # ========== Finish selection ==========
                if self.message == 3:
                    break
                self.btn2pushed = False
                i += 1
            else:
                e += 1

        # ========== Show message if the zenith < 83 in all images ==========
        if e == len(files):
            self.msgBox(
                text_title="Star not found in images",
                text_header="Select another star",
                text_body="The selected star does not appear in the image",
            )
            self.ui.finish_auto.setHidden(True)

        # ========== Save npy output data file ==========
        np.save(self.ui.save_file_auto.text(), results)

        # ========== Set hidden the control buttons ==========
        self.ui.add_btn_auto.setHidden(True)
        self.ui.remove_btn_auto.setHidden(True)
        self.ui.finish_btn_auto.setHidden(True)

        # ========== Show the finish label and enable widgets ==========
        self.ui.finish_auto.setHidden(False)
        self.control_widget(True)

        del results, selected_points, removed_points, max_dim, plus_width, plus_height

    """Manual stars selection. The results are save in npy file for calculate center and
        generate azimuth and zenith calibartion matrix.
            Receive:
                lat_ : float
                    Camera latitude
                lon_ : float
                    Camera longitude
                elev_ : float
                    Elevation over sea level
                star_ : string
                    Selected star name
                path_ : str
                    Images path
    
            Return:
                results : npy file
                    File with star azimuth, zenith and x, y position
        """

    def identify_star(self):
        # ========== Disable buttons and widget==========
        self.control_widget(False)
        self.ui.finish.setHidden(True)
        self.ui.finish_btn.setEnabled(False)
        self.ui.info.setHidden(False)
        self.message = -1

        # ========== Get input data ==========
        lon_ = self.ui.longitude.value()
        lat_ = self.ui.latitude.value()
        elev_ = self.ui.elevation.value()
        star = self.ui.stars.currentText()
        path = self.ui.images_path.text()

        results = []
        selected_points = []
        i = 0
        for fichero in utils.read_img_path(path):

            gray = cv2.imread(str(path) + str(fichero), 0)

            # ========== Get image size ==========
            img_h, img_w = np.shape(gray)

            # Select Region of interest (ROI)
            cv2.namedWindow("Select star", cv2.WINDOW_GUI_NORMAL)
            r = cv2.selectROI("Select star", gray)
            cv2.destroyAllWindows()

            imCrop = gray[int(r[1]) : int(r[1] + r[3]), int(r[0]) : int(r[0] + r[2])]
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(imCrop)
            coord = (maxLoc[0] + (r[0]), maxLoc[1] + r[1])
            coord_region = (maxLoc[0], maxLoc[1])
            object_zenith, object_azim = utils.get_star(
                name=star,
                lat_=lat_,
                date_=utils.get_date_img(fichero),
                lon_=lon_,
                elev_=elev_,
            )
            image_region = cv2.circle(imCrop, coord_region, 10, (255, 255, 255), 2)
            img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
            if len(image_region) != 0:
                cv2.imwrite("data/tmp/tmp.png", image_region)
            if len(selected_points) > 0:
                for point in selected_points:
                    image_result = cv2.circle(img, point, 4, (0, 255, 0), 2)
            image_result = cv2.circle(img, coord, 10, (0, 46, 255), 2)
            size = image_result.shape
            step = image_result.size / size[0]
            qformat = QtGui.QImage.Format_Indexed8
            if len(size) == 3:
                if size[2] == 4:
                    qformat = QtGui.QImage.Format_RGBA8888
                else:
                    qformat = QtGui.QImage.Format_RGB888

            pixmap_region = QtGui.QPixmap("data/tmp/tmp.png")
            img = QtGui.QImage(image_result, size[1], size[0], step, qformat)
            img = img.rgbSwapped()
            self.ui.show_image.setPixmap(
                QtGui.QPixmap.fromImage(img).scaled(
                    951, 591, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
                )
            )
            cv2.destroyAllWindows()

            results_to_add = (coord[0], coord[1], object_zenith, object_azim)
            point = (coord[0], coord[1])

            # ========== Show the buttons and information area ==========
            self.ui.add_btn.setHidden(False)
            self.ui.remove_btn.setHidden(False)
            self.ui.finish_btn.setHidden(False)
            self.ui.label_date.setHidden(False)
            self.ui.label_points.setHidden(False)

            # ========== Show information data and image with selection ==========
            self.ui.date.setText(str(utils.get_date_img(fichero)))
            self.ui.selected_points.setText(str(len(selected_points)))
            self.ui.img_height_info.setText(str(img_h))
            self.ui.img_width_info.setText(str(img_w))
            self.ui.azimut_info.setText(str(round(object_azim, 2)))
            self.ui.zenit_info.setText(str(round(object_zenith, 2)))
            self.ui.region_img.setPixmap(pixmap_region)
            self.ui.region_img.setScaledContents(True)

            # ========== Buttons control (Add, Remove and Finish) ==========
            self.ui.finish_btn.setEnabled(True)
            while self.btn2pushed != True:
                QtWidgets.QApplication.processEvents()
            if self.message == 0:
                selected_points.append(point)
                results.append(results_to_add)
            if self.message == 3:
                break
            self.btn2pushed = False
            i += 1

        # ========== Save data ==========
        np.save(self.ui.save_file.text(), results)

        # ========== Restore buttons and widgets ==========
        self.ui.add_btn.setHidden(True)
        self.ui.remove_btn.setHidden(True)
        self.ui.finish_btn.setHidden(True)
        self.ui.finish.setHidden(False)
        self.control_widget(True)

    """Calculate center and generate calibration matrix for azimuth and zenith. The results are save in npy file for 
        azimuth and zenith calibartion matrix.
                Receive:
                    img_h : int
                        Image height
                    img_w : int
                        Image width
                    input_files : array
                        Stars data files path
                    polynomial_degree : int
                        Polynomial degree for adjust zenith
                    flip_vertical : boolean
                        Vertical flip for calibration matrix
                    flip_horizontal : boolean
                        Horizontal flip for calibration matrix
                Return:
                    azimuth_matrix : npy file
                        Azimuth calibration matrix file
                    zenith_matrix : npy file
                        Zenith calibration matrix file
    """

    def calculate_center(self):
        # ========== Disable buttons and widget==========
        self.control_widget(False)
        self.ui.azimut_matrix_plot.clear()
        self.ui.zenit_matrix_plot.clear()
        self.ui.adjus_plot.clear()
        self.ui.verticalWidget_center.setHidden(True)
        self.ui.progressBar.setValue(0)

        # ========== Get input data ==========
        zenlimit = 20
        img_h = int(self.ui.height_img.value())
        img_w = int(self.ui.width_img.value())
        y_est = img_h / 2
        x_est = img_w / 2
        data_file = utils.read_files(self.input_stars)
        print(data_file)
        if data_file == []:
            self.msgBox(
                "Error with input data",
                "Error with stars file",
                "Please select a valid star data file",
            )
            self.control_widget(True)
            return False

        # ==========  ==========
        data = data_file[data_file[:, 2] > zenlimit]
        col = np.array(data[:, 0])
        fila = np.array(data[:, 1])
        ZenStar = np.array(data[:, 2])
        AziStar = np.array(data[:, 3])
        AziStar = np.where(AziStar > 180, (AziStar - 360), AziStar)
        AziStar = np.where(AziStar < -180, (AziStar + 360), AziStar)
        desvi0 = 99999
        center_est = [x_est, y_est]
        steps_center = [[250, 5], [50, 1], [0.5, 0.01], [0.05, 0.001]]
        count = 0

        for steps in steps_center:
            self.ui.progressBar.setHidden(False)
            for var1 in np.arange(-(steps[0]), (steps[0]), (steps[1])):
                for var2 in np.arange(-(steps[0]), (steps[0]), (steps[1])):
                    centrocol = (center_est[0]) + var1
                    centrofila = (center_est[1]) + var2
                    seno = centrocol - col
                    coseno = centrofila - fila
                    d_radial = np.sqrt(seno * seno + coseno * coseno)
                    angulo = np.rad2deg(np.arctan2(seno, coseno))
                    angulo = np.where(angulo > 180, (angulo - 360), angulo)
                    angulo = np.where(angulo < -180, (angulo + 360), angulo)
                    dif = angulo - AziStar
                    desvi = utils.circular_std(dif)
                    if desvi < desvi0:
                        center_col = centrocol
                        center_row = centrofila
                        desvi0 = desvi
                    count += 1
                    self.ui.progressBar.setValue(int(count / 40000 * 100) - 5)
                QtCore.QCoreApplication.processEvents()

            center_est[0] = center_col
            center_est[1] = center_row
        self.ui.progressBar.setHidden(True)
        self.ui.verticalWidget_center.setHidden(False)
        self.ui.center_img.setText(
            str(round(center_est[0], 3)) + " x " + str(round(center_est[1], 3))
        )
        flip = 0
        if self.ui.flip_vertical.isChecked():
            flip = 1
        if self.ui.flip_horizontal.isChecked():
            flip = 2
        if self.ui.flip_vertical.isChecked() and self.ui.flip_horizontal.isChecked():
            flip = 3

        azimut, zenit, shift_north = utils.calculate_matrix(
            center_est[0],
            center_est[1],
            int(img_h),
            int(img_w),
            data_file,
            self.ui.poly_degree.value(),
            flip,
        )
        self.ui.progressBar.setValue(100)
        self.ui.shift_north.setText(str(round(shift_north, 2)) + "º")
        pixmap_azimut = QtGui.QPixmap("data/tmp/azimut.png")
        self.ui.azimut_matrix_plot.setPixmap(pixmap_azimut)
        self.ui.azimut_matrix_plot.setScaledContents(True)

        pixmap_zenit = QtGui.QPixmap("data/tmp/zenit.png")
        self.ui.zenit_matrix_plot.setPixmap(pixmap_zenit)
        self.ui.zenit_matrix_plot.setScaledContents(True)

        pixmap_adjust = QtGui.QPixmap("data/tmp/adj_degree.png")
        self.ui.adjus_plot.setPixmap(pixmap_adjust)
        self.ui.adjus_plot.setScaledContents(True)

        if self.ui.save_azimut.text() != "":
            np.save(self.ui.save_azimut.text(), azimut)
        if self.ui.save_zenit.text() != "":
            np.save(self.ui.save_zenit.text(), zenit)
        self.control_widget(True)

        del azimut, zenit

    def calculate_fov(self):
        self.control_widget(False)
        self.ui.stop_fov.setHidden(False)
        self.btn2pushed = False
        self.ui.remaing.clear()

        f1 = lambda y, x: -1.0 * (
            np.sin(np.sqrt(x * x + y * y)) / (np.sqrt(x * x + y * y))
        )
        azimut = np.load(self.ui.input_azimut_fov.text())
        zenit = np.load(self.ui.input_zenit_fov.text())
        img_h = np.shape(azimut)[0]
        img_w = np.shape(azimut)[1]
        rpd = np.pi / 180
        az = azimut * rpd
        zen = zenit * rpd
        fov = zen * np.nan
        count = 0
        self.ui.progressBar_fov.setHidden(False)
        stoped = False
        for i in np.arange(1, img_h - 1):
            if self.btn2pushed == True:
                stoped = True
                break
            start = perf_counter()
            for j in np.arange(1, img_w - 1):
                zen_v = zen[i, j]
                az_v = az[i, j]
                if not np.isnan(az.all()) and not np.isnan(zen.all()):
                    if self.btn2pushed == True:
                        stoped = True
                        break
                    x = zen_v * np.cos(az_v)
                    y = zen_v * np.sin(az_v)
                    x1 = zen[i + 1, j] * np.cos(az[i + 1, j])
                    x2 = zen[i - 1, j] * np.cos(az[i - 1, j])
                    lado1 = np.abs((x2 - x1) / 2)
                    y1 = zen[i, j + 1] * np.sin(az[i, j + 1])
                    y2 = zen[i, j - 1] * np.sin(az[i, j - 1])
                    lado2 = np.abs((y2 - y1) / 2)
                    x_1 = x - lado1 / 2
                    x_2 = x + lado1 / 2
                    y_1 = y - lado2 / 2
                    y_2 = y + lado2 / 2
                    if (
                        not np.isnan(x_1.all())
                        or not np.isnan(x_2.all())
                        or not np.isnan(y_1.all())
                        or not np.isnan(y_2.all())
                    ):
                        qa1 = dblquad(f1, x_1, x_2, lambda x: y_1, lambda x: y_2)
                        fov[i, j] = np.abs(qa1[0])

                    QtCore.QCoreApplication.processEvents()
                    count += 1

                else:
                    continue
            progress = 100 * i / np.float(len(np.arange(1, img_h - 1)))
            self.ui.progressBar_fov.setValue(progress)
            stop = perf_counter()
            remaining = round((stop - start) * (img_h - i))
            self.ui.remaing.setText(
                "Estimated time " + str(utils.convert(remaining)) + " remaining"
            )
        self.ui.stop_fov.setHidden(True)
        self.ui.remaing.clear()
        if stoped == False:
            utils_plots.plot_matrix(data=fov, title="FOV matrix", type="fov")
            pixmap_fov = QtGui.QPixmap("data/tmp/fov.png")
            self.ui.fov_matrix_plot.setPixmap(pixmap_fov)
            self.ui.fov_matrix_plot.setScaledContents(True)

            if self.ui.save_fov.text() != "":
                np.save(self.ui.save_fov.text(), fov)
        else:
            self.ui.remaing.setText("The FOV matrix calculation have been stopped")
        self.control_widget(True)

    def check_calibration(self):
        self.ui.save_check_data.setHidden(False)
        lat = self.ui.latitude_util.value()
        lon = self.ui.longitude_util.value()
        elev = self.ui.elevation_util.value()
        star = self.ui.stars_util.currentText()
        img_path = self.ui.images_path_util.text()
        azimut_matrix = np.load(self.ui.input_azimut_util.text())
        zenit_matrix = np.load(self.ui.input_zenit_util.text())

        results = []
        selected_points = []
        teoric_points = []
        distances = []
        azimut_lst = []
        azimut_brightness = []
        zenit_lst = []
        zenit_brightness = []
        i = 0
        e = 0

        # ========== Get a list with all image in folder path ==========
        files = utils.read_img_path(img_path)
        for fichero in files:

            # ========== Get azimuth and zenith for selected star ==========
            zenit_star, azimut_star = utils.get_star(
                name=star,
                lat_=lat,
                date_=utils.get_date_img(fichero),
                lon_=lon,
                elev_=elev,
            )

            if zenit_star < 83:
                self.ui.progressBar_util.setHidden(False)
                self.ui.info_util_check.setHidden(False)
                self.ui.save_check_data.setEnabled(True)

                # ========== Read image as grayscale mode ==========
                img = cv2.imread(str(img_path) + str(fichero), 0)

                # ========== Get image size ==========
                img_h, img_w = np.shape(img)
                max_dim = np.max((img_h, img_w))
                plus_width = int(np.ceil(max_dim / 100))
                plus_height = int(np.ceil(max_dim / 100))

                # ========== Get pixel position by azimuth and zenith matrix ==========
                teoric_coord = utils.select_pixel(
                    azimut_star,
                    zenit_star,
                    np.array(azimut_matrix),
                    np.array(zenit_matrix),
                )
                if azimut_star < 0:
                    azimut_star = azimut_star + 360

                # ========== Select a region to find the maximum bright pixel and get the position ==========
                imCrop = img[
                    int(teoric_coord[1])
                    - plus_width : int(teoric_coord[1])
                    + plus_width,
                    int(teoric_coord[0] - plus_height) : int(
                        teoric_coord[0] + plus_height
                    ),
                ]
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(imCrop)
                coord = (
                    maxLoc[0] + (teoric_coord[0] - plus_height),
                    maxLoc[1] + teoric_coord[1] - plus_width,
                )

                # ========== Calculate pixel distance ==========
                distance = utils.pixel_distance(
                    teoric_coord[0], teoric_coord[1], coord[0], coord[1],
                    np.array(azimut_matrix), np.array(zenit_matrix)
                )

                if distance >= 0:
                    distances.append(distance)
                    azimut_lst.append(azimut_star)
                    zenit_lst.append(zenit_star)
                    selected_points.append(coord)
                    teoric_points.append(teoric_coord)
                    azimut_brightness.append(azimut_matrix[coord[1], coord[0]])
                    zenit_brightness.append(zenit_matrix[coord[1], coord[0]])

                # ========== Draw a circle in select and teoric points ==========
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                if len(selected_points) > 0:
                    for point in selected_points:
                        image_result = cv2.circle(img, point, 4, (0, 255, 0), 2)
                if len(teoric_points) > 0:
                    for teo_point in teoric_points:
                        image_result = cv2.circle(img, teo_point, 4, (12, 12, 205), 2)
                image_result = cv2.circle(img, coord, 10, (255, 255, 255), 6)

                # ========== Show selected image ==========
                size = image_result.shape
                step = image_result.size / size[0]
                qformat = QtGui.QImage.Format_Indexed8
                if len(size) == 3:
                    if size[2] == 4:
                        qformat = QtGui.QImage.Format_RGBA8888
                    else:
                        qformat = QtGui.QImage.Format_RGB888
                img = QtGui.QImage(image_result, size[1], size[0], step, qformat)
                img = img.rgbSwapped()
                self.ui.img_util_check.setPixmap(
                    QtGui.QPixmap.fromImage(img).scaled(
                        841,
                        561,
                        QtCore.Qt.KeepAspectRatio,
                        QtCore.Qt.SmoothTransformation,
                    )
                )

                # ========== Data to add at the output file ==========
                results_to_add = (coord[0], coord[1], zenit_star, azimut_star)
                point = (coord[0], coord[1])
                QtCore.QCoreApplication.processEvents()

                self.ui.progressBar_util.setValue(int(i / len(files) * 100))

                i += 1
            else:
                e += 1
        self.ui.progressBar_util.setHidden(True)
        self.check_data = azimut_lst, zenit_lst, distances
        if len(self.check_data[0]) < 2:
            self.ui.save_check_data.setHidden(True)

        # ========== Show message if the zenith < 83 in all images ==========
        if e == len(files):
            self.msgBox(
                text_title="Star not found in images",
                text_header="Select another star",
                text_body="The selected star does not appear in the image",
            )
            self.ui.finish_auto.setHidden(True)
        else:
            if i >= 2:
                # ========== Plot data and save ==========
                utils_plots.plot_pixel_distances(
                    distances, np.max(distances), len(distances)
                )
                pixmap_distance = QtGui.QPixmap("data/tmp/dist.png")
                self.ui.show_graph_1_util.setPixmap(pixmap_distance)
                self.ui.show_graph_1_util.setScaledContents(True)

                utils_plots.plot_pixel_azi_zen(distances, azimut_lst, "azim")
                pixmap_distance_azim = QtGui.QPixmap("data/tmp/dist_azim.png")
                self.ui.show_graph_2_util.setPixmap(pixmap_distance_azim)
                self.ui.show_graph_2_util.setScaledContents(True)

                utils_plots.plot_pixel_azi_zen(distances, zenit_lst, "zen")
                pixmap_distance_zen = QtGui.QPixmap("data/tmp/dist_zen.png")
                self.ui.show_graph_3_util.setPixmap(pixmap_distance_zen)
                self.ui.show_graph_3_util.setScaledContents(True)

                utils_plots.plot_check_azimuth(azimut_lst, azimut_brightness)
                pixmap_check_azimuth = QtGui.QPixmap("data/tmp/adj_azim.png")
                self.ui.show_graph_4_util.setPixmap(pixmap_check_azimuth)
                self.ui.show_graph_4_util.setScaledContents(True)

                utils_plots.plot_check_zenith(zenit_lst, zenit_brightness)
                pixmap_check_zenith = QtGui.QPixmap("data/tmp/adj_zen.png")
                self.ui.show_graph_5_util.setPixmap(pixmap_check_zenith)
                self.ui.show_graph_5_util.setScaledContents(True)

                utils_plots.plot_check_azimuth(
                    azim_object=azimut_lst, azim_brightness=azimut_brightness
                )

            if i == 1:
                self.msgBox(
                    text_title="Warning",
                    text_header="Only appear one time in images",
                    text_body="Not showed the information about calibration",
                )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    application = mywindow()

    application.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
