"""
03StudentManager
"""
from tkinter import *
from tkinter import ttk
database = []

with open ('studentMarks.txt') as file:
    studentTotal = file.readline() #reads the first line so it's not part of the database list
    for line in file:
        data = line.strip().split(',') #takes out all the \n and separates the data into lines, and then each line into comma separated substrings
        database.append(data[0:])




root = Tk()
root.title("Student Database")
root.geometry("800x600")

myTree = ttk.Treeview(root)

myTree['columns']=("ID","Name","cMark","eMark","oPerc","sGrade")
columns=myTree['columns']

myTree.column("#0", width=0, stretch=NO)
myTree.column("ID", anchor=CENTER, width=100)
myTree.column("Name", anchor=W, width=200)
myTree.column("cMark", anchor=CENTER, width=100)
myTree.column("eMark", anchor=CENTER, width=100)
myTree.column("oPerc", anchor=CENTER, width=100)
myTree.column("sGrade", anchor=CENTER, width=100)

myTree.heading("#0", text="", anchor=W)
myTree.heading("ID", text="Student Number", anchor=CENTER, command=lambda c=columns: sortTree(myTree, c, False))
myTree.heading("Name", text="Student Name", anchor=W)
myTree.heading("cMark", text="Total Coursework Marks", anchor=W)
myTree.heading("eMark", text="Exam Marks", anchor=W)
myTree.heading("oPerc", text="Overall Percentage", anchor=W)
myTree.heading("sGrade", text="Student Grade", anchor=W)

#places our database on the treeview
def placeData():
    #adds everything
    global count
    count=0
    for record in cMarkSort:
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
                 

    
myTree.pack(pady=20)

#Rearranges the treeview list based on the typed input in the entry box by Name
def filterName(*args):
    items=myTree.get_children()
    search = searchVar.get()
    for eachItem in items:
        if search in myTree.item(eachItem)['values'][1]:
            search_var=myTree.item(eachItem)['values']
            myTree.delete(eachItem)
            myTree.insert("",0,values=search_var)

searchFrame = LabelFrame (root, text = "Filter by Name")
searchFrame.pack(padx=10, pady=10)
searchVar = StringVar()
searchEntry = Entry(searchFrame, textvariable=searchVar)
searchVar.trace("w", filterName)
searchEntry.pack (pady=20, padx=20, side = LEFT)
#-----------------------------------------------------------------------------------#


placeData()
root.mainloop()