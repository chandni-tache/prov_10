#!/usr/bin/python
"""
This is the main script for Lock Down Browser, a kiosk-oriented web browser
Written by Tache Technologies

"""
import pdb
from PySide2.QtWidgets import QLineEdit
# import testFormMain  testFormVer_BColor
# from testFormMain import Ui_MainWindow
from testFormVer_BColor import Ui_MainWindow
# from testFormVer_BColorStyle import Ui_MainWindow
# from testFormVer_BColor3 import Ui_MainWindow
from accessCodeForm import Ui_Dialog
import PySide2
from time import sleep
import logging
import os
from PySide2 import QtWidgets
from PySide2.QtWidgets import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
try:
    directory = os.environ["APPDATA"] + '\\Provlog'
    os.stat(directory)
except:
    try:
        os.mkdir(directory)
    except:
        print("directory not created")
import keyboard

file_handler = logging.FileHandler(os.environ["APPDATA"] + '\\Provlog\\provLock.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

appNum_handler = logging.FileHandler(os.environ["APPDATA"] + '\\Provlog\\ApplicationRuning.log', 'w')
appNum_handler.setLevel(logging.ERROR)
appNum_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(appNum_handler)
# from PySide2.QtGui import QComboBox, QPushButton
# import PySide2
# QT Binding imports
# log.basicConfig(filename='provLock.log',level=log.DEBUG,format = "%(levelname)s:%(asctime)s:%(message)s")

for i in range(0, 1):
    try:
        """Try to import PySide2"""
        print("Hello 1")

        # from PySide2.QtGui import QIcon, QKeySequence
        from PySide2.QtGui import QIcon, QKeySequence
        from PySide2.QtCore import (
            QUrl, QTimer, QObject, QEvent,
            Qt, QTemporaryFile, QDir, QCoreApplication, qVersion, Signal,
            QSizeF
        )

        from PySide2.QtWidgets import (
            QMainWindow, QAction, QWidget, QApplication, QSizePolicy,
            QToolBar, QDialog, QMenu
        )
        # from PySide2.QtWebKit import QWebEngineSettings
        from PySide2.QtPrintSupport import QPrinter, QPrintDialog
        # from PySide2.QtWebKitWidgets import QWebView, QWebEnginePage
        from PySide2.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage
        from PySide2.QtNetwork import (QNetworkRequest, QNetworkAccessManager, QNetworkProxy)
    except ImportError as e:
        print("Qt5 import error")
        print(e)
        pass

# Standard library imports
import tzlocal
import platform
import sys
import os
import argparse
import yaml
import json
import psutil
import requests
from multiprocessing import Queue
import urllib3
import re
import subprocess
import datetime
import site
import time as Time
import socket
from PySide2 import QtCore, QtGui
from functools import partial
from PySide2 import QtXml
import pyHook
from key_window import key_dict_windows
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtWebEngine import *
from PySide2.QtWebEngineWidgets import *
import PySide2.QtCore
import PySide2.QtWidgets
import PySide2.QtGui

# MESSAGE STRINGS
# You can override this string with the "page_unavailable_html" setting.
# Just set it to a filename of the HTML you want to display.
# It will be formatted agains the configuration file, so you can
# include any config settings using {config_key_name}
DEFAULT_404 = """<h2>Sorry, can't go there</h2>
<p>This page is not available on this computer.</p>
<script>setTimeout('history.back()', 5000);</script>
"""
DEFAULT_LOADING = '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>ProV</title>
    </head>
    <body style=" height: 100%;background-color: #F8F8F8;"><!--start body-->
        <div class="container"><!--starcontainer-->
            <img src="{}{}img{}logo.png"alt="logo" class="center" style="opacity: .3; height: 400px;display: block;margin-left: auto;margin-right: auto;margin-top: 1%;"/>
            <h1 style="color: #DBDBDB;font-size: 80px;text-align: center;font-family: arial;">Provlock</h1>
        </div><!--end container-->
    </body><!--end body-->
</html>
    </body>
'''.format(os.getcwd(), os.sep, os.sep)

# This text will be shown when the start_url can't be loaded
# Usually indicates lack of network connectivity.
# It can be overridden by giving a filename in "network_down_html"
# and will be formatted against the config.

DEFAULT_NETWORK_DOWN = """<h2>Network Error</h2>
<p>The start page, {start_url}, cannot be reached.
This indicates a network connectivity problem.</p>
<p>Staff, please check the following:</p>
<ul>
<li>Ensure the network connections at the computer and at the switch,
hub, or wall panel are secure</li>
<li>Restart the computer</li>
<li>Ensure other systems at your location can access the same URL</li>
</ul>
<p>If you continue t
o get this error, contact technical support</p> """

# This is shown when an https site has a bad certificate and ssl_mode is set
# to "strict".

CERTIFICATE_ERROR = """<h1>Certificate Problem</h1>
<p>The URL <strong>{url}</strong> has a problem with its SSL certificate.
For your security and protection, you will not be able to access it from
 this browser.</p>
<p>If this URL is supposed to be reachable,
 please contact technical support for help.</p>
<p>You can return to the <a href='{start_url}'>start page</a>, or wait and
you'll be returned to the
 <a href='javascript: history.back();'>previous page</a>.</p>
<script>setTimeout('history.back()', 5000);</script>
"""

# Shown when content is requested that is not HTML, text, or
# something specified in the content handlers.

UNKNOWN_CONTENT_TYPE = """<h1>Failed: unrenderable content</h1>
<p>The browser does not know how to handle the content type
<strong>{mime_type}</strong> of the file <strong>{file_name}</strong>
 supplied by <strong>{url}</strong>.</p>"""

# This is displayed while a file is being downloaded.

DOWNLOADING_MESSAGE = """<H1>Downloading</h1>
<p>Please wait while the file <strong>{filename}</strong> ({mime_type})
downloads from <strong>{url}</strong>."""

"""
:param str
"""


def debug(message):
    """Log or print a message if the global DEBUG is true."""
    if not DEBUG and not DEBUG_LOG:
        pass
    else:
        message = message.__str__()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        debug_message = ts + ":: " + message
        if DEBUG:
            print(debug_message)
        if DEBUG_LOG:
            try:
                fh = open(DEBUG_LOG, 'a')
                fh.write(debug_message + "\n")
                fh.close
            except:
                print("unable to write to log file {}".format(DEBUG_LOG))


# Define our default configuration settings
CONFIG_OPTIONS = {
    "allow_external_content": {"default": False, "type": bool},
    "allow_plugins": {"default": False, "type": bool},
    "allow_popups": {"default": False, "type": bool},
    "allow_printing": {"default": False, "type": bool},
    "bookmarks": {"default": {}, "type": dict},
    "bookmarks_Combo": {"default": {}, "type": dict},
    "content_handlers": {"default": {}, "type": dict},
    "default_encoding": {"default": "utf-8", "type": str},
    "default_password": {"default": None, "type": str},
    "default_user": {"default": None, "type": str},
    "enable_diagnostic": {"default": False, "type": bool},
    "force_js_confirm": {"default": "ask", "type": str,
                         "values": ("ask", "accept", "deny")},
    "fullscreen": {"default": False, "type": bool},
    "icon_theme": {"default": None, "type": str},
    "navigation": {"default": True, "type": bool},
    "navigation_layout": {"default":
                              ['back', 'forward', 'refresh', 'stop',
                               'zoom_in', 'zoom_out', 'separator',
                               'bookmarks', 'separator', 'spacer',
                               'quit', 'Bookmarks_Combo'], "type": list},
    "network_down_html": {"default": DEFAULT_NETWORK_DOWN,
                          "type": str, "is_file": True},
    "page_unavailable_html": {"default": DEFAULT_404, "type": str,
                              "is_file": True},
    "print_settings": {"default": {}, "type": dict},
    "privacy_mode": {"default": True, "type": bool},
    "proxy_server": {"default": None, "type": str,
                     "env": "http_proxy"},
    "quit_button_mode": {"default": "reset", "type": str,
                         "values": ["reset", "close"]},
    "quit_button_text": {"default": "I'm &Finished", "type": str},
    "screensaver_url": {"default": "about:blank", "type": str},
    "ssl_mode": {"default": "strict", "type": str,
                 "values": ["strict", "ignore"]},
    "start_url": {"default": "about:blank", "type": str},
    "stylesheet": {"default": None, "type": str},
    "suppress_alerts": {"default": False, "type": bool},
    "timeout": {"default": 0, "type": int},
    "timeout_mode": {"default": "reset", "type": str,
                     "values": ["reset", "close", "screensaver"]},
    "user_agent": {"default": None, "type": str},
    "user_css": {"default": None, "type": str},
    "whitelist": {"default": None},  # don't check type here
    "window_size": {"default": None},  # don't check type
    "zoom_factor": {"default": 1.0, "type": float},
    "Restrictions": {"default": {}, "type": dict},
    "rule_id": {"default": None, "type": str},
    "rule_name": {"default": None, "type": str},
    "access_id": {"default": 0, "type": int},
    "test_url": {"default": "https://google.com", "type": str}
}
# insertAccessActivity {"access_log_id":21,"activity":"window"}
config = {}
lTime = ['']
para = {"access_token": [''], "machine_type": "", "machine_name": "", "timezone": ""}
activity = {"access_log_id": 0, "activity": "", 'performed_on': ''}
my_timezone = tzlocal.get_localzone()
print(my_timezone)

now = datetime.datetime.now()
# print (now.strftime("%a, %Y-%m-%d %H:%M"))
performed_on = str(now.strftime("%a, %Y-%m-%d %H:%M"))

machine_type = platform.system()
machine_name = platform.node()
for k in para.keys():
    if k == 'access_token':
        para[k] = ['']
    elif k == 'machine_type':
        para[k] = machine_type
    elif k == 'machine_name':
        para[k] = machine_name
    elif k == "timezone":
        para[k] = str(my_timezone)


class NumOfAppOpen(QMessageBox):
    # listApp=['chrome','firefox','Skype', 'LyncMonitor']
    def __init__(self, parent=None):
        super(NumOfAppOpen, self).__init__(parent)
        pass

    def process_exists(self):
        return
        # listApp = ['firefox.exe', 'TeamViewer.exe']
        listApp = ['chrome.exe', 'firefox.exe', 'Skype.exe', 'TeamViewer.exe', 'LyncMonitor.exe']
        for proc in psutil.process_iter():
            # print (proc.name())
            if proc.name() in listApp:
                # pdb.set_trace()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setInformativeText("The Application will be closed forcefully")
                msg.setWindowTitle("ERROR!!!")
                msg.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # added by RSR
                # msg.setDetailedText("The details are as follows:")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setText("Looks like  application {} is Open".format(proc.name().upper()))
                msg.show()
                try:
                    proc.terminate()
                except:
                    pass
                # sys.exit(1)


class AccessCode(QDialog):
    # Temporary
    accessCode = []
    acCount = 0
    eL = []

    def closeEvent(self, *args, **kwargs):
        app.quit()
        sys.exit(3)

    def __init__(self, options, apprefer=None, window=None, parent=None):
        super(AccessCode, self).__init__(parent)
        self.app = apprefer
        self.window = window
        self.uiAc = Ui_Dialog()
        self.uiAc.setupUi(self)
        self.options = options
        self.setWindowTitle("ACCESS CODE")
        logger.debug("value of OPTIONS in init {}".format(options))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & QtCore.Qt.WindowCloseButtonHint)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # added by RSR
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.uiAc.pushButtonSubmit.clicked.connect(self.submitAcode)
        self.uiAc.lineEdit.textChanged.connect(self.getAccessCode)
        self.setModal(False)
        self.show()

    def keyPressEvent(self, event):
        if event.key() + 1 == Qt.Key_Enter:
            print("I came in submit ENTER")
            self.submitAcode()

    def moveEvent(self, event):
        return True
        position = self.app.desktop().screen().rect().center() - self.rect().center()
        event.ignore()
        self.move(position)
        print('i came in MoveEvent')
        return True

    def submitAcode(self):
        BASE_URL = "http://tachetechnologies.com/provApi/provConsole/api/v1/"
        VIEW_RULE_URL = BASE_URL + "viewrulebylog"
        INSERT_ACCESS_URL = BASE_URL + "insertAccessActivity"
        print("I came in submit access code")
        # pdb.set_trace()
        if AccessCode.accessCode == AccessCode.eL:
            msg = QMessageBox()
            msg.setWindowTitle("ACCESS CODE")
            msg.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  #
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Please Enter Access Code")
            msg.show()
        else:
            if AccessCode.acCount == 3:
                print("QUITING=========================================================")
            para["access_token"] = self.accessCode[0]
            print("para is {}".format(para))
            print("value of OPTIONS in submitAcode {}".format(self.options))
            try:
                response = requests.post(VIEW_RULE_URL, data=json.dumps(para))
            except Exception as e:
                print("Exception is e", e, "\n")
                pass
            print("this is the value of response {}\n".format(response))
            jsonData = response.json()
            if jsonData['status'] == 'success':
                # Set that the data has been retrieved successfully.
                print(jsonData)
                print(jsonData['Restrictions'])
                # sys.exit(1)
                print("========== printing bookmarks")
                print(jsonData['Restrictions']['BOOKMARKS'])
                print("this is response of our code finish\n")
                configfile = {}
                if self.options.config_file:
                    print("loading configuration from 22")
                    self.file = open(os.environ["APPDATA"] + '\\Provlog\\config_file.yaml', 'w')
                    self.file.seek(0, 2)
                    yaml.safe_dump(jsonData, self.file)
                    self.file.close()
                    self.file = open(os.environ["APPDATA"] + '\\Provlog\\config_file.yaml', 'r')
                    configfile = yaml.safe_load(self.file)
                    self.parse_config(configfile, self.options)
                    self.setModal(False)
                    self.hide()
                    self.accept()
                    self.file.close()
                    self.window.loadBookMarksAndBrowser()
                    self.window.onLoadFinished()

            elif jsonData['status'] == 'failed':
                print("value of Access Code is {}".format(AccessCode.accessCode))
                self.setModal(True)
                # app.quit()
                # return False

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("ACCESS CODE")
                msg.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
                msg.setStandardButtons(QMessageBox.Ok)
                # msg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                #     "font: 8pt \"Roboto\";\n"
                #     "border-width: 1px;\n"
                #     # "margin-left: 600px!important;\n"
                #     "\n"
                #     "position: absolute;\n"
                #     # "left: 100px;\n"
                #     "float: right!important; \n"
                #     "max-width: 300px!important;\n"
                #     "padding: 1px;\n"
                #     "height: 22px!important;\n"
                #     "border-color: rgb(170, 0, 0);\n"
                #     "color: #606060;")

                error_message = jsonData['msg']

                if AccessCode.acCount == 2:
                    debug("ACESS CODE COUNT\n\n")
                    debug(AccessCode.acCount)
                    error_message += (' ' + str(3))
                    self.app.quit()
                msg.setText(error_message)
                msg.show()

            # Increase the access count
            AccessCode.acCount += 1

    def getAccessCode(self, text):
        # StartHere
        if len(AccessCode.accessCode) == 0:
            pass
        else:
            AccessCode.accessCode.pop(0)
        AccessCode.accessCode.append(text)
        if AccessCode.accessCode == ['']:
            AccessCode.accessCode = []
        print("value of Access Code is {}".format(AccessCode.accessCode))

    def parse_config(self, file_config, options):
        options = vars(options)
        for key, metadata in CONFIG_OPTIONS.items():
            options_val = options.get(key)
            file_val = file_config.get(key)
            env_val = os.environ.get(metadata.get("env", ''))
            default_val = metadata.get("default")
            vals = metadata.get("values")
            debug("key: {}, default: {}, file: {}, options: {}".format(
                key, default_val, file_val, options_val
            ))
            if vals:
                options_val = (options_val in vals and options_val) or None
                file_val = (file_val in vals and file_val) or None
                env_val = (env_val in vals and env_val) or None
            if metadata.get("is_file"):
                filename = options_val or env_val
                if not filename:
                    config[key] = default_val
                else:
                    try:
                        with open(filename, 'r') as fh:
                            config[key] = fh.read()
                    except IOError:
                        debug("Could not open file {} for reading.".format(
                            filename)
                        )
                        config[key] = default_val
            else:
                set_values = [
                    val for val in (options_val, env_val, file_val)
                    if val is not None
                ]
                if len(set_values) > 0:
                    config[key] = set_values[0]
                else:
                    config[key] = default_val
            if metadata.get("type") and config[key]:
                debug("{} cast to {}".format(key, metadata.get("type")))
                config[key] = metadata.get("type")(config[key])
        debug(repr(config))
        print("value of Config Dict in Parse Config is: {}".format(config))


from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from PySide2 import QtCore


class MainWindow(QMainWindow):
    """This is the main application window class
    '''testFormMain.Ui_MainWindow'''
    it defines the GUI window for the browser
    """
    # myCloseSignal=Signal()
    # global config
    countEsc = 0
    screenShort = 0
    lineEditUrl = []

    def activityLog(self, keypUser):
        try:
            if config.get("access_id"):
                access_log_id = config.get("access_id")
                activity['access_log_id'] = access_log_id
                activity['activity'] = keypUser
                now = datetime.datetime.now()
                performed_on = str(now.strftime("%a, %Y-%m-%d %H:%M:%S"))
                activity['performed_on'] = performed_on
                resAct = requests.post("http://tachetechnologies.com/provApi/provConsole/api/v1/insertAccessActivity",
                                       data=json.dumps(activity))
                # resActjson=resAct.json()
                # print("activity data is {}".format(activity))
                # print("jasonData is escape {}".format(resActjson))
                # print("status is escape {}".format(resActjson['status']))
        except Exception as e:
            print("FROM ACTIVITY LOG ")
            print(e)

    def keyPressEvent(self, e):
        if int(e.modifiers()) == (Qt.ControlModifier + Qt.AltModifier):
            print("Ctrl+ Alt Key Before is pressed")
            e.ignore()
            print("Ctrl+ Alt Key is After pressed")
        return super(MainWindow, self).keyPressEvent(e)

    def moveEvent(self, event):
        self.activityLog('Try To Move MainWindow')
        event.ignore()
        self.move(0, 0)
        print('i came in MoveEvent')
        return True

    def mouseMoveEvent(self, event):
        print('mouseMoveEvent: x= {}, y= {}'.format(event.x(), event.y()))
        return True

    def closeEvent(self, event):
        try:
            self.activityLog('closeMainWindow')
        except:
            print("INTERNET NOT PRESENT")
        cmsg = QMessageBox()
        cmsg.setIcon(QMessageBox.Critical)

        """
        Show the question message
        """
        # cmsg.setStyleSheet("background-color: rgb(255, 255, 255);")
        # cmsg.setStyleSheet("background-color:#ffffff!important;")
        flags = cmsg.StandardButton.Yes
        flags |= cmsg.StandardButton.No
        question = "Do you really want to end test?"
        response = cmsg.question(self, "Confirmation", question, flags)

        if response == cmsg.Yes:
            self.activityLog('closeMainWindowYES')
            print("You've choosed Yes!!!")
            event.accept()
            app.quit()
            app.exit()
            sys.exit(78)
            return True
        elif cmsg.No:
            self.activityLog('closeMainWindowNo')
            print("You've choosed No!!!")
            event.ignore()
            return False
        else:
            cmsg.setStyleSheet("background-color:#ffffff")
            cmsg.show()
            print("You chose wisely!")

    def getRelativeFrameGeometry(self):
        print("i came getRelativeFrameGeometry here\n")
        g = self.geometry()
        fg = self.frameGeometry()
        # sleep(400)
        return fg.translated(-g.left(), -g.top())

    def mkDirForScreenCapture(self):
        self.dirName = os.environ["APPDATA"] + '\\Provlog\\MyScreenShot'
        if not os.path.exists(self.dirName):
            # os.makedirs(directory)
            os.mkdir(self.dirName)
        print("Path is created:{}".format(self.dirName))

    def screenCaptureWidget(self):
        return
        print("i came screenCaptureWidget here\n")
        rfg = self.getRelativeFrameGeometry()
        self.screenShort += 1
        # filename='.\\MyScreenShot\\'
        # Path to be created
        filename = ('.\\{}\\'.format(self.dirName))
        # os.mkdir( filename)
        print("Path is created")
        fileformat = 'png'
        op = 'MyScreenShot' + '_' + str(self.screenShort) + '.png'
        pixmap = QPixmap.grabWindow(self.winId(),
                                    rfg.left(), rfg.top(),
                                    rfg.width(), rfg.height())
        pixmap.save(filename + op, fileformat)

    def __init__(self, options, app=None, parent=None):
        """Construct a MainWindow Object."""
        super(MainWindow, self).__init__(parent)
        # Load config file
        self.app = app
        self.listApp = None
        # pdb.set_trace()
        print(" loading configuration from '{}'".format(options))
        '''
        loader = QtUiTools.QUiLoader()
        uifile = QtCore.QFile("testForm.ui")
        uifile.open(QtCore.QFile.ReadOnly)
        myWindowUi = loader.load(uifile)
        uifile.close()  
        '''
        self.options = options

        """INSTALL EVENT FILTER"""
        # self.installEventFilter(self)

        self.setWindowTitle("PROVLOCK")
        self.setMouseTracking(False)  # for mouse movement tracking

        self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)  # added by RSR
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinMaxButtonsHint)  # added by RSR
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint) #added by RSR

        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowCancelButtonHint)
        # self.showFullScreen()
        # pd.set_trace()
        # self.resize(300,300)

        app.aboutToQuit.connect(self.closeEvent)
        # app.quit().connect(self.closeEvent())
        # self.myCloseSignal.connect(self.closeEventFun())
        # app.connect(app,SIGNAL("aboutToQuit()"),self.closeEvent())
        # app.aboutToQuit.connect(self.closeEventFun())
        # self.connect(self,app,SIGNAL("app.aboutToQuit"),self,self.closeEventFun())

        self.build_ui(options)

    # ## END OF CONSTRUCTOR ###
    def line_edit_text_changed(self, text):
        return
        self.lineEditUrl.clear()
        self.lineEditUrl.append(text)
        print("value of lineEditUrl Code is {}".format(self.lineEditUrl))
        # if 'www.' in text:
        # eL = QEvent()
        if config != {}:
            print("reach in line_edit_text_changed is\n")
            # print("value of config is {}".format(config))
            listWht = config.get("Restrictions")
            print("Value of listWhite is: {}\n".format(listWht))
            # print("Value o# f website is: {}\n".format(listWht['website']))
            print("value of lineEditUrl Code is {}".format(self.lineEditUrl))
            # pdb.set_trace()
            # for value in listWht['website']:
            for txt in range(0, len(listWht['website'])):
                print("list of website: {}".format(listWht['website'][txt]['value']))
                if self.lineEditUrl[0] == listWht['website'][txt]['value']:
                    print("yes it is here")
                    self.load = 'http://' + self.lineEditUrl[0]
                    self.webSearch.load(QUrl(self.load))
                    print("yes it is loading")
                '''
                elif self.lineEditUrl[0] != listWht['website'][txt]['value']:
                    self.webSearch.load(QUrl.fromLocalFile(".\\examples\\custom404.html")) 
                    self.webSearch.setHtml(DEFAULT_404)
                '''
            ''' 
            if eL.key()+1 == Qt.Key_Enter:
                print("Hello  Enter is PRESSED in linedit")      
            '''

    def setLineEditText(self, index):
        text = self.uiMwin.bookMarkCombo.currentText()
        # item=self.config.get("Restrictions")
        # print("value of item is: {}".format(item))
        # text = item[index+1]["url"]
        # self.uiMwin.tabWidget.setTabText(1,"HELP")
        # self.uiMwin.tabWidget.setCurrentIndex(1)
        # self.uiMwin.lineEdit.setText(text)
        # self.webSearch = QWebView()
        # self.webSearch.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.urlSearch = text
        print("LOAD URL", text)
        self.webSearch.page().runJavaScript("window.location.href=" + '"' + text + '";')
        # self.webSearch.load(QUrl(text))
        self.uiMwin.tabWidget.setCurrentIndex(1)
        return False
        # self.webSearch.load(QUrl(self.urlSearch))
        # self.vBoxSearch  = QtGui.QVBoxLayout()
        # print("reach in urlSearch is: {}".format(self.urlSearch))
        # self.vBoxSearch.addWidget(self.lineEdit)
        # self.vBoxSearch.addWidget(self.webSearch)
        # self.search_option.setLayout(self.vBoxSearch)

    def OnKeyboardEvent(self, event):
        # print ('Key:{}'.format(event.Key))
        if event.Key.lower() in ['lwin', 'tab', 'lmenu']:
            return False  # block these keys
        else:
            # return True to pass the event to other handlers
            return True

    def process_exists(self):
        if self.listApp == None:
            self.listApp = []
            print("\n=====================OPTIONS PROCESS")
            print("\n", config)
            apps = config.get("Restrictions").items()[1][1]
            for a1 in apps:
                self.listApp.append(a1.get("value").lower())
            print("\n\n=========")
        print(self.listApp)
        # listApp = ['chrome.exe','firefox.exe','Skype.exe', 'TeamViewer.exe', 'LyncMonitor.exe']
        for proc in psutil.process_iter():
            if proc.name().lower() in self.listApp:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setInformativeText("The Application will be closed forcefully")
                msg.setWindowTitle("ERROR!!!")
                msg.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # added by RSR
                # msg.setDetailedText("The details are as follows:")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setText("Looks like  application {} is Open".format(proc.name().upper()))
                msg.show()
                msg.show()
                try:
                    proc.terminate()
                except:
                    pass
                # return True

    def check_external_storage(self):
        usb_command = "wmic path CIM_LogicalDevice where \"Description like 'USB%'\" get /value"
        pattern = "Availability="
        usb_proc = subprocess.Popen(usb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = usb_proc.communicate()
        new_devices = re.findall(pattern, str(stdout))
        if new_devices > DEVICES:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText("Kindly remove the external device")
            msg.setWindowTitle("ERROR!!!")
            msg.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # added by RSR
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("Looks like you have plugged in an external device")
            msg.show()
            msg.show()
            return True

    def check_inter(self, paasd):
        print(":::CHECKING PAASD", paasd, "\n\n")
        if paasd:
            return False
        for i in range(1):
            self.msg_net = QMessageBox()
            self.msg_net.setIcon(QMessageBox.Warning)
            self.msg_net.setInformativeText("No Internet")
            self.msg_net.setWindowTitle("ERROR!!!")
            self.msg_net.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # added by RSR
            # msg.setDetailedText("The details are as follows:")
            self.msg_net.setStandardButtons(QMessageBox.Ok)
            self.msg_net.setText("Ther is no internet conncection ")
            self.msg_net.show()
            print(e)

    def build_ui(self, options):
        """Set up the user interface for the main window.

        Unlike the constructor, this method is re-run
        whenever the browser is "reset" by the user.
        """
        debug("build_ui")
        # ui = self.loadUiWidget("testForm.ui")
        # ui.show()
        # pdb.set_trace()
        # self.setupUi(self)
        self.uiMwin = Ui_MainWindow()
        self.uiMwin.setupUi(self)
        # self.uiMwin.centralwidget.setMouseTracking(True)
        self.accessCode = AccessCode(options, app, self)  # calling Access Code Class
        # self.accessCode.setUpParameter()
        # self.setWindowFlags(self.WindowDeactivate) # very important remove x button of window
        # self.showFullScreen()
        # self.setFixedSize(self.size())
        # self.setSizeGripEnabled(False)
        self.resize(200, 300)

        """
        self.mkDirForScreenCapture()
        self.timer = QTimer()
        self.timer.start(10000)
        #t.timeout.connect(self.getRelativeFrameGeometry)
        self.timer.timeout.connect(self.screenCaptureWidget)
        #self.dragMoveEvent()
        self.apptimer = QTimer()
        self.apptimer.setInterval(20000)
        self.apptimer.timeout.connect(self.process_exists)
        self.apptimer.start()
        self.stimer1 = QTimer()
        self.stimer1.setInterval(4000)
        self.stimer1.timeout.connect(st,88)
        self.stimer1.start()

        self.stimer = QTimer()
        self.stimer.setInterval(5000)
        self.stimer.timeout.connect(self.check_external_storage)
        self.stimer.start()

"""
        # self.uiMwin.lineEdit.textChanged.connect(self.line_edit_text_changed)
        # self.uiMwin.Quit.clicked.connect(self.close)
        # self.accessCode.uiAc.pushButtonSubmit.clicked.connect(self.loadBookMarksAndBrowser)
        # self.accessCode.uiAc.pushButtonSubmit.clicked.connect(self.onLoadFinished)
        # self.uiAc.pushButtonSubmit.clicked.connect(self.callMainWindow)
        # self.accessCode.close()
        # self.tabWidget.clicked.connect(self.openTab)
        # myuiform.Ui_MainWindow.lineEdit.setText("hello  how r u?")

        '''
        self.bookMarkCobo.addItem("cat")
        self.bookMarkCobo.addItem("Bat")
        self.bookMarkCobo.addItem("sat")
        '''
        self.uiMwin.bookMarkCombo.currentIndexChanged.connect(self.setLineEditText)
        debug("loading configuration from '{}'".format(options.config_file))

        self.popup = None
        # pdb.set_trace()
        '''
        qb_mode_callbacks = {'close': self.close, 'reset': self.reset_browser}
        to_mode_callbacks = {'close': self.close,
                             'reset': self.reset_browser,
                             'screensaver': self.screensaver}
        self.screensaver_active = False
        '''
        print("===============================================WEBVIEW CONFIG")
        print(options, "options")
        # self.webTest = CusTomWebview(CONFIG_OPTIONS,self.uiMwin,False)
        self.webTest = NewWebView(CONFIG_OPTIONS, self.uiMwin, False)

        self.uiMwin.closebutton.clicked.connect(self.close)
        # self.webTest.loadFinished.connect(self.webTest.)
        # self.webTest.connect(self.webTest, SIGNAL('loadFinished(bool)'), self.loadFinished)
        # self.webTest.loadFinished.connect(self.loadFinished)
        # self.webTest.setHtml(DEFAULT_LOADING)

        # self.webSearch =  CusTomWebview(CONFIG_OPTIONS,self.uiMwin,True)
        # self.webSearch = QWebEngineView()

        self.webSearch = NewWebView(CONFIG_OPTIONS, self.uiMwin, True)

        # self.webSearch.load(QUrl(urlSearch))

        # self.webSearch.setHtml(DEFAULT_LOADING)

        self.vBoxTest = QtWidgets.QVBoxLayout()
        # self.fBoxSearch  = QtGui.QFormLayout()

        # vBoxlayout.addWidget(pushButton2)
        self.vBoxTest.addWidget(self.webTest)

        # self.fBoxSearch.addWidget(self.uiMwin.lineEdit)
        # self.fBoxSearch.addWidget(self.webSearch)
        self.uiMwin.tabWidget.setCurrentIndex(0)
        # self.fBoxSearch.addRow(self.uiMwin.lineEdit)

        #self.uiMwin.formLayout.addRow(self.webSearch)
        # self.fBoxSearch.addRow(self.webSearch)
        #self.uiMwin.search_option.setLayout(self.uiMwin.formLayout)
        self.uiMwin.test_console.setLayout(self.vBoxTest)

        self.vBoxSearch = QtWidgets.QVBoxLayout()
        self.vBoxSearch.addWidget(self.webSearch)
        self.uiMwin.search_option.setLayout(self.vBoxSearch)






        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # added by RSR
        self.activateWindow()
        # create a hook manager
        hm = pyHook.HookManager()
        print('hm is:{}'.format(hm))
        # watch for all keyboard events
        hm.KeyDown = self.OnKeyboardEvent
        # set the hook
        # print ("hm.KeyDown:{}".format(hm.KeyDown))
        hm.HookKeyboard()

        # self.uiMwin.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        # self.tab3  = QtGui.QWidget()
        # self.tabWidget.addTab(tab3,"Other's")
        # self.uiMwin.tabWidget.addTab(self.tab3, "Other's Console")
        # self.installEventFilter(self.webTest)
        # self.installEventFilter(self.webSearch)

        # ##END OF UI SETUP###

    def ip(self):
        print("STARTING.....")
        self.networkThread = NetworkThread(self)
        print("STARTING.....edfdgdf")

        def prif(**kwargs):
            print("NO INTERNET", kwargs, "\n\n")

        self.networkThread.connected.connect(prif)
        print("STARTING.....dsouhfisdf")
        self.networkThread.run()

    def hide2(self, a):
        print("\n====================HIDHIDEHIDEDE")
        self.uiMwin.backbutton.hide()
        self.uiMwin.fwbutton.hide()
        self.uiMwin.status_txt1.hide()

    def hide22(self, a):
        print("\n====================SHOWSHOW")
        self.uiMwin.backbutton.show()
        self.uiMwin.fwbutton.show()
        self.uiMwin.status_txt1.show()

    def loadBookMarksAndBrowser(self):
        # print("value of config Dict is {}".format(config))
        for value in config.get("Restrictions").items():
            # pdb.set_trace()
            if 'BOOKMARKS' in value:
                for txt in range(0, len(value[1])):
                    self.uiMwin.bookMarkCombo.addItem(value[1][txt]['value'])
                    self.default = value[1][txt]['value']
                break
                # self.uiMwin.bookMarkCombo.addItem(value[val][i])
        # self.webTest.loadFinished.connect(self.onLoadFinished)
        self.webSearch.load(value[1][0]['value'])
        # self.uiMwin.tabWidget.setCurrentIndex(1)

    def onLoadFinished(self):
        print("valuein loadFinished till page not load\n")
        if config.get("test_url"):
            urlTest = config.get("test_url")
            self.webTest.load(QUrl(urlTest))
            print("valuein loadFinished till page not load\n", urlTest)
        print("TEST URL IS NOW", urlTest)
        # urlTest="https://testconsole.provexam.com/#/pages/testconsole"
        # urlTest="http://tachetechnologies.com"
        print("loadFinished till page is loading\n")
        # self.setWindowFlags(self.windowFlags() | ~Qt.WindowStaysOnTopHint) #added by RSR
        # self.setWindowFlags(~Qt.WindowStaysOnTopHint)

    def screensaver(self):
        """Enter "screensaver" mode
        This method puts the browser in screensaver mode, where a URL
        is displayed while the browser is idle.  Activity causes the browser to
        return to the home screen.
        """
        debug("screensaver started")
        self.screensaver_active = True
        if self.popup:
            self.popup.close()
        if self.config.get("navigation"):
            self.navigation_bar.hide()
        self.test_console.setZoomFactor(self.config.get("zoom_factor"))
        self.test_console.load(QUrl(self.config.get("screensaver_url")))
        self.event_filter.timeout.disconnect()
        self.event_filter.activity.connect(self.reset_browser)

    def reset_browser(self):
        """Clear the history and reset the UI.

        Called whenever the inactivity filter times out,
        or when the user clicks the "finished" button in
        'reset' mode.
        """
        # Clear out the memory cache
        QWebEngineSettings.clearMemoryCaches()
        self.test_console.history().clear()
        # self.navigation_bar.clear() doesn't do its job,
        # so remove the toolbar first, then rebuild the UI.
        debug("RESET BROWSER")
        if self.event_filter:
            self.event_filter.blockSignals(True)
        if self.screensaver_active is True:
            self.screensaver_active = False
            self.event_filter.activity.disconnect()
        if self.event_filter:
            self.event_filter.blockSignals(False)
        if hasattr(self, "navigation_bar"):
            self.removeToolBar(self.navigation_bar)
        self.build_ui()

    def zoom_in(self):
        """Zoom in action callback.

        Note that we cap zooming in at a factor of 3x.
        """
        if self.test_console.zoomFactor() < 3.0:
            self.test_console.setZoomFactor(
                self.test_console.zoomFactor() + 0.1
            )
            self.nav_items["zoom_out"].setEnabled(True)
        else:
            self.nav_items["zoom_in"].setEnabled(False)

    def zoom_out(self):
        """Zoom out action callback.

        Note that we cap zooming out at 0.1x.
        """
        if self.test_console.zoomFactor() > 0.1:
            self.test_console.setZoomFactor(
                self.test_console.zoomFactor() - 0.1
            )
            self.nav_items["zoom_in"].setEnabled(True)
        else:
            self.nav_items["zoom_out"].setEnabled(False)

    def show_diagnostic(self):
        "Display a dialog box with some diagnostic info"
        QT_VERSION_STR = "5.2"
        data = {
            "OS": os.uname(),
            "USER": (os.environ.get("USER")
                     or os.environ.get("USERNAME")),
            "Python": sys.version,
            "Qt": QT_VERSION_STR,
            "Script Date": (
                datetime.datetime.fromtimestamp(
                    os.stat(__file__).st_mtime).isoformat()
            )
        }
        html = "\n".join([
            "<h1>System Information</h1>",
            "<h2>Please click &quot;",
            self.config.get("quit_button_text").replace("&", ''),
            "&quot; when you are finished.</h2>",
            "<ul>",
            "\n".join([
                "<li><b>{}</b>: {}</li>".format(k, v)
                for k, v in data.items()
            ]),
            "</ul>"
        ])
        self.test_console.setHtml(html)


# ## END Main Application Window Class def ## #


class InactivityFilter(QTimer):
    """This defines an inactivity filter.

    It's basically a timer that resets when user "activity"
    (Mouse/Keyboard events) are detected in the main application.
    """
    activity = Signal()

    def __init__(self, timeout=0, parent=None):
        """Constructor for the class.

        args:
          timeout -- number of seconds before timer times out (integer)
        """
        super(InactivityFilter, self).__init__(parent)
        # timeout needs to be converted from seconds to milliseconds
        self.timeout_time = timeout * 1000
        self.setInterval(self.timeout_time)
        self.start()

    def eventFilter(self, object, event):
        """Overridden from QTimer.eventFilter"""
        if event.type() in (
                QEvent.MouseMove, QEvent.MouseButtonPress,
                QEvent.HoverMove, QEvent.KeyPress,
                QEvent.KeyRelease
        ):
            self.activity.emit()
            print("\n\n================KEYBOARD EVENT IS IN TIMER===========")
            self.start(self.timeout_time)
            # commented this debug code,
            # because it spits out way to much information.
            # uncomment if you're having trouble with the timeout detecting
            # user inactivity correctly to determine what it's detecting
            # and ignoring:

            # debug ("Activity: %s type %d" % (event, event.type()))
            # else:
            # debug("Ignored event: %s type %d" % (event, event.type()))
        return QObject.eventFilter(self, object, event)


class WcgNetworkAccessManager(object):
    """Overridden so we can get debug info from responses"""

    def __init__(self):
        super(WcgNetworkAccessManager, self).__init__()
        # add event listener on "load finished" event
        self.finished.connect(self._finished)
        self.failed_urls = []

    def _finished(self, reply):
        headers = [
            (str(k), str(v))
            for k, v in reply.rawHeaderPairs()
        ]
        url = reply.url().toString()
        # getting status is bit of a pain
        status = reply.attribute(
            QNetworkRequest.HttpStatusCodeAttribute
        )
        # track the URLs that failed
        if status is None or status >= 400:
            self.failed_urls.append(url)
        debug(
            "Got {status} from {url}, headers: {headers}"
                .format(status=status, headers=headers, url=url)
        )

    def reset_failed_urls(self):
        self.failed_urls = []

    def createRequest(self, op, request, iodata):
        ops = ['HEAD', 'GET', 'PUT', 'POST', 'DELETE', 'CUSTOM']
        url = str(request.url())
        headers = [str(x) for x in request.rawHeaderList()]
        debug(
            "{op} request to {url}, headers: {headers}"
                .format(op=ops[op], url=url, headers=headers)
        )
        return super(WcgNetworkAccessManager, self).createRequest(op, request, iodata)


from PySide2.QtWebEngineWidgets import *
from PySide2.QtWebEngine import QtWebEngine


class CusTomWebview(QWebEngineView):
    """This is the webview for the application.

    It represents a browser window, either the main one or a popup.
    It's a simple wrapper around QWebView that configures some basic settings.
    """

    def bac(self, backbutton):
        print("=============================================BACK CLASSS")
        print(self.page().history())
        print(self.page().history().canGoBack())
        print(self.page().history().count())

        if self.page().history().canGoBack():
            print("CAN GO BACK AND GOIND")
            self.page().history().back()
        else:
            rMyIcon = QtGui.QPixmap("back_d.png");
            rMyIcon.setMaximumWidth = 50
            backbutton.setIcon((rMyIcon))
            backbutton.setIconSize(QtCore.QSize(20, 20))
            print("CANNOT GO BACK ")
        print("===============================================END")
        print("\n\n")

    def fww(self, fwbutton):
        print("=============================================FORWARD CLASSS")
        print(self.page().history())
        print(self.page().history().canGoForward())
        print(self.page().history().count())
        if self.page().history().canGoForward():
            print("CAN GO FORWARD AND GOIND")
            self.page().history().forward()
        else:
            rMyIcon = QtGui.QPixmap("forward_d.png");
            rMyIcon.setMaximumWidth = 50
            fwbutton.setIcon((rMyIcon))
            fwbutton.setIconSize(QtCore.QSize(20, 20))
            print("CANNOT GO FORWARD ")
        print("===============================================END")
        print("\n\n")

    def __init__(self, config, Ui, change, parent=None, **kwargs):
        """Constructor for the class"""
        super(CusTomWebview, self).__init__(parent)
        self.ui = Ui
        self.change = change
        self.kwargs = kwargs
        self.config = config
        self.loadProgress.connect(self.progress)
        self.nam = (kwargs.get('networkAccessManager')
                    or WcgNetworkAccessManager())
        self.setPage(WCGWebPage(config=config))
        self.page().setNetworkAccessManager(self.nam)
        self.settings().setAttribute(
            QWebEngineSettings.JavascriptCanOpenWindows,
            config.get("allow_popups").get("default")
        )
        print("========================================HERE")
        if config.get('user_css'):
            self.settings().setUserStyleSheetUrl(QUrl(config.get('user_css').get("default")))
        # JavascriptCanCloseWindows is in the API documentation,
        # but apparently only exists after 4.8
        QT_VERSION_STR = '5.2'
        if True or QT_VERSION_STR >= '4.8':
            self.settings().setAttribute(
                QWebEngineSettings.JavascriptCanCloseWindows,
                config.get("allow_popups").get("default")
            )
        self.settings().setAttribute(
            QWebEngineSettings.PrivateBrowsingEnabled,
            config.get("privacy_mode").get("default")
        )
        self.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.settings().setAttribute(
            QWebEngineSettings.PluginsEnabled,
            config.get("allow_plugins").get("default")
        )
        self.page().setForwardUnsupportedContent(
            config.get("allow_external_content").get("default")
        )
        self.setZoomFactor(config.get("zoom_factor").get("default"))

        # add printing to context menu if it's allowed
        if config.get("allow_printing").get("default"):
            self.print_action = QAction("Print", self)
            self.print_action.setIcon(QIcon.fromTheme("document-print"))
            self.print_action.triggered.connect(self.print_webpage)
            self.page().printRequested.connect(self.print_webpage)
            self.print_action.setToolTip("Print this web page")

        # Set up the proxy if there is one set
        if config.get("proxy_server").get("default"):
            if ":" in config["proxy_server"].default:
                proxyhost, proxyport = config["proxy_server"].default.split(":")
            else:
                proxyhost = config["proxy_server"]
                proxyport = 8080
            self.nam.setProxy(QNetworkProxy(
                QNetworkProxy.HttpProxy, proxyhost, int(proxyport)
            ))

        # connections for customwebview
        self.page().networkAccessManager().authenticationRequired.connect(
            self.auth_dialog
        )
        self.page().unsupportedContent.connect(self.handle_unsupported_content, type=Qt.QueuedConnection)
        self.page().downloadRequested.connect(self.download)
        self.page().networkAccessManager().sslErrors.connect(
            self.sslErrorHandler
        )
        self.urlChanged.connect(self.onLinkClick)

        def load_done():
            self.ui.status_txt1.hide()
            """ this is done to back and forward button images when webview has finished loading new url """
            if not self.change:
                return
            if self.page().history().canGoBack():
                rMyIcon = QtGui.QPixmap("back.png");
                self.ui.backbutton.setIcon(QtGui.QIcon(rMyIcon))
                self.ui.backbutton.setIconSize(QtCore.QSize(20, 20))
            else:
                rMyIcon = QtGui.QPixmap("back_d.png");
                self.ui.backbutton.setIcon(QtGui.QIcon(rMyIcon))
                self.ui.backbutton.setIconSize(QtCore.QSize(20, 20))
            if self.page().history().canGoForward():
                rMyIcon = QtGui.QPixmap("forward.png");
                self.ui.fwbutton.setIcon(QtGui.QIcon(rMyIcon))
                self.ui.fwbutton.setIconSize(QtCore.QSize(20, 20))
            else:
                rMyIcon = QtGui.QPixmap("forward_d.png");
                self.ui.fwbutton.setIcon(QtGui.QIcon(rMyIcon))
                self.ui.fwbutton.setIconSize(QtCore.QSize(20, 20))
            print("Load done")

        self.loadFinished.connect(load_done)

    def createWindow(self, type):
        """Handle requests for a new browser window.

        Method called whenever the browser requests a new window
        (e.g., <a target='_blank'> or window.open()).
        Overridden from QWebView to allow for popup windows, if enabled.
        """
        if self.config.get("allow_popups").get("default"):
            self.kwargs["networkAccessManager"] = self.nam
            self.popup = CusTomWebview(
                self.config,
                **self.kwargs
            )
            # This assumes the wi   ndow manager has an "X" icon
            # for closing the window somewhere to the right.
            self.popup.setObjectName("web_content")
            self.popup.setWindowTitle(
                "Click the 'X' to close this window! ---> "
            )
            self.popup.page().windowCloseRequested.connect(self.popup.close)
            self.popup.show()
            return self.popup
        else:
            debug("Popup not loaded on {}".format(self.url().toString()))

    def contextMenuEvent(self, event):
        """Handle requests for a context menu in the browser.

        Overridden from QWebView,
        to provide right-click functions according to user settings.
        """
        return False
        menu = QMenu(self)
        for action in [
            QWebEnginePage.Back, QWebEnginePage.Forward,
            QWebEnginePage.Reload, QWebEnginePage.Stop
        ]:
            action = self.pageAction(action)
            if action.isEnabled():
                menu.addAction(action)
        if self.config.get("allow_printing").get("default"):
            menu.addAction(self.print_action)
        menu.exec_(event.globalPos())

    def sslErrorHandler(self, reply, errorList):
        """Handle SSL errors in the browser.

        Overridden from QWebView.
        Called whenever the browser encounters an SSL error.
        Checks the ssl_mode and responds accordingly.
        """
        if self.config.get("ssl_mode").get("default") == 'ignore':
            reply.ignoreSslErrors()
            debug("SSL error ignored")
            debug(", ".join([str(error.errorString()) for error in errorList]))
        else:
            self.setHtml(
                CERTIFICATE_ERROR.format(
                    url=reply.url().toString(),
                    start_url=self.config.get("start_url").get("default")
                ))

    def auth_dialog(self, reply, authenticator):
        """Handle requests for HTTP authentication

        This is called when a page requests authentication.
        It might be nice to actually have a dialog here,
        but for now we just use the default credentials from the config file.
        """
        debug("Auth required on {}".format(reply.url().toString()))
        default_user = self.config.get("default_user").get("default")
        default_password = self.config.get("default_password").get("default")
        if (default_user):
            authenticator.setUser(default_user)
        if (default_password):
            authenticator.setPassword(default_password)

    def progress(self, a):
        if 1 < a < 99:
            self.ui.status_txt1.show()
        else:
            self.ui.status_txt1.hide()

    def download(self, request):
        """Handle a download request

        This is needed for certain types of download links
        """

        reply = self.nam.get(request)
        reply.finished.connect(partial(self.handle_unsupported_content, reply))

    def handle_unsupported_content(self, reply):
        """Handle requests to open non-web content

        Called basically when the reply from the request is not HTML
        or something else renderable by qwebview.  It checks the configured
        content-handlers for a matching MIME type, and opens the file or
        displays an error per the configuration.
        """
        self.reply = reply
        self.content_type = self.reply.header(
            QNetworkRequest.ContentTypeHeader
        )
        self.content_filename = re.match(
            '.*;\s*filename=(.*);',
            bytes(self.reply.rawHeader(b'Content-Disposition')).decode('UTF-8')
        )
        self.content_filename = QUrl.fromPercentEncoding(
            (
                self.content_filename.group(1).encode('UTF-8')
                if self.content_filename
                else b''
            )
        )
        content_url = self.reply.url()
        debug(
            "Loading url {} of type {}".format(
                content_url.toString(), self.content_type
            ))
        if not self.config.get("content_handlers").get(str(self.content_type)):
            self.setHtml(UNKNOWN_CONTENT_TYPE.format(
                mime_type=self.content_type,
                file_name=self.content_filename,
                url=content_url.toString()))
        else:
            if self.reply.isFinished:
                self.display_downloaded_content()
            else:
                self.reply.finished.connect(self.display_downloaded_content)
            if str(self.url().toString()) in ('', 'about:blank'):
                self.setHtml(DOWNLOADING_MESSAGE.format(
                    filename=self.content_filename,
                    mime_type=self.content_type,
                    url=content_url.toString()))
            else:
                # print(self.url())
                self.load(self.url())

    def display_downloaded_content(self):
        """Open downloaded non-html content in a separate application.

        Called when an unsupported content type is finished downloading.
        """
        debug("displaying downloaded content from {}".format(self.reply.url()))

        file_path = (
            QDir.toNativeSeparators(
                QDir.tempPath() + "/XXXXXX_" + self.content_filename
            )
        )
        myfile = QTemporaryFile(file_path)
        myfile.setAutoRemove(False)
        if myfile.open():
            myfile.write(self.reply.readAll())
            myfile.close()
            subprocess.Popen([
                (self.config.get("content_handlers")
                 .get(str(self.content_type)).get("default")),
                myfile.fileName()
            ])

            # Sometimes downloading files opens an empty window.
            # So if the current window has no URL, close it.
            if (str(self.url().toString()) in ('', 'about:blank')):
                self.close()

    def onLinkClick(self, url):
        """Handle clicked hyperlinks.

        Overridden from QWebView.
        Called whenever the browser navigates to a URL;
        handles the whitelisting logic and does some debug logging.
        """
        debug("Request URL: {}".format(url.toString()))
        if not url.isEmpty():
            # If whitelisting is enabled, and this isn't the start_url host,
            # check the url to see if the host's domain matches.
            if (
                    self.config.get("whitelist").get("default")
                    and not (url.host() ==
                             QUrl(self.config.get("start_url").get("default")).host())
                    and not str(url.toString()) == 'about:blank'
            ):
                site_ok = False
                pattern = re.compile(str("(^|.*\.)(" + "|".join(
                    [re.escape(w)
                     for w
                     in self.config.get("whitelist").get("default")]
                ) + ")$"))
                debug("Whitelist pattern: {}".format(pattern.pattern))
                if re.match(pattern, url.host()):
                    site_ok = True
                if not site_ok:
                    debug("Site violates whitelist: {}, {}".format(
                        url.host(), url.toString())
                    )
                    self.setHtml(self.config.get("page_unavailable_html").get("default")
                                 .format(**self.config))
            if not url.isValid():
                debug("Invalid URL {}".format(url.toString()))
            else:
                debug("Load URL {}".format(url.toString()))

    def onLoadFinished(self, ok):
        """Handle loadFinished events.

        Overridden from QWebView.
        This function is called when a page load finishes.
        We're checking to see if the load was successful;
        if it's not, we display either the 404 error (if
        it's just some random page), or a "network is down" message
        (if it's the start page that failed).
        """
        # "ok==false" doesn't always mean a complete failure
        # and we shouldn't automatically assume the entire page failed to load.

        # Check the WcgNetworkAccessManager's failed_urls to see if our requested
        # url failed to load.  If it's not in there, load anyway.
        print("==========DEBUG ON LOAD isFinished new new ")
        print(str(ok))
        if not ok:
            if self.url().toString() not in self.nam.failed_urls:
                ok = True
        if not ok:
            if (
                    self.url().host() == QUrl(self.config.get("start_url").get("default")).host()
                    and str(self.url().path()).rstrip("/") ==
                    str(QUrl(self.config.get("start_url").get("default")).path()).rstrip("/")
            ):
                self.setHtml(self.config.get("network_down_html").get("default")
                             .format(**self.config), QUrl())
                debug("Start Url doesn't seem to be available;"
                      " displaying error")
            else:
                debug("**PAGE LOAD FAILED, URL: {}".format(self.url().toString()))
                self.setHtml(
                    self.config.get("page_unavailable_html").get("default")
                        .format(**self.config), QUrl()
                )
        self.nam.reset_failed_urls()
        return True

    def print_webpage(self):
        """Print the webpage to a printer.

        Callback for the print action.
        Should show a print dialog and print the webpage to the printer.
        """
        print_settings = self.config.get("print_settings", {})

        if print_settings.get("mode") == "high":
            printer = QPrinter(mode=QPrinter.HighResolution)
        else:
            printer = QPrinter(mode=QPrinter.ScreenResolution)

        # set which printer
        # FIXME: This isn't documented, because it doesn't seem to work...
        if print_settings.get("printer_name"):
            debug(
                "Setting printer to: {}".format(
                    print_settings.get("printer_name"))
            )
            printer.setPrinterName(print_settings.get("printer_name"))
            debug("Printer is now: {}".format(printer.printerName()))

        # Set the units
        unit_name = print_settings.get("size_unit", 'Millimeter').title()
        try:
            unit = getattr(QPrinter, unit_name)
        except AttributeError:
            debug(
                "Specified print size unit '{}' not found, using default."
                    .format(unit_name)
            )
            unit = QPrinter.Millimeter

        # Set the margins
        margins = list(
            print_settings.get("margins", printer.getPageMargins(unit))
        )
        margins.append(unit)
        printer.setPageMargins(*margins)

        # Set the Orientation
        orientation = print_settings.get("orientation", 'Portrait').title()
        printer.setOrientation(
            getattr(QPrinter, orientation, QPrinter.Portrait)
        )

        # Set the paper size
        paper_size = print_settings.get("paper_size")
        if type(paper_size) in (list, tuple):
            # Assume it's a width/height spec
            printer.setPaperSize(QSizeF(*paper_size), unit)
        elif paper_size is not None:  # Assume it's a size name
            printer.setPaperSize(getattr(QPrinter, paper_size, 'AnsiA'))
        # If paper_size is None, we just leave it at the printer's default

        # Set the resolution
        resolution = print_settings.get("resolution")
        if resolution:
            printer.setResolution(int(resolution))

        # Show a print dialog, unless we want silent printing
        if not print_settings.get("silent"):
            print_dialog = QPrintDialog(printer, self)
            print_dialog.setWindowTitle("Print Page")
            if not print_dialog.show() == QDialog.Accepted:
                return False

        self.print_(printer)
        return True


# ### END CUSTOMWEBVIEW DEFINITION ### #

# ### WCGWEBPAGE #### #


class NewWebView(QWebEngineView):
    def __init__(self, config, Ui, change, parent=None, **kwargs):
        """Constructor for the class"""
        super(NewWebView, self).__init__(parent)
        self.config = config
        self.uiMwin = Ui
        self.change = change
        self.loadFinished.connect(self.donelo)

        if self.change:
            self.loadProgress.connect(self.Donefg)
            self.uiMwin.backbutton.clicked.connect(self.bacl)
            self.uiMwin.fwbutton.clicked.connect(self.fwcl)

    def fwcl(self):
        self.uiMwin.tabWidget.setCurrentIndex(1)
        self.forward()

    def bacl(self):
        self.uiMwin.tabWidget.setCurrentIndex(1)
        self.back()

    def donelo(self, ok, *args, **kwargs):
        print("OK,ok", ok, "\n\n", *args, **kwargs)
        if self.change:
            self.uiMwin.status_txt1.hide()
            if self.page().action(QWebEnginePage.Back).isEnabled():
                self.uiMwin.backbutton.setIcon(QtGui.QPixmap("back.png"))
            else:
                self.uiMwin.backbutton.setIcon(QtGui.QPixmap("back_d.png"))
            if self.page().action(QWebEnginePage.Forward).isEnabled():
                self.uiMwin.fwbutton.setIcon(QtGui.QPixmap("forward.png"))
            else:
                self.uiMwin.fwbutton.setIcon(QtGui.QPixmap("forward_d.png"))

    def Donefg(self, *args, **kwargs):
        movie = QtGui.QMovie("loading.gif")
        self.uiMwin.status_txt1.setMovie(movie)
        movie.start()
        self.uiMwin.status_txt1.show()

    def contextMenuEvent(self, *args, **kwargs):
        return False


class WCGWebPage(QWebEnginePage):
    """Subclassed QWebEnginePage representing the actual web page object in the browser.

    This was subclassed so that some functions can be overridden.
    """

    def pageAction(self, a):
        super.pageAction(a)

    def __init__(self, parent=None, config=None):
        """Constructor for the class"""
        super(WCGWebPage, self).__init__(parent)
        self.config = config or {}

    def javaScriptConsoleMessage(self, message, line, sourceid):
        """Handle console.log messages from javascript.

        Overridden from QWebEnginePage so that we can
        send javascript errors to debug.
        """
        debug('Javascript Error in "{}" line {}: {}'.format(
            sourceid, line, message)
        )

    def javaScriptConfirm(self, frame, msg):
        """Handle javascript confirm() dialogs.

        Overridden from QWebEnginePage so that we can (if configured)
        force yes/no on these dialogs.
        """
        if self.config.get("force_js_confirm").get("default") == "accept":
            return True
        elif self.config.get("force_js_confirm").get("default") == "deny":
            return False
        else:
            return QWebEnginePage.javaScriptConfirm(self, frame, msg)

    def javaScriptAlert(self, frame, msg):
        if not self.config.get("suppress_alerts").get("default"):
            return QWebEnginePage.javaScriptAlert(self, frame, msg)

    def userAgentForUrl(self, url):
        """Handle reqests for the browser's user agent

        Overridden from QWebEnginePage so we can force a user agent from the config.
        """
        return (
                self.config.get("user_agent").get("default")
                or QWebEnginePage.userAgentForUrl(self, url)
        )


# ### END WCGWEBPAGE DEFINITION ### #


class NewNM(PySide2.QtNetwork.QNetworkAccessManager):

    def __init__(self):
        super(NewNM, self).__init__()
        # add event listener on "load finished" event
        self.finished.connect(self._finished)

    def _finished(self, reply):
        status = reply.attribute(
            PySide2.QtNetwork.QNetworkRequest.HttpStatusCodeAttribute
        )
        # track the URLs that failed
        print("STATUS IS :::", status, "\n\n")


class checkIThread(QtCore.QThread):
    done = PySide2.QtCore.Signal(bool)

    def __init__(self):
        print("MAKINGsss")
        QtCore.QThread.__init__(self)

    def run(self):
        try:
            print("WORLING")
            a = socket.create_connection(("google.com", 80))
            self.emit(True)
        except Exception as e:
            print("No Internet")
            print(e)
            self.emit(False)


class NetworkThread(QtCore.QThread):
    connected = QtCore.Signal(bool)

    def run(self, *args, **kwargs):
        print("RUNNING")
        try:
            a = socket.create_connection(("google.com", 80))
        except Exception as e:
            self.emit(bytes())
            print("No Internet")
            print(e)


# ######## Main application code begins here ################## #


if __name__ == "__main__":
    # Create the qapplication object,
    # so it can interpret the qt-specific CLI args
    rVal = False
    app = QApplication(sys.argv)

    NumOfAppOpen = NumOfAppOpen()
    NumOfAppOpen.process_exists()
    usb_command = "wmic path CIM_LogicalDevice where \"Description like 'USB%'\" get /value"
    pattern = "Availability="
    npattern = "USB Mass Storage Device"
    usb_proc = subprocess.Popen(usb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = usb_proc.communicate()

    if re.search(npattern, str(stdout)):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setInformativeText("Kindly remove the external device")
        msg.setWindowTitle("ERROR!!!")
        # msg.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint) #added by RSR
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText("Looks like you have plugged in an external device")
        msg.show()

    DEVICES = re.findall(pattern, str(stdout))
    # NumOfAppOpen.resize(500,500)
    # NumOfAppOpen.show()
    # sys.exit(NumOfAppOpen.show())
    # pdb.set_trace()
    curDir = os.getcwd()
    print(curDir)

    fp = open(os.environ["APPDATA"] + '\\Provlog\\testForm_prov1', 'w')
    fp.write("python testForm.py -c config_file.yaml")
    fp.close()
    if os.path.isfile(os.path.expanduser(os.environ["APPDATA"] + '\\Provlog\\testForm_prov1')):
        default_config_file = os.path.expanduser(os.environ["APPDATA"] + '\\Provlog\\config_file.yaml')
        print(",_hello 11")
        print(default_config_file)
    elif os.path.isfile("/etc/wcgbrowser.yaml"):
        print("hello 12")
        default_config_file = "/etc/wcgbrowser.yaml"
    else:
        default_config_file = None
        print("hello 13")

    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--url", action="store", dest="start_url",
        help="Start browser at URL"
    )
    # Start URL
    parser.add_argument(
        "-f", "--fullscreen", action="store_true", default=argparse.SUPPRESS,
        dest="fullscreen", help="Start browser FullScreen"
    )
    # Full Screen
    parser.add_argument(
        "-n", "--no-navigation", action="store_false", default=argparse.SUPPRESS,
        dest="navigation", help="Start browser without Navigation controls"
    )
    # No Navigation
    parser.add_argument(
        "-c", "--config-file", action="store", default=default_config_file,
        dest="config_file", help="Specifiy an alternate config file"
    )
    # Config file
    parser.add_argument(
        "-d", "--debug", action="store_true", default=False, dest="DEBUG",
        help="Enable debugging output to stdout"
    )
    # Debug
    parser.add_argument(
        "--debug_log", action="store", default=None, dest="debug_log",
        help="Enable debug output to the specified filename"
    )
    # Debug Log
    parser.add_argument(
        "-t", "--timeout", action="store", type=int, default=argparse.SUPPRESS,
        dest="timeout",
        help="Define the timeout in seconds after which to reset the browser"
             "due to user inactivity"
    )
    # Timeout
    parser.add_argument(
        "-i", "--icon-theme", action="store", default=None, dest="icon_theme",
        help="override default icon theme with other Qt/KDE icon theme"
    )
    # icon theme
    parser.add_argument(
        "-z", "--zoom", action="store", type=float, default=argparse.SUPPRESS,
        dest="zoomfactor", help="Set the zoom factor for web pages"
    )
    # Default zoom factor
    parser.add_argument(
        "-p", "--popups", action="store_true", default=argparse.SUPPRESS,
        dest="allow_popups", help="Allow the browser to open new windows"
    )
    # Allow popups
    parser.add_argument(
        "-u", "--user", action="store", dest="default_user",
        help="Set the default username used for URLs"
             " that require authentication"
    )
    # Default HTTP user
    parser.add_argument(
        "-w", "--password", action="store", dest="default_password",
        help="Set the default password used for URLs"
             " that require authentication"
    )
    # Default HTTP password
    parser.add_argument(
        "-e", "--allow_external", action="store_true", default=argparse.SUPPRESS,
        dest='allow_external_content',
        help="Allow the browser to open content in external programs."
    )
    # Allow launching of external programs
    parser.add_argument(
        "-g", "--allow_plugins", action="store_true", default=argparse.SUPPRESS,
        dest='allow_plugins',
        help="Allow the browser to use plugins like"
             " Flash or Java (if installed)"
    )
    # Allow browser plugins
    parser.add_argument(
        "--size", action="store", dest="window_size", default=None,
        help="Specify the default window size in pixels (widthxheight),"
             " or 'max' to maximize"
    )
    # Window size
    parser.add_argument(
        "--proxy_server", action="store", dest="proxy_server", default=None,
        help="Specify a proxy server string, in the form host:port"
    )

    print(app.arguments())
    appArg = app.arguments()
    argss = ([str(x) for x in list(app.arguments())][1:])
    print("printing args 1\n")
    print(argss)
    args = parser.parse_args([str(x) for x in list(app.arguments())][2:])
    print("printing args 2\n")
    print(args)
    DEBUG = args.DEBUG
    print("hello 15.1")
    DEBUG_LOG = args.debug_log
    print("hello 16")
    if not args.config_file:
        print("hello 16999")
        print(args.config_file)
        debug("No config file found or specified; using defaults.")

    # run the actual application
    # pdb.set_trace()
    # accessCode=AccessCode(args)

    mainwin = MainWindow(args, app)  # args is input parameter here
    # myWidget = MyWidget()
    mainwin.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    mainwin.setWindowTitle("PROVLOCK")
    app.installEventFilter(mainwin)
    # mainwin.showFullScreen()
    # mainwin.setSizePolicy()
    mainwin.setMouseTracking(True)
    mainwin.resize(300, 300)
    mainwin.show()

    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    print("hello 17")
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print("hello 18")
        print(e)
