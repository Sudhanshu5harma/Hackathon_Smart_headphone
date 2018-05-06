# Hackathon_Smart_headphone


# Idea - 

The idea behind smart headphones is to ease the work of using keys or controls to toggle audio/video by making the headphones smarter. 
Smart Headphones can recognize if they are being worn and not, and automatically pause and resume all audio streams(and related video streams)accordingly.  
In addition, the headphone is also designed in a way that it automatically adjusts the volume based on the surrounding noise level. 

# Working - 

The technology used behind the smart headphones is simple to integrate and easy to implement.  
An IR sensor is used to sense if the headphone is being worn or not, the data is received using an Arduino and based on the received data, the audio/ video of the system is controlled. 
Another feature of the headphone is automatic increase/decrease in the volume of streaming media depending on the levels of ambient noise. 
A microphone is used to receive the data, and based on the data received by the microphone, system volume is changed. 


## Code contain - 

- Arduino file keep checking the data for IR sensor and sending that to python. 
- Python file for controlling volume sense the microphone sound and make the threshold for every 3 seconds and if the sound remain same for 3 second it declare it as noise and according to it increase or decrease the volume.   
- Python file for pausing and unpausing get the data from arduino and before the desired task of switching off and on the media it using the subprocess and os process to access sound card. 



### Installation and start development  



```sh 
$ sudo apt-get update 
$ sudo apt-get install python pip 
$ sudo apt-get install portaudio19-dev python-dev alsa-utils 
```

### Development 

Want to contribute? Great! 


Make a change in your file and instantanously see your updates!  
Feel free to drop a mail on "sharmasudhanshu2110@gmail.com" Saying subject - Smart Headphone 
Open your favorite Terminal and run these commands. 


```sh
$ git clone https://github.com/sudhanshu55/Hackathon_Smart_headphone
``` 
### Reference 
[Download Arduino on linux ](https://www.arduino.cc/en/Main/Software "Download") 
[Arduino Reference ](https://www.arduino.cc/en/Guide/Linux "Linux help") 
[Soundmeter](https://pypi.org/project/soundmeter/ "soundmeter") 
[Subprocess](https://docs.python.org/2/library/subprocess.html "Subprocess") 
[PySerial](http://pyserial.readthedocs.io/en/latest/shortintro.html "Serial communication") 


### Todos

 - Make volume detection more structural.  
 - Add new features.  
 --  For Phones.  
 -- Work for windows.  

### Working on 

- PCB design to eliminate Arduino. 
- Bluetooth Data transfer. 

License 
----

Apache License 2.0




