"""
03StudentManager
"""
from tkinter import *
from tkinter import ttk


#list of lists that recieves the data from txt file
database = []

with open ('studentMarks.txt') as file:
    studentTotal = file.readline() #reads the first line so it's not part of the database list
    for line in file:
        data = line.strip().split(',') #takes out all the \n and separates the data into lines, and then each line into comma separated substrings
        database.append(data[0:])

#sorts by database list based on the highest total marks
sortedByTotalM = database.copy()
sortedByTotalMReverse = database.copy()
sortedByTotalM.sort(key=lambda x: int(x[2]+x[3])) #ascending
sortedByTotalMReverse.sort(key=lambda x: int(x[2]+x[3]), reverse=True) #descending

#sort by name
sortedByName = database.copy()
sortedByName.sort(key=lambda x: x[1])

root = Tk()
root.title("Student Database")

#top frame for better layout
topFrame = Frame(root)
topFrame.pack(side = TOP)
#this is the Treeview widget
myTree = ttk.Treeview(topFrame)
myTree.grid(row=0, column=0, pady=12)

#the columns for Treeview
myTree['columns']=("ID","Name","cMark","eMark","oPerc","sGrade")
columns=myTree['columns']

#the variables for Treeview
myTree.column("#0", width=0, stretch=NO)
myTree.column("ID", anchor=CENTER, width=100)
myTree.column("Name", anchor=W, width=200)
myTree.column("cMark", anchor=CENTER, width=100)
myTree.column("eMark", anchor=CENTER, width=100)
myTree.column("oPerc", anchor=CENTER, width=100)
myTree.column("sGrade", anchor=CENTER, width=100)

#the heading names for Treeview
myTree.heading("#0", text="", anchor=W)
myTree.heading("ID", text="Student Number", anchor=CENTER, command=lambda c=columns: sortTree(myTree, c, False))
myTree.heading("Name", text="Student Name", anchor=W)
myTree.heading("cMark", text="Total Coursework Marks", anchor=W)
myTree.heading("eMark", text="Exam Marks", anchor=W)
myTree.heading("oPerc", text="Overall Percentage", anchor=W)
myTree.heading("sGrade", text="Student Grade", anchor=W)

#places our database on the treeview based on name
def placeData():
    #Clears everything
    for record in myTree.get_children():
        myTree.delete(record)
    #adds everything
    global count
    count=0
    for record in sortedByName:
        if int(record[5]) >= 70:
            grade = " A"
        elif int(record[5]) < 70 and int(record[5]) >= 60:
            grade = " B"
        elif int(record[5]) < 60 and int(record[5]) >= 50:
            grade = " C"
        elif int(record[5]) < 50 and int(record[5]) >= 40:
            grade = " D"
        else:
            grade = " F"
        myTree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4] + "%", record[5] + grade))
        count+=1
            
#places our database on the treeview based on Lowest Total Marks
def placeDataMarks():
    #Clears everything
    for record in myTree.get_children():
        myTree.delete(record)
    #adds everything
    global count
    count=0
    for record in sortedByTotalM:
        if int(record[5]) >= 70:
            grade = " A"
        elif int(record[5]) < 70 and int(record[5]) >= 60:
            grade = " B"
        elif int(record[5]) < 60 and int(record[5]) >= 50:
            grade = " C"
        elif int(record[5]) < 50 and int(record[5]) >= 40:
            grade = " D"
        else:
            grade = " F"
        myTree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4] + "%", record[5] + grade))
        count+=1

#places our database on the treeview based on Highest Total Marks
def placeDataMarksR():
    #Clears everything
    for record in myTree.get_children():
        myTree.delete(record)
    #adds everything
    global count
    count=0
    for record in sortedByTotalMReverse:
        if int(record[5]) >= 70:
            grade = " A"
        elif int(record[5]) < 70 and int(record[5]) >= 60:
            grade = " B"
        elif int(record[5]) < 60 and int(record[5]) >= 50:
            grade = " C"
        elif int(record[5]) < 50 and int(record[5]) >= 40:
            grade = " D"
        else:
            grade = " F"
        myTree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4] + "%", record[5] + grade))
        count+=1

#Rearranges the treeview list based on the typed input in the entry box by Name and places that item on the very top
def filterName(*args):
    items=myTree.get_children()
    search = searchVar.get()
    for eachItem in items:
        if search in myTree.item(eachItem)['values'][1]:
            search_var=myTree.item(eachItem)['values']
            myTree.delete(eachItem)
            myTree.insert("",0,values=search_var)



#Label for total number of database entries
lenLabel=Label(topFrame, text=("Total entries in database: " + studentTotal))
lenLabel.grid(row=1, column=0)

#middle frame
midFrame = Frame(root)
midFrame.pack()

#search bar for filtering based on name
searchVar = StringVar()
searchEntry = Entry(midFrame, textvariable=searchVar)
searchEntry.grid(row=0, column=0, padx=8, pady=12)

buttonSearch=Button(midFrame, text="Filter by Name", command=filterName)
buttonSearch.grid(row=0, column=1, padx=8, pady=12)

#bottom frame
botFrame = Frame(root)
botFrame.pack()

#buttons to execute functions
button1=Button (botFrame, text="Sort By Name", command=placeData)
button2=Button (botFrame, text="Sort By Highest Total Marks", command=placeDataMarksR)
button3=Button (botFrame, text="Sort By Lowest Total Marks", command=placeDataMarks)
button1.grid(row=0, column=0, padx=8, pady=12)
button2.grid(row=0, column=1, padx=8, pady=12)
button3.grid(row=0, column=2, padx=8, pady=12)
#-----------------------------------------------------------------------------------#

#calls the method to place things into treeview
placeData()
#executes the program loop
root.mainloop()