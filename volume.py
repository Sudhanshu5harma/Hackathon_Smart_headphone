import os
import subprocess
def signfind(x):
    if x<0:
         return '-'
    else:
        return '+'


def main():

    avgnoise=subprocess.check_output('soundmeter --collect --seconds 3 | grep avg',shell=True)
    strbuff=str(avgnoise)
    print('*********************')
    noisevolprev=int(strbuff[14:])
    print(noisevolprev)
    print('*********************')
    while True:
        
        avgnoise=subprocess.check_output('soundmeter --collect --seconds 3 | grep avg',shell=True)
        strbuff=str(avgnoise)
        noisevolcurr=int(strbuff[14:])
        print('*********************')
        print(noisevolcurr)
        print('*********************')
        update_vol=noisevolcurr-noisevolprev
        noisevolprev=noisevolcurr
        print(update_vol)

        update_vol=update_vol/70;
        print(update_vol)
        os.system("pactl set-sink-volume 0 " +signfind(update_vol)+ str(abs(update_vol)) +"%")
        

if __name__ == '__main__':
	main()
