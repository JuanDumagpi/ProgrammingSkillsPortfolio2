"""
01MathsQuiz
"""
#Imports random for the RNG, and Tkinter
import random
from tkinter import *

#This tracks the difficulty with 1 being easy, 2 being moderate, and 3 being hard
difficulty = 1

#Creates the random numbers for the digits as variables
fdigit1 = random.randint(0,9)
fdigit2 = random.randint(10,99)
fdigit3 = random.randint(100,999)
sdigit1 = random.randint(0,9)
sdigit2 = random.randint(10,99)
sdigit3 = random.randint(100,999)
            
#creates the root window, along with the title and background color
root =Tk()
root.title("Math Quiz")
root.configure (bg="#357EC7")

#Tracks the score of the player.
score = IntVar()
#Less points are acquired with less life per question. 10 of 2 life, 5 if 1, 0 fails the question.
life = IntVar()
#Tracks the progress of the player through the 10 questions
prog = IntVar()

#When this function is called, it generates a new random number for each variable
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
    difMen = Toplevel() #creates a window on the top
    difMen.resizable(0,0) #prevents resizing
    difMen.configure (bg="#357EC7") #changes the background color
    difMen.attributes('-topmost', 'true') #makes sure this window is always in front
    difLb = Label(difMen, text="Choose difficulty", bg="#357EC7", fg="white").pack() #makes a label for selecting difficulty
    #these buttons calls the setDifficulty() function as well as closes the toplevel window
    eButton = Button(difMen, text = "Easy", command = lambda: [setDifficulty(1), difMen.destroy()], bg="#357EC7", fg="white").pack()
    mButton = Button(difMen, text = "Medium", command = lambda: [setDifficulty(2), difMen.destroy()], bg="#357EC7", fg="white").pack()
    hButton = Button(difMen, text = "Hard", command = lambda: [setDifficulty(3), difMen.destroy()], bg="#357EC7", fg="white").pack()

def setDifficulty(d):
    global difficulty
    score.set(0) #resets the score
    difficulty = d #sets the difficulty according to which button was pressed in the difMen window
    play.destroy() #deletes the Play button
    displayProblem() #starts the quiz
    displayAnswerField() #adds the input entry box for answers
    
def disablePlay():
    play.config(state='disabled') #disables the play button while difMen window is active

#Used to determine if the question is about addition or subtraction
def decideOperation():
    global operator
    operations = ("+", "-") #set of available operators
    operator = random.choice(operations) #picks one of the two operators in the operations set
    label2.config(text=(operator)) #changes the label2 operator the current operator being used

def displayProblem():
    life.set(1) #resets the life to 1
    lifeLabel.config(text=("Life: " + str(life.get()))) #changes the life counter in its label
    randomize() #calls the randomize function to randomize the numbers in each digit
    decideOperation() #calls the decideOperation function to randomize the operation in this question
    if difficulty == 1: #if the difficulty is set to easy, it uses only 1 digit for each number
        label1.config(text= (fdigit1))
        label3.config(text= (sdigit1))
    elif difficulty == 2: #if the difficulty is set to moderate, it uses only 2 digits for each number
        label1.config(text= (fdigit2))
        label3.config(text= (sdigit2))
    elif difficulty == 3: #if the difficulty is set to hard, it uses 3 digits for each number
        label1.config(text= (fdigit3))
        label3.config(text= (sdigit3))
    displayResults() #calls the displayResults function to check if the quiz is over, or the next question is shown
    root.update_idletasks() #updates the root window

def displayResults():
    if prog.get() < 10: #if this isn't the last question, move to the next question
        prog.set(prog.get() + 1)
        progress.config(text=(str(prog.get()))+" of 10")
    else: #if this is the last question:
        confirm.destroy() #remove the confirm button
        ans.grid_remove() #hide the text field
        results = Toplevel() #creates a top level window showing the results of the quiz
        results.title("Results")
        results.geometry('400x50')
        results.resizable(0,0)
        results.configure (bg="#357EC7")
        endscore = Label(results, text=("Your score is " + str(score.get()) + " of 100"), bg="#357EC7", fg="white") #label showing your score out of 100
        endscore.pack() #packs in the endscore label
        #this creates ta button that prompts if the player wants to play again, to show the difficulty menu, reset the progress label, and exit this top level window
        tryAgain = Button(results, text = "Try Again?", command = lambda: [displayMenu(), results.destroy(), prog.set(0)], bg="#357EC7", fg="white").pack()
        
