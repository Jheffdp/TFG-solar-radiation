# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Qt\help_auto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_auto(object):
    def setupUi(self, help_auto):
        help_auto.setObjectName("help_auto")
        help_auto.resize(568, 513)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo_app-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help_auto.setWindowIcon(icon)
        help_auto.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.help_manual = QtWidgets.QTextBrowser(help_auto)
        self.help_manual.setGeometry(QtCore.QRect(20, 10, 541, 451))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.help_manual.setFont(font)
        self.help_manual.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.help_manual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.help_manual.setLineWidth(0)
        self.help_manual.setObjectName("help_manual")
        self.close_btn = QtWidgets.QPushButton(help_auto)
        self.close_btn.setGeometry(QtCore.QRect(240, 470, 88, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(help_auto)
        QtCore.QMetaObject.connectSlotsByName(help_auto)

    def retranslateUi(self, help_auto):
        _translate = QtCore.QCoreApplication.translate
        help_auto.setWindowTitle(_translate("help_auto", "Identify star (automatic mode) - Help"))
        self.help_manual.setHtml(_translate("help_auto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Latitude:</span><span style=\" font-size:9pt;\"> 90º N to -90º S</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Longitude:</span><span style=\" font-size:9pt;\"> -180º W to 180º E</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Elevation:</span><span style=\" font-size:9pt;\"> Meters above sea level.</span>                    </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Star:</span><span style=\" font-size:9pt;\"> Select a star from PyEphem library catalog to perform the calibration.</span>                    </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Images path:</span><span style=\" font-size:9pt;\"> Select the folder where are located the images for the calibration. The supported filename format is “calib_ymd_hm.extension” (Example: calib_20200224_0235.jpg or calib_20200224_0235.png). The tools menú includes a tool to rename the files to this format.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Save file:</span><span style=\" font-size:9pt;\"> Select the path to save the output.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Custom:</span><span style=\" font-size:9pt;\"> Select this option if previous calibration matrices are known</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">    - Input azimuth matrix:</span><span style=\" font-size:9pt;\"> Select the azimuth matrix</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">    - Input zenith matrix:</span><span style=\" font-size:9pt;\"> Select the zenith matrix</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Default:</span><span style=\" font-size:9pt;\"> Select this option for generate a default calibration matrix.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">    - Angle shift from North:</span><span style=\" font-size:9pt;\"> The shift between the top of the image and the location of North in the image. If the North in the image is in clockwise direction regards the top of the image, the shift (in degrees) must be negative.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">    - Extreme zenith:</span><span style=\" font-size:9pt;\"> Maximum zenith angle viewed in the image (it can be higher than 90º)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Add point:</span><span style=\" font-size:9pt;\"> To add the selected point to the data set.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Remove point:</span><span style=\" font-size:9pt;\"> To reject the selected point in the data set.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Finish:</span><span style=\" font-size:9pt;\"> To finish the point selection.</span></p></body></html>"))
        self.close_btn.setText(_translate("help_auto", "Close"))
import img.resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_auto = QtWidgets.QDialog()
    ui = Ui_help_auto()
    ui.setupUi(help_auto)
    help_auto.show()
    sys.exit(app.exec_())
