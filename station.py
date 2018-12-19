class Station():
    def __init__(self, name, common_name,lat,lng, x = 0, y = 0):
        self.name = name                    # prolog name ex. mrt_blue_...
        self.common_name = common_name      # ex. Phaya Thai
        self.lat = lat
        self.lng = lng
        self.x = x
        self.y = y

    def getType(self):
        return self.name.split("_")[0]

    def getFullName(self):
        out = ""

        train_type =  self.name.split("_")[0]
        if train_type == "bts":
            train_type += self.name.split("_")[1]
            out += "BTS " + self.common_name +  " [" + self.name.split("_")[1] + " line]"

        if train_type == "mrt":
            train_type += self.name.split("_")[1]
            out += "MRT " + self.common_name +  " [" + self.name.split("_")[1] + " line]"


        if train_type == "arl":
            out += "Airport Link " + self.common_name

        return out

    def getLineName(self):
        out = ""
        train_type = self.name.split("_")[0]
        if train_type == "bts":
            train_type += self.name.split("_")[1]
            out += "BTS " + self.name.split("_")[1] + " line"

        if train_type == "mrt":
            train_type += self.name.split("_")[1]
            out += "MRT "  + self.name.split("_")[1] + " line"

        if train_type == "arl":
            out += "Airport Link"

        return out


    def __str__(self):
        return "Station object: "+ self.name

    def __repr__(self):
        return "Station object: "+ self.name

    def __unicode__(self):
        return "Station object: "+ self.name
