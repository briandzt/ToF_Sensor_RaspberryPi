import serial
import time
import numpy as np
import pika
import sys

### Program used for calibration
#### Factor file is stored in form of [mode, value]
##### mode 1 stands for additive, mode 2 stands for multiplicative

### Port init and variable declaration ###
port = serial.Serial('/dev/ttyUSB0',baudrate=500000,parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
command = input('1 for reset, 2 for calibration')
notworking = []
if command == 1:
	factor = [(2,1)]*160
	np.save('Calibrationfactor.npy',factor)
if command == 2:
	factor = np.load('Calibrationfactor.npy')
	### Data gathering ###
	x = input('enter starting id')
	y = input('enter ending id')+1
	actual = input('enter actual distance')
	for ID in range(x,y):
		data = []
		for num in range(1,5000): #number can be changed
			comd='A'+str(ID)+'\r'
			port.write(comd)
			a=port.readline()
			if '->'in a:
				b=a.split('->')
				data.append(b[2])
			else:
				print'something wrong with sensor',ID
				data.append(-1)
				break
		if -1 in data:
			notworking.append(ID)
		else:
			meanval = np.mean(data)
			addfc = actual-meanval
			multfc = actual/float(meanval)
			sample = [x*multfc for x in data]
			if multfc < 1:
				factor[ID] = (2,multfc)
			else:
				factor[ID] = (1,addfc)
print notworking

