from flask import Flask, jsonify, request
import json
import datetime
import geocoder
from pymongo import MongoClient
from bcrypt import hashpw, gensalt
import string
import random
from bson.json_util import dumps



app= Flask(__name__)

client = MongoClient()
db = client.ind_ultimate

@app.route("/get", methods=['GET'])
def get():
    #usr = db.users.find_one()
    return "k"

    #input = db.users.find({'email':request.json['email'], 'password':hashpw(request.json['password'].encode('utf-8').gensalt())}).count()
#    if input == 0:
    #    return 'didnt_work'
#    elif input == 1:
#        return 'worked'
#    else:
#        return 'didnt_work'

#login
@app.route('/login', methods=['POST'])
def login():
  response = {}      
  response["response"] = "success"
  response = json.dumps(response)
  return response

#create user
@app.route("/createuser", methods=['POST'])
def create_user():
    #Need validation(Email)
    user={
      'first_name': request.json['first_name'],
      'last_name': request.json['last_name'],
      'phone_number':request.json['phone_number'],
      'password': hashpw(request.json['password'].encode('utf-8'),gensalt()),
      'email': request.json['email'],
      'city': request.json['city'],
            }

    response = {}      
    response["response"] = "success"
    response = json.dumps(response)
    return response
   # try:
      #  db.users.insert_one(user)
       # return 'worked'
  #  except:
      #  return 'didnt_work'



if __name__ == "__main__":
    app.debug = True
    app.run()
