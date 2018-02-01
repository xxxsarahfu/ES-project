This is one of the device in the project - Linkit Smart 7688 Duo by MediaTek + Adxl345 as a sensor node.
Protocol: MQTT

Since Linkit Samrt 7688 have 2 parts: MCU (compatible with Arduino) & MPU (OpenWrt, Linux), the two files are uploaded to MCU & MPU, respectively.
	a. adxl345.ino: upload to MCU with Arduino IDE. 
			-- get sensor data.
	b. mqtt+mcu2mpu.py: upload to MPU. 
			-- get data from MCU to MPU, and then send data with MQTT to gateway.

