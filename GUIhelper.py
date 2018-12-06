from PyQt5 import QtCore,QtNetwork
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json, constants
from geopy.distance import geodesic

import time

class GUIhelper(QtCore.QObject):
    findPlaceLoaded = QtCore.pyqtSignal(dict,int)
    stations_list = None
    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.pyqtSlot()
    def findPlace(self,name,reqid=0):

        api_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'  # Set destination URL
        post_fields = {'input': name,
                       "inputtype":"textquery",
                       "fields":"formatted_address,name,geometry",
                       "locationbias":"circle:2000@13.750955,100.5435993",
                       "key":constants.API_KEY}  # Set POST fields

        url = api_url +"?"+ urlencode(post_fields)



        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))

        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(lambda reply, id=reqid: self.handleResponse(reply,id))
        self.nam.get(req)


    def handleResponse(self, reply,id):
        er = reply.error()

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


    def findNearestStation(self, lat,lng):
        print(str(lat) + " " + str(lng))
        minDist  = 9999999999
        minStation = None
        coords_1 = (lat,lng)
        try:

            for station in self.stations_list:
                length = geodesic(coords_1,(station.lat,station.lng))
                if length < minDist:
                    minDist = length
                    minStation = station
        except Exception as e:
            print(e)

        print("Closest station :" + minStation.name +" Dist :" + str(minDist))
        return (minStation,minDist)
