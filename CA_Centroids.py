# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:24:18 2019

@author: chris.bargman5
"""

import pandas as pd
import csv
CA_most_to_least = pd.read_csv("C:/Users/chris.bargman5/Desktop/Geog701/projects/Excel/California/CA_most_to_least.csv")


CA_xcoords = []
with open("C:/Users/chris.bargman5/Desktop/Geog701/projects/Excel/California/CA_most_to_least.csv", "r",encoding = 'unicode_escape') as csvfile:
    reader = csv.reader(csvfile)
    RowNum = 0
    for line in reader:
        if RowNum >= 1:
            CA_xcoords.append(line[8])
        RowNum = RowNum + 1
print (CA_xcoords)



CA_ycoords = []
with open("C:/Users/chris.bargman5/Desktop/Geog701/projects/Excel/California/CA_most_to_least.csv", "r",encoding = 'unicode_escape') as csvfile:
    reader = csv.reader(csvfile)
    RowNum = 0
    for line in reader:
        if RowNum >= 1:
            CA_ycoords.append(line[9])
        RowNum = RowNum + 1
print (CA_ycoords)

#CENTROIDS
#for SFinformer
x = CA_xcoords[:135]
y = CA_ycoords[:135]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_SFinformer = getmeancenter(x1,y1)
print(Centroid_SFinformer)

#for EcoInternetDrGB
x = CA_xcoords[314:381]
y = CA_ycoords[314:381]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_EcoInternetDrGB = getmeancenter(x1,y1)
print(Centroid_EcoInternetDrGB)

#for EcoInternetDrGB
x = CA_xcoords[314:381]
y = CA_ycoords[314:381]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_EcoInternetDrGB = getmeancenter(x1,y1)
print(Centroid_EcoInternetDrGB)

#for Simfly1
x = CA_xcoords[441:499]
y = CA_ycoords[441:499]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Simfly1 = getmeancenter(x1,y1)
print(Centroid_Simfly1)

#for sandiegoinforme
x = CA_xcoords[499:550]
y = CA_ycoords[499:550]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_sandiegoinforme = getmeancenter(x1,y1)
print(Centroid_sandiegoinforme)

#for footy90com
x = CA_xcoords[597:642]
y = CA_ycoords[597:642]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_footy90com = getmeancenter(x1,y1)
print(Centroid_footy90com)

#for techieappy
x = CA_xcoords[642:684]
y = CA_ycoords[642:684]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_techieappy = getmeancenter(x1,y1)
print(Centroid_techieappy)

#for zennie62
x = CA_xcoords[684:724]
y = CA_ycoords[684:724]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_zennie62 = getmeancenter(x1,y1)
print(Centroid_zennie62)

#for zennie62
x = CA_xcoords[684:724]
y = CA_ycoords[684:724]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_zennie62 = getmeancenter(x1,y1)
print(Centroid_zennie62)

#for schoolmoneyorg
x = CA_xcoords[834:867]
y = CA_ycoords[834:867]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_schoolmoneyorg = getmeancenter(x1,y1)
print(Centroid_schoolmoneyorg)

#for Politics_Info
x = CA_xcoords[867:900]
y = CA_ycoords[867:900]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Politics_Info = getmeancenter(x1,y1)
print(Centroid_Politics_Info)

#for iBoldNews
x = CA_xcoords[900:932]
y = CA_ycoords[900:932]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_iBoldNews = getmeancenter(x1,y1)
print(Centroid_iBoldNews)

#for somsirsa
x = CA_xcoords[932:964]
y = CA_ycoords[932:964]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_somsirsa = getmeancenter(x1,y1)
print(Centroid_somsirsa)

#for MaxineSykes
x = CA_xcoords[1111:1139]
y = CA_ycoords[1111:1139]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_MaxineSykes = getmeancenter(x1,y1)
print(Centroid_MaxineSykes)

#for FantasyAlarm
x = CA_xcoords[1268:1293]
y = CA_ycoords[1268:1293]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_FantasyAlarm = getmeancenter(x1,y1)
print(Centroid_FantasyAlarm)

#for LidarMonkey_CA
x = CA_xcoords[1293:1317]
y = CA_ycoords[1293:1317]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_LidarMonkey_CA = getmeancenter(x1,y1)
print(Centroid_LidarMonkey_CA)

#for Fischer_History
x = CA_xcoords[1407:1429]
y = CA_ycoords[1407:1429]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Fischer_History = getmeancenter(x1,y1)
print(Centroid_Fischer_History)

#for forkbender
x = CA_xcoords[1429:1451]
y = CA_ycoords[1429:1451]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_forkbender = getmeancenter(x1,y1)
print(Centroid_forkbender)

#for bomzfashion
x = CA_xcoords[1538:1559]
y = CA_ycoords[1538:1559]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_bomzfashion = getmeancenter(x1,y1)
print(Centroid_bomzfashion)

#for CrisisDigest
x = CA_xcoords[1559:1580]
y = CA_ycoords[1559:1580]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_CrisisDigest = getmeancenter(x1,y1)
print(Centroid_CrisisDigest)

#for ninonaprea
x = CA_xcoords[1642:1662]
y = CA_ycoords[1642:1662]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_ninonaprea = getmeancenter(x1,y1)
print(Centroid_ninonaprea)

#for AtlCurbAppeal
x = CA_xcoords[1662:1682]
y = CA_ycoords[1662:1682]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_AtlCurbAppeal = getmeancenter(x1,y1)
print(Centroid_AtlCurbAppeal)

#for BobbyFischerTru
x = CA_xcoords[1740:1759]
y = CA_ycoords[1740:1759]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_BobbyFischerTru = getmeancenter(x1,y1)
print(Centroid_BobbyFischerTru)

#for debruning_CA
x = CA_xcoords[1779:1798]
y = CA_ycoords[1779:1798]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_debruning_CA = getmeancenter(x1,y1)
print(Centroid_debruning_CA)

#for Rocketnews1
x = CA_xcoords[1798:1816]
y = CA_ycoords[1798:1816]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Rocketnews1 = getmeancenter(x1,y1)
print(Centroid_Rocketnews1)

#for WineRackCity
x = CA_xcoords[1834:1852]
y = CA_ycoords[1834:1852]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_WineRackCity = getmeancenter(x1,y1)
print(Centroid_WineRackCity)

#for mantisman7
x = CA_xcoords[1852:1870]
y = CA_ycoords[1852:1870]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_mantisman7 = getmeancenter(x1,y1)
print(Centroid_mantisman7)

#for collabregate
x = CA_xcoords[1887:1904]
y = CA_ycoords[1887:1904]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_collabregate = getmeancenter(x1,y1)
print(Centroid_collabregate)

#for thegalianogroup
x = CA_xcoords[1904:1921]
y = CA_ycoords[1904:1921]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_thegalianogroup = getmeancenter(x1,y1)
print(Centroid_thegalianogroup)

#for updatedliving
x = CA_xcoords[2153:2166]
y = CA_ycoords[2153:2166]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_updatedliving = getmeancenter(x1,y1)
print(Centroid_updatedliving)

#for jamesvgingerich
x = CA_xcoords[2180:2194]
y = CA_ycoords[2180:2194]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_jamesvgingerich = getmeancenter(x1,y1)
print(Centroid_jamesvgingerich)

#for JoePlumberSeatt
x = CA_xcoords[2260:2273]
y = CA_ycoords[2260:2273]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_JoePlumberSeatt = getmeancenter(x1,y1)
print(Centroid_JoePlumberSeatt)


#for sailing_news
x = CA_xcoords[2275:2286]
y = CA_ycoords[2275:2286]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_sailing_news = getmeancenter(x1,y1)
print(Centroid_sailing_news)

#for robinsnewswire
x = CA_xcoords[2286:2299]
y = CA_ycoords[2286:2299]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_robinsnewswire = getmeancenter(x1,y1)
print(Centroid_robinsnewswire)

#for StateStatus_AK
x = CA_xcoords[2363:2375]
y = CA_ycoords[2363:2375]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_StateStatus_AK = getmeancenter(x1,y1)
print(Centroid_StateStatus_AK)

#for atltreepros
x = CA_xcoords[2434:2445]
y = CA_ycoords[2434:2445]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_atltreepros = getmeancenter(x1,y1)
print(Centroid_atltreepros)

#for 60sfolks
x = CA_xcoords[2478:2489]
y = CA_ycoords[2478:2489]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_60sfolks = getmeancenter(x1,y1)
print(Centroid_60sfolks)

#for Tshombe77
x = CA_xcoords[2489:2500]
y = CA_ycoords[2489:2500]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Tshombe77 = getmeancenter(x1,y1)
print(Centroid_Tshombe77)

#for 4PawShop
x = CA_xcoords[2652:2662]
y = CA_ycoords[2652:2662]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_4PawShop = getmeancenter(x1,y1)
print(Centroid_4PawShop)

#for OkaidokuNews
x = CA_xcoords[2767:2776]
y = CA_ycoords[2767:2776]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_OkaidokuNews = getmeancenter(x1,y1)
print(Centroid_OkaidokuNews)

#for SavePrivacyNow
x = CA_xcoords[2785:2794]
y = CA_ycoords[2785:2794]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_SavePrivacyNow = getmeancenter(x1,y1)
print(Centroid_SavePrivacyNow)

#for GoalReporter
x = CA_xcoords[2794:2803]
y = CA_ycoords[2794:2803]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_GoalReporter = getmeancenter(x1,y1)
print(Centroid_GoalReporter)

#for MrBill_94592
x = CA_xcoords[2803:2812]
y = CA_ycoords[2803:2812]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_MrBill_94592 = getmeancenter(x1,y1)
print(Centroid_MrBill_94592)

#for MrBill_94592
x = CA_xcoords[2803:2812]
y = CA_ycoords[2803:2812]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_MrBill_94592 = getmeancenter(x1,y1)
print(Centroid_MrBill_94592)

#for RunGomez
x = CA_xcoords[2851:2860]
y = CA_ycoords[2851:2860]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_RunGomez = getmeancenter(x1,y1)
print(Centroid_RunGomez)

#for AbruzzoTweets
x = CA_xcoords[2871:2878]
y = CA_ycoords[2871:2878]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_AbruzzoTweets = getmeancenter(x1,y1)
print(Centroid_AbruzzoTweets)

#for KAIJUKING23
x = CA_xcoords[2939:2947]
y = CA_ycoords[2939:2947]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_KAIJUKING23 = getmeancenter(x1,y1)
print(Centroid_KAIJUKING23)

#for howappealing
x = CA_xcoords[2963:2971]
y = CA_ycoords[2963:2971]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_howappealing = getmeancenter(x1,y1)
print(Centroid_howappealing)

#for 420Cyber
x = CA_xcoords[2971:2979]
y = CA_ycoords[2971:2979]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_420Cyber = getmeancenter(x1,y1)
print(Centroid_420Cyber)

#for GreenEnergy
x = CA_xcoords[3003:3011]
y = CA_ycoords[3003:3011]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_GreenEnergy = getmeancenter(x1,y1)
print(Centroid_GreenEnergy)

#for LAunvrz
x = CA_xcoords[3091:3098]
y = CA_ycoords[3091:3098]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_LAunvrz = getmeancenter(x1,y1)
print(Centroid_LAunvrz)

#for genphys
x = CA_xcoords[3119:3126]
y = CA_ycoords[3119:3126]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_genphys = getmeancenter(x1,y1)
print(Centroid_genphys)

#for ganja_seeds
x = CA_xcoords[3144:3151]
y = CA_ycoords[3144:3151]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_ganja_seeds = getmeancenter(x1,y1)
print(Centroid_ganja_seeds)

#for RonDeLord
x = CA_xcoords[3163:3170]
y = CA_ycoords[3163:3170]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_RonDeLord = getmeancenter(x1,y1)
print(Centroid_RonDeLord)

#for SondLloydWebBot
x = CA_xcoords[3177:3182]
y = CA_ycoords[3177:3182]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_SondLloydWebBot = getmeancenter(x1,y1)
print(Centroid_SondLloydWebBot)

#for Fandustry
x = CA_xcoords[3182:3189]
y = CA_ycoords[3182:3189]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Fandustry = getmeancenter(x1,y1)
print(Centroid_Fandustry)

#for TraffickStop101
x = CA_xcoords[3196:3203]
y = CA_ycoords[3196:3203]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_TraffickStop101 = getmeancenter(x1,y1)
print(Centroid_TraffickStop101)

#for AppTrailerFish
x = CA_xcoords[3337:3342]
y = CA_ycoords[3337:3342]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_AppTrailerFish = getmeancenter(x1,y1)
print(Centroid_AppTrailerFish)

#for BadassActivist
x = CA_xcoords[3381:3385]
y = CA_ycoords[3381:3385]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_BadassActivist = getmeancenter(x1,y1)
print(Centroid_BadassActivist)

#for BenjaminDeMers
x = CA_xcoords[3409:3413]
y = CA_ycoords[3409:3413]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_BenjaminDeMers = getmeancenter(x1,y1)
print(Centroid_BenjaminDeMers)

#for Bloom_THC
x = CA_xcoords[3447:3450]
y = CA_ycoords[3447:3450]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Bloom_THC = getmeancenter(x1,y1)
print(Centroid_Bloom_THC)

#for brianhurley
x = CA_xcoords[3471:3475]
y = CA_ycoords[3471:3475]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_brianhurley = getmeancenter(x1,y1)
print(Centroid_brianhurley)

#for California_trav
x = CA_xcoords[3503:3509]
y = CA_ycoords[3503:3509]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_California_trav = getmeancenter(x1,y1)
print(Centroid_California_trav)

#for CannabisBizNews
x = CA_xcoords[3519:3525]
y = CA_ycoords[3519:3525]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_CannabisBizNews = getmeancenter(x1,y1)
print(Centroid_CannabisBizNews)

#for comedynews
x = CA_xcoords[3585:3589]
y = CA_ycoords[3585:3589]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_comedynews = getmeancenter(x1,y1)
print(Centroid_comedynews)

#for cueincsa
x = CA_xcoords[3619:3623]
y = CA_ycoords[3619:3623]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_cueincsa = getmeancenter(x1,y1)
print(Centroid_cueincsa)

#for dennisjromero
x = CA_xcoords[3669:3672]
y = CA_ycoords[3669:3672]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_dennisjromero = getmeancenter(x1,y1)
print(Centroid_dennisjromero)

#for diving_news
x = CA_xcoords[3687:3692]
y = CA_ycoords[3687:3692]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_diving_news = getmeancenter(x1,y1)
print(Centroid_diving_news)

#for e2youngenginee1
x = CA_xcoords[3731:3735]
y = CA_ycoords[3731:3735]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_e2youngenginee1 = getmeancenter(x1,y1)
print(Centroid_e2youngenginee1)

#for FitspoGabby
x = CA_xcoords[3821:3825]
y = CA_ycoords[3821:3825]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_FitspoGabby = getmeancenter(x1,y1)
print(Centroid_FitspoGabby)

#for gdlcolorado
x = CA_xcoords[3860:3865]
y = CA_ycoords[3860:3865]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_gdlcolorado = getmeancenter(x1,y1)
print(Centroid_gdlcolorado)

#for GillesKLEIN
x = CA_xcoords[3869:3873]
y = CA_ycoords[3869:3873]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_GillesKLEIN = getmeancenter(x1,y1)
print(Centroid_GillesKLEIN)

#for IbuPertiwi_
x = CA_xcoords[3946:3949]
y = CA_ycoords[3946:3949]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_IbuPertiwi_ = getmeancenter(x1,y1)
print(Centroid_IbuPertiwi_)

#for idivafashion
x = CA_xcoords[3949:3955]
y = CA_ycoords[3949:3955]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_idivafashion = getmeancenter(x1,y1)
print(Centroid_idivafashion)

#for James_Escarcega
x = CA_xcoords[3986:3991]
y = CA_ycoords[3986:3991]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_James_Escarcega = getmeancenter(x1,y1)
print(Centroid_James_Escarcega)

#for JamesAria1
x = CA_xcoords[3991:3994]
y = CA_ycoords[3991:3994]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_JamesAria1 = getmeancenter(x1,y1)
print(Centroid_JamesAria1)

#for Jaynarkliner
x = CA_xcoords[4010:4015]
y = CA_ycoords[4010:4015]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Jaynarkliner = getmeancenter(x1,y1)
print(Centroid_Jaynarkliner)

#for jaynya13
x = CA_xcoords[4015:4020]
y = CA_ycoords[4015:4020]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_jaynya13 = getmeancenter(x1,y1)
print(Centroid_jaynya13)

#for LAcycleHelper
x = CA_xcoords[4112:4118]
y = CA_ycoords[4112:4118]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_LAcycleHelper = getmeancenter(x1,y1)
print(Centroid_LAcycleHelper)

#for Lady_Aimee
x = CA_xcoords[4118:4122]
y = CA_ycoords[4118:4122]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Lady_Aimee = getmeancenter(x1,y1)
print(Centroid_Lady_Aimee)

#for LAPDZBorquez
x = CA_xcoords[4130:4136]
y = CA_ycoords[4130:4136]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_LAPDZBorquez = getmeancenter(x1,y1)
print(Centroid_LAPDZBorquez)

#for lillys_news
x = CA_xcoords[4166:4171]
y = CA_ycoords[4166:4171]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_lillys_news = getmeancenter(x1,y1)
print(Centroid_lillys_news)

#for MKT_Deporte
x = CA_xcoords[4307:4311]
y = CA_ycoords[4307:4311]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_MKT_Deporte = getmeancenter(x1,y1)
print(Centroid_MKT_Deporte)

#for MotorcyclesView
x = CA_xcoords[4319:4322]
y = CA_ycoords[4319:4322]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_MotorcyclesView = getmeancenter(x1,y1)
print(Centroid_MotorcyclesView)

#for MPlenke
x = CA_xcoords[4322:4326]
y = CA_ycoords[4322:4326]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_MPlenke = getmeancenter(x1,y1)
print(Centroid_MPlenke)

#for mtsarabia
x = CA_xcoords[4339:4345]
y = CA_ycoords[4339:4345]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_mtsarabia = getmeancenter(x1,y1)
print(Centroid_mtsarabia)

#for MyMartialArtsTV
x = CA_xcoords[4364:4370]
y = CA_ycoords[4364:4370]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_MyMartialArtsTV = getmeancenter(x1,y1)
print(Centroid_MyMartialArtsTV)

#for overtesports
x = CA_xcoords[4428:4433]
y = CA_ycoords[4428:4433]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_overtesports = getmeancenter(x1,y1)
print(Centroid_overtesports)

#for Patroyale
x = CA_xcoords[4449:4454]
y = CA_ycoords[4449:4454]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Patroyale = getmeancenter(x1,y1)
print(Centroid_Patroyale)

#for phoneweekuk
x = CA_xcoords[4466:4470]
y = CA_ycoords[4466:4470]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_phoneweekuk = getmeancenter(x1,y1)
print(Centroid_phoneweekuk)

#for QueerWire
x = CA_xcoords[4502:4505]
y = CA_ycoords[4502:4505]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_QueerWire = getmeancenter(x1,y1)
print(Centroid_QueerWire)

#for RealEstate361
x = CA_xcoords[4524:4529]
y = CA_ycoords[4524:4529]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_RealEstate361 = getmeancenter(x1,y1)
print(Centroid_RealEstate361)

#for robinsportsnews
x = CA_xcoords[4569:4575]
y = CA_ycoords[4569:4575]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_robinsportsnews = getmeancenter(x1,y1)
print(Centroid_robinsportsnews)

#for RosieRiveterDFW
x = CA_xcoords[4588:4592]
y = CA_ycoords[4588:4592]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_RosieRiveterDFW = getmeancenter(x1,y1)
print(Centroid_RosieRiveterDFW)

#for rotolytics
x = CA_xcoords[4592:4596]
y = CA_ycoords[4592:4596]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_rotolytics= getmeancenter(x1,y1)
print(Centroid_rotolytics)

#for rpstranslations
x = CA_xcoords[4604:4607]
y = CA_ycoords[4604:4607]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_rpstranslations= getmeancenter(x1,y1)
print(Centroid_rpstranslations)

#for SanjayNursing
x = CA_xcoords[4627:4631]
y = CA_ycoords[4627:4631]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_SanjayNursing= getmeancenter(x1,y1)
print(Centroid_SanjayNursing)

#for Sourcers
x = CA_xcoords[4725:4731]
y = CA_ycoords[4725:4731]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Sourcers= getmeancenter(x1,y1)
print(Centroid_Sourcers)

#for tigerbeat
x = CA_xcoords[4822:4826]
y = CA_ycoords[4822:4826]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_tigerbeat= getmeancenter(x1,y1)
print(Centroid_tigerbeat)

#for TowTruckNews
x = CA_xcoords[4848:4853]
y = CA_ycoords[4848:4853]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_TowTruckNews= getmeancenter(x1,y1)
print(Centroid_TowTruckNews)

#for Volleyballwatch
x = CA_xcoords[4917:4920]
y = CA_ycoords[4917:4920]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_Volleyballwatch= getmeancenter(x1,y1)
print(Centroid_Volleyballwatch)

#for wat3rFascility
x = CA_xcoords[4932:4936]
y = CA_ycoords[4932:4936]
x1 = [float(i) for i in x]
y1 = [float(i) for i in y]

def getmeancenter(a,b):
    long_X = sum(a) / len(a)
    lat_Y = sum(b) / len(b)
    return long_X, lat_Y
    
Centroid_wat3rFascility= getmeancenter(x1,y1)
print(Centroid_wat3rFascility)

















































































