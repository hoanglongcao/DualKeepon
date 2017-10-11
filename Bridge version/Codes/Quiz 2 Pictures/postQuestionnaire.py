# -*- coding: iso-8859-1 -*-

from Tkinter import *

import time

import data as d
import logic as l
import controller as c

sheet_answer_questionnaire = d.excel_file['Post-quest Answers']

if d.role_definition == "Left Female & Right Male":
    right_robot = "HOMME"# homme = man
    left_robot = "FEMME"# femme = woman
elif d.role_definition == "Left Male & Right Female":
    right_robot = "FEMME"
    left_robot = "HOMME"
elif d.role_definition == "Left Teacher & Right Peer":
    right_robot = "CAMARADE"# camarade = peer
    left_robot = "PROFESSEURE"# professeure = female professor
elif d.role_definition == "Left Peer & Right Teacher":
    right_robot = "PROFESSEURE"
    left_robot = "CAMARADE"

message_robot_left = "ROBOT A GAUCHE = " + left_robot#robot à gauche=left robot
message_robot_right = "ROBOT A DROITE = " + right_robot#robot à droite=right robot

def postQuestionnaire():
    """Creates the Questionnaire window"""
    root = Tk()
    root.title('Robot Quiz - Post Questionnaire')
    widthScreen = root.winfo_screenwidth()#1366
    heightScreen = root.winfo_screenheight()#768
    root.attributes("-fullscreen", True)#full screen disavantage:toolbar disappear
    
    ######################### SCROLLBAR ON ENTIRE WINDOW ###################
    sbar = Scrollbar(root,orient="vertical")
    sbar.pack(side=RIGHT, fill=Y)
    canvas = Canvas(root,yscrollcommand=sbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    sbar.config(command=canvas.yview)
    frameCanvas = Frame(canvas)
    
    ######################### INSTRUCTIONS ###################
    instructionLabel = Label(frameCanvas,text=d.dictionary_instructions["instruction"],\
                             wraplength = widthScreen,font = ('',18, ""))
    instructionLabel.pack(fill=X,pady=int(15.0/768.0*heightScreen))
    
    ######################### OPEN QUESTIONS ###################
    newFrame = Frame(frameCanvas)
    newFrame.pack()
    entries = [Entry(newFrame,width = 70) for j in range(len(d.liste_open))]
    # width = length in characters
    # (but no limitation in the number of characters!)
    for i in range(len(d.liste_open)):
        labelOpen = Label(newFrame,text=d.liste_open[i],\
                          wraplength = widthScreen,anchor=W,font = ('',10, "bold"))
        labelOpen.pack(fill=X,pady=(int(15.0/768.0*heightScreen),0))
        entries[i].pack(fill=X)
        
    #################### MCQ (MULTIPLE ANSWERS) ##########################
    multipleVar = [[IntVar() for j in range(len(d.liste_multiple_answers))] for j in range(len(d.liste_multiple))]
    for i in range(len(d.liste_multiple)):
        labelMultiple = Label(newFrame,text=d.liste_multiple[i],\
                              wraplength = widthScreen,anchor=W,font = ('',10, "bold"))
        labelMultiple.pack(fill=X,pady=(int(15.0/768.0*heightScreen),0))
        for j in range(len(d.liste_multiple_answers[i])):
            choiceMultiple = Checkbutton(newFrame,text = d.liste_multiple_answers[i][j],\
                                         variable = multipleVar[i][j],wraplength = widthScreen,anchor=W)
            choiceMultiple.pack(fill=X)
            
    #################### MCQ (ONE ANSWER) ##########################
    singleVar = [IntVar() for j in range(len(d.liste_single))]
    for i in range(len(d.liste_single)):
        labelSingle = Label(newFrame,text=d.liste_single[i],\
                            wraplength = widthScreen,anchor=W,font = ('',10, "bold"))
        labelSingle.pack(fill=X,pady=(int(15.0/768.0*heightScreen),0))
        for j in range(len(d.liste_single_answer[i])):
            choiceSingle = Radiobutton(newFrame,text = d.liste_single_answer[i][j],\
                                       variable = singleVar[i],value = j + 1,wraplength = widthScreen,anchor=W)
            choiceSingle.pack(fill=X)
            
    #################### LIKERT LEFT ROBOT##########################
    newFrame2 = Frame(frameCanvas)
    newFrame2.pack()
    subFrame1 = Frame(newFrame2,padx=50)
    subFrame1.pack(side = "left")
    labelRobotLeft = Label(subFrame1,text=message_robot_left,font = ('',15, "bold"))
    labelRobotLeft.pack(fill=X,pady=(int(15.0/768.0*heightScreen),0))
    messageLikert = "1 = " + d.dictionary_configuration["lowest"] + ", " + \
                    str(d.dictionary_configuration["scale"]) + " = " + d.dictionary_configuration["highest"]
    labelConfig = Label(subFrame1,text=messageLikert,anchor=W)
    labelConfig.pack(fill=X,pady=(int(15.0/768.0*heightScreen),0))
    frameLikert = Frame(subFrame1)
    frameLikert.pack(fill=X)
    likertVarLeft = []
    for i in range(len(d.liste_likert)):
        subLikertVar = []
        for j in range(len(d.liste_item[i])):
            subLikertVar.append(IntVar())
        likertVarLeft.append(subLikertVar)
    for i in range(len(d.liste_likert)):
        labelLikert = Label(frameLikert,text=d.liste_likert[i],\
                            font = ('',10, "bold"),wraplength = int(widthScreen/4),anchor=W)
        labelLikert.pack(fill=X)
        for k in range(len(d.liste_item[i])):
            itemFrame = Frame(frameLikert)
            itemFrame.pack(fill=X)
            labelItem = Label(itemFrame,text=d.liste_item[i][k],anchor=W)#,wraplength = widthScreen)
            labelItem.grid(row = 0, column = 0)
            for j in range(d.dictionary_configuration["scale"]):
                choiceLikert = Radiobutton(itemFrame,text = str(j+1),\
                                           variable = likertVarLeft[i][k],value = j + 1,wraplength = widthScreen,anchor=E)
                choiceLikert.grid(row = 0, column = j+1)
            
    #################### LIKERT RIGHT ROBOT##########################
    subFrame2 = Frame(newFrame2)
    subFrame2.pack(side = "right",padx=50)
    labelRobotLeft = Label(subFrame2,text=message_robot_right,font = ('',15, "bold"))
    labelRobotLeft.pack(fill=X,pady=(int(15.0/768.0*heightScreen),0))
    messageLikert = "1 = " + d.dictionary_configuration["lowest"] + ", " + \
                    str(d.dictionary_configuration["scale"]) + " = " + d.dictionary_configuration["highest"]
    labelConfig = Label(subFrame2,text=messageLikert,anchor=W)
    labelConfig.pack(fill=X,pady=(int(15.0/768.0*heightScreen),0))
    frameLikert = Frame(subFrame2)
    frameLikert.pack(fill=X)
    likertVarRight = []
    for i in range(len(d.liste_likert)):
        subLikertVar = []
        for j in range(len(d.liste_item[i])):
            subLikertVar.append(IntVar())
        likertVarRight.append(subLikertVar)
    for i in range(len(d.liste_likert)):
        labelLikert = Label(frameLikert,text=d.liste_likert[i],\
                            font = ('',10, "bold"),wraplength = int(widthScreen/4),anchor=W)
        labelLikert.pack(fill=X)
        for k in range(len(d.liste_item[i])):
            itemFrame = Frame(frameLikert)
            itemFrame.pack(fill=X)
            labelItem = Label(itemFrame,text=d.liste_item[i][k],anchor=W)#,wraplength = widthScreen)
            labelItem.grid(row = 0, column = 0)
            for j in range(d.dictionary_configuration["scale"]):
                choiceLikert = Radiobutton(itemFrame,text = str(j+1),\
                                           variable = likertVarRight[i][k],value = j + 1,wraplength = widthScreen,anchor=E)
                choiceLikert.grid(row = 0, column = j+1)
            
    ######################### BUTTON ###################
    button = Button(frameCanvas, text=d.dictionary_instructions["button"],font = ('',10, "bold"),\
                    command = lambda : buttonSave(root,entries,multipleVar,singleVar,likertVarLeft,likertVarRight))
    button.pack(pady=10)
    
    ######################### SCROLLBAR ON ENTIRE WINDOW (END) ###################
    newFrame.update_idletasks()
    canvas.create_window((0,0), window=frameCanvas, anchor="n")#anchor position of the scrollbar
    canvas.configure(scrollregion=canvas.bbox("all"))
    root.mainloop()
               
def buttonSave(root,entries,multipleVar,singleVar,likertVarLeft,likertVarRight):
    """
    Create the button to save the answers in the Excel file
    and to destroy the window
    """
    listeEntries = []
    for entry in entries:
        listeEntries.append(entry.get())
        
    listeMulti = []
    for i in range(len(d.liste_multiple)):
        newListe = []
        for j in range(len(d.liste_multiple_answers[i])):
            newListe.append(multipleVar[i][j].get())
        listeMulti = listeMulti + newListe
        # liste of 1 or 0 to say which check button has been clicked
        
    listeSingle = []
    for i in range(len(d.liste_single)):
        value = singleVar[i].get()
        listeSingle.append(d.liste_single_answer[i][value-1])
        
    listeLikertLeft = []
    for i in range(len(likertVarLeft)):
        for j in range(len(likertVarLeft[i])):
            listeLikertLeft.append(likertVarLeft[i][j].get())

    listeLikertRight = []
    for i in range(len(likertVarRight)):
        for j in range(len(likertVarRight[i])):
            listeLikertRight.append(likertVarRight[i][j].get())

    totalListeLeft = d.liste_time + [d.robots_definition,d.role_definition] + l.liste_participant_data + \
                     listeEntries + listeMulti + listeSingle + [message_robot_left] + listeLikertLeft
    totalListeRight = d.liste_time + [d.robots_definition,d.role_definition] + l.liste_participant_data + \
                      listeEntries + listeMulti + listeSingle + [message_robot_right] + listeLikertRight
    sheet_answer_questionnaire.append(totalListeLeft)
    sheet_answer_questionnaire.append(totalListeRight)
    d.excel_file.save("Quiz_Multiple_Answers.xlsx")
    root.destroy()
