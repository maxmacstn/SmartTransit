from PyQt5 import QtCore,QtNetwork
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json, constants

import time

class GUIhelper(QtCore.QObject):
    findPlaceLoaded = QtCore.pyqtSignal(dict)

    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.pyqtSlot()
    def findPlace(self,name):

        api_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'  # Set destination URL
        post_fields = {'input': name,
                       "inputtype":"textquery",
                       "fields":"formatted_address,name,geometry",
                       "locationbias":"circle:2000@13.750955,100.5435993",
                       "key":constants.API_KEY}  # Set POST fields

        url = api_url +"?"+ urlencode(post_fields)



        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))

        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)

    def handleResponse(self, reply):

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:
            bytes_string = reply.readAll()
            json_data =  json.loads(str(bytes_string, 'utf-8'))
            print(json_data)
            self.findPlaceLoaded.emit(json_data)

        else:
            print("Error occured: ", er)
            print(reply.errorString())

