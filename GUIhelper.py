from PyQt5 import QtCore,QtNetwork
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json, constants
from geopy.distance import geodesic
from pyswip import prolog

import time

class GUIhelper(QtCore.QObject):
    findPlaceLoaded = QtCore.pyqtSignal(dict,int)
    onErrorOccur = QtCore.pyqtSignal(str)
    nam = QtNetwork.QNetworkAccessManager()

    onLoad = False

    stations_list = None
    def __init__(self):
        QtCore.QObject.__init__(self)


    @QtCore.pyqtSlot()
    def findPlace(self,name,reqid=0):
        print("findPlace "+ name)

        if self.onLoad:
            return
        self.onLoad = True
        api_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'  # Set destination URL
        post_fields = {'input': name,
                       "inputtype":"textquery",
                       "fields":"formatted_address,name,geometry",
                       "locationbias":"circle:2000@13.750955,100.5435993",
                       "key":constants.API_KEY}  # Set POST fields

        url = api_url +"?"+ urlencode(post_fields)



        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))

        self.nam.finished.connect(lambda reply, id=reqid: self.handleResponse(reply,id))
        self.nam.get(req)


    def handleResponse(self, reply,id):
        er = reply.error()
        self.nam.finished.disconnect()
        self.onLoad = False
        if er == QtNetwork.QNetworkReply.NoError:
            bytes_string = reply.readAll()
            json_data =  json.loads(str(bytes_string, 'utf-8'))
            # print(json_data)
            self.findPlaceLoaded.emit(json_data,id)

            # try:
            #     self.findNearestStation(json_data["candidates"][0]["geometry"]["location"]["lat"],json_data["candidates"][0]["geometry"]["location"]["lng"])
            # except Exception as e:
            #     print("Error in findNearestStation " + str(e))
        else:

            print("Error occured: ", er)
            print(reply.errorString())
            self.onErrorOccur.emit(reply.errorString()+"\nPlease check your internet connection")

    def findNearestStation(self, lat,lng):
        print(str(lat) + " " + str(lng))
        minDist  = 9999999999
        minStation = None
        coords_1 = (lat,lng)
        try:

            for station in self.stations_list:
                length = geodesic(coords_1,(station.lat,station.lng)).km
                if length < minDist:
                    minDist = length
                    minStation = station
        except Exception as e:
            print(e)

        print("Closest station :" + minStation.name +" Dist :" + str(minDist))
        return (minStation.name,minDist)

    def findMinTimeRoute(self,start_sta, dest_sta):
        return [start_sta,"bts_sukhumvit_phaya_thai", "arl_phaya_thai", "arl_ratchaprarop","arl_makkasan","mrt_blue_phetchaburi",dest_sta]

    def getObject(self,station_list_str):
        stations = []
        for station_name in station_list_str:
            for station in self.stations_list:
                if station.name == station_name:
                    stations.append(station)

        if len(stations) != len(station_list_str):
            print(stations)
            raise Exception("Error convert list of string to Station object")
        return  stations

    # def findPath(self, start_name, dest_name):
    #
    #     return list[]