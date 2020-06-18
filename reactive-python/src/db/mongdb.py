#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient["agate"]
mycol = mydb["mth_six_record"]

myquery = {"msisdn": "18209597088"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
