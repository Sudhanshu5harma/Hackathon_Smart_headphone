import os
import subprocess
import serial

def idgetter(x):
	pid_list=[]
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
			pid_list.append(int(strbuff))
			strbuff=""
	return pid_list


def pauser():
	to_pause=[]
	noiseMakers=subprocess.check_output('pacmd list-sink-inputs| grep -e application.process.id ',shell=True)
	noiseMakers=str(noiseMakers)
	to_pause=idgetter(noiseMakers)
	for i in to_pause:
		os.system('kill -STOP '+str(i))
	return to_pause


def resumer(x):

	for i in x:
		os.system('kill -CONT '+str(i))



def main():
	paused=False
	ser=serial.Serial('/dev/ttyACM1',9600)
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
