#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


import requests
import math
import time
from datetime import datetime
import os
import pandas as pd
import json
from math import radians, cos, sin, asin, sqrt

global Radius, df, df_sorted
global previous_speeds
global previous_speeds_ind
global process_stats
global process_stats_prv
global myjson
global flight_img_lookup

flight_img_lookup = {
"CLX":"CLX.jpg",
"UKV":"UKV.jpg",
"GTI":"GTI.jpg",
"FDX":"FDX.jpg",
"NOZ":"NOZ.jpg",
"LDM":"LDM.jpg",
"WAT":"WAT.jpg",
"WZZ":"WZZ.jpg",
"WMT":"WMT.jpg",
"WJA":"WJA.jpg",
"VTI":"VTI.jpg",
"VOZ":"VOZ.jpg",
"VOI":"VOI.jpg",
"VLG":"VLG.jpg",
"VIV":"VIV.jpg",
"VIR":"VIR.jpg",
"UGD":"UGD.jpg",
"UAL":"UAL.jpg",
"TZP":"TZP.jpg",
"TVJ":"TVJ.jpg",
"TUA":"TUA.jpg",
"TRA":"TRA.jpg",
"TLM":"TLM.jpg",
"THY":"THY.jpg",
"TAR":"TAR.jpg",
"PLM":"PLM.jpg",
"HVN":"HVN.jpg",
"GCR":"GCR.jpg",
"CXA":"CXA.jpg",
"TVS":"TVS.jpg",
"TOM":"TUI.png",
"THA":"THA.jpg",
"TGW":"TGW.jpg",
"TAP":"TAP.jpg",
"SXS":"SXS.jpg",
"SWR":"SWR.jpg",
"SWG":"SWG.jpg",
"SWA":"SWA.jpg",
"SLM":"SLM.jpg",
"SKU":"SKU.jpg",
"SJX":"SJX.jpg",
"SIA":"SIA.jpg",
"SEJ":"SEJ.jpg",
"SDM":"SDM.jpg",
"SCX":"SCX.jpg",
"SBI":"SBI.jpg",
"SAS":"SAS.jpg",
"SAA":"SAA.jpg",
"RYR":"RYR.jpg",
"RJA":"RJA.jpg",
"RBA":"RBA.jpg",
"RAM":"RAM.jpg",
"QTR":"QTR.jpg",
"QFA":"QFA.jpg",
"PGT":"PGT.jpg",
"OMS":"OMS.jpg",
"NKS":"NKS.jpg",
"DTA":"DTA.jpg",
"DLH":"DLH.jpg",
"CSZ":"CSZ.jpg",
"CQH":"CQH.jpg",
"APJ":"APJ.jpg",
"ALK":"ALK.jpg",
"SHT":"BAW.jpg",
"RVF":"RVF.jpg",
"PIA":"PIA.jpg",
"PAL":"PAL.jpg",
"OMA":"OMA.jpg",
"NRL":"NRL.jpg",
"NOS":"NOS.jpg",
"NOK":"NOK.jpg",
"NIA":"NIA.jpg",
"NGR":"NGR.jpg",
"MEA":"MEA.jpg",
"MAY":"MAY.jpg",
"MAS":"MAS.jpg",
"LVL":"LVL.jpg",
"LOT":"LOT.jpg",
"LNI":"LNI.jpg",
"LGL":"LGL.jpg",
"LAN":"LAN.jpg",
"KQA":"KQA.jpg",
"KOS":"KOS.jpg",
"KAR":"KAR.jpg",
"KAL":"KAL.jpg",
"FPY":"FPY.jpg",
"GFA":"GFA.jpg",
"GIA":"GIA.jpg",
"HAL":"HAL.jpg",
"GLO":"GLO.jpg",
"KNE":"KNE.jpg",
"KLM":"KLM.jpg",
"JZR":"JZR.jpg",
"JSX":"JSX.jpg",
"JST":"JST.jpg",
"JJA":"JJA.jpg",
"JBU":"JBU.jpg",
"JAL":"JAL.jpg",
"ITY":"ITY.jpg",
"IRA":"IRA.jpg",
"IGO":"IGO.jpg",
"ICE":"ICE.jpg",
"IBS":"IBS.jpg",
"IBJ":"IBJ.jpg",
"IBE":"IBE.jpg",
"IAW":"IAW.jpg",
"HYI":"HYI.jpg",
"HKE":"HKE.jpg",
"FMX":"FMX.jpg",
"FIN":"FIN.jpg",
"FFT":"FFT.jpg",
"FEG":"FEG.jpg",
"FDB":"FDB.jpg",
"FBU":"FBU.jpg",
"FBK":"FBK.jpg",
"FAD":"FAD.jpg",
"EXS":"EXS.jpg",
"CHH":"CHH.jpg",
"AWQ":"AWQ.jpg",
"UEA":"UEA.jpg",
"UAE":"UAE.jpg",
"RYS":"RYS.jpg",
"MSR":"MSR.jpg",
"MMZ":"MMZ.jpg",
"MPE":"MPE.jpg",
"KME":"KME.jpg",
"KAP":"KAP.jpg",
"FJI":"FJI.jpg",
"EZY":"EZY.jpg",
"EWG":"EWG.jpg",
"EVA":"EVA.jpg",
"ETH":"ETH.jpg",
"ETD":"ETD.jpg",
"ELY":"ELY.jpg",
"EJU":"EJU.jpg",
"EDW":"EDW.jpg",
"DAL":"DAL.jpg",
"CYP":"CYP.jpg",
"CUB":"CUB.jpg",
"CUA":"CUA.jpg",
"CTV":"CTV.jpg",
"CTN":"CTN.jpg",
"CSN":"CSN.jpg",
"CRL":"CRL.jpg",
"CRC":"CRC.jpg",
"CQN":"CQN.jpg",
"CPA":"CPA.jpg",
"CMP":"CMP.jpg",
"CFG":"CFG.jpg",
"CES":"CES.jpg",
"CEB":"CEB.jpg",
"CAL":"CAL.jpg",
"CAY":"CAY.jpg",
"BWA":"BWA.jpg",
"BRQ":"BRQ.jpg",
"BEL":"BEL.jpg",
"VXP":"VXP.jpg",
"RZO":"RZO.jpg",
"ROI":"ROI.jpg",
"NGT":"NGT.jpg",
"MXY":"MXY.jpg",
"LLR":"LLR.jpg",
"FLI":"FLI.jpg",
"DLM":"DLM.jpg",
"BTN":"BTN.jpg",
"BTK":"BTK.jpg",
"BTI":"BTI.jpg",
"BRU":"BRU.jpg",
"BLU":"BLU.jpg",
"BKP":"BKP.jpg",
"BHS":"BHS.jpg",
"BBC":"BBC.jpg",
"BAW":"BAW.jpg",
"BAV":"BAV.jpg",
"AZW":"AZW.jpg",
"AZU":"AZU.jpg",
"AXY":"AXY.jpg",
"AXM":"AXM.jpg",
"AWT":"AWT.jpg",
"AVA":"AVA.jpg",
"AUA":"AUA.jpg",
"ASA":"ASA.jpg",
"ARU":"ARU.jpg",
"AND":"AND.jpg",
"ANA":"ANA.jpg",
"AKJ":"AKJ.jpg",
"AJA":"AJA.jpg",
"AHY":"AHY.jpg",
"ADH":"ADH.jpg",
"ACI":"ACI.jpg",
"AAY":"AAY.jpg",
"AAR":"AAR.jpg",
"AAL":"AAL.jpg",
"TSC":"TSC.jpg",
"THT":"THT.jpg",
"SZN":"SZN.jpg",
"SLI":"SLI.jpg",
"ROU":"ROU.jpg",
"REU":"REU.jpg",
"MNG":"MNG.jpg",
"MSC":"MSC.jpg",
"MAU":"MAU.jpg",
"KZR":"KZR.jpg",
"HOP":"HOP.jpg",
"GRL":"GRL.jpg",
"FWI":"FWI.jpg",
"EIN":"EIN.jpg",
"DAH":"DAH.jpg",
"CCA":"CCA.jpg",
"AXB":"AXB.jpg",
"AWA":"AWA.jpg",
"ASV":"ASV.jpg",
"ASL":"ASL.jpg",
"ARG":"ARG.jpg",
"ANZ":"ANZ.jpg",
"ANG":"ANG.jpg",
"AMX":"AMX.jpg",
"AMU":"AMU.jpg",
"AMC":"AMC.jpg",
"AIE":"AIE.jpg",
"AIC":"AIC.jpg",
"AFR":"AFR.jpg",
"AFL":"AFL.jpg",
"AEE":"AEE.jpg",
"AEA":"AEA.jpg",
"ACA":"ACA.jpg",
"ABY":"ABY.jpg",
"ABL":"ABL.jpg",
"LZB":"LZB.png",
"SVA":"SVA.png",
"SKW":"SKW.jpg",
"GWI":"GWI.jpg",
"EZS":"EZS.jpg",
"ENY":"ENY.jpg",
"PRM":"PRM.jpg",
"NWA":"DAL.jpg",
"TWA":"AAL.jpg",
"AWE":"AAL.jpg",
"USA":"AAL.jpg",
"BVX":"BVX.png",
"UPS":"UPS.png",
"VJT":"VJT.png",
"SIL":"SIL.png",
"EK":"UAE.jpg",
"AA":"AAL.jpg",
"WN":"SWA.jpg",
"JIA":"AAL.jpg",
"TUI":"TUI.png",
"ABW":"ABW.png",
"PAY":"PAY.jpg",
"GEC":"DLH.jpg",
"BER":"BER.jpg",
"EJA":"EJA.png",
"KLC":"KLM.jpg",
"TPC":"TPC.jpg",
"BCS":"BCS.png",
}

