# DualKeepon
A portable system with My Keepon robots to study user preferences using a pairwise comparison method.

This project is a collaboration between:
>Robotics and Multibody Mechanics Research Group (Vrije University Brussel)

>Human-Robot Interaction Lab (University of Southern Denmark).

Contact:
> Hoang-Long Cao: hoancao (at) vub (dot) ac (dot) be

> Lars Christian Jensen: larscj (at) sdu (dot) dk

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/Dual-Keepon-speech.png)

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/DualKeepon-Hardware.png)

##Hacking MyKeepon

A tutorial of hacking MyKeepon robot can  be found in our website: http://probo.vub.ac.be/HackingKeepon. For this DualKeepon project, no shield for Arduino is needed.

This work was presented at the 2013 International Summer School on Social HRI and RO-MAN 2014.

Atelier 3: Hacking Keepon – Bram Vanderborght, Cao Hoang Long, Greet Van de Perre (Vrije Universiteit Brussel, Belgium) and James Kennedy and Tony Belpaeme (Plymouth University, UK)
http://www.tech.plymouth.ac.uk/SoccE/ALIZ-E/summerschool/programme2.html

H.-L. Cao, G. Van de Perre, R. Simut, C. Pop, A. Peca, D. Lefeber, and B. Vanderborght, "Enhancing my keepon robot: A simple and low-cost solution for robot platform in human-robot interaction studies," in Proceedings of the 23rd IEEE International Symposium on Robot and Human Interactive Communication, Edinburgh, UK, August 2014, pp. 555-560. 
http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6926311

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/image008%5B1%5D.jpg)
![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/image010%5B1%5D.jpg)
![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/image012%5B1%5D.jpg)

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/summerschool-1.jpg)

##Hardware

The schematic and PCB layout can be downloaded here: https://github.com/hoanglongcao/DualKeepon/tree/master/PCB

Harware connection

>Upload the Arduino firmware (new and stable). Arduino Nano with ATmega328P. Baud rate 9600.

>Connect 2 Arduinos to 2 USB ports of PC.

>Connect to the stereo output of PC.

>Connect to LEFT Keepon and RIGHT Keepon. The connector has 6 contact points: (V0,CL,DA,GND) as in the previous Hacking Keepon project, and (S+ and S-) which are the connection to Keepon’s speaker. The (X) pin is unused.

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut1.png)

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut2.jpg)

How to connect to Keepon’s speaker: Pull out the speaker connection and connect it with 2 wires to (S+ and S-).

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut3.png)

##How to use the software
Visual Studio 2013 is used. New versions should be able to run the software. The software source code can be downloaded here: https://github.com/hoanglongcao/DualKeepon/tree/master/Software-VS2013

After running the software, 2 windows appear to connect with 2 Keepons by selecting the corresponding COM Ports. Make sure that you connect the ViKeepon LEFT to the LEFT Keepon and the ViKeepon RIGHT to the right one. You can test if you connect correctly by clicking Jump or Bend button.

>In case you make a wrong connection, click close port and choose another port. Then click Open port again.
Input UserName and Gender then RUN EXPERIMENT. These data is used to create a text file with user data and his/her answers later in the experiment.

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut4.png)
 
An experiment window will appear in fullscreen mode.

Click START to begin the experiment when user is ready.

The software then loads all questions in the database. See next section How to create the database.

Click NEXT to move to the next question.

After the experiment finished, Keepon says Thank you and user can QUIT or View Log to review their answers. This log is also saved in a text file under “users” folder.

>If the same user runs again the experiment, the log file will be continued. Each experiment log is saved together with the time.

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut5.png)

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut6.png)

##Create the database

The database is organized as the following figure.  If you are using VS to run the software, the database is stored under bin/Debug/_data/

![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut7.png)
![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut8.png)
![alt tag](https://github.com/hoanglongcao/DualKeepon/blob/master/img/tut9.png)

question_xx folder is used to store the context of question number xx.

>Pictures of the left and right images must be name 1 and 2.

>question.txt: your text for the question.

>	_audio folder: store the audio files for the question. The number of files is unlimited. You need to follow the format : <1....n>_<Paul/Paula>. You should create these sound files with only left (for Paul) or right channel (for Paula).

user folder is used to store the log file (username, gender, answers)

sound files for great choice and thank you

Picture files 1 and 2 for the screen of saying goodbye.

File extensions:
>Pictures: jpg, jpef, png, gif, bmp

>Sounds: mp3, wav, wma, w4a, ogg

>If you want to add more extensions, edit the source code.

##Important notes
If you want to replace the files, keep the same names.

Feel free to modify the source code.
