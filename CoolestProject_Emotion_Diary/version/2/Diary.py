# !/usr/bin/python3
from tkinter import *

gui = Tk()




# Mood selection variable
mood = StringVar()
desc = StringVar()

# Screen 4
def startDescriptionInputScreen(gui):
    descLabel = None
    descInput = None
    descEnter = None
    def descriptionInputHandler():
        descLabel.pack_forget()
        descInput.pack_forget()
        descEnter.pack_forget()
        labelText = str('mood = ' + mood + '. Description = ' + desc)
        tempLabel = Label(gui,
                          text = labelText)
        tempLabel.pack( anchor = W )

    var = StringVar()

    descLabel = Label(gui,
                      text = "Description:")
    descLabel.pack( anchor = W )

    descInput = Entry(gui,
                      textvariable = desc)
    descInput.pack( anchor = W )

    descEnter = Button(gui,
                       text = "Enter:",
                       command = descriptionInputHandler)
    descEnter.pack( anchor = W )
        
    

# Screen 3
def startMoodSelectionScreen(gui):
    R1 = None
    R2 = None
    R3 = None
    

    def moodSelectionHandler():
        global mood
        if var.get() == 1:
            mood = "Happy"
        elif var.get() == 2:
            mood = "Content"
        elif var.get() == 3:
            mood = "Un-Happy"
        R1.pack_forget()
        R2.pack_forget()
        R3.pack_forget()
        startDescriptionInputScreen(gui)

    var = IntVar()
    R1 = Radiobutton(gui,
                     text = ":)",
                     variable = var,
                     value = 1,
                     command = moodSelectionHandler)
    R1.pack( anchor = W )

    R2 = Radiobutton(gui,
                     text = ":|",
                     variable = var,
                     value = 2 ,
                     command = moodSelectionHandler)
    R2.pack( anchor = W )

    R3 = Radiobutton(gui,
                     text = ":(",
                     variable = var,
                     value = 3,
                     command = moodSelectionHandler)
    R3.pack( anchor = W)
    
startMoodSelectionScreen(gui)



gui.mainloop()
