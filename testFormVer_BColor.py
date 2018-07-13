# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testFormMain.ui'
#
# Created: Tue May 22 15:08:26 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import os
from PySide2 import QtCore, QtGui, QtWidgets
import base64


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        print("==================================CALLING UI MAINWINDOW")
        print("\n")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 558)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #E6E6E6;")



        # self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)

        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget  QTabBar::tab{\n"
                                     "border-color: #aa0000;\n"
                                     "min-width: 12em;\n"
                                     "padding: 4px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "height: 30px"
                                     "}\n"
                                     "\n"
                                     
                                     "QTabWidget  QTabBar::tab:!selected{\n"
                                     "padding-left:50px;\n"
                                     "background-color: #E6E6E6;\n"
                                     "font: 15px \"Roboto\";\n"
                                     "color: #606060;\n"
                                     "border-right: 1px solid #D3D3D3;\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget  QTabBar::tab:selected{\n"
                                     "background-color: #EEEEEE;\n"
                                     "font: 16px \"Roboto\";\n"
                                     "color: #606060;\n"
                                     "border-right: 1px solid #D3D3D3;\n"
                                     "text-align: center"
                                     "}\n"
                                     "\n"
                                     "")

        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        print("==================================CALLING UI MAINWINDOW3")
        print("\n")

        self.corner_widget = QtWidgets.QWidget()
        self.corner_widget.setStyleSheet("min-width: 350px;float: right!important; \n")
        # self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.corner_widget)
        # self.horizontalLayout.setSpacing(0)
        # self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.closebutton = QtWidgets.QPushButton("")
        rMyIcon = QtGui.QPixmap("close.png")
        # rMyIcon.loadFromData(base64.b64decode(back_d))
        rMyIcon.setMaximumWidth = 50
        self.closebutton.setIcon(rMyIcon)
        self.closebutton.setIconSize(QtCore.QSize(20, 20))
        self.closebutton.setObjectName("closeBtn")
        self.closebutton.setMaximumWidth(30)
        self.closebutton.setStyleSheet(
            # "margin-left: 600px!important;\n"
            "\n"
            "border:none;\n"
            "position: absolute;\n"

            # "left: 100px;\n"

            "float: right!important; \n"
            "max-width: 30px!important;\n"
            "min-width: 30px!important;\n"
            "padding: 1px;\n"
            "height: 28px!important;\n"
            "color: #606060;")

        # self.bookMarkCombo = QtGui.QComboBox(self.centralwidget)
        self.bookMarkCombo = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookMarkCombo.sizePolicy().hasHeightForWidth())
        # self.bookMarkCombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.bookMarkCombo.setFont(font)
        self.bookMarkCombo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 8pt \"Roboto\";\n"
                                         "border-width: 1px;\n"
                                         # "margin-left: 600px!important;\n"
                                         "\n"
                                         "position: absolute;\n"
                                         # "left: 100px;\n"
                                         "float: right!important; \n"
                                         "max-width: 300px!important;\n"
                                         "min-width: 300px!important;\n"
                                         "padding: 1px;\n"
                                         "height: 22px!important;\n"
                                         "border-color: rgb(170, 0, 0);\n"
                                         "color: #606060;")
        self.bookMarkCombo.setEditable(False)
        # self.bookMarkCombo.setCurrentText("")
        self.bookMarkCombo.setFrame(True)
        self.bookMarkCombo.setObjectName("bookMarkCombo")

        self.status_txt1 = QtWidgets.QLabel()
        movie = QtGui.QMovie("loading.gif")
        self.status_txt1.setMovie(movie)
        # movie.start()
        self.status_txt1.setLayout(QtWidgets.QHBoxLayout())
        self.status_txt1.setStyleSheet(
            "border:none;\n"
            "margin-right:0px;\n"
            "position: absolute;\n"
            # "left: 100px;\n"
            "max-width: 60px!important;\n"
            "min-width: 60px!important;\n"
            "padding: 0px;\n"
            "height: 60px!important;\n"
        )
        self.horizontalLayout.addWidget(self.status_txt1)
        print("==================================CALLING UI MAINWINDOW4")
        print("\n")

        width = 20
        self.backbutton = QtWidgets.QPushButton("")
        rMyIcon = QtGui.QPixmap("back_d.png")
        # rMyIcon.loadFromData(base64.b64decode(back_d))
        rMyIcon.setMaximumWidth = 50
        self.backbutton.setIcon(rMyIcon)
        self.backbutton.setIconSize(QtCore.QSize(20, 20))
        self.backbutton.setObjectName("backBtn")
        self.backbutton.setMaximumWidth(width)
        self.backbutton.setStyleSheet(
            # "margin-left: 600px!important;\n"
            "\n"
            "border:none;\n"
            "position: absolute;\n"

            # "left: 100px;\n"

            "float: right!important; \n"
            "max-width: 30px!important;\n"
            "min-width: 30px!important;\n"
            "padding: 1px;\n"
            "height: 28px!important;\n"
            "color: #606060;")

        self.horizontalLayout.addWidget(self.backbutton)

        self.fwbutton = QtWidgets.QPushButton("")
        self.fwbutton.isFlat = True
        rMyIcon = QtGui.QPixmap("forward_d.png")
        self.fwbutton.setIcon((rMyIcon))
        self.fwbutton.setIconSize(QtCore.QSize(20, 20))
        self.fwbutton.setObjectName("fwBtn")
        self.fwbutton.setMaximumWidth(width)
        self.fwbutton.setStyleSheet(
            # "margin-left: 600px!important;\n"
            "\n"
            "border:none;\n"
            "margin-right:15px;\n"
            "position: absolute;\n"
            # "left: 100px;\n"
            "float: right!important; \n"
            "max-width: 20px!important;\n"
            "min-width: 20px!important;\n"
            "padding: 1px;\n"
            "height: 22px!important;\n"
        )
        self.horizontalLayout.addWidget(self.fwbutton)

        self.horizontalLayout.addWidget(self.bookMarkCombo)

        self.horizontalLayout.addWidget(self.closebutton)

        # self.label_provImage = QtGui.QLabel(self.centralwidget)
        self.label_provImage = QtWidgets.QLabel(self.centralwidget)
        self.label_provImage.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_provImage.sizePolicy().hasHeightForWidth())
        self.label_provImage.setSizePolicy(sizePolicy)
        # self.label_provImage.setMinimumSize(QtCore.QSize(100, 2000))
        self.label_provImage.setMaximumSize(QtCore.QSize(150, 3500))
        font = QtGui.QFont()
        self.label_provImage.setFont(font)
        self.label_provImage.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_provImage.setStyleSheet("")
        self.label_provImage.setText("")
        # self.label_provImage.setPixmap(QtGui.QPixmap("icons/ProvLogoMain.png"))
        self.label_provImage.show()
        self.label_provImage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_provImage.setWordWrap(True)
        self.label_provImage.setObjectName("label_provImage")
        self.label_provImage.setScaledContents(True)
        # self.horizontalLayout.addWidget(self.label_provImage)
        # self.Quit = QtGui.QPushButton(self.centralwidget)
        # self.Quit = QtGui.QPushButton(self.centralwidget)
        # self.Quit = QtGui.QToolButton(self.centralwidget)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.Quit.sizePolicy().hasHeightForWidth())
        # self.Quit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        # self.Quit.setFont(font)
        # self.Quit.setStyleSheet("QToolButton#Pressed{\n"
        #     "background: transparent;\n"
        #     "padding: 2px 2px!important;\n"
        #     "max-width: 10px!important;\n"
        #     "text-align: center;\n"
        #     "display: inline-block;\n"
        #     "}\n"
        #     "QToolButton#Quit:pressed {\n"
        #     "    border-style: inset;\n"
        #     "}\n"
        #     "\n"
        #     "")
        # self.Quit.setObjectName("Quit")
        # self.horizontalLayout.addWidget(self.Quit)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        # self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")

        self.test_console = QtWidgets.QWidget()
        self.test_console.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.test_console.setObjectName("test_console")
        self.tabWidget.addTab(self.test_console, "")

        self.search_option = QtWidgets.QWidget()
        self.search_option.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_option.setObjectName("search_option")

        # self.tabWidget.setCornerWidget(self.Quit)
        #self.formLayout = QtWidgets.QFormLayout(self.search_option)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.lineEdit = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.lineEdit)

        self.tabWidget.addTab(self.search_option, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        # MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        button_icon = QtGui.QPixmap(self.get_push_button_path())
        # self.Quit.setIcon(button_icon)

        self.retranslateUi(MainWindow)
        self.bookMarkCombo.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(1)
        # QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.tabWidget.setCurrentIndex)
        self.tabWidget.currentChanged.connect(self.tabWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tabWidget.setCornerWidget(self.corner_widget)
        # self.tabWidget.setCornerWidget(self.bookMarkCombo)
        # self.tabWidget.setCornerWidget(self.Quit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None))
        # self.Quit.setText(QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_console),
                                  QtWidgets.QApplication.translate("MainWindow", "Test Console", None))

        #self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "Look Here For Help", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_option),
                                  QtWidgets.QApplication.translate("MainWindow", "Search Option", None))

    def get_push_button_path(self):
        return "{}{}img{}cross.png".format(os.getcwd(), os.sep, os.sep)