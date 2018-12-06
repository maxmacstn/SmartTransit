import sys
from PyQt5 import QtCore, QtGui, uic, QtWebEngineWidgets
from PyQt5.QtWidgets import *
from mapWidget import MapWidget
from GUIhelper import GUIhelper
import csv
import os,time
from station import Station

form_class = uic.loadUiType("ui_asset/smartTransit.ui")[0]
gui_station_data = "ui_asset/gui_station_data.csv"


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
    stations_list = []
    start_sta = None
    dest_sta = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.mapWidget = MapWidget(self.mapWidget)
        self.pushButton_search.clicked.connect(self.displayRoute)
        self.stations_list =  self.getStationList()


        # Setup guihelper and move to another thread
        self.guiHelper = GUIhelper()
        self.guiHelper.stations_list = self.stations_list
        self.helperThread = QtCore.QThread()
        self.guiHelper.findPlaceLoaded.connect(self.onPlaceLoaded)
        self.guiHelper.moveToThread(self.helperThread)
        self.helperThread.start()


    def initUI(self):
        pass

    def displayRoute(self):
        self.mapWidget.showRoute()
        print(self.lineEdit_start.text())

        self.guiHelper.findPlace(self.lineEdit_start.text(),1)


    def onPlaceLoaded(self,args,id):
        print("onPlaceLoaded " + str(args))
        try:
            if id == 1:
                self.start_sta = self.guiHelper.findNearestStation(args["candidates"][0]["geometry"]["location"]["lat"],args["candidates"][0]["geometry"]["location"]["lng"])[0]
                self.label_start_sta.setText(self.start_sta.name)
                self.guiHelper.findPlace(self.lineEdit_dest.text(), 2)
            if id == 2:
                self.dest_sta = self.guiHelper.findNearestStation(args["candidates"][0]["geometry"]["location"]["lat"],args["candidates"][0]["geometry"]["location"]["lng"])[0]
                self.label_dest_sta.setText(self.dest_sta.name)


        except Exception:
            if id == 1:
                self.label_start_sta.setText("Error")
            elif id == 2:
                self.label_dest_sta.setText("Error")
    def getStationList(self):
        stations = []
        with open(gui_station_data, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                stations.append(Station(row[0], row[1], row[2],row[3]))
        # for station in stations:
        #     print(station.lng)

        return stations

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