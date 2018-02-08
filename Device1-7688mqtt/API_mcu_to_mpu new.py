import time  
import sys  
import httplib, urllib  
import json

import numpy as np
from sklearn.cluster import KMeans
from sklearn import cluster, datasets, metrics
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import time
from scipy.spatial.distance import cdist,pdist



sys.path.insert(0, '/usr/lib/python2.7/bridge/')  
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

deviceId = "DsNAo1VS"  
deviceKey = "vI2YPiwY0ydd9AKa"


def post_to_mcs(payload):  
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

while True:  
    queue = np.random.rand(0,3)

    x0 = value.get("x")
    y0 = value.get("y")
    z0 = value.get("z")
    s0 = value.get("s")
    
    newdata = {x0,y0,z0}
    np.vstack([queue,newdata])

    print(queue)

    payload = {"datapoints":
                [{"dataChnId":"x","values":{"value":x0}},
                {"dataChnId":"y","values":{"value":y0}},
                {"dataChnId":"z","values":{"value":z0}},
                {"dataChnId":"s","values":{"value":s0}}]}
    post_to_mcs(payload)
    time.sleep(5)