# File path to store and retrieve previous speeds
groundspeeds_file = "previous_groundspeeds.json"

# Load previous speeds from the file
#try:
    #with open(groundspeeds_file, 'r') as file:
        #previous_groundspeeds = json.load(file)
#except FileNotFoundError:
    #previous_groundspeeds = {}

def haversine(lat1, long1, lat2, long2):
    radius = 3959.87433
    dLat, dLon, lat1, lat2 = radians(lat2 - lat1), radians(long2 - long1), radians(lat1), radians(lat2)
    x = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    y = 2 * asin(sqrt(x))
    return radius * y

my_list = ['SCHEDULED', 'PRE-DEPARTURE', 'HOLDING POSITION', 'TAXIING FOR TAKEOFF / LEFT GATE', 'TAKING OFF', 'EN ROUTE', 'DESCENDING', 'FINAL APPROACH', 'ARRIVING SHORTLY', 'LANDED']

def find_coordinates(i, data1):
    global distance
    global ETA
    global nm_distance



    for item in data1:
        if item['icao'] == i['flight_plan']['arrival']:
            lat2 = item['latitude']
            long2 = item['longitude']
            lat1 = i['latitude']
            long1 = i['longitude']
            distance = haversine(lat1, long1, lat2, long2)
            nm_distance = distance * 0.86897624
            if i['groundspeed'] == 0 and nm_distance <= 4:
                return my_list[9]
            if i['groundspeed'] != 0:
                if nm_distance > 50 and i['altitude'] > 10000:
                    return my_list[5]
                elif nm_distance >= 4 and nm_distance <= 50 and i['groundspeed'] >= 215:
                    return my_list[6]
                elif nm_distance >= 4 and i['groundspeed'] < 215 and nm_distance <= 50 and i['groundspeed'] > 50:
                    return my_list[7]
                elif i['groundspeed'] >= 50 and nm_distance <= 4 and i['groundspeed'] < 200:
                    return my_list[8]
                elif i['groundspeed'] < 50 and nm_distance <= 4:
                    return my_list[9]

