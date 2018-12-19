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
    start_place_name = None
    start_place_to_sta_dist = 0
    dest_sta = None
    dest_place_name = None
    dest_place_to_dest_dist = 0
    arl_icon = QtGui.QIcon()
    bts_icon = QtGui.QIcon()
    circle_icon = QtGui.QIcon()
    mrt_icon = QtGui.QIcon()
    pin_icon = QtGui.QIcon()
    taxi_icon = QtGui.QIcon()
    walk_icon = QtGui.QIcon()

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
        self.guiHelper.onErrorOccur.connect(self.displayQueryError)
        self.guiHelper.moveToThread(self.helperThread)
        self.helperThread.start()

        self.label_start_sta.hide()
        self.label_dest_sta.hide()
        self.pushButton_clear.clicked.connect(self.clearQuery)

        self.treeWidget.hide()
        self.setFixedSize(self.sizeHint())

        self.arl_icon.addPixmap(QtGui.QPixmap('ui_asset/arl.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bts_icon.addPixmap(QtGui.QPixmap('ui_asset/bts.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.circle_icon.addPixmap(QtGui.QPixmap('ui_asset/circle.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mrt_icon.addPixmap(QtGui.QPixmap('ui_asset/mrt.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pin_icon.addPixmap(QtGui.QPixmap('ui_asset/pin.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.taxi_icon.addPixmap(QtGui.QPixmap('ui_asset/taxi.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.walk_icon.addPixmap(QtGui.QPixmap('ui_asset/walk.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        movie = QtGui.QMovie("ui_asset/loading_io.gif")
        self.label_loading.setMovie(movie)
        movie.setScaledSize(QtCore.QSize(30, 30))
        movie.start()
        self.label_loading.hide()

        self.label_logo.resize(300, 113)
        self.pixmap_logo = QtGui.QPixmap('ui_asset/logo_300.png')
        self.pixmap_logo = self.pixmap_logo.scaled(self.label_logo.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_logo.setPixmap(self.pixmap_logo)


        # self.label_loading.layout().addWidget(QLabel('Loading...'))


    def initUI(self):
        pass

    def displayRoute(self):
        if (not self.lineEdit_start.text() or not  self.lineEdit_dest.text()):
            self.displayQueryError("Please input in both field")
            return
        self.label_loading.show()
        self.guiHelper.findPlace(self.lineEdit_start.text(),1)


    def onPlaceLoaded(self,args,id):
        print("onPlaceLoaded " + str(args))


        try:
            if id == 1:
                nearestStation = self.guiHelper.findNearestStation(args["candidates"][0]["geometry"]["location"]["lat"],args["candidates"][0]["geometry"]["location"]["lng"])
                self.start_sta = nearestStation[0]
                self.start_place_to_sta_dist = nearestStation[1]
                self.start_place_name = args["candidates"][0]['name']
                self.label_start_sta.setText(self.start_sta)
                self.guiHelper.findPlace(self.lineEdit_dest.text(), 2)
            elif id == 2:
                nearestStation = self.guiHelper.findNearestStation(args["candidates"][0]["geometry"]["location"]["lat"],args["candidates"][0]["geometry"]["location"]["lng"])
                self.dest_sta = nearestStation[0]
                self.dest_place_to_dest_dist = nearestStation[1]
                self.dest_place_name = args["candidates"][0]['name']
                self.label_dest_sta.setText(self.dest_sta)
                if self.start_sta is not None:
                    self.showResult()
                    self.label_loading.hide()


        except Exception as e:
            self.label_loading.hide()

            print("Error in on place loaded "+ str(e))

            if id == 1:
                self.label_start_sta.setText("Error: Place not found")
                self.start_sta = None
            elif id == 2:
                self.label_dest_sta.setText("Error: Place not found")

    def getStationList(self):
        stations = []
        with open(gui_station_data, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                stations.append(Station(row[0], row[1], float(row[2]),float(row[3]),int(row[4]),int(row[5])))
        # for station in stations:
        #     print(station.lng)

        return stations

    def showResult(self):
        if (self.start_place_to_sta_dist > 30 or self.dest_place_to_dest_dist > 30):
            self.displayQueryError("Error: Input place is too far from stations")
            return




        print(self.guiHelper.findMinTimeRoute(self.start_sta, self.dest_sta))
        stations_route = self.guiHelper.getObject(self.guiHelper.findMinTimeRoute(self.start_sta, self.dest_sta))
        # stations_route = self.stations_list


        #Display output in navigation bar
        self.label_start_sta.show()
        self.label_dest_sta.show()

        self.label_start_sta.setText("Found nearest station : " + stations_route[0].getFullName())
        self.label_dest_sta.setText("Found nearest station: "+  stations_route[len(stations_route) -1].getFullName())

        #Display route in map
        self.mapWidget.showRoute(stations_route)


        steps = []

        start_place = QTreeWidgetItem(["[Start] "+ self.start_place_name])
        start_place.setIcon(0,self.pin_icon)
        steps.append(start_place)


        if self.start_place_to_sta_dist > 0.05:

            if self.start_place_to_sta_dist < 1:
                commuteDist = QTreeWidgetItem(["Walk  "+ str(int(self.start_place_to_sta_dist*1000)) + " m"])
                commuteDist.setIcon(0,self.walk_icon)
            else:
                commuteDist = QTreeWidgetItem(["Taxi {0:.2f} km".format(self.start_place_to_sta_dist)])
                commuteDist.setIcon(0,self.taxi_icon)
            steps.append(commuteDist)



        lastLineName = None
        for station in stations_route:
            if station.getLineName() != lastLineName:
                trainLine = QTreeWidgetItem([station.getLineName()])
                if "BTS" in station.getLineName():
                    trainLine.setIcon(0,self.bts_icon)
                if "Airport Link" in station.getLineName():
                    trainLine.setIcon(0,self.arl_icon)
                if "MRT" in station.getLineName():
                    print(station.getLineName())
                    trainLine.setIcon(0,self.mrt_icon)

                lastLineName = station.getLineName()
                steps.append(trainLine)
                item = QTreeWidgetItem([station.common_name])
                item.setIcon(0, self.circle_icon)
                trainLine.addChild(item)
            else:
                item = QTreeWidgetItem([station.common_name])
                item.setIcon(0, self.circle_icon)
                steps[len(steps)-1].addChild(item)

        if self.dest_place_to_dest_dist > 0.05:
            if self.dest_place_to_dest_dist < 1:
                commuteDist = QTreeWidgetItem(["Walk  "+ str(int(self.dest_place_to_dest_dist*1000)) + " m"])
                commuteDist.setIcon(0,self.walk_icon)

            else:
                commuteDist = QTreeWidgetItem(["Taxi {0:.2f} km".format(self.dest_place_to_dest_dist)])
                commuteDist.setIcon(0,self.taxi_icon)

            steps.append(commuteDist)

        start_place = QTreeWidgetItem(["[Destination] " + self.dest_place_name])
        start_place.setIcon(0, self.pin_icon)
        steps.append(start_place)

        w = QWidget()
        w.resize(510, 210)

        self.treeWidget.clear()
        self.treeWidget.resize(500, 200)
        # self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(["Steps"])
        for step in steps:
            self.treeWidget.addTopLevelItem(step)
        self.treeWidget.expandAll()
        self.treeWidget.show()
        self.treeWidget.setRootIsDecorated(False)
        self.setFixedSize(self.sizeHint())

    def displayQueryError(self,error_message):
        em = QErrorMessage(self)
        em.showMessage(error_message)
        self.label_loading.hide()


    def clearQuery(self):
        self.label_start_sta.hide()
        self.label_dest_sta.hide()
        self.treeWidget.clear()
        self.treeWidget.hide()
        self.lineEdit_dest.clear()
        self.lineEdit_start.clear()
        self.mapWidget.clearRoute()

        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(lambda : self.setFixedSize(self.sizeHint()))
        self.my_qtimer.start(200)






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