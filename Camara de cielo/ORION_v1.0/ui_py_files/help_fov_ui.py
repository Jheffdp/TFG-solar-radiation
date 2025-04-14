# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt/help_fov.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_fov(object):
    def setupUi(self, help_fov):
        help_fov.setObjectName("help_fov")
        help_fov.resize(436, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo_app-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help_fov.setWindowIcon(icon)
        help_fov.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.help_manual = QtWidgets.QTextBrowser(help_fov)
        self.help_manual.setGeometry(QtCore.QRect(10, 10, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.help_manual.setFont(font)
        self.help_manual.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.help_manual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.help_manual.setLineWidth(0)
        self.help_manual.setObjectName("help_manual")
        self.close_btn = QtWidgets.QPushButton(help_fov)
        self.close_btn.setGeometry(QtCore.QRect(180, 100, 88, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(help_fov)
        QtCore.QMetaObject.connectSlotsByName(help_fov)

    def retranslateUi(self, help_fov):
        _translate = QtCore.QCoreApplication.translate
        help_fov.setWindowTitle(_translate("help_fov", "Calculate FOV matrix - Help"))
        self.help_manual.setHtml(_translate("help_fov",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\'; font-size:9pt; font-weight:600;\">Input azimuth and zenith matrix:</span><span style=\" font-family:\'Open Sans\'; font-size:9pt;\"> To select the path of each matrix file</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Open Sans\'; font-size:9pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\'; font-size:9pt; font-weight:600;\">Save fov matrix:</span><span style=\" font-family:\'Open Sans\'; font-size:9pt;\"> To select the path to save fov matrix file</span></p></body></html>"))
        self.close_btn.setText(_translate("help_fov", "Close"))
import img.resource


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    help_fov = QtWidgets.QDialog()
    ui = Ui_help_fov()
    ui.setupUi(help_fov)
    help_fov.show()
    sys.exit(app.exec_())
