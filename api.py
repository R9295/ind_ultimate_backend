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

# Team code generator
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

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
  count = db.users.find({"email":request.json['email']}).count()

  if count == 0:
    response = {}      
    response["response"] = "failure"
    response = json.dumps(response)
    return response
  
  if count == 1:
    count = db.users.find_one({"email":request.json['email']})
    user = db.users.find({"email":request.json['email'],"password":hashpw(request.json['password'].encode('utf-8'),count['password'].encode('utf-8')) }).count()
    print request.json['password']
    if user == 1:
      response = {}      
      response["response"] = "success"
      response = json.dumps(response)
      return response  
    else:
      response = {}      
      response["response"] = "failure"
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
    try:
      db.users.insert_one(user)
      response = {}      
      response["response"] = "success"
      response = json.dumps(response)
      return response
    except:
      response = {}      
      response["response"] = "failure"
      response = json.dumps(response)
      return response
        

    response = {}      
    response["response"] = "success"
    response = json.dumps(response)
    return response


#create team
@app.route("/createteam", methods=['POST'])
def create_team():
  team = {
  "name": request.json['name'],
  "join_code": "%s"%(id_generator()),
  "captain": "need_to_add",
  "members": ["need_to_add"],
  "city":request.json['city'],
  "contact":request.json['contact']
  }
  try:
    db.teams.insert_one(team)
    response = {}      
    response["response"] = "success"
    response = json.dumps(response)
    return response
  except:
    response = {}      
    response["response"] = "failure"
    response = json.dumps(response)
    return response

#get teams(For now with all teams not just of the user)
@app.route("/getteam", methods=['GET'])
def get_team():
  teams = db.teams.find()
  return dumps(teams)
if __name__ == "__main__":
    app.debug = True
    app.run()
