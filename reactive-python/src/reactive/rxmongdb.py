import pymongo
from rx import create
from rx import Observable
import sys
import os
from rx import from_

def query():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient["agate"]
    mycol = mydb["mth_six_record"]
    # myquery = {"channel_id": "BOSS"}
    # mydoc = mycol.find(myquery)
    mydoc = mycol.find()
    return mydoc

# Query customers with IDs 1, 3, and 5
from_(query().pipe(
    ops.groupBy(lambda rol: rol['channel_id'])
)).subscribe(lambda r: print(r))


# from_(open("python-study/reactive-python/src/file/rxtest.txt")).subscribe(lambda l: print(l))