def displayAnswerField():  
    global confirm #makes this button accessible by other functions
    ans.grid(row = 2, column = 1) #places the text field for answers
    confirm = Button (root, text="Confirm", command = isCorrect, bg="#357EC7", fg="white") #creates the button for checking answers
    confirm.grid(row = 5, column = 1, padx = 20, pady = 20) #places the button on the specified area on the grid
    
def isCorrect():
    global difficulty
    global operator
    answer = int(ans.get().strip()) #takes the input from the text field and erases any spaces!
    #checks the difficulty level, and uses the appropriate number of digits
    if difficulty == 1:
        no1 = fdigit1
        no2 = sdigit1
    elif difficulty == 2:
        no1 = fdigit2
        no2 = sdigit2
    elif difficulty ==3:
        no1 = fdigit3
        no2 = sdigit3
    ansadd = no1 + no2 #variable if using sum
    ansmin = no1 - no2 #variable if using difference
    if operator == "+": #checks the current operator,
        if answer == ansadd: #then checks if the user input matches the sum of the 2 numbers
            getPoint() #gives points based on remaining life
            displayProblem() #moves to the next problem
        else: #if you're wrong, you lose a life
            loseLife()
    elif operator == "-": #checks, the current operator,
        if answer == ansmin: #then checks if the user input matches the difference of the 2 numbers
            getPoint() #gives points based on remaining life
            displayProblem() #moves to the next problem
        else: #if you're wrong, you lose a life
            loseLife()
    ans.delete(0, 'end') #clears the entry box after pressing the button

def getPoint():
    if life.get() == 1: #if you have 1 life, you get 10 points for scoring
        score.set(score.get() + 10) 
        scoreLabel.config(text =("Score: " + str(score.get()))) #updates the score label
    elif life.get() == 0: #if you have 0 lives, you get 10 points for scoring
        score.set(score.get() + 5)
        scoreLabel.config(text =("Score: " + str(score.get()))) #updates the score label
        life.set(1) #resets your life to 1 for the next question
    
def loseLife():
    if life.get() == 1: #if you have 1 life, you lose 1 life
        life.set(life.get() - 1)
        lifeLabel.config(text=("Life: " + str(life.get())))
    else: #if you have 0 lives, it resets to 1 and moves on to the next question
        life.set(life.get() + 1)
        displayProblem()


head = Label(root, text="Math Quiz", font=("Inter", 24, "bold"), bg="#357EC7", fg="white") #shows the label in big letters on top
head.grid(row = 0, column=0, columnspan=3, padx = 40, pady = 40) #places the label in its proper area in the grid

label1 = Label(root, font=("Inter", 16, "bold"), text="", bg="#357EC7", fg="white") #label for the first digit
label1.grid(row = 1, column = 0, padx = 20, pady = 20) 

label2 = Label(root, font=("Inter", 20, "bold"), text="", bg="#357EC7", fg="white") #label for the 2nd digit
label2.grid(row = 1, column = 1, padx = 20, pady = 20)

label3 = Label(root, font=("Inter", 16, "bold"), text="", bg="#357EC7", fg="white") #label for the 3rd digit
label3.grid(row = 1, column = 2, padx = 20, pady = 20)

lifeLabel = Label(root, font=("Inter", 16, "bold"), text=("Life: " + str(life.get())), bg="#357EC7", fg="white") #label for the life
lifeLabel.grid(row = 3, column = 1, padx = 20, pady = 20)

scoreLabel = Label(root, font=("Inter", 16, "bold"), text=("Score: " + str(score.get())), bg="#357EC7", fg="white") #label for the score
scoreLabel.grid(row = 4, column = 1, padx = 20, pady = 20)

ans = Entry(root) #entry field for inputting the answers, not placed until the quiz starts

#creates and places the Play button which shows the difficulty menu and disables this button
play = Button(root, font=("Inter", 16, "bold"), text="Play", command = lambda: [displayMenu(), disablePlay()], bg="#357EC7", fg="white")
play.grid(row = 5, column = 1, padx = 20, pady = 20)

#creates the label for the progress of the quiz, to show which question you are on
progress= Label(root, text=(str(prog.get()))+" of 10", bg="#357EC7", fg="white")
progress.grid(row = 6, column = 0, columnspan = 3)

#runs the program loop
root.mainloop()