def find_coordinates3(i, data1):
    global distance
    global ETA
    global nm_distance

    for item in data1:
        if item['icao'] == i['flight_plan']['arrival']:
            lat2 = item['latitude']
            long2 = item['longitude']
            lat1 = i['latitude']
            long1 = i['longitude']
            distance = haversine(lat1, long1, lat2, long2)
            nm_distance = distance * 0.86897624
            #return math.trunc(round(nm_distance, 1))
            return nm_distance

def find_coordinates4(i, data1):
    global distance
    global ETA
    global nm_distance


    for item in data1:
        if item['icao'] == i['flight_plan']['arrival']:
            lat2 = item['latitude']
            long2 = item['longitude']
            lat1 = i['latitude']
            long1 = i['longitude']
            distance = haversine(lat1, long1, lat2, long2)
            nm_distance = distance * 0.86897624
            my_string = i['flight_plan']['enroute_time']
            if i['groundspeed'] > 50 and (i['groundspeed'] >= 250 or nm_distance <= 100):
                hours = nm_distance / i['groundspeed']
                total_minutes = hours * 60
                converted_hours = total_minutes // 60
                xHours = round(converted_hours, 0)
                converted_minutes = total_minutes % 60
                xMin = round(converted_minutes, 0)
                return str(math.trunc(xHours)) + ' hours ' + str(math.trunc(xMin)) + ' minutes'
            elif nm_distance >= 5:
                if (i['flight_plan']['enroute_time'])[0:1] == '0' and i['flight_plan']['enroute_time'] != '0000':
                    return my_string[1:2] + ' hours ' + my_string[2:4] + ' minutes'
                if i['flight_plan']['enroute_time'] != '0000':
                    return my_string[0:2] + ' hours ' + my_string[2:4] + ' minutes'
                elif i['flight_plan']['enroute_time'] == '0000':
                    return "---"
            else:
                return "---"


