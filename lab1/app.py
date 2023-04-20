#!/usr/bin/python3
import sys

from flask import Flask
from flask import request, render_template

import redis
import json
import datetime

APP_PORT = 8000
REDIS_PORT = sys.argv[1]

rdb = redis.Redis(host="localhost", port=REDIS_PORT)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():

    today = datetime.date.today().strftime("%Y-%m-%d")

    return render_template("login.html", date=today, error="")


@app.route('/login', methods=['GET'])
def login_show():

    today = datetime.date.today().strftime("%Y-%m-%d")

    return render_template("login.html", date=today, error="")


@app.route('/create', methods=['GET'])
def create_show():

    today = datetime.date.today().strftime("%Y-%m-%d")

    return render_template("create.html", date=today, error="")


@app.route('/login', methods=['POST'])
def login():

    today = datetime.date.today().strftime("%Y-%m-%d")
    
    name = request.form.get("user")
    password = request.form.get("password")

    key = "user:" + name

    try:
        jsdata = json.loads( rdb.get(key).decode() )
    except:
        return render_template("login.html", data=today, error="Error")
    
    if not jsdata["password"] == password:
        return render_template("login.html", data=today, error="Invalid credentials")

    return render_template("update.html", user=name, password=password)


@app.route('/create', methods=['POST'])
def create():

    name = request.form.get("user")
    password = request.form.get("password")

    today = datetime.date.today().strftime("%Y-%m-%d")
    td = datetime.date.today().toordinal()

    rkey = "user:" + name

    user_exists = False
    try:
        jsdata = json.loads( rdb.get(rkey).decode() )
        user_exists = True
    except:
        pass

    if user_exists:
        return render_template("create.html", data=today, error="Name is already used.")

    jsdata = {"name":   name,
            "password": password,
            "date":     td,
            }

    jsdump = json.dumps(jsdata)
    rdb.set(rkey, jsdump)

    return render_template("login.html", date=today, error="Created")


@app.route('/update', methods=['POST'])
def update():

    name = request.form.get("user")
    password = request.form.get("password")

    td = datetime.date.today().toordinal()

    jsdata = {"name":   name,
            "password": password,
            "date":     td,
            }

    jsdump = json.dumps(jsdata)

    rkey = "user:" + name
    rdb.set(rkey, jsdump)

    return render_template("update.html", user=name, password=password)


@app.route('/list', methods=['GET'])
def list():

    users = []
    for key in rdb.scan_iter("user:*"):
        jsdata = json.loads( rdb.get(key).decode() )
        users.append(jsdata["name"])

    return render_template("list.html", users=users)


@app.route('/delete', methods=['POST'])
def delete():

    name = request.form.get("user")
    
    rkey = "user:" + name
    rdb.delete(rkey)

    users = []
    for key in rdb.scan_iter("user:*"):
        jsdata = json.loads( rdb.get(key).decode() )
        users.append(jsdata["name"])

    return render_template("list.html", users=users)


if __name__ == "__main__":
    app.run(debug = False, host = "0.0.0.0", port = APP_PORT)
