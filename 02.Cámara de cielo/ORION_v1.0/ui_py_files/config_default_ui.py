# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Qt\config_default.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 381)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo_app-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 10, 378, 54))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_lat = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_lat.setFont(font)
        self.label_lat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lat.setObjectName("label_lat")
        self.verticalLayout_2.addWidget(self.label_lat)
        self.latitude = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.latitude.setFont(font)
        self.latitude.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.latitude.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.latitude.setSpecialValueText("")
        self.latitude.setMinimum(-90.0)
        self.latitude.setMaximum(90.0)
        self.latitude.setObjectName("latitude")
        self.verticalLayout_2.addWidget(self.latitude)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_lon = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_lon.setFont(font)
        self.label_lon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lon.setObjectName("label_lon")
        self.verticalLayout_3.addWidget(self.label_lon)
        self.longitude = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.longitude.setFont(font)
        self.longitude.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.longitude.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.longitude.setMinimum(-180.0)
        self.longitude.setMaximum(180.0)
        self.longitude.setObjectName("longitude")
        self.verticalLayout_3.addWidget(self.longitude)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_elev = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_elev.setFont(font)
        self.label_elev.setAlignment(QtCore.Qt.AlignCenter)
        self.label_elev.setObjectName("label_elev")
        self.verticalLayout_4.addWidget(self.label_elev)
        self.elevation = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.elevation.setFont(font)
        self.elevation.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.elevation.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.elevation.setDecimals(1)
        self.elevation.setMaximum(8000.0)
        self.elevation.setObjectName("elevation")
        self.verticalLayout_4.addWidget(self.elevation)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 71, 261, 54))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_img_w = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_img_w.setFont(font)
        self.label_img_w.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_w.setObjectName("label_img_w")
        self.verticalLayout_12.addWidget(self.label_img_w)
        self.width_img = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.width_img.setFont(font)
        self.width_img.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.width_img.setDecimals(0)
        self.width_img.setMaximum(5000.0)
        self.width_img.setObjectName("width_img")
        self.verticalLayout_12.addWidget(self.width_img)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_img_h = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_img_h.setFont(font)
        self.label_img_h.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_h.setObjectName("label_img_h")
        self.verticalLayout_13.addWidget(self.label_img_h)
        self.height_img = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.height_img.setFont(font)
        self.height_img.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.height_img.setDecimals(0)
        self.height_img.setMaximum(5000.0)
        self.height_img.setObjectName("height_img")
        self.verticalLayout_13.addWidget(self.height_img)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 130, 361, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_14.addWidget(self.label_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.images_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.images_path.setFont(font)
        self.images_path.setObjectName("images_path")
        self.horizontalLayout_14.addWidget(self.images_path)
        self.images_path_btn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.images_path_btn.setObjectName("images_path_btn")
        self.horizontalLayout_14.addWidget(self.images_path_btn)
        self.verticalLayout_14.addLayout(self.horizontalLayout_14)
        self.verticalLayout_20.addLayout(self.verticalLayout_14)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_20.addWidget(self.label_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.input_azimut = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.input_azimut.setFont(font)
        self.input_azimut.setObjectName("input_azimut")
        self.horizontalLayout_12.addWidget(self.input_azimut)
        self.input_azimut_btn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.input_azimut_btn.setObjectName("input_azimut_btn")
        self.horizontalLayout_12.addWidget(self.input_azimut_btn)
        self.verticalLayout_20.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem6)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_21.addWidget(self.label_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.input_zenit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.input_zenit.setFont(font)
        self.input_zenit.setObjectName("input_zenit")
        self.horizontalLayout_13.addWidget(self.input_zenit)
        self.input_zenit_btn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.input_zenit_btn.setObjectName("input_zenit_btn")
        self.horizontalLayout_13.addWidget(self.input_zenit_btn)
        self.verticalLayout_21.addLayout(self.horizontalLayout_13)
        self.verticalLayout.addLayout(self.verticalLayout_21)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(70, 340, 321, 33))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.close_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setAutoDefault(True)
        self.close_btn.setDefault(False)
        self.close_btn.setFlat(False)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.save_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_3.addWidget(self.save_btn)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 320, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saved = QtWidgets.QLabel(Dialog)
        self.saved.setGeometry(QtCore.QRect(210, 310, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.saved.setFont(font)
        self.saved.setAlignment(QtCore.Qt.AlignCenter)
        self.saved.setObjectName("saved")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Config defaults inputs values"))
        self.label_lat.setText(_translate("Dialog", "Latitude"))
        self.label_lon.setText(_translate("Dialog", "Longitude"))
        self.label_elev.setText(_translate("Dialog", "Elevation"))
        self.label_img_w.setText(_translate("Dialog", "Image width"))
        self.label_img_h.setText(_translate("Dialog", "Image height"))
        self.label_3.setText(_translate("Dialog", "Images path"))
        self.images_path_btn.setText(_translate("Dialog", "..."))
        self.label_8.setText(_translate("Dialog", "Azimuth matrix"))
        self.input_azimut_btn.setText(_translate("Dialog", "..."))
        self.label_9.setText(_translate("Dialog", "Zenith matrix"))
        self.input_zenit_btn.setText(_translate("Dialog", "..."))
        self.close_btn.setText(_translate("Dialog", "Close"))
        self.save_btn.setText(_translate("Dialog", "Save"))
        self.saved.setText(_translate("Dialog", "Saved!"))
import img.resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
