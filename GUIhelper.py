from PyQt5 import QtCore,QtNetwork
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json, constants
from geopy.distance import geodesic
from pyswip import Prolog
from caluculate_price import *

import time

class GUIhelper(QtCore.QObject):
    findPlaceLoaded = QtCore.pyqtSignal(dict,int)           #Pyqt Signal that returns place query data
    onErrorOccur = QtCore.pyqtSignal(str)
    nam = QtNetwork.QNetworkAccessManager()

    onLoad = False

    stations_list = None
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.prolog = Prolog()
        self.prolog.consult("train_path.pl")


    #Find place using Google API
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
        # return [start_sta,"bts_sukhumvit_phaya_thai", "arl_phaya_thai", "arl_ratchaprarop","arl_makkasan","mrt_blue_phetchaburi",dest_sta]

        result = list(self.prolog.query("astar( "+ start_sta+", "+ dest_sta +", X,Y,Z)"))[0]
        cost = result['Y']
        resultList = []
        for r in result['Z']:
            resultList.append(str(r))

        print(resultList)


        # return [start_sta,"bts_sukhumvit_phaya_thai", "arl_phaya_thai", "arl_ratchaprarop","arl_makkasan","mrt_blue_phetchaburi",dest_sta]
        return  (cost,resultList)

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


    def calculate_price(self,stations_route):
        price = 0
        prices = []
        lines = []
        lastLineName = None
        startIndex = 0
        endIndex = 0

        lastItemNum = len(stations_route) - 1

        for i, station in enumerate(stations_route):
            stationName = station.name
            thisLinePrice = 0

            if "tao_poon" in stationName:
                stationName = "mrt_tao_poon"
            elif "siam" in stationName:
                stationName = "bts_siam"

            if i == lastItemNum:
                if lastLineName == "bts":
                    thisLinePrice = bts_prices[startIndex][endIndex]
                elif lastLineName == "mrt":
                    thisLinePrice = mrt_prices[startIndex][endIndex]
                elif lastLineName == "arl":
                    thisLinePrice = arl_prices[count]
                lines.append(lastLineName)
                prices.append(thisLinePrice)
                price += thisLinePrice

            elif station.getType() != lastLineName:
                if lastLineName != None:

                    if lastLineName == "bts":
                        thisLinePrice = bts_prices[startIndex][endIndex]
                    elif lastLineName == "mrt":
                        thisLinePrice = mrt_prices[startIndex][endIndex]
                    elif lastLineName == "arl":
                        thisLinePrice = arl_prices[count]
                    lines.append(lastLineName)
                    prices.append(thisLinePrice)
                    price += thisLinePrice

                lastLineName = station.getType()
                if lastLineName == "bts":
                    startIndex = bts_stations.index(stationName)
                    endIndex = startIndex
                elif lastLineName == "mrt":
                    startIndex = mrt_stations.index(stationName)
                    endIndex = startIndex

                count = 0

            else:
                if lastLineName == "bts":
                    endIndex = bts_stations.index(stationName)
                elif lastLineName == "mrt":
                    endIndex = mrt_stations.index(stationName)

                count += 1

        print("Sum price: " + str(price))
        print("Price list: ", prices)
        print("Line list: ", lines)

        return price