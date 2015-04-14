#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ ='Grupo_02'

''' 
# --- MODULES --------------------------------
'''
from flask import Flask, render_template

from flask_googlemaps import GoogleMaps

from flask import request

from flask_googlemaps import Map

import json

import twitter

import io

import utilidades_varias

''' 
-------------------------------------------
# --- MAIN --------------------------------
-------------------------------------------
'''
N_TWITS = 1000 #Contador de twits. Se almacenan hasta 1000 twits.
app = Flask(__name__)
GoogleMaps(app)

def search(tema):

    l_coord = []

    twitter_api = utilidades_varias.login_twitter() 
    results = twitter_api.search.tweets(q = tema, count = N_TWITS, geocode='40.25,-3.45,10000km')
    utilidades_varias.save_json("twits",results) 

    with open('twits.json') as data_file: 
	    data = json.load(data_file)

    for estado in data["statuses"]: 
    	if estado["geo"]:
    		coord = estado["coordinates"]
    		xy=[coord.values()[1][1] , coord.values()[1][0]]
    		l_coord.append(xy) 

    return l_coord

@app.route("/map", methods=['POST'])
def mapview():
    tema = request.form['text']
    coord = search(tema)
    mymap = Map(
        identifier="view-side",
		lat = 40.3450396,
		lng = -3.6517684,
        zoom=6,
		markers = coord,
		style="height:800px;width:800px;margin:0;"
	)
    return render_template('map.html', mymap=mymap) 

@app.route("/")
def index():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(debug=True)


