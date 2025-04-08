#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

import datetime as dt
import os
import shutil
import cv2
import pytz
from PyQt5 import QtWidgets, QtCore
from ui_py_files.rename_images_ui import Ui_rename_image


class rename_images(QtWidgets.QDialog):

    def __init__(self):
        super(rename_images, self).__init__()
        self.ui = Ui_rename_image()
        self.ui.setupUi(self)
        self.ui.progressBar.setHidden(True)
        self.ui.done.setHidden(True)

        # ========== Fill comboBox  with timezones ==========
        for tz in pytz.common_timezones:
            self.ui.comboBox.addItem(str(tz))
        index = self.ui.comboBox.findText("UTC", QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.comboBox.setCurrentIndex(index)

        # ========== Select images path ==========
        self.ui.input_btn.clicked.connect(
            lambda: self.img_path(path_field=self.ui.input_path.setText, caption="Select images folder"))

        # ========== Select save images path ==========
        self.ui.output_btn.clicked.connect(
            lambda: self.img_path(path_field=self.ui.output_path.setText, caption="Select folder for images save"))

        # ========== Run rename function ==============
        self.ui.rename_btn.clicked.connect(
            lambda: self.check_inputs_fields()
        )

        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))

    """ Check input fields to rename images """

    def check_inputs_fields(self):
        self.ui.done.setHidden(True)
        all_fine = True
        if self.ui.input_path.text() == '':
            self.msgBox(text_title="Error", text_header="Not images folder specified",
                        text_body="Please select the image folder")
            all_fine = False
        else:
            formats_list = [self.ui.format_1.isChecked(), self.ui.format_2.isChecked(), self.ui.format_3.isChecked(),
                            self.ui.format_4.isChecked(), self.ui.format_5.isChecked(), self.ui.format_6.isChecked(),
                            self.ui.format_7.isChecked(), ]
            not_selected = True
            for format in formats_list:
                if format == True:
                    not_selected = False
            if not_selected == True:
                self.msgBox(text_title="Error", text_header="No file input format selected",
                            text_body="Please select the format file")
                all_fine = False
            else:
                if self.ui.output_path.text() == '':
                    self.msgBox(text_title="Error", text_header="Not output folder specified",
                                text_body="Please select the output folder")
                    all_fine = False
        if all_fine == True:
            self.run_rename()

    """ Show messages errors for input data check
        Receive:
            text_header : string
                Window header text
            text_body : string
                Body text message error              
    """

    def msgBox(self, text_title, text_header, text_body):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(text_header)
        msg.setInformativeText(text_body)
        msg.setWindowTitle(text_title)
        msg.exec_()

    """ Select images folder is used for: Identify stars manual and automatic mode """

    def img_path(self, path_field, caption):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        directory = dialog.getExistingDirectory(caption=caption)
        dst = (str(directory) + "/")
        path_field(dst)

    """ Flip images """

    def flip_images(self, image_to_flip):
        original_img = cv2.imread(image_to_flip)
        flipped_img = original_img
        if self.ui.vertical_flip.isChecked() and self.ui.horizontal_flip.isChecked():
            flipped_img = cv2.flip(original_img, -1)
        else:
            if self.ui.vertical_flip.isChecked():
                flipped_img = cv2.flip(original_img, 0)
            else:
                if self.ui.horizontal_flip.isChecked():
                    flipped_img = cv2.flip(original_img, 1)
        return flipped_img

    def read_img_path(self, path):
        lstDir = os.listdir(path)
        lst_files = []
        for file in sorted(lstDir):
            lst_files.append(file)
        return lst_files

    ''' Read the filename format '''

    def read_format_name(self, format_name):
        bad_format = False
        yy, m, d, hh, mm = 0, 0, 0, 0, 0

        # ========== Format 1: YMDHHMM ===========
        if self.ui.format_1.isChecked():
            if len(format_name) == 12:
                try:
                    yy, m, d, hh, mm = format_name[:4], format_name[4:6], format_name[6:8], format_name[
                                                                                            8:10], format_name[10:12]
                except (ValueError, IndexError):
                    bad_format = True
            else:
                bad_format = True

        # ========== Format 2: YMD_HHMM ===========
        if self.ui.format_2.isChecked():
            if len(format_name) == 13:
                try:
                    date, time = format_name.split('_')
                    yy, m, d, hh, mm = date[:4], date[4:6], date[6:8], time[0:2], time[2:4]
                except (ValueError, IndexError):
                    bad_format = True
            else:
                bad_format = True

        # ========== Format 3: Y_M_D-HH_MM ===========
        if self.ui.format_3.isChecked():
            if len(format_name) == 13:
                try:
                    date, time = format_name.split('-')
                    yy, m, d = date.split('_')
                    hh, mm = time.split('_')
                except (ValueError, IndexError):
                    bad_format = True
            else:
                bad_format = True

        # ========== Format 4: text_YMD_HHMM ===========
        if self.ui.format_4.isChecked():
            try:
                text, date, time = format_name.split('_')
                yy, m, d = date[0:4], date[4:6], date[6:8]
                hh, mm = time[0:2], time[2:4]
            except (ValueError, IndexError):
                bad_format = True

        # ========== Format 5: Model_CAM_YMD_HHMMSS_# ===========
        if self.ui.format_5.isChecked():
            try:
                elements = format_name.split('_')
                yy, m, d, hh, mm = elements[2][0:4], elements[2][4:6], elements[2][6:8], elements[3][0:2], elements[3][
                                                                                                           2:4]
            except (ValueError, IndexError):
                bad_format = True

        # ========== Format 6: Model_CAM_YMD_HHMMSS_#_# ===========
        if self.ui.format_6.isChecked():
            try:
                elements = format_name.split('_')
                yy, m, d, hh, mm = elements[2][0:4], elements[2][4:6], elements[2][6:8], elements[3][0:2], elements[3][
                                                                                                           2:4]
            except (ValueError, IndexError):
                bad_format = True

        # ========== Format 7: HHMM (Time only) ===========
        if self.ui.format_7.isChecked():
            if len(format_name) == 4:
                date = self.ui.calendarWidget.selectedDate()
                try:
                    hh, mm = format_name[0:2], format_name[2:4]
                    yy, m, d = date.year(), date.month(), date.day()
                except (ValueError, IndexError):
                    bad_format = True
            else:
                bad_format = True
        return yy, m, d, hh, mm, bad_format

    """ Rename images files for calibration"""

    def run_rename(self):

        path = self.ui.input_path.text()
        path_output = self.ui.output_path.text()
        count = 0
        timezone = self.ui.comboBox.currentText()
        files = self.read_img_path(path)
        self.ui.progressBar.setHidden(False)
        bad_format_count = 0
        for file in files:
            try:
                name, ext = file.split('.')
                if ext == 'png' or ext == 'jpg':
                    yy, m, d, hh, mm, bad_format = self.read_format_name(str(name))
                    if bad_format == True:
                        bad_format_count += 1
                    else:
                        file_datetime = dt.datetime(int(yy), int(m), int(d), int(hh), int(mm))
                        mytimezone = pytz.timezone(timezone)  # my current timezone
                        file_datetime_adj = mytimezone.localize(file_datetime)  # localize function
                        adjust_datetime = file_datetime_adj.astimezone(pytz.timezone("UTC"))
                        calib_file_name = "calib_" + adjust_datetime.strftime("%Y%m%d_%H%M")

                        # ========== Flip images ==========
                        if self.ui.vertical_flip.isChecked() or self.ui.horizontal_flip.isChecked():
                            image = self.flip_images(image_to_flip=path + file)
                            cv2.imwrite(path_output + calib_file_name + "." + ext, image)
                        else:
                            shutil.copy(path + file, path_output + calib_file_name + "." + ext)
                    count += 1
            except (ValueError, IndexError):
                continue

            self.ui.progressBar.setValue(int(count / len(files) * 100))
        self.ui.done.setHidden(False)
        self.ui.progressBar.setHidden(True)

        if count == bad_format_count:
            self.ui.done.setHidden(True)
            self.ui.progressBar.setHidden(True)
            self.msgBox(text_title="Error", text_header="There is no file with the selected format",
                        text_body="Please select the correct format")
