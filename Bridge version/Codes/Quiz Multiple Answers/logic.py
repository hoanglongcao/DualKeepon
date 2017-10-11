from Tkinter import *
from PIL import Image, ImageTk

import math

import data as d
import controller as c

sheet_data_voices = d.excel_file['Datas Gendered Voices']
sheet_data_appearance = d.excel_file['Datas Identical Voices']
sheet_data_teacher_and_peer = d.excel_file['Datas Teacher and Peer']

liste_participant_data = []

def configurationCheck(dictionnary,val):
    """To check the dictionary for the General sheet"""
    count = 0
    for value in dictionnary.values():
        if value == val:
            count = count + 1
    return count

def resizePicture(a,height):
    """Resize the picture in the wanted height
    Argument:
    - a = str of the pictures
    - height = height of the picture in pixel
    """
    img = Image.open(a)
    x, y = img.size
    yNew = height
    xNew = int(yNew*float(x)/y)
    newImage = img.resize((xNew,yNew),Image.ANTIALIAS)
    newImage.save(a)
    return a

def buttonRegister(window,name,firstName,listeAge,listeGender,lineName,lineFirst):
    """Manage the button for the register window
    Store the personal data of the participant in the global variable
    liste_participant_data"""
    a = listeAge.curselection()
    b = listeGender.curselection()
    # verify if the fields are completed
    # if not, the field is put in red
    if name == "":
        lineName["bg"] = "red"
    if firstName == "":
        lineFirst["bg"] = "red"
    if a == ():
        listeAge["bg"] = "red"
    if b == ():
        listeGender["bg"] = "red"
    else:
        age = listeAge.get(a)
        gender = listeGender.get(b)
        liste_participant_data.append(name)
        liste_participant_data.append(firstName)
        liste_participant_data.append(age)
        liste_participant_data.append(gender)
        window.destroy()

def configurationGenderedVoice(listeAnswer):
    """Reorganized the results of the quiz following
    the configuration of the system (gendered voices)"""
    listeAnswerFinal = []
    numberChoiceFemale = 0
    numberChoiceMale = 0
    for j in range(len(listeAnswer)):
        listeAnswerFinal.append(listeAnswer[j][0])
        if d.role_definition == 'Left Female & Right Male':
            if listeAnswer[j][1] == 'right':
                numberChoiceMale = numberChoiceMale + 1
                listeAnswerFinal.append(1)
            else:
                numberChoiceFemale = numberChoiceFemale + 1
                listeAnswerFinal.append(0)
        elif d.role_definition == 'Left Male & Right Female':
            if listeAnswer[j][1] == 'right':
                numberChoiceFemale = numberChoiceFemale + 1
                listeAnswerFinal.append(0)
            else:
                numberChoiceMale = numberChoiceMale + 1
                listeAnswerFinal.append(1)
    return listeAnswerFinal,[numberChoiceFemale,numberChoiceMale]

def configurationIdenticalVoice(listeAnswer):
    """Reorganized the results of the quiz following
    the configuration of the system (identical voices for both robots)"""
    listeAnswerFinal = []
    numberChoiceKeepon = 0
    numberChoiceNao = 0
    for j in range(len(listeAnswer)):
        listeAnswerFinal.append(listeAnswer[j][0])
        if d.role_definition == 'Left Keepon & Right Nao':
            if listeAnswer[j][1] == 'right':
                numberChoiceNao = numberChoiceNao + 1
                listeAnswerFinal.append(0)
            else:
                numberChoiceKeepon = numberChoiceKeepon + 1
                listeAnswerFinal.append(1)
        elif d.role_definition == 'Left Nao & Right Keepon':
            if listeAnswer[j][1] == 'right':
                numberChoiceKeepon = numberChoiceKeepon + 1
                listeAnswerFinal.append(1)
            else:
                numberChoiceNao = numberChoiceNao + 1
                listeAnswerFinal.append(0)
    return listeAnswerFinal,[numberChoiceNao,numberChoiceKeepon]

def configurationTeacherPeer(listeAnswer):
    """Reorganized the results of the quiz following
    the configuration of the system (peer vs teacher robot)"""
    listeAnswerFinal = []
    numberChoiceTeacher = 0
    numberChoicePeer = 0
    for j in range(len(listeAnswer)):
        listeAnswerFinal.append(listeAnswer[j][0])
        if d.role_definition == 'Left Teacher & Right Peer':
            if listeAnswer[j][1] == 'right':
                numberChoicePeer = numberChoicePeer + 1
                listeAnswerFinal.append(0)
            else:
                numberChoiceTeacher = numberChoiceTeacher + 1
                listeAnswerFinal.append(1)
        elif d.role_definition == 'Left Peer & Right Teacher':
            if listeAnswer[j][1] == 'right':
                numberChoiceTeacher = numberChoiceTeacher + 1
                listeAnswerFinal.append(1)
            else:
                numberChoicePeer = numberChoicePeer + 1
                listeAnswerFinal.append(0)
    return listeAnswerFinal,[numberChoicePeer,numberChoiceTeacher]

def writeExcel(listeAnswer):
    """Write and save all the information (participant's data, answers
    from the quiz) in the Excel file"""
    listeConfiguration = [d.robots_definition,d.role_definition]
    if d.role_definition == 'Left Female & Right Male' or d.role_definition == 'Left Male & Right Female':
        a,b = configurationGenderedVoice(listeAnswer)
        liste = d.liste_time + listeConfiguration + liste_participant_data + a + b
        sheet_data_voices.append(liste)
    elif d.role_definition == 'Left Male & Right Male' or d.role_definition == 'Left Female & Right Female':
        a,b = configurationIdenticalVoice(listeAnswer)
        liste = d.liste_time + listeConfiguration + liste_participant_data + a + b
        sheet_data_appearance.append(liste)
    elif d.role_definition == 'Left Teacher & Right Peer' or d.role_definition == 'Left Peer & Right Teacher':
        a,b = configurationTeacherPeer(listeAnswer)
        liste = d.liste_time + listeConfiguration + liste_participant_data + a + b
        sheet_data_teacher_and_peer.append(liste)
    d.excel_file.save("Quiz_Multiple_Answers.xlsx")

#############################################
### MANAGEMENT OF THE WINDOW FOR THE QUIZ ###
#############################################

def enableAnswer(frameAnswer):
    """To enable the button of the answers"""
    for child in frameAnswer.winfo_children():
        child.configure(state='normal')

def enableBouton(buttonNext):
    """To enable the button to confirm the chosen answer
    and go the next question"""
    buttonNext["state"] = NORMAL

def nextQuestion(window,widthScreen,heightScreen,buttonNext,fieldLabel,labelPicture,answerVar,frameAnswer,listeAnswer,numberQuestion):
    """Management of the window for the quiz"""
    a = d.answers_quiz[numberQuestion][answerVar.get()-1]
    if a[1] == 'right':
        c.launchRobotQuestionEndRight(numberQuestion)
        c.playVoiceEndQuestionR(numberQuestion)
    else:
        c.launchRobotQuestionEndLeft(numberQuestion)
        c.playVoiceEndQuestionL(numberQuestion)
    listeAnswer.append(d.answers_quiz[numberQuestion][answerVar.get()-1])
    answerVar.set(0)
    numberQuestion = numberQuestion + 1
    
    for widget in frameAnswer.winfo_children():# to destroy all the answers
        widget.destroy()
        
    if numberQuestion == d.total_number_question:# end quiz
        window.destroy()
        writeExcel(listeAnswer)
    else:# next question
        fieldLabel["text"] = d.messages_quiz[numberQuestion]
        picture = resizePicture(d.list_pictures[numberQuestion],int(0.5*heightScreen))
        photo = ImageTk.PhotoImage(file = picture)
        labelPicture["image"] = photo
        for j in range(len(d.answers_quiz[numberQuestion])):# question answers
            choice = Radiobutton(frameAnswer,indicatoron = 0,text = d.answers_quiz[numberQuestion][j][0],variable = answerVar,value = j + 1,\
                                 font = ('',int(13.0/768.0*heightScreen), ""),wraplength = int(0.1*widthScreen),\
                                 command = lambda : enableBouton(buttonNext))
            choice.pack(side='left',padx=25,expand=1)
        buttonNext['state'] = "disabled"
        buttonNext['command'] = lambda : nextQuestion(window,widthScreen,heightScreen,buttonNext,\
                                                      fieldLabel,labelPicture,answerVar,frameAnswer,listeAnswer,numberQuestion)

        for child in frameAnswer.winfo_children():# to disable the frameAnswer
            child.configure(state='disable')
            
        window.update_idletasks()
        window.update()
        
        length = c.getLengthAudio(numberQuestion)
        c.playVoiceQuestion(numberQuestion)
        c.launchRobotQuestion(numberQuestion)
        
        window.after(int(1000*math.ceil(length)),enableAnswer,frameAnswer)
    window.mainloop()
