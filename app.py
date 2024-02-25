from flask import Flask, jsonify, render_template, request, session, redirect
import requests
import webbrowser
import time
import json
import numpy as np
import pandas as pd
import VATSIMchecker_new
import math
import time
import os
from math import radians, cos, sin, asin, sqrt

global value
global g_dep_arr_tag

#http://127.0.0.1:4444/

app = Flask(__name__, static_url_path='')

def get_price(p_dep_arr_tag,airportcode):
    global g_dep_arr_tag
    global value

    value = value + 1
    
    if p_dep_arr_tag == ' ':
       p_dep_arr_tag = 'D'
       
    #print("dep_arr_tag: " +  p_dep_arr_tag)  

    # convert into JSON:
    data_json = VATSIMchecker_new.process_me(p_dep_arr_tag,airportcode)    

    #print(data_json[0])
    return(data_json)
    
@app.route('/Airport/<ad_airportcode>')
def stuff(ad_airportcode):
    ad_airportcode = ad_airportcode.upper()
    #print(ad_airportcode[0:1])
    #print(ad_airportcode[1:10])
    price=get_price(ad_airportcode[0:1],ad_airportcode[1:10])
    
    price = json.loads(price)
    #print(price)
    #for items in price: #["data"]:
     #   print(items["age"])
        
    return jsonify(result=price)

#@app.route('/')
#def root():
#    return app.send_static_file('airport1.html')

@app.route('/')
def index():
    return render_template('airport1.html')
#main driver function

value = 0
if __name__ == '__main__':

	app.run(debug=True, host='localhost', port=4444)
