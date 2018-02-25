import os
import subprocess
import serial

db_space=['saavn','']
db_k=['youtube']
db_med=['']


def namegetter(x):
	name_list=[]
	strbuff=""
	read=False
	stopread=False
	for i in x:
		if i=='"':
			if read:
				stopread=True
			read=~read
			continue
		if read:
		  strbuff+=i
		if stopread:
			stopread=False
			pid_list.append(str(strbuff))
			strbuff=""
	return name_list


def pauser():
	to_pause=[]
	noiseMakers=subprocess.check_output('pacmd list-sink-inputs| grep -e application.name ',shell=True)
	noiseMakers=str(noiseMakers)
	to_pause=namegetter(noiseMakers)
	for i in to_pause:
		os.system('xdotool search --name '+str(i)+'')
	return to_pause


def resumer(x):

	for i in x:
		os.system('kill -CONT '+str(i))



def main():
	paused=False
	ser=serial.Serial('/dev/ttyACM0',9600)
	while True:

		p=ser.readline()

		if  (p[:4]==b'play' and paused):
			resumer(frozen)
			paused=False

		if (p[:5]==b'pause' and ~paused):
			frozen=pauser()
			paused=True






if __name__ == '__main__':
	main()
