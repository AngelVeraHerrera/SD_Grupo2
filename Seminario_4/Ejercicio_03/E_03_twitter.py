#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ ='Grupo_02'

''' 
# --- MODULES --------------------------------
'''
from flask import Flask, render_template

from flask_googlemaps import GoogleMaps

from flask_googlemaps import Map

import utilidades_varias

def menu():
    option = 0
    utilidades_varias.clear() # Clear the terminal
    print '***************************************'
    print '**     "BÚSQUEDA DE TWITS" v2        **'
    print '**       by A. Vera & A.Pastor       **'
    print '***************************************'
    print '* Introduzca un tema para buscar:     *'
    print '***************************************'
    tema = raw_input('Tema -> ')
    utilidades_varias.clear()
    return tema

''' 
-------------------------------------------
# --- MAIN --------------------------------
-------------------------------------------
'''
N_TWITS = 1000 #Contador de twits. Se almacenan hasta 1000 twits.

tema = menu()
l_coord = []
app = Flask(__name__)
GoogleMaps(app)
    
twitter_api = utilidades_varias.login_twitter() 
results = twitter_api.search.tweets(q = tema, count = N_TWITS, geocode='36.516667,-6.283333,1000km')
utilidades_varias.save_json("twits",results) 

with open('twits.json') as data_file: 
	data = json.load(data_file)


for estado in data["statuses"]: 
	if estado["geo"]:
		coord = estado["coordinates"]
		xy=[coord.values()[1][1] , coord.values()[1][0]]
		l_coord.append(xy) 

@app.route("/map")
def mapview():
	mymap = Map( 
		identifier="view-side",
		lat = 36.516667,
		lng = -6.283333,
		markers = lista,
		style="height:800px;width:800px;margin:0;"
	)
	return render_template('map.html', mymap=mymap) 

if __name__ == "__main__":
    app.run(debug=True)


