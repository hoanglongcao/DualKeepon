# -*- coding: iso-8859-1 -*-

from openpyxl import load_workbook
from Tkinter import *

import time
import serial
import threading

import data as d

########################################################################
### INITIALIZATION OF THE ROBOTS FOLLOWING THE CHOSEN CONFIGURATION ####
########################################################################
if d.robots_definition == "2 Keepon":
    import keepon as k
    keepon_right = serial.Serial(d.right_keepon_USB,9600)
    time.sleep(0.5)
    keepon_left = serial.Serial(d.left_keepon_USB,9600)
    time.sleep(0.5)
elif d.robots_definition == "2 Nao":
    import nao as n
    robot_IP_right = str(d.robotConfiguration(d.sheet_nao,"Nao","IP robot")["Right Robot IP"])
    port_right = d.robotConfiguration(d.sheet_nao,"Nao","USB Port")["Right Robot USB"]
    robot_IP_left = str(d.robotConfiguration(d.sheet_nao,"Nao","IP robot")["Left Robot IP"])
    port_left = d.robotConfiguration(d.sheet_nao,"Nao","USB Port")["Left Robot USB"]
elif d.robots_definition == "Left Keepon & Right Nao":
    import keepon as k
    import nao as n
    keepon_left = serial.Serial(d.left_keepon_USB,9600)
    time.sleep(0.5)
    robot_IP_right = str(d.robotConfiguration(d.sheet_nao,"Nao","IP robot")["Right Robot IP"])
    port_right = d.robotConfiguration(d.sheet_nao,"Nao","USB Port")["Right Robot USB"]
elif d.robots_definition == "Left Nao & Right Keepon":
    import keepon as k
    import nao as n
    keepon_right = serial.Serial(d.right_keepon_USB,9600)
    time.sleep(0.5)
    robot_IP_left = str(d.robotConfiguration(d.sheet_nao,"Nao","IP robot")["Left Robot IP"])
    port_left = d.robotConfiguration(d.sheet_nao,"Nao","USB Port")["Left Robot USB"]

########################## FOR TESTS DURING DEVELOPMENT #######################
elif d.robots_definition == "Test 1 real Nao (left)":
    import nao as n
    robot_IP_left = str(d.robotConfiguration(d.sheet_nao,"Nao","IP robot")["Left Robot IP"])
    port_left = d.robotConfiguration(d.sheet_nao,"Nao","USB Port")["Left Robot USB"]
elif d.robots_definition == "Test 1 voices Nao (left)":
    import nao as n
    robot_IP_left = str(d.robotConfiguration(d.sheet_nao,"Nao","IP robot")["Left Robot IP"])
    port_left = d.robotConfiguration(d.sheet_nao,"Nao","USB Port")["Left Robot USB"]
elif d.robots_definition == "Test 1 movements nao (left) and voices on computer":
    import nao as n
    robot_IP_left = str(d.robotConfiguration(d.sheet_nao,"Nao","IP robot")["Left Robot IP"])
    port_left = d.robotConfiguration(d.sheet_nao,"Nao","USB Port")["Left Robot USB"]
elif d.robots_definition == "Test only voices Keepon":
    import keepon as k
elif d.robots_definition == "Test only right Keepon":
    import keepon as k
    keepon_right = serial.Serial(d.right_keepon_USB,9600)
    time.sleep(0.5)
elif d.robots_definition == "Test only voices Nao on computer":
    import nao as n
##############################################################################

def wakeUpRobot():
    """To wake up the robot (for Nao)"""
    if d.robots_definition == "2 Keepon":
        return
    elif d.robots_definition == "2 Nao":
        n.wakeUpNao(robot_IP_left,port_left)
        n.wakeUpNao(robot_IP_right,port_right)
    elif d.robots_definition == "Left Keepon & Right Nao":
        n.wakeUpNao(robot_IP_right,port_right)
    elif d.robots_definition == "Left Nao & Right Keepon":
        n.wakeUpNao(robot_IP_left,port_left)
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        n.wakeUpNao(robot_IP_left,port_left)
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only voices Nao on computer" or \
         d.robots_definition == "Test only voices Keepon" or \
         d.robots_definition == "Test 1 voices Nao (left)" or\
         d.robots_definition == "Test only right Keepon":
        return
    
