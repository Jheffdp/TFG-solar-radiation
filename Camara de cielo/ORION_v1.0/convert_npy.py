#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import utils_convert as util
from ui_py_files.convert_npy_ui import Ui_Dialog_convert


class dialog_convert(QtWidgets.QDialog):

    def __init__(self):
        super(dialog_convert, self).__init__()
        self.ui = Ui_Dialog_convert()
        self.ui.setupUi(self)

        # =============== Set progress bar and done hidden ===============
        self.ui.progressBar.setHidden(True)
        self.ui.done.setHidden(True)

        # =============== Select npy files ===============
        self.ui.input_files_btn.clicked.connect(lambda: self.select_npy_files())

        # =============== Select folder path for converted files ===============
        self.ui.save_files_btn.clicked.connect(lambda: self.coverted_files_path())

        # =============== Select folder path for converted files ===============
        self.ui.convert_btn.clicked.connect(lambda: self.convert_file())

        # =============== Close button ===============
        self.ui.close_btn.clicked.connect(lambda: QtWidgets.QDialog.close(self))

        self.files = []

    """ Select list npy files for convert """

    def select_npy_files(self):
        self.ui.input_list_npy.clear()
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setNameFilter("Numpy files(*.npy)")
        dialog.setDefaultSuffix(".npy")
        directory = dialog.getOpenFileNames(caption="Select npy files", filter="Numpy files(*.npy)")
        for dst in directory[0]:
            self.ui.input_list_npy.addItem(str(dst))
        self.files = directory[0]

    """ Select folder path for converted files """

    def coverted_files_path(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        directory = dialog.getExistingDirectory(caption="Select folder for converted files")
        dst = (str(directory) + "/")
        self.ui.save_files_path.setText(dst)

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

    def convert_file(self):
        save_path = self.ui.save_files_path.text()
        self.ui.done.setHidden(True)
        self.ui.progressBar.setValue(0)
        if (len(self.files) > 0) and (save_path != ""):
            self.ui.progressBar.setHidden(False)
            count = 0
            for file in self.files:
                QtCore.QCoreApplication.processEvents()
                if self.ui.mat_file.isChecked():
                    util.npy_to_mat(file, save_path)
                if self.ui.hdf5_file.isChecked():
                    util.npy_to_h5(file, save_path)
                if self.ui.csv_comma_file.isChecked():
                    util.npy_to_csv(file, save_path, ',')
                if self.ui.csv_tab_file.isChecked():
                    util.npy_to_csv(file, save_path, '\t')
                count += 1

                self.ui.progressBar.setValue(int(count / len(self.files) * 100))
            self.ui.progressBar.setHidden(True)
            self.ui.done.setHidden(False)
        else:
            if len(self.files) == 0:
                self.msgBox(text_title="Error", text_header="Files to convert is empty",
                            text_body="Please select the files to convert")
            else:
                if save_path == "":
                    self.msgBox(text_title="Error", text_header="Save folder path is empty",
                                text_body="Please select path for converted files")
