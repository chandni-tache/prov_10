# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accessCodeForm.ui'
#
# Created: Tue May 22 17:38:11 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import os
from PySide2 import QtCore, QtGui,QtWidgets
from PySide2.QtWidgets import QDialog
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        """
        :type Dialog: QDialog
        """
        print("==============----------------DIALOG MAKING ACCESSCODE")
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 200)
        Dialog.setMaximumSize(500,200)
        Dialog.setStyleSheet("background-color:white;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(500, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)

        # Dialog.setAutoFillBackground(True)
        # # Replacing the background color of the qdialog
        # background_palette = QtGui.QPalette()
        # background_color = QtGui.QColor(255, 255, 255)
        # background_palette.setColor(
        #     QtGui.QPalette.Background, background_color)
        # Dialog.setPalette(background_palette)
        # Dialog.setStyleSheet(
        #     "background-color: #E6232C, color:#000;")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        #self.label.setText("ACCESS CODE")
        #self.label.setPixmap(QtGui.QPixmap("icons/ProvLogo.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_info = QtWidgets.QLabel(Dialog)
        self.label_info.setStyleSheet("color: rgb(170, 0, 0);\n"
"font-size: 8pt \"MS Shell Dlg 2\";")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "text-align: center;\n"
            "margin-left: 90px; \n"
            "border-width: 2px;\n"
            "border-radius: 2px;\n"
            "border-color: #000;\n"
            "min-width: 8em;\n"
            "width: 50%;\n"
            "padding: 5px;\n"
            "color: #333;\n"
            "font: 75 10pt \"Roboto \";")
        self.lineEdit.setPlaceholderText("ENTER ACCESS CODE")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 30))
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButtonSubmit = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSubmit.sizePolicy().hasHeightForWidth())
        self.pushButtonSubmit.setSizePolicy(sizePolicy)
        self.pushButtonSubmit.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButtonSubmit.setMaximumSize(QtCore.QSize(400, 30))
        self.pushButtonSubmit.setStyleSheet("\n"
            "QPushButton#pushButtonSubmit {\n"
            "    background-color: #E6232C;\n"
            "    border-style: outset;\n"
            "    margin-left: 90px; \n"
            "    width: 100%;\n"
            "    border-width: 1px;\n"
            "    border-radius: 2px;\n"
            "    border-color: 1px solid #E6232C;\n"
            "    color: #ffffff;\n"
            "    font: bold 14px;\n"
            "    min-width: 6em;\n"
            "    padding: 5px;\n"
            "}\n"
            "QPushButton#pushButtonSubmit:pressed {\n"
            "   \n"
            "    background-color: #E6232C;\n"
            "    color: #ffffff;\n"
            "    border-style: inset;\n"
            "}")
        button_icon = QtGui.QIcon(self.get_push_button_path())
        self.pushButtonSubmit.setIcon(button_icon)
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        self.verticalLayout.addWidget(self.pushButtonSubmit)
        spacerItem3 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Dialog)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None))
        self.label_info.setText(QtWidgets.QApplication.translate("Dialog", "PLEASE ENTER ACCESS CODE", None))
        self.pushButtonSubmit.setText(QtWidgets.QApplication.translate("Dialog", "SUBMIT", None))

    def get_push_button_path(self):
        return "{}{}img{}arrow.png".format(os.getcwd(),os.sep, os.sep)

import icons_rc