def restRobot():
    """To rest the robot (for Nao)"""
    if d.robots_definition == "2 Keepon":
        return
    elif d.robots_definition == "2 Nao":
        n.restNao(robot_IP_left,port_left)
        n.restNao(robot_IP_right,port_right)
    elif d.robots_definition == "Left Keepon & Right Nao":
        n.restNao(robot_IP_right,port_right)
    elif d.robots_definition == "Left Nao & Right Keepon":
        n.restNao(robot_IP_left,port_left)
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        n.restNao(robot_IP_left,port_left)
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only voices Nao on computer" or \
         d.robots_definition == "Test only voices Keepon" or \
         d.robots_definition == "Test 1 voices Nao (left)" or\
         d.robots_definition == "Test only right Keepon":
        return

def volumeRobot():
    """To fix the volume of the robot (for Nao)"""
    if d.robots_definition == "2 Keepon":
        return
    elif d.robots_definition == "2 Nao":
        n.volume(robot_IP_left,port_left,d.left_nao_volume)
        n.volume(robot_IP_right,port_right,d.right_nao_volume)
    elif d.robots_definition == "Left Keepon & Right Nao":
        n.volume(robot_IP_right,port_right,d.right_nao_volume)
    elif d.robots_definition == "Left Nao & Right Keepon":
        n.volume(robot_IP_left,port_left,d.left_nao_volume)
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        n.volume(robot_IP_left,port_left,d.left_nao_volume)
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only voices Nao on computer" or \
         d.robots_definition == "Test only voices Keepon" or \
         d.robots_definition == "Test 1 voices Nao (left)" or\
         d.robots_definition == "Test only right Keepon":
        return

def initializeRobot():
    """To initialize the robot"""
    if d.robots_definition == "2 Keepon":
        k.initialize(2,keepon_right)
        k.initialize(3,keepon_left)
        # the lines put in comments cause a crush of the system during a running
        # I don't know why
##        a = k.initialize(3,keepon_right)
##        b = k.initialize(2,keepon_left)
##        a.start()
##        b.start()
    elif d.robots_definition == "2 Nao":
        a = n.initialize(2,robot_IP_left,port_left)
        b = n.initialize(3,robot_IP_right,port_right)
        a.start()
        b.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = k.initialize(2,keepon_left)
        b = n.initialize(3,robot_IP_right,port_right)
        a.start()
        b.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = k.initialize(3,keepon_right)
        b = n.initialize(2,robot_IP_left,port_left)
        a.start()
        b.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        b = n.initialize(2,robot_IP_left,port_left)
        b.start()
    elif d.robots_definition == "Test only right Keepon":
        a = k.initialize(3,keepon_right)
        a.start()
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only voices Nao on computer" or \
         d.robots_definition == "Test only voices Keepon" or \
         d.robots_definition == "Test 1 voices Nao (left)":
        return
        
def playVoiceWelcome():
    """To play the voice of robot in the welcome window"""
    if d.robots_definition == "2 Keepon":
        a = threading.Thread(None, k.otherVoices, None, ("Welcome window",), {})
        a.start()
    elif d.robots_definition == "2 Nao":
        a = threading.Thread(None, n.otherVoices, None, ("Welcome window",2,robot_IP_left,port_left), {})
        b = threading.Thread(None, n.otherVoices, None, ("Welcome window",3,robot_IP_right,port_right), {})
        a.start()
        b.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = threading.Thread(None, k.otherVoices, None, ("Welcome window",), {})
        b = threading.Thread(None, n.otherVoices, None, ("Welcome window",3,robot_IP_right,port_right), {})
        b.start()
        a.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = threading.Thread(None, n.otherVoices, None, ("Welcome window",2,robot_IP_left,port_left), {})
        b = threading.Thread(None, k.otherVoices, None, ("Welcome window",), {})
        b.start()
        a.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 voices Nao (left)":
        a = threading.Thread(None, n.otherVoices, None, ("Welcome window",2,robot_IP_left,port_left), {})
        a.start()
