import sys
from PyQt5 import QtCore, QtGui, uic, QtWebEngineWidgets
from PyQt5.QtWidgets import *
from mapWidget import MapWidget

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
        self.pushButton_go.clicked.connect(self.displayRoute)


    def initUI(self):
        pass

    def displayRoute(self):
        self.mapWidget.showRoute()


def launch():
    app = QApplication(sys.argv)
    w = SmartTransitGUI()
    w.setWindowTitle('SmartTransit')
    print("Launch GUI")
    w.show()
    app.exec_()


launch()