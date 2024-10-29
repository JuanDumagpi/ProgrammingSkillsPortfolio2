"""
02AlexaTellMeAJoke
"""

#Imports Tkinter
import random
from tkinter import *

setup=[] #list for the setup of the joke
punch=[] #list for the punchline of the joke


file = open('randomJokes.txt') #opens the joke txt file

#using the document, takes each line, splits it int two between the question mark
for line in file:
    setup.append("".join(line.split('?')[0])) #takes the strings at the left side of the ? and places them into the setup list
    punch.append("".join(line.split('?')[1])) #takes the string at the right side of the ? and places them into the punch list

file.close() #closes the file

#basic tkinter startup stuff
root=Tk()
root.title("A Funny Program")
root.configure(bg="#357EC7")
root.geometry("1000x150")

#Label for the Joke
label = Label(root, text="Wanna see a funny joke?", bg="#357EC7", fg="white", font=("Inter", 20, "bold"))
label.pack(padx=80, pady=20)

#button that changes the label from setuo to punchline
button = Button(root, text="Alexa, Tell me a joke.", command=lambda: [setupJoke(), buttonChange()], bg="#357EC7", fg="white")
button.pack(padx=80, pady=20)

#these functions change the buttons to alternate between asking for a joke, and asking for the punchline
def buttonChange():
        button.config(text="What's the punchline?", command=lambda: [punchJoke(), buttonReset()])
def buttonReset():
        button.config(text="Alexa, Tell me a joke.", command=lambda: [setupJoke(), buttonChange()])

#randomizes the joke
randomJoke = random.randint(0, 10)
def jokePicker():
    global randomJoke
    randomJoke = random.randint(0, len(setup)-1) #takes an integer from 0 to the number of total jokes/lines in the text file

#changes the label the the setup of the joke and strips out any line breaks
def setupJoke():
    label.config(text=str((setup[randomJoke]).strip('\n') + "?"))

#changes the label to the punchline of the joke and strips out any linebreaks
def punchJoke():
    label.config(text=punch[randomJoke].strip('\n'))
    jokePicker()
    
#executes the loop
root.mainloop()