##        n.otherVoices("Welcome window",2,robot_IP_left,port_left)
    elif d.robots_definition == "Test only voices Keepon":
        a = threading.Thread(None, k.otherVoices, None, ("Welcome window"), {})
        a.start()
    elif d.robots_definition == "Test only right Keepon":
        a = threading.Thread(None, k.otherVoices, None, ("Welcome window"), {})
        a.start()
    elif d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        a = threading.Thread(None, n.otherVoicesTest, None, (2,"Welcome window"), {})
        a.start()
    elif d.robots_definition == "Test only voices Nao on computer":
        a = threading.Thread(None, n.otherVoicesTest, None, (2,"Welcome window"), {})
        b = threading.Thread(None, n.otherVoicesTest, None, (3,"Welcome window"), {})
        a.start()
        b.start()
    elif d.robots_definition == "Test no voices no movements":
        return

def playVoiceEnd():
    """To play the voice of robot in the end window"""
    if d.robots_definition == "2 Keepon":
        a = threading.Thread(None, k.otherVoices, None, ("End window",), {})
        a.start()
    elif d.robots_definition == "2 Nao":
        a = threading.Thread(None, n.otherVoices, None, ("End window",2,robot_IP_left,port_left), {})
        b = threading.Thread(None, n.otherVoices, None, ("End window",3,robot_IP_right,port_right), {})
        a.start()
        b.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = threading.Thread(None, k.otherVoices, None, ("End window",), {})
        b = threading.Thread(None, n.otherVoices, None, ("End window",3,robot_IP_right,port_right), {})
        a.start()
        b.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = threading.Thread(None, n.otherVoices, None, ("End window",2,robot_IP_left,port_left), {})
        b = threading.Thread(None, k.otherVoices, None, ("End window",), {})
        a.start()
        b.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 voices Nao (left)":
        a = threading.Thread(None, n.otherVoices, None, ("End window",2,robot_IP_left,port_left), {})
        a.start()
    elif d.robots_definition == "Test only voices Keepon" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer" or \
         d.robots_definition == "Test only right Keepon":
        a = threading.Thread(None, k.otherVoices, None, ("End window",), {})
        a.start()
    elif d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        a = threading.Thread(None, n.otherVoicesTest, None, (2,"End window"), {})
        a.start()
    elif d.robots_definition == "Test only voices Nao on computer":
        a = threading.Thread(None, n.otherVoicesTest, None, (2,"End window"), {})
        b = threading.Thread(None, n.otherVoicesTest, None, (3,"End window"), {})
        a.start()
        b.start()
    elif d.robots_definition == "Test no voices no movements":
        return

def playVoiceQuestion(i):
    """To play the voice of robot during one question"""
    if d.robots_definition == "2 Keepon":
        a = threading.Thread(None, k.quizVoices, None, (2,i), {})
        a.start()
    elif d.robots_definition == "2 Nao":
        a = threading.Thread(None, n.quizVoices, None, (2,robot_IP_left,port_left,i), {})
        b = threading.Thread(None, n.quizVoices, None, (3,robot_IP_right,port_right,i), {})
        a.start()
        b.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = threading.Thread(None, k.quizVoices, None, (2,i), {})
        a.start()
        b = threading.Thread(None, n.quizVoices, None, (3,robot_IP_right,port_right,i), {})
        b.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = threading.Thread(None, n.quizVoices, None, (2,robot_IP_left,port_left,i), {})
        b = threading.Thread(None, k.quizVoices, None, (2,i), {})
        a.start()
        b.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 voices Nao (left)":
        a = threading.Thread(None, n.quizVoices, None, (2,robot_IP_left,port_left,i), {})
        a.start()
    elif d.robots_definition == "Test only voices Keepon" or \
         d.robots_definition == "Test only right Keepon":
        a = threading.Thread(None, k.quizVoices, None, (2,i), {})
        a.start()
    elif d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        a = threading.Thread(None, n.quizVoicesTest, None, (2,i), {})
        a.start()
    elif d.robots_definition == "Test only voices Nao on computer":
        a = threading.Thread(None, n.quizVoicesTest, None, (2,i), {})
        b = threading.Thread(None, n.quizVoicesTest, None, (3,i), {})
        a.start()
        b.start()
    elif d.robots_definition == "Test no voices no movements":
        return

def getLengthAudio(i):
    """To get the length of an audio file"""
    if d.robots_definition == "2 Keepon":
        return k.getLength(2,i)
    elif d.robots_definition == "2 Nao":
