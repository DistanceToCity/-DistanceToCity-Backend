
import sys
sys.path.append(".")
from Abstractions.file import FileAdditions
from math import sin, cos, sqrt, atan2, radians
import json
class Interface: 
    def __init__(self):
        self.CSV = FileAdditions("./geo.csv")
    def set_geo(self, title, geo):
        return self.CSV.append(title, geo)
    def get_list_geo(self):
        return json.dumps(self.CSV.read())
    def get_geo_by_title(self, titlePlace):
        for title, geo in self.CSV.read():
            if(title == titlePlace):
                return [float(geo[0]), float(geo[1])]
    def delete_geo_by_title(self, title):
       return self.CSV.delete(title)
    def get_distance(self, my_geo, my_geo_second):
        
        R = 6373.0
        lat1 = radians(my_geo[0])
        lon1 = radians(my_geo[1])
        lat2 = radians(my_geo_second[0])
        lon2 = radians(my_geo_second[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance


