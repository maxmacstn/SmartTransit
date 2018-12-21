from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from station import Station



class MapWidget(QWidget):
    def __init__(self, parent):
        super(MapWidget, self).__init__(parent)
        self.image = None

        self.resize(1300, 800)

        self.hilightStationList = []

        label = QLabel(self)
        label.resize(1300, 800)
        self.pixmap = QPixmap('ui_asset/train_map_1300x800.jpg')
        self.pixmap = self.pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        #Animation
        self.runningStation = 0
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.animateRoute)
        timer.start(500)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.hilightStation(painter)
        painter.end()

    def hilightStation(self, painter):
        stroke = 2
        radius = 13


        for station in self.hilightStationList:
            painter.setPen(QtGui.QPen(QtCore.Qt.black, stroke, QtCore.Qt.SolidLine))
            painter.setBrush(QtGui.QBrush(QtCore.Qt.green, QtCore.Qt.SolidPattern))

            if self.hilightStationList.index(station) == self.runningStation % len(self.hilightStationList):
                painter.setPen(QtGui.QPen(QtCore.Qt.black, stroke, QtCore.Qt.SolidLine))
                painter.setBrush(QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern))
                painter.drawEllipse(station.x - radius / 2, station.y - radius / 2, radius, radius)

            painter.drawEllipse(station.x - radius/2, station.y - radius/2, radius, radius)

    def showRoute(self,stations):
        self.runningStation = 0
        self.hilightStationList = stations
        self.update()

    def animateRoute(self):
        self.runningStation += 1
        self.update()

    def clearRoute(self):
        self.runningStation = 0
        self.hilightStationList = []
        self.update()

