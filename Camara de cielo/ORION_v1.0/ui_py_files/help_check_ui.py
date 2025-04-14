# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Qt\help_check.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_check(object):
    def setupUi(self, help_check):
        help_check.setObjectName("help_check")
        help_check.resize(530, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo_app-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help_check.setWindowIcon(icon)
        help_check.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.help_manual = QtWidgets.QTextBrowser(help_check)
        self.help_manual.setGeometry(QtCore.QRect(10, 10, 511, 311))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.help_manual.setFont(font)
        self.help_manual.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.help_manual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.help_manual.setLineWidth(0)
        self.help_manual.setObjectName("help_manual")
        self.close_btn = QtWidgets.QPushButton(help_check)
        self.close_btn.setGeometry(QtCore.QRect(220, 330, 88, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(help_check)
        QtCore.QMetaObject.connectSlotsByName(help_check)

    def retranslateUi(self, help_check):
        _translate = QtCore.QCoreApplication.translate
        help_check.setWindowTitle(_translate("help_check", "Check calibration - Help"))
        self.help_manual.setHtml(_translate("help_check", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Latitude:</span> 90º N to -90º S</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Longitude:</span> -180º W to 180º E</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Elevation:</span> Meters above mean sea level</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                    </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Star:</span> Select a star from PyEphem library catalog to perform the calibration.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Images path:</span> Select the folder where are located the images for the calibration. The supported filename format is “calib_ymd_hm.extension” (Example: calib_20200224_0235.jpg or calib_20200224_0235.png). The tools menú includes a tool to rename the files to this format.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Input azimuth and zenith matrix:</span> To select the path for each matrix file.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Save data:</span> Save .txt file with the generated data from calibration check. These data are: image datetime, azimuth, zenith and distance between the selected pixel from calibration and the brightest pixel.</p></body></html>"))
        self.close_btn.setText(_translate("help_check", "Close"))
import img.resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_check = QtWidgets.QDialog()
    ui = Ui_help_check()
    ui.setupUi(help_check)
    help_check.show()
    sys.exit(app.exec_())
