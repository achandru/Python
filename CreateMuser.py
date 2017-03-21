#! python
import urllib
import string
import random
import struct
import json  ## for JSON Parsing
from threading import Thread

def createUsers(): 	#to create a uniqueUsers
    devid = deviceIdGenerator() 
    advid = advertiseIdGenerator()
    ipaddress = generateIp()
    osType = 'Android'	#fixed Values
    lat='20.0'	#fixed values
    lon='70.0'	#fixed values
    webServiceURL = 'http://ind-devapi.yupl.us/v1.4/app/user/create'	#it is the path it will connects webserver
    params = urllib.urlencode({'devid' : devid, 'advid' : advid, 'osType' : osType, 'lat' : lat, 'lon' : lon, 'X-Forwarded-For' : ipaddress}) # to call different parameters
    webServOutPut = urllib.urlopen(webServiceURL, params).read()	#to rea the parameter values
    #print ("deviceId is " +devid + ";" + " Advertiser Id is " +advid + ";" + "ip address is " +ipaddress)	#to print all values
    ParsedOutPut= json.loads(webServOutPut)  ##Parse the JSON
    print(ParsedOutPut['uid']+','+ParsedOutPut['cr_ts']) ## print from parsed JSON
    #print webServOutPut		#It is the O/p given by Server

def deviceIdGenerator(size=6, chars=string.ascii_uppercase + string.digits):	#to create a unique deviceId
    devid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
    return devid

def advertiseIdGenerator(size=6, chars=string.ascii_uppercase + string.digits):	#to create a unique AdvertiseID
    advid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
    return advid

def generateIp():	#to create a unique ipAddress
    ipaddress = "192.168."	#Standered IP values#    
    ipaddress += ".".join(map(str, (random.randint(0, 255) for _ in range(2))))  
    return ipaddress

for _ in range(0,10):	#endUsers values
	Thread(target=createUsers()).start()	#calling all the functions at a time

