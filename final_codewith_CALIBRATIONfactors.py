import serial
import time
import numpy
import pika
import sys
import numpy as np

### Port Initialization
port = serial.Serial('/dev/ttyUSB0',baudrate=500000,parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
port2 = serial.Serial('/dev/ttyUSB1',baudrate=500000,parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
port3 = serial.Serial('/dev/ttyUSB2',baudrate=500000,parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
port4 = serial.Serial('/dev/ttyUSB3',baudrate=500000,parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
port5 = serial.Serial('/dev/ttyUSB4',baudrate=500000,parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

### sensor id arrangement based on string alingment in the SRC
ID1=[148,114,153,151,143,150,145,136,147,144,132,137,126,135,134,124,128,111,117,118,113,115,114,127,101,102,94,44,112,22,24,23,25,119,157,158];
ID2=[133,138,139,149,122,140,129,146,77,131,48,123,42,130,116,159,154,152,160,92,99,87,93,98,100,63,40,32,36];
ID3=[31,33,26,35,30,4,15,21,16,11,3,60,58,56,53,45,47,55,49,41,43,120,96,97,106,91,70,90] ;
ID4=[34,156,37,39,38,155,62,88,61,89,68,69,13,110,142,82,66,50,28,65,29,12,10,5,7,75,27,125,121];
ID5=[71,72,76,51,52,54,59,83,105,85,109,81,86,84,95,107,108,104,103,19,57,20,2,17,14,1,6,9,18,67,64,74,80,73,78,79];

reading1=[] 
reading2=[] 
reading3=[] 
reading4=[]
reading5=[]

x = input('enter starting id')
y = input('enter ending id')+1
z=input('how many readings per sensor?') 


### additive calibration factors arrays(obtained from Matlab code)
add_array1=np.array([20.97,-1.85,44.81,-9.39,20.97,36.24,-23.60,-12.60,43.89,28.32,-1.08,15.28,30.66,-17.25,24.93,38.27,43.69,48.55,15.52,0.98,0.98,-8.44,-1.85,22.24,45.99,2.53,33.42,14.28,22.11,34.98,-35.14,41.21,3.24,-17.22,-13.32,44.81]*z);
add_array2=np.array([75.35,75.35,-85.86,12.54,-90.78,55.13,-53.19,-19.46,2.84,-33.09,63.13,43.69,13.13,-150.51,-81.35,-58.60,55.45,543.99,54.03,29.54,33.11,324.95,32.53,87.60,21.70,15.25,1.93,7.73,54.25]*z);
add_array3=np.array([13.68,-4.85,-51.96,21.89,0.34,135.58,-127.83,783.20,390.20,607.59,142.73,-0.64,-52.56,-24.28,-8.89,110.59,-10.21,19.04,17.69,-12.78,-23.10,151.15,128.00,13.71,116.70,117.64,25.68,37.43]*z);
add_array4=np.array([93.56,92.89,16.68,-11.06,-24.84,68.32,-3.17,81.53,59.15,27.11,69.27,23.22,57.18,18.21,88.37,51.26,-28.43,-24.39,12.85,-14.25,22.69,45.77,-73.05,16.55,-92.27,41.52,-17.73,27.10,26.70]*z);
add_array5=np.array([94.44,20.82,88.52,87.34,-46.13,-10.44,5.85,12.15,56.17,10.95,55.25,-10.01,30.62,10.26,18.75,7.54,28.52,-2.88,28.52,-6.69,-20.84,8.34,9.82,36.19,-20.31,-31.25,-26.28,32.55,8.54,27.65,45.85,19.70,-25.25,23.56,-0.75,2.88]*z);    

start_time=time.time()
for num in range(1,z+1):
	with open ('exp26.txt','a') as f:
		f.write(time.ctime())
		f.write('\n')
	
	count= 0
	for ID in ID1:	
		comd='A'+str(ID)+'\r'
		port.write(comd)
		data=port.readline()
		if "->" in data:
			a=data.split("->")
			b=a[1]
			sensorid=b
			distance=a[2]
			string= sensorid+" "+distance
			#	print string
		distance=int(distance) 
		reading1.append(distance)
		reading1=reading1+add_array1[count]
		print reading1
		with open ('exp26.txt','a') as f:
			f.write(reading1)
			f.write('\n')
		count = count+1
	
	count = 0
	for ID in ID2:
		comd='A'+str(ID)+'\r'
		port.write(comd)
		data=port.readline()
		if "->" in data:
			a=data.split("->")
			b=a[1]
			sensorid=b
			distance=a[2]
			string= sensorid+" "+distance
		distance=int(distance)
		reading2.append(distance)
		reading2=reading2+add_array2[count]
		with open ('exp26.txt','a') as f:
			f.write(reading2)
			f.write('\n')
		count = count+1
	
	count = 0
	for ID in ID3:
		comd='A'+str(ID)+'\r'
		port.write(comd)
		data=port.readline()
		if "->" in data:
			a=data.split("->")
			b=a[1]
			sensorid=b
			distance=a[2]
			string= sensorid+" "+distance
			#       print string
		distance=int(distance)
		reading3.append(distance)
		reading3=reading3+add_array3[count]
		with open ('exp26.txt','a') as f:
			f.write(reading3)
			f.write('\n')
		count = count+1
	
	count = 0
	for ID in ID4:
		comd='A'+str(ID)+'\r'
		port.write(comd)
		data=port.readline()
		if "->" in data:
			a=data.split("->")
			b=a[1]
			sensorid=b
			distance=a[2]
			string= sensorid+" "+distance
			#       print string 
		distance=int(distance)
		reading4.append(distance)
		reading4=reading4+add_array4[count]
		with open ('exp26.txt','a') as f:
			f.write(reading4)
			f.write('\n')
		count = count+1
		
	count = 0
	for ID in ID5:
		comd='A'+str(ID)+'\r'
		port.write(comd)
		data=port.readline()
		if "->" in data:
			a=data.split("->")
			b=a[1]
			sensorid=b
			distance=a[2]
			string= sensorid+" "+distance
			#       print string
		distance=int(distance)
		reading5.append(distance)
		reading5=reading5+add_array5[count]
		with open ('exp26.txt','a') as f:
			f.write(reading5)
			f.write('\n')
		count = count+1
#	text_file=open ("exp26.txt","r") 
#	lines=text_file.read() 
#	text_file.close()

	#credential=pika.PlainCredentials('test','test')

	#connection = pika.BlockingConnection(pika.ConnectionParameters(host='128.113.122.214',credentials=credential))

	#channel = connection.channel()

	#channel.queue_declare(queue='task_queue', durable=True)

	#message = ' '.join(sys.argv[1:]) or lines
	#channel.basic_publish(exchange='',
        #              routing_key='task_queue',
        #              body=message,
        #              properties=pika.BasicProperties(
        #                 delivery_mode = 2, # make message persist$
        #              ))
#	print(" [x] Sent all sensor reading")
	#connection.close()
    



end_time=time.time() 
total=end_time-start_time 
print total