def find_coordinates2(i, data1):
    global distance
    global ETA
    global nm_distance
    global previous_speeds

    for item in data1:
        if item['icao'] == i['flight_plan']['departure']:
            global qwe
            lat4 = item['latitude']
            long4 = item['longitude']
            lat3 = i['latitude']
            long3 = i['longitude']
            distance = haversine(lat3, long3, lat4, long4)
            nauticalMiles = distance * 0.86897624
            if i['groundspeed'] == 0 and nauticalMiles < 2 and previous_speeds.get(i['callsign']) == True:
                return my_list[3]
            elif i['groundspeed'] == 0 and nauticalMiles < 2 and i['transponder'] == i['flight_plan']['assigned_transponder']:
                return my_list[1]
            elif i['groundspeed'] == 0 and nauticalMiles < 2:
                return my_list[0]
            elif i['groundspeed'] != 0:


                hours1 = nauticalMiles / i['groundspeed']
                tm = hours1 * 60
                ch = tm // 60
                xHours1 = round(ch, 0)
                cm = tm % 60
                xMin1 = round(cm, 0)

                if i['groundspeed'] < 50 and nauticalMiles < 5:
                    return my_list[3]
                elif i['groundspeed'] >= 50 and i['groundspeed'] <= 200 and nauticalMiles <= 50:
                    return my_list[4]
                elif i['altitude'] <= 10000 and nauticalMiles <= 50:
                    return my_list[5]
                else:
                    return my_list[6]

def nm(i, data1):
    global distance
    global ETA
    global nm_distance

    for item in data1:
        if item['icao'] == i['flight_plan']['departure']:
            lat4 = item['latitude']
            long4 = item['longitude']
            lat3 = i['latitude']
            long3 = i['longitude']
            distance = haversine(lat3, long3, lat4, long4)
            nauticalMiles = distance * 0.86897624
            #return math.trunc(round(nauticalMiles, 0))
            return nauticalMiles

def get_flight_img(mystr):
    global flight_img_lookup

    if mystr[:3] in flight_img_lookup:
       return(flight_img_lookup[mystr[:3]])
    else:
       return("default.jpg")

choice, input_depCode, input_arrivalCode, input_callsign = None, None, None, None

