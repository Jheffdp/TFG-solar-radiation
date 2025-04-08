# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Qt\help_manual.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_manual_2(object):
    def setupUi(self, help_manual_2):
        help_manual_2.setObjectName("help_manual_2")
        help_manual_2.resize(536, 451)
        font = QtGui.QFont()
        font.setFamily("Arial")
        help_manual_2.setFont(font)
        help_manual_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.help_manual = QtWidgets.QTextBrowser(help_manual_2)
        self.help_manual.setGeometry(QtCore.QRect(10, 10, 511, 391))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.help_manual.setFont(font)
        self.help_manual.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.help_manual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.help_manual.setLineWidth(0)
        self.help_manual.setObjectName("help_manual")
        self.close_btn = QtWidgets.QPushButton(help_manual_2)
        self.close_btn.setGeometry(QtCore.QRect(220, 410, 88, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(help_manual_2)
        QtCore.QMetaObject.connectSlotsByName(help_manual_2)

    def retranslateUi(self, help_manual_2):
        _translate = QtCore.QCoreApplication.translate
        help_manual_2.setWindowTitle(_translate("help_manual_2", "Identify star (manual mode) - Help"))
        self.help_manual.setHtml(_translate("help_manual_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Latitude: </span>90º N to -90º S</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Longitude:</span> -180º W to 180º E</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Elevation:</span> Meters above sea level.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Star:</span> Select a star from PyEphem library catalog to perform the calibration.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Images path:</span> Select the folder where are located the images for the calibration. The supported filename format is “calib_ymd_hm.extension” (Example: calib_20200224_0235.jpg or calib_20200224_0235.png). The tools menú includes a tool to rename the files to this format.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Save file:</span> Select the path to save the output.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Point selection window:</span> In this a rectangle around a star can be dragged by the user. In this area the brightest point is selected. For skip the image press C.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Add point:</span> To add the selected point to the data set.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Remove point:</span> To reject the selected point in the data set.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Finish:</span> To finish the point selection.</p></body></html>"))
        self.close_btn.setText(_translate("help_manual_2", "Close"))
import img.resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_manual_2 = QtWidgets.QDialog()
    ui = Ui_help_manual_2()
    ui.setupUi(help_manual_2)
    help_manual_2.show()
    sys.exit(app.exec_())
