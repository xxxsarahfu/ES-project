#-------------------------------------------------------------------------------
# Copyright 2016 Congduc Pham, University of Pau, France.
# 
# Congduc.Pham@univ-pau.fr
#
# This file is part of the low-cost LoRa gateway developped at University of Pau
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------
# Jul/2016 adapted by N. Bertuol under C. Pham supervision 
# 
# nicolas.bertuol@etud.univ-pau.fr
#
# Oct/2016. re-designed by C. Pham to use self-sufficient script per cloud
# Congduc.Pham@univ-pau.fr

import urllib2
import subprocess
import time
import ssl
import socket
import datetime
import sys
import re

reload(sys)
import paho.mqtt.client as mqtt 

#test channel
_def_device_id='272740'
_def_device_key='YZTGW8V1WUK9DFRS'
mqttHost = "35.186.155.168"

client = None 

# upload multiple data
def uploadMultipleData(data_array):
	global client 
	if len(data_array) < 5:
		return
		
	if data_array[0]=='':
		data_array[0]=_def_device_key

	if data_array[1]=='':
		data_array[1]=_def_device_id
		
	iteration = 2 
	fieldNumber = 1
	pload = '\!' + data_array[0] + '#' + data_array[1] + '#' + str(data_array[2]) + '/' + str(data_array[3]) + '/' + str(data_array[4]) 
	topic = "mcs/1"
	client.publish(topic, payload = pload)
	time.sleep(0.2)
	print("FINISH MQTT\n")

# main
# -------------------

def main():
	global client 
	client = mqtt.Client()
	client.connect(mqttHost)
	while True:
		
		data= sys.stdin.readline()	
		c = data.find("!")
		if c >= 0:
			ldata = data[c+1: -1]
			print ldata 
		else:
			continue
			

		# get number of '#' separator
		nsharp = ldata.count('#')			
		#no separator
		if nsharp==0:
			#will use default channel and field
			data=['','']
			
			#contains ['', '', "s1", s1value, "s2", s2value, ...]
			data_array = data + re.split("/", ldata)		
		elif nsharp==1:
			#only 1 separator
			
			data_array = re.split("#|/", ldata)
			
			#if the first item has length > 1 then we assume that it is a channel write key
			if len(data_array[0])>1:
				#insert '' to indicate default field
				data_array.insert(1,'');		
			else:
				#insert '' to indicate default channel
				data_array.insert(0,'');		
		else:
			data_array = re.split("#|/", ldata)	
			
		#just in case we have an ending CR or 0
		data_array[len(data_array)-1] = data_array[len(data_array)-1].replace('\n', '')
		data_array[len(data_array)-1] = data_array[len(data_array)-1].replace('\0', '')	
		
		#test if there are characters at the end of each value, then delete these characters
		digital = True
		i = 2 
		while i < len(data_array) :
			if len(data_array[i]) == 0:
				digital = False
				break
			while not data_array[i][len(data_array[i])-1].isdigit() :
				print  data_array[i][len(data_array[i])-1]
				digital = False
				break	
			i += 1 
		

		if digital:	
			uploadMultipleData(data_array) # upload all data in the fields		
		else:
			print "Error data receive"
	
if __name__ == "__main__":
	main()
	