##        length1 = n.getLength(2,robot_IP_left,port_left,i)
##        length2 = n.getLength(3,robot_IP_right,port_right,i)
##        return max(length1,length2)
        length1 = n.getLengthBis(2,i)
        length2 = n.getLengthBis(3,i)
        return max(length1,length2)
    elif d.robots_definition == "Left Keepon & Right Nao":
        return k.getLength(2,i)
    elif d.robots_definition == "Left Nao & Right Keepon":
        return k.getLength(2,i)
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 voices Nao (left)":
        return n.getLengthBis(2,i)
    elif d.robots_definition == "Test only voices Keepon" or \
         d.robots_definition == "Test only right Keepon":
        return k.getLength(2,i)
    elif d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        return n.getLengthTest(2,i)
    elif d.robots_definition == "Test only voices Nao on computer":
        length1 = n.getLengthTest(2,i)
        length2 = n.getLengthTest(3,i)
        return max(length1,length2)
    elif d.robots_definition == "Test no voices no movements":
        return 1

def playVoiceEndQuestionL(i):
    """To play the voice of left robot at the end of a question"""
    if d.robots_definition == "2 Keepon" or \
       d.robots_definition == "Left Keepon & Right Nao":
        a = threading.Thread(None, k.quizVoices, None, (3,i), {})
        a.start()
    elif d.robots_definition == "2 Nao" or \
         d.robots_definition == "Left Nao & Right Keepon":
        a = threading.Thread(None, n.quizVoices, None, (4,robot_IP_left,port_left,i), {})
        a.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 voices Nao (left)":
        a = threading.Thread(None, n.quizVoices, None, (4,robot_IP_left,port_left,i), {})
        a.start()
    elif d.robots_definition == "Test only voices Keepon":
        a = threading.Thread(None, k.quizVoices, None, (3,i), {})
        a.start()
    elif d.robots_definition == "Test only voices Nao on computer" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        a = threading.Thread(None, n.quizVoicesTest, None, (4,i), {})
        a.start()
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only right Keepon":
        return

def playVoiceEndQuestionR(i):
    """To play the voice of right robot at the end of a question"""
    if d.robots_definition == "2 Keepon" or d.robots_definition == "Left Nao & Right Keepon":
        a = threading.Thread(None, k.quizVoices, None, (4,i), {})
        a.start()
    elif d.robots_definition == "2 Nao" or d.robots_definition == "Left Keepon & Right Nao":
        a = threading.Thread(None, n.quizVoices, None, (5,robot_IP_right,port_right,i), {})
        a.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test only voices Keepon" or\
         d.robots_definition == "Test only right Keepon":
        a = threading.Thread(None, k.quizVoices, None, (4,i), {})
        a.start()
    elif d.robots_definition == "Test only voices Nao on computer":
        a = threading.Thread(None, n.quizVoicesTest, None, (5,i), {})
        a.start()
    elif d.robots_definition == "Test no voices no movements" or\
         d.robots_definition == "Test 1 real Nao (left)" or\
         d.robots_definition == "Test 1 movements nao (left) and voices on computer" or\
         d.robots_definition == "Test 1 voices Nao (left)":
        return

def launchRobotWelcome():
    """To play the movements of the robot at the welcome window"""
    if d.robots_definition == "2 Keepon":
        a = k.launch("Welcome window",3,keepon_right)
        b = k.launch("Welcome window",2,keepon_left)
        a.start()
        b.start()
    elif d.robots_definition == "2 Nao":
        a = n.launch("Welcome window",3,robot_IP_right,port_right)
        b = n.launch("Welcome window",2,robot_IP_left,port_left)
        a.start()
        b.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = n.launch("Welcome window",3,robot_IP_right,port_right)
        b = k.launch("Welcome window",2,keepon_left)
        a.start()
        b.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = k.launch("Welcome window",3,keepon_right)
        b = n.launch("Welcome window",2,robot_IP_left,port_left)
        a.start()
        b.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        b = n.launch("Welcome window",2,robot_IP_left,port_left)
        b.start()
    elif d.robots_definition == "Test only right Keepon":
        a = k.launch("Welcome window",3,keepon_right)
        a.start()
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only voices Nao on computer" or\
         d.robots_definition == "Test 1 voices Nao (left)" or \
         d.robots_definition == "Test only voices Keepon":
        return

