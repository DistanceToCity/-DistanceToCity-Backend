import sys
sys.path.append(".")
from Implementations.interface import Interface
from flask import Flask
from flask import jsonify
from flask import request
import json
from Implementations.interface import Interface
app = Flask(__name__)

class Backend(Interface):
    def distance(self, geo, tile_place):
       return { "value": self.geo_a(geo, tile_place), "prefiks" : "km"} 
    def distance(self, geo_a, geo_b):
       return { "value": self.get_distance(geo_a, geo_b), "prefiks" : "km"} 
    def set_place(self):
       return 1
    def list_places(self):
        res = {}
        for item in json.loads(self.get_list_geo()):
            city = item[0]
            coordinates = ",".join(item[1]).strip()  # Join coordinates and remove trailing newline
            res[city] = coordinates
        return res 
    def delete_place(self):
        return 1


    


Data = Backend()
@app.route('/list_places')
def list_places():
    return jsonify(Data.list_places())
@app.route('/distance')
def distance():
    client_geo =  request.args.get('client_geo').split(",")
    geo = [float(client_geo[0]), float(client_geo[1])]
    title_geo = request.args.get('title_geo')
    response = jsonify(Data.distance(geo, Data.get_geo_by_title(title_geo)))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/distanceFromTwoPoints')
def distanceFromTwoPoints():
    client_geo_a_point =  request.args.get('client_geo_a_point').split(",")
    client_geo_b_point =  request.args.get('client_geo_b_point').split(",")
    geo_a = [float(client_geo_a_point[0]), float(client_geo_a_point[1])]
    geo_b = [float(client_geo_b_point[0]), float(client_geo_b_point[1])]
    title_geo = request.args.get('title_geo')
    response = jsonify(Data.distance(geo_a, geo_b))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/delete_place')
def delete_place():
    return 'delete_place'
app.run()