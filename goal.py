#!/usr/bin/python3

import cgi, cgitb
import os
import json
import MySQLdb
import passwords

form = cgi.FieldStorage()

conn = MySQLdb.connect(host = passwords.SQL_HOST, user = passwords.SQL_USER, passwd = passwords.SQL_PASSWD, db = "goal")
cursor = conn.cursor()


def index():
    print("Content-type: text/plain")
    print("Status: 200 OK")
    print()
    print("This is the index.")
    print("I have so many goals want to accomplish.")

def travelGoal():
    print("Content-type: text/plain")
    print("Status: 200 OK")
    print()
    print("Switherland vacation - 3 weeks + living on mountains")

def redirectTravel():
    print("Status: 302 Redirect")
    print("Location: travelGoal")
    print()

def jsonExample():
   print("Status: 200 OK")
   print("Content-type: application/json")
   print()
   x = [1,2,30,20, {"foo": "bar"}]
   x_json = json.dumps(x, indent=2)
   print(x_json)

def simpleGoal():
   cursor.execute("SELECT * FROM simple_goal;")
   results = cursor.fetchall()
   cursor.close()

   print("Status: 200 OK")
   print("Content-type: application/json")
   print()
   results_json = json.dumps(results, indent=2)
   print(results_json)

def simpleGoalIndividual(id):
   intID = int(id)
   cursor.execute("SELECT * FROM simple_goal WHERE id=%s", (id))
   result = cursor.fetchall()
   cursor.close()

   print("Status: 200 OK")
   print("Content-type: application/json")
   print()
   result_json = json.dumps(result, indent=2)
   print(result_json)




if "PATH_INFO" in os.environ:
    pathinfo = os.environ["PATH_INFO"]
else:
    pathinfo = "/"

if pathinfo == "/":
    index()
elif pathinfo == "/travelGoal":
    travelGoal()
elif pathinfo == "/redirectTravel":
    redirectTravel()
elif pathinfo == "/JSONExample":
    jsonExample()
elif "/simple_goal" in pathinfo:
    if pathinfo == "/simple_goal":
       simpleGoal()
    else:
       simpleGoalIndividual(str(pathinfo[13:]))


conn.commit()
conn.close()