def launchRobotEnd():
    """To play the movements of the robot at the end window"""
    if d.robots_definition == "2 Keepon":
        a = k.launch("End window",3,keepon_right)
        b = k.launch("End window",2,keepon_left)
        a.start()
        b.start()
    elif d.robots_definition == "2 Nao":
        a = n.launch("End window",3,robot_IP_right,port_right)
        b = n.launch("End window",2,robot_IP_left,port_left)
        a.start()
        b.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = n.launch("End window",3,robot_IP_right,port_right)
        b = k.launch("End window",2,keepon_left)
        a.start()
        b.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = k.launch("End window",3,keepon_right)
        b = n.launch("End window",2,robot_IP_left,port_left)
        a.start()
        b.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        b = n.launch("End window",2,robot_IP_left,port_left)
        b.start()
    elif d.robots_definition == "Test only right Keepon":
        a = k.launch("End window",3,keepon_right)
        a.start()
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only voices Nao on computer" or\
         d.robots_definition == "Test 1 voices Nao (left)" or \
         d.robots_definition == "Test only voices Keepon":
        return

def launchRobotQuestion(i):
    """To play the movements of the robot during a question"""
    if d.robots_definition == "2 Keepon":
        a = k.launch("quiz",3,keepon_right,i)
        b = k.launch("quiz",2,keepon_left,i)
        a.start()
        b.start()
    elif d.robots_definition == "2 Nao":
        a = n.launch("quiz",3,robot_IP_right,port_right,i)
        b = n.launch("quiz",2,robot_IP_left,port_left,i)
        a.start()
        b.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = n.launch("quiz",3,robot_IP_right,port_right,i)
        b = k.launch("quiz",2,keepon_left,i)
        a.start()
        b.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = k.launch("quiz",3,keepon_right,i)
        b = n.launch("quiz",2,robot_IP_left,port_left,i)
        a.start()
        b.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        b = n.launch("quiz",2,robot_IP_left,port_left,i)
        b.start()
    elif d.robots_definition == "Test only right Keepon":
        a = k.launch("quiz",3,keepon_right,i)
        a.start()
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only voices Nao on computer" or\
         d.robots_definition == "Test 1 voices Nao (left)" or \
         d.robots_definition == "Test only voices Keepon":
        return

def launchRobotQuestionEndLeft(i):
    """To play the movements of the left robot at the end of a question"""
    if d.robots_definition == "2 Keepon":
        a = k.launch("quiz",4,keepon_left,i)
        a.start()
    elif d.robots_definition == "2 Nao":
        a = n.launch("quiz",4,robot_IP_left,port_left,i)
        a.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = k.launch("quiz",4,keepon_left,i)
        a.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = n.launch("quiz",4,robot_IP_left,port_left,i)
        a.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer":
        b = n.launch("quiz",4,robot_IP_left,port_left,i)
        b.start()
    elif d.robots_definition == "Test no voices no movements" or \
         d.robots_definition == "Test only right Keepon" or\
         d.robots_definition == "Test only voices Nao on computer" or\
         d.robots_definition == "Test 1 voices Nao (left)" or \
         d.robots_definition == "Test only voices Keepon":
        return

def launchRobotQuestionEndRight(i):
    """To play the movements of the right robot at the end of a question"""
    if d.robots_definition == "2 Keepon":
        a = k.launch("quiz",5,keepon_right,i)
        a.start()
    elif d.robots_definition == "2 Nao":
        a = n.launch("quiz",5,robot_IP_right,port_right,i)
        a.start()
    elif d.robots_definition == "Left Keepon & Right Nao":
        a = n.launch("quiz",5,robot_IP_right,port_right,i)
        a.start()
    elif d.robots_definition == "Left Nao & Right Keepon":
        a = k.launch("quiz",5,keepon_right,i)
        a.start()
    ######################## FOR TESTS DURING DEVELOPMENT #####################
    elif d.robots_definition == "Test only right Keepon ":
        a = k.launch("quiz",5,keepon_right,i)
        a.start()
    elif d.robots_definition == "Test 1 real Nao (left)" or \
         d.robots_definition == "Test 1 movements nao (left) and voices on computer" or \
         d.robots_definition == "Test no voices no movements" or\
         d.robots_definition == "Test only voices Nao on computer" or\
         d.robots_definition == "Test 1 voices Nao (left)" or \
         d.robots_definition == "Test only voices Keepon":
        return
