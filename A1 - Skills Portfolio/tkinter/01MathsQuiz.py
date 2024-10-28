"""
01MathsQuiz
"""
#Imports random for the RNG, and Tkinter
import random
from tkinter import *

#Tracks the progress of the player through the 10 questions
progress = 0
#This tracks the difficulty with 1 being easy, 2 being moderate, and 3 being hard
difficulty = 1

fdigit1 = random.randint(0,9)
fdigit2 = random.randint(10,99)
fdigit3 = random.randint(100,999)
sdigit1 = random.randint(0,9)
sdigit2 = random.randint(10,99)
sdigit3 = random.randint(100,999)

def randomize():
    global fdigit1
    global fdigit2
    global fdigit3
    global sdigit1
    global sdigit2
    global sdigit3
    fdigit1 = random.randint(0,9)
    fdigit2 = random.randint(10,99)
    fdigit3 = random.randint(100,999)
    sdigit1 = random.randint(0,9)
    sdigit2 = random.randint(10,99)
    sdigit3 = random.randint(100,999)

#Display Menu for selecting difficulty
def displayMenu():
    difMen = Toplevel()
    difMen.resizable(0,0)
    difMen.attributes('-topmost', 'true')
    difLb = Label(difMen, text="Choose difficulty").pack()
    eButton = Button(difMen, text = "Easy", command = lambda: [setDifficulty(1), difMen.destroy()]).pack()
    mButton = Button(difMen, text = "Medium", command = lambda: [setDifficulty(2), difMen.destroy()]).pack()
    hButton = Button(difMen, text = "Hard", command = lambda: [setDifficulty(3), difMen.destroy()]).pack()

def setDifficulty(d):
    global difficulty
    difficulty = d
    play.destroy()
    displayProblem()
    displayAnswerField()
    
def disablePlay():
    play.config(state='disabled')

#Used to determine if the question is about addition or subtraction
def decideOperation():
    global operator
    operations = ("+", "-")
    operator = random.choice(operations)
    label2.config(text=(operator))

def displayProblem():
    global life
    life = 1
    randomize()
    decideOperation()
    if difficulty == 1:
        head.config(text="Question #")
        label1.config(text= (fdigit1))
        label3.config(text= (sdigit1))
    elif difficulty == 2:
        head.config(text="Question #")
        label1.config(text= (fdigit2))
        label3.config(text= (sdigit2))
    elif difficulty == 3:
        head.config(text="Question #")
        label1.config(text= (fdigit3))
        label3.config(text= (sdigit3))
    root.update_idletasks()
        
def displayAnswerField():      
    ans.pack()
    confirm = Button (root, text="Confirm", command = isCorrect)
    confirm.pack()
    
def isCorrect():
    global difficulty
    global operator
    global score
    global life
    answer = int(ans.get().strip())
    if difficulty == 1:
        no1 = fdigit1
        no2 = sdigit1
    elif difficulty == 2:
        no1 = fdigit2
        no2 = sdigit2
    elif difficulty ==3:
        no1 = fdigit3
        no2 = sdigit3
    ansadd = no1 + no2
    ansmin = no1 - no2
    if operator == "+":
        print(ansadd)
        print(answer)
        if answer == ansadd:
            if life == 1:
                score.set(score.get() + 10)

            elif life == 0:
                score.set(score.get() + 5)

            displayProblem()
        else:
            if life == 1:
                loseLife()
                print("Try again!")
            elif life == 0:
                loseLife()
                print("Too bad!")
                displayProblem()
    elif operator == "-":
        print(ansmin)
        print(answer)
        if answer == ansmin:
            if life == 1:
                score.set(score.get() + 10)

            elif life == 0:
                sscore.set(score.get() + 5)

            displayProblem()
        else:
            if life == 1:
                loseLife()
                print("Try again!")
            elif life == 0:
                loseLife()
                print("Too bad!")
                displayProblem()
    
def loseLife():
    global life
    if life ==1:
        life -=1
    else:
        life =1
    lifeLabel.config(lifeLabel.config(text="Life: " + str(life)))
            
root =Tk()

#Tracks the score of the player.
score = IntVar()
#Less points are acquired with less life per question. 10 of 2 life, 5 if 1, 0 fails the question.
life = IntVar()

root.title("Math Quiz")
root.geometry("800x600")

head = Label(root, text="Math Quiz", font=("Inter", 24, "bold"))
head.pack()

label1 = Label(root, text="")
label1.pack()
label2 = Label(root, text="")
label2.pack()
label3 = Label(root, text="")
label3.pack()
lifeLabel = Label(root, text="Life: " + str(life))
lifeLabel.pack()
scoreLabel = Label(root, text=score.get())
scoreLabel.pack()
ans = Entry(root)

play = Button(root, text="Play", command = lambda: [displayMenu(), disablePlay()])
play.pack()










root.mainloop()