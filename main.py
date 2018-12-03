import sys
from PyQt5 import QtCore, QtGui, uic, QtWebEngineWidgets
from PyQt5.QtWidgets import *
from mapWidget import MapWidget
from GUIhelper import GUIhelper
import os,time

form_class = uic.loadUiType("ui_asset\\smartTransit.ui")[0]



# Catch Error and display through MessageBox
def catch_exceptions(t, val, tb):
    if t == RuntimeError:
        print("Thread failed")
        return
    QMessageBox.critical(None, "An exception was raised", "Exception type: {}".format(t))
    old_hook(t, val, tb)


old_hook = sys.excepthook
sys.excepthook = catch_exceptions


class Communicate(QtCore.QObject):
    updateBW = QtCore.pyqtSignal(int)



class SmartTransitGUI(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.mapWidget = MapWidget(self.mapWidget)
        self.pushButton_start_search.clicked.connect(self.displayRoute)

        # Setup guihelper and move to another thread
        self.guiHelper = GUIhelper()
        self.helperThread = QtCore.QThread()
        self.guiHelper.findPlaceLoaded.connect(self.onPlaceLoaded)
        self.guiHelper.moveToThread(self.helperThread)
        self.helperThread.start()


    def initUI(self):
        pass

    def displayRoute(self):
        self.mapWidget.showRoute()
        print(self.lineEdit_start.text())
        self.guiHelper.findPlace(self.lineEdit_start.text())

    def onPlaceLoaded(self,args):
        print("onPlaceLoaded " + str(args))
        self.lineEdit_start.setText(args["candidates"][0]["name"])


def launch():
    app = QApplication(sys.argv)
    w = SmartTransitGUI()
    w.setWindowTitle('SmartTransit')

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
    app.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)

    print("Launch GUI")
    w.show()
    app.exec_()


launch()