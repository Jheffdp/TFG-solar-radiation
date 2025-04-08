# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt/help_center.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_center(object):
    def setupUi(self, help_center):
        help_center.setObjectName("help_center")
        help_center.resize(475, 192)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo_app-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help_center.setWindowIcon(icon)
        help_center.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.help_manual = QtWidgets.QTextBrowser(help_center)
        self.help_manual.setGeometry(QtCore.QRect(10, 10, 451, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.help_manual.setFont(font)
        self.help_manual.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.help_manual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.help_manual.setLineWidth(0)
        self.help_manual.setObjectName("help_manual")
        self.close_btn = QtWidgets.QPushButton(help_center)
        self.close_btn.setGeometry(QtCore.QRect(190, 150, 88, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(help_center)
        QtCore.QMetaObject.connectSlotsByName(help_center)

    def retranslateUi(self, help_center):
        _translate = QtCore.QCoreApplication.translate
        help_center.setWindowTitle(_translate("help_center", "Calculate center and calibration matrix - Help"))
        self.help_manual.setHtml(_translate("help_center",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Image width:</span> pixels</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Image height:</span> pixels</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Input files path:</span> Select the data files generated on stars identification.</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Save azimuth and zenith matrix:</span> Select the path to save each matrix file.</p></body></html>"))
        self.close_btn.setText(_translate("help_center", "Close"))
import img.resource


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    help_center = QtWidgets.QDialog()
    ui = Ui_help_center()
    ui.setupUi(help_center)
    help_center.show()
    sys.exit(app.exec_())