def parse_json_url(url, url2,p_dep_arr_tag,airportcode):
    global distance, df, df_sorted, input_depCode, input_arrivalCode, input_callsign, choice
    global d, c, a

    global x, y

    global lat1, lat2, long1, long2
    global flight_img_lookup

    response = requests.get(url)
    data = response.json()

    if p_dep_arr_tag == 'D':
       choice = 'departure'
    elif p_dep_arr_tag == 'A':
       choice = 'arrival'
    else:
       choice = 'status'

    #choice = input('Departure, Arrival, or Live Flight Status? (type in departure, arrival, or status) >>> ')
    if choice == 'departure':
        input_depCode = airportcode #'KDFW'
        input_arrivalCode = ''
        input_callsign = ''
    elif choice == 'arrival':
        input_arrivalCode = airportcode
        input_depCode = ''
        input_callsign = ''
    elif choice == 'status':
        input_callsign = airportcode
        input_depCode = ''
        input_arrivalCode = ''
        #print('---------------------------------------------------------------------------------------------------------------')
        #print('Aircraft are listed by distance from their DEPARTURE airport')
        #print("Type 'Ctrl + C' to exit")

    d, c, a = 0, 0, 0

    response = requests.get(url2)
    data1 = response.json()

    flight_info = []

    for i in data['pilots']:
        if i['flight_plan'] is not None and i['flight_plan']['departure'] != i['flight_plan']['arrival']:
            var_departure = i['flight_plan']['departure']
            var_arrival = i['flight_plan']['arrival']
            var_callsign = i['callsign'][:3]
            callsign = i['callsign']

            if (var_departure == input_depCode and input_callsign == '' and input_arrivalCode == ''):
                flight = {
                    'Callsign': i['callsign'],
                    'Aircraft': i['flight_plan']['aircraft_short'],
                    'Route': i['flight_plan']['departure'] + ' - ' + i['flight_plan']['arrival'],
                }
                new1_status = find_coordinates(i, data1)
                if new1_status is None:
                    new1_status = find_coordinates2(i, data1)
                #if new1_status is None:
                    #new1_status = my_list[2]
                flight['Status'] = new1_status

                if choice == 'departure':
                    flight['Distance from Airport (nm)'] = nm(i, data1)
                else:
                    flight['Distance from Airport (nm)'] = find_coordinates3(i, data1)
                flight['GS'] = str(i['groundspeed']) + 'kts'

                flight['Time Remaining'] = find_coordinates4(i, data1)
                flight_info.append(flight)
                d += 1

            elif (var_arrival == input_arrivalCode and input_callsign == '' and input_depCode == ''):
                flight = {
                    'Callsign': i['callsign'],
                    'Aircraft': i['flight_plan']['aircraft_short'],
                    'Route': i['flight_plan']['departure'] + ' - ' + i['flight_plan']['arrival'],
                }

                new2_status = find_coordinates(i, data1)

                if new2_status is None:
                    new2_status = find_coordinates2(i, data1)
                #if new2_status is None:
                    #new2_status = my_list[2]
                flight['Status'] = new2_status

                if choice == 'departure':
                    flight['Distance from Airport (nm)'] = nm(i, data1)
                else:
                    flight['Distance from Airport (nm)'] = find_coordinates3(i, data1)
                flight['GS'] = str(i['groundspeed']) + 'kts'
                flight['Time Remaining'] = find_coordinates4(i, data1)
                flight_info.append(flight)
                a += 1

            elif (var_callsign == input_callsign and input_arrivalCode == '' and input_depCode == ''):
                flight = {
                    'Callsign': i['callsign'],
                    'Aircraft': i['flight_plan']['aircraft_short'],
                    'Route': i['flight_plan']['departure'] + ' - ' + i['flight_plan']['arrival'],
                }
                new3_status = find_coordinates(i, data1)
                if new3_status is None:
                    new3_status = find_coordinates2(i, data1)
                #if new3_status is None:
                    #new3_status = my_list[2]
                flight['Status'] = new3_status

                if choice == 'departure':
                    flight['Distance from Airport (nm)'] = nm(i, data1)
                else:
                    flight['Distance from Airport (nm)'] = find_coordinates3(i, data1)
                flight['GS'] = str(i['groundspeed']) + 'kts'
                flight['Time Remaining'] = find_coordinates4(i, data1)
                flight_info.append(flight)
                c += 1

            elif (callsign == input_callsign and input_arrivalCode == '' and input_depCode == ''):
                flight = {
                    'Callsign': i['callsign'],
                    'Aircraft': i['flight_plan']['aircraft_short'],
                    'Route': i['flight_plan']['departure'] + ' - ' + i['flight_plan']['arrival'],
                }
                new_status = find_coordinates(i, data1)
                if new_status is None:
                    new_status = find_coordinates2(i, data1)
                #if new_status is None:
                    #new_status = my_list[2]
                flight['Status'] = new_status

                if choice == 'departure':
                    flight['Distance from Airport (nm)'] = nm(i, data1)
                else:
                    flight['Distance from Airport (nm)'] = find_coordinates3(i, data1)
                flight['GS'] = str(i['groundspeed']) + 'kts'
                flight['Time Remaining'] = find_coordinates4(i, data1)
                flight_info.append(flight)
                c += 1

    df = pd.DataFrame(flight_info)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)

    status_order = pd.CategoricalDtype(categories=my_list, ordered=True)
    if d > 0 or c > 0 or a > 0:
        df.dropna(subset=['Time Remaining'], inplace=True)


    if (a+c+d) > 0:
        df["fimage"] = df["Callsign"].apply(get_flight_img)
        df['Status'] = df['Status'].astype(status_order)

        #if choice == 'departure':
        #    df_sorted = df.sort_values(by=['Status', 'Distance from Airport (nm)'], ascending=[True, True])
        #else:
        #    df_sorted = df.sort_values(by=['Status', 'Distance from Airport (nm)'], ascending=[False, True])

        df_sorted = df
        df_sorted.rename(columns={"Time Remaining" : "TimeRemaining"}, inplace=True)
        df_sorted.rename(columns={"Distance from Airport (nm)" : "DistancefromAirport"}, inplace=True)

        if choice == 'departure':
            df_sorted = df.sort_values(by=['Status', 'DistancefromAirport'], ascending=[True, True])
        else:
            df_sorted = df.sort_values(by=['Status', 'DistancefromAirport'], ascending=[False, True])
    else:
        df_sorted = df

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#MAIN PROCEDURE
def process_me(p_dep_arr_tag,airportcode):
    global previous_speeds
    global previous_speeds_ind
    global process_stats
    global process_stats_prv
    global myjson

    #if (previous_speeds_ind == 1 and process_stats == "running"):
    #   return(myjson)

    #print("previous run status: " + process_stats)

    #process_stats = "running"
    #print(p_dep_arr_tag + "/" + airportcode + "/" + "START---" + process_stats)

    json_url = 'https://data.vatsim.net/v3/vatsim-data.json'
    json_url2 = 'https://gist.githubusercontent.com/friedNoodle1000/9fda31d3dd90fbc723905a21327182dd/raw/3bba677f558a935158efc9e249c0dcb48310a9ad/iata-icao.json'

    response = requests.get(json_url)
    data = response.json()

    #print("prev speed : " + str(previous_speeds_ind))

    #print(json.dumps(previous_speeds, indent=2))

    if previous_speeds_ind == 0:
        for i in data['pilots']:
               previous_speeds[i['callsign']] = False

    previous_speeds_ind = 1

    for i in data['pilots']:
        gs = int(i.get('groundspeed'))
        if gs > 0:
           ##print(f"Setting {i['callsign']} to True")
           previous_speeds[i['callsign']] = True
           ##print(gs)

    #print(json.dumps(previous_speeds, indent=2))

    parse_json_url(json_url, json_url2,p_dep_arr_tag,airportcode)
    #print(df_sorted.to_string(index=False))

    debug_ind = "Y"

    # if debug_ind == "Y":
       # if p_dep_arr_tag == "A":
           # for index, row in df_sorted.iterrows():
               # print(row['From'])
               # if row['From'] == "Undefined":
                  # now = datetime.now()
                  # current_time = now.strftime("%H:%M:%S")
                  # print(p_dep_arr_tag + "/" + airportcode + "/" + current_time)
                  # break

       # if p_dep_arr_tag == "D":
           # for index, row in df_sorted.iterrows():
               # print(row['Destination'])
               # if row['Destination'] == "Undefined":
                  # now = datetime.now()
                  # current_time = now.strftime("%H:%M:%S")
                  # print(p_dep_arr_tag + "/" + airportcode + "/" + current_time)
                  # break
    myjson = df_sorted.to_json(orient="records")
    #print(myjson)
    #print("---------------------------------------------------------------------------------------------------------------")
    #time.sleep(15)
    #print(p_dep_arr_tag + "/" + airportcode + "/" + "END")
    process_stats = "completed"
    process_stats_prv = process_stats
    return(myjson)

#process_me('D','KDFW')

process_stats = "starting"

previous_speeds_ind = 0
gist_raw = 'https://gist.githubusercontent.com/friedNoodle1000/6456eb99ff544e31de7e71c386ce3f1f/raw/c830fc24541598a105ff0e2444e4e5f6ae5be9f3/previous_speeds.json'
#previous_speeds = {}

response1 = requests.get(gist_raw)
previous_speeds = response1.json()

gist_id = "6456eb99ff544e31de7e71c386ce3f1f"

response2 = requests.post(
    f'https://api.github.com/gists/6456eb99ff544e31de7e71c386ce3f1f',
    headers={'Authorization': f'token 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'},
    json={
        'files': {
            'previous_speeds.json': {
                'content': json.dumps(previous_speeds, indent=2)
            }
        }
    }
)

#for testing
#print(get_flight_img1("AFR133"))
#process_me("D","KDFW")