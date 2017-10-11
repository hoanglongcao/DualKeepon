################################ EXAMPLE DOCS #########################
#http://doc.aldebaran.com/2-1/naoqi/core/albehaviormanager.html#albehaviormanager
# -*- encoding: UTF-8 -*- 

import time
import threading
import pyglet

from naoqi import ALProxy

import data as d

import pyglet

##############################################
### USED ONLY DURING DEVELOPMENT FOR TESTS ###
##############################################

def lengthTest(numberColumn):
    voice = d.robotData("End window",numberColumn,"Nao Voices")
    length = 0.0
    for i in range(len(voice)):
        if type(voice[i]) != long and type(voice[i]) != float:
            a = 'Voices/' + voice[i]
            sound = pyglet.resource.media(a)
            length = sound.duration
            print(a + " :" + str(length))
    print('\n')

def lengthQuizTest(numberColumn):
    voice = d.robotData("quiz",numberColumn,"Nao Voices")
    length = 0.0
    for i in range(len(voice)):
        for j in range(len(voice[i][j])):
            if type(voice[i][j]) != long and type(voice[i][j]) != float:
                a = 'Voices/' + voice[i]
                sound = pyglet.resource.media(a)
                length = sound.duration
                print("Question " + str(i+1) + " :" + str(length))
    print('\n')

def getLengthTest(numberColumn,i):
    """ To get the length of the audio files for the quiz window
    Arguments:
    - numberColumn: 2 (left) or 3 (right) (main voices)
    - robotIP
    - port
    - i: question number
    """
    voice = d.robotData("quiz",numberColumn,"Nao Voices")# data.py,numberColumn = 2 always
    length = 0.0
    for j in range(len(voice[i])):
        if type(voice[i][j]) == long or type(voice[i][j]) == float:
            length = length + voice[i][j]
        else:
            a = 'Voices/' + voice[i][j]
            sound = pyglet.resource.media(a)
            length = length + sound.duration
    return length

def quizVoicesTest(numberColumn,i):
    voice = d.robotData("quiz",numberColumn,"Nao Voices")
    length = 0.0
    for j in range(len(voice[i])):
        if type(voice[i][j]) == long or type(voice[i][j]) == float:
            time.sleep(voice[i][j]+length)
        else:
            player = pyglet.media.Player()
            a = 'Voices/' + voice[i][j]
            sound = pyglet.resource.media(a)
            length = sound.duration
            player.queue(sound)
            player.play()
            
def otherVoicesTest(numberColumn,window):
    voice = d.robotData(window,numberColumn,"Nao Voices")
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

##################
### NAO VOICES ###
##################
def quizVoices(numberColumn,robotIP,port,i):
    """ To play the audio files for the quiz
    Arguments:
    - numberColumn = 2 (left) or 3 (right) (main voices)
    4 or 5 (voices for end question)
    - robotIP
    - port
    - i: number of the question
    """
    aup = ALProxy("ALAudioPlayer",robotIP, port)
    voice = d.robotData("quiz",numberColumn,"Nao Voices")
    for j in range(len(voice[i])):
        if type(voice[i][j]) == long or type(voice[i][j]) == float:
            time.sleep(voice[i][j])
        else:
            a = str("/home/nao/voices/" + voice[i][j])# important!! 
            fileId = aup.loadFile(a)# take only str (and not unicode!)
            aup.play(fileId)

def getLength(numberColumn,robotIP,port,i):
    """ To get the length of the audio files for the quiz window
    Arguments:
    - numberColumn: 2 (left) or 3 (right) (main voices)
    - robotIP
    - port
    - i: question number
    WARNING: this function is not used yet because it seems causing troubles
    for the system (see next function: getLengthBis)
    """
    aup = ALProxy("ALAudioPlayer",robotIP, port)
    voice = d.robotData("quiz",numberColumn,"Nao Voices")# data.py,numberColumn = 2 always
    length = 0.0
    for j in range(len(voice[i])):
        if type(voice[i][j]) == long or type(voice[i][j]) == float:
            length = length + voice[i][j]
        else:
            a = str("/home/nao/voices/" + voice[i][j])# important!!
            fileId = aup.loadFile(a)# take only str (and not unicode!)
            time.sleep(0.1)# to let the program load the file. If not, length = 0
            length = length + aup.getFileLength(fileId)
    return length + 1
    # because getFileLength return a int which means that the number will be rounded
    # down --> underestimation of the length. We add 1 second for security

def getLengthBis(numberColumn,i):
    """ To get the length of the audio files for the quiz
    Arguments:
    - numberColumn = 2 (main voices) 3 or 4 (voices for end question)
    - i --> number of the question
    WARNING: this function has been written to replace the function getLength
    and then trying to solve the problems with the audio files.
    It improves the system but didn't resolve completely the audio files issues
    """
    voice = d.robotData("quiz",numberColumn,"Nao Voices")
    length = 0.0
    for j in range(len(voice[i])):
        if type(voice[i][j]) == long or type(voice[i][j]) == float:
            length = length + voice[i][j]
        else:
            a = 'Voices/' + voice[i][j]
            sound = pyglet.resource.media(a)
            length = length + sound.duration# to get length in second of the audio file
    return length

def otherVoices(window,numberColumn,robotIP,port):
    """ To play the audio files for the welcome and end window
    Arguments:
    - window: Welcome window or End window
    - numberColumn: 2 (left) or 3 (right) (main voices)
    - robotIP
    - port
    """
    aup = ALProxy("ALAudioPlayer",robotIP, port)
    voice = d.robotData(window,numberColumn,"Nao Voices")
    for j in range(len(voice)):
        if type(voice[j]) == long or type(voice[j]) == float:
            time.sleep(voice[j])
        else:
            a = str("/home/nao/voices/" + voice[j])# important!! 
            fileId = aup.loadFile(a)# take only str (and not unicode!)
            aup.play(fileId)

def volume(robotIP,port,level):
    """ To put the volume of the robot"""
    aup = ALProxy("ALAudioDevice",robotIP,port)
    aup.setOutputVolume(level)

#####################
### NAO MOVEMENTS ###
#####################
def launch(window,numberColumn,robotIP,port,*i):
    """ To launch the movements of a Nao
    Arguments:
    - window : for keeponMovement --> "quiz" or other
    - numberColumn : 2 (left) or 3 (right)
    4 or 5 (end question)
    - robotIP and port: initialisation of the Nao
    - i: question number (might be useless following the window)
    """
    managerProxy = ALProxy("ALBehaviorManager",robotIP,port)
    listeNao = d.robotData(window,numberColumn,"Nao")
    listeNaoInitialization = d.robotData("Position Initialisation",numberColumn,"Nao")
    if window == "quiz":# i is a tuple, we have to transform it in int
        a = threading.Thread(None, naoMove, None, (listeNao,listeNaoInitialization,window,managerProxy,i[0]), {})
    else:
        a = threading.Thread(None, naoMove, None, (listeNao,listeNaoInitialization,window,managerProxy), {})
    return a

def initialize(numberColumn,robotIP,port):
    """ To initialize the Nao"""
    #time.sleep(0.5)
    managerProxy = ALProxy("ALBehaviorManager",robotIP,port)
    listeNao = d.robotData("Position Initialisation",numberColumn,"Nao")
    a = threading.Thread(None, naoMove, None, ([],listeNao,"Position Initialisation",managerProxy), {})
    return a

def wakeUpNao(robotIP,port):
    """ To wake up the Nao"""
    managerProxy = ALProxy("ALMotion",robotIP,port)
    managerProxy.wakeUp()

def restNao(robotIP,port):
    """ To rest the Nao"""
    managerProxy = ALProxy("ALMotion",robotIP,port)
    managerProxy.rest()

def runBehavior(managerProxy,behaviorName):
    ''' Launch a behavior, if possible.
    Used in naoMove(listeNao,window,managerProxy,*i)
    Arguments:
    - managerProxy: for ALProxy
    - behaviorName: str path of the behavior name
    '''
    # Check that the behavior exists.
    if (managerProxy.isBehaviorInstalled(behaviorName)):
    # Returns true if it is a valid behavior
        # Check that it is not already running.
        if (not managerProxy.isBehaviorRunning(behaviorName)):
            # Launch behavior. This is a blocking call, use post if you do not
            # want to wait for the behavior to finish.
            managerProxy.runBehavior(behaviorName)
            # method post: http://doc.aldebaran.com/2-1/dev/naoqi/index.html#naoqi-proxy
            time.sleep(0.5)
        else:
            print (behaviorName + " is already running.")
    else:
        print (behaviorName + " Behavior not found.")
        return
    names = managerProxy.getRunningBehaviors()# Return running behaviors
    print ("Running behaviors:")
    print (names)

def naoMove(listeNao,listeNaoInitialization,window,managerProxy,*i):
    """ Execute the list of instructions of the Keepon,
    contained in the parameter listeKeepon. Used in launchKeepon()
    Arguments:
    - listeNao : list of instructions
    - window: "quiz" or other
    - managerProxy: initialisation of the Nao with proxy (from the controller.py)
    - i: not mandatory following the case
    """
    if window == "quiz":
        for j in range(len(listeNao[i[0]])):# i is a tuple, we have to transform it in int
            if type(listeNao[i[0]][j]) == str:
                path = "behaviors_master_thesis/" + listeNao[i[0]][j]
                runBehavior(managerProxy,path)
            else:
                time.sleep(listeNao[i[0]][j])
    else:
        for j in range(len(listeNao)):
            if type(listeNao[j]) == str:
                path = "behaviors_master_thesis/" + listeNao[j]
                runBehavior(managerProxy,path)
            else:
                time.sleep(listeNao[j])
    for j in range(len(listeNaoInitialization)):
        if type(listeNaoInitialization[j]) == str:
            path = "behaviors_master_thesis/" + listeNaoInitialization[j]
            runBehavior(managerProxy,path)
        else:
            time.sleep(listeNaoInitialization[j])
