# DualKeepon
A portable system with My Keepon robots to study user preferences using a pairwise comparison method

##Hacking MyKeepon

A tutorial of hacking MyKeepon robot can  be found in our website: http://probo.vub.ac.be/HackingKeepon/

##Hardware connection
Upload the Arduino firmware (new and stable). Arduino Nano with ATmega328P. Baud rate 9600.

Connect 2 Arduinos to 2 USB ports of PC.

Connect to the stereo output of PC.

Connect to LEFT Keepon and RIGHT Keepon. The connector has 6 contact points: (V0,CL,DA,GND) as in the previous Hacking Keepon project, and (S+ and S-) which are the connection to Keepon’s speaker. The (X) pin is unused.

How to connect to Keepon’s speaker: Pull out the speaker connection and connect it with 2 wires to (S+ and S-).

##How to use the software
Visual Studio 2013 is used. New versions should be able to run the software.

After running the software, 2 windows appear to connect with 2 Keepons by selecting the corresponding COM Ports. Make sure that you connect the ViKeepon LEFT to the LEFT Keepon and the ViKeepon RIGHT to the right one. You can test if you connect correctly by clicking Jump or Bend button.

>In case you make a wrong connection, click close port and choose another port. Then click Open port again.
Input UserName and Gender then RUN EXPERIMENT. These data is used to create a text file with user data and his/her answers later in the experiment.
 
An experiment window will appear in fullscreen mode.

Click START to begin the experiment when user is ready.

The software then loads all questions in the database. See next section How to create the database.

Click NEXT to move to the next question.

After the experiment finished, Keepon says Thank you and user can QUIT or View Log to review their answers. This log is also saved in a text file under “users” folder.

>If the same user runs again the experiment, the log file will be continued. Each experiment log is saved together with the time.

##Create the database

The database is organized as the following figure.  If you are using VS to run the software, the database is stored under bin/Debug/_data/
   
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
