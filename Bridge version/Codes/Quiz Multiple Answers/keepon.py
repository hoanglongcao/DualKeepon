# -*- coding: iso-8859-1 -*-

import data as d

import time
import threading
import pyglet

#####################
### KEEPON VOICES ###
#####################

def quizVoices(numberColumn,i):
    """ To play the audio files for the quiz
    Arguments:
    - numberColumn = 2 (main voices) 3 or 4 (voices for end question)
    - i --> number of the question
    """
    voice = d.robotData("quiz",numberColumn,"Keepon Voices")
    length = 0.0
    for j in range(len(voice[i])):
        if type(voice[i][j]) == long or type(voice[i][j]) == float:
            time.sleep(voice[i][j] + length)
        else:
            player = pyglet.media.Player()
            a = 'Voices/' + voice[i][j]
            sound = pyglet.resource.media(a)
            length = sound.duration
            player.queue(sound)
            player.play()

def getLength(numberColumn,i):
    """ To get the length of the audio files for the quiz
    Arguments:
    - numberColumn = 2 (main voices) 3 or 4 (voices for end question)
    - i --> number of the question
    """
    voice = d.robotData("quiz",numberColumn,"Keepon Voices")
    length = 0.0
    for j in range(len(voice[i])):
        if type(voice[i][j]) == long or type(voice[i][j]) == float:
            length = length + voice[i][j]
        else:
            a = 'Voices/' + voice[i][j]
            sound = pyglet.resource.media(a)
            length = length + sound.duration# to get length in second of the audio file
    return length

def otherVoices(window):
    """ To play the audio files for the welcome and end window
    Arguments:
    - window: Welcome window or End window
    """
    voice = d.robotData(window,2,"Keepon Voices")
    length = 0.0
    for j in range(len(voice)):
        if type(voice[j]) == long or type(voice[j]) == float:
            time.sleep(voice[j]+length)
        else:
            player = pyglet.media.Player()
            a = 'Voices/' + voice[j]
            sound = pyglet.resource.media(a)
            length = sound.duration
            player.queue(sound)
            player.play()

########################
### KEEPON MOVEMENTS ###
########################
            
def launch(window,numberColumn,keepon,*i):
    """ To launch the movements of a Keepon
    Arguments:
    - window : for keeponMove --> "quiz" or other
    - numberColumn = 2 (left) or 3 (right)
    4 or 5 (end question)
    - keepon: initialisation of the Keepon with serial (from the controller.py)
    - i: question number (useless if window != "quiz")
    """
    listeKeepon = d.robotData(window,numberColumn,"Keepon")
    listeKeeponInitialization = d.robotData("Position Initialisation",numberColumn,"Keepon")
    if window == "quiz":# i is a tuple, we have to transform it in int
        a = threading.Thread(None, keeponMove, None, (listeKeepon,listeKeeponInitialization,window,keepon,i[0]), {})
    else:
        a = threading.Thread(None, keeponMove, None, (listeKeepon,listeKeeponInitialization,window,keepon), {})
    return a

def initialize(numberColumn,keepon):
    listeKeepon = d.robotData("Position Initialisation",numberColumn,"Keepon")
    a = threading.Thread(None, keeponMove, None, (listeKeepon,"Position Initialisation",keepon), {})
    return a

def keeponMove(listeKeepon,listeKeeponInitialization,window,keepon,*i):
    """ Execute the list of instructions of the Keepon,
    contained in the parameter listeKeepon. Used in launchKeepon()
    Arguments:
    - listeKeepon : list of instructions
    - window: "quiz" or other
    - keepon: initialisation of the Keepon with serial (from the controller.py)
    - i: not mandatory following the case
    """
    if window == "quiz":
        a = i[0]# i is a tuple, we have to transform it in int
        for j in range(len(listeKeepon[a])):
            if type(listeKeepon[a][j]) == str:
                keepon.write(listeKeepon[a][j])
            else:
                time.sleep(listeKeepon[a][j])
    else:
        for j in range(len(listeKeepon)):
            if type(listeKeepon[j]) == str:
                keepon.write(listeKeepon[j])
            else:
                time.sleep(listeKeepon[j])
    for j in range(len(listeKeeponInitialization)):
        if type(listeKeeponInitialization[j]) == str:
                keepon.write(listeKeeponInitialization[j])
            else:
                time.sleep(listeKeeponInitialization[j])
