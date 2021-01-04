from flask import Flask, request
from flask_restful import Api, Resource, reqparse
#flask is used for setting up the api
app = Flask(__name__)
api = Api(app)
#This code is used to read the payload of the post in storing the radio profiles
radio_put_args = reqparse.RequestParser()
radio_put_args.add_argument("alias", type=str)
radio_put_args.add_argument("allowed_locations", type=str,action ="append")
#This code is used to read the payload of the post in the retrival of radio's location
location_put_args = reqparse.RequestParser()
location_put_args.add_argument("location", type=str)
#The information will be stored in 2 dictionary one contains allias and list of allowed locations and the other one contains the current location
radios = {}
locations = {}
#Storage of radio profiles
class Radios(Resource):
    def post(self, id):
        args = radio_put_args.parse_args()
        radios[id] = args
        #Creating location for the radio and assigning the defaut value to it. (undefined)
        locations[id] = {"location": "undefined"}
         return None
#Setting and retrieving locations
class Location(Resource):
    def get(self, id):
        if locations[id]=={"location": "undefined"}:
            return None,"404 NOT FOUND"
        else:
            return locations[id],"200 OK"

    def post(self, id):
        args = location_put_args.parse_args()
        if args["location"] in radios[id]["allowed_locations"]:
            locations[id] = args
            return None,"200 OK"
        else:
            return None,"403 FORBIDDEN"
#the api for posting the radios
api.add_resource(Radios, "/radios/<int:id>")
#the api for posting and getting location
api.add_resource(Location, "/radios/<int:id>/location")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
