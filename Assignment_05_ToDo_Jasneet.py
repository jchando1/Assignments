"""
Course Name: Foundations of Programming (Python)
Assignment Number: 5
Student Name: Jasneet Chandok
Last Update Date: 3/12/2019
"""
#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

#!/usr/bin/env python3.6


# Step 1 - Load data from a file
objInputFile= open('C:\\Users\\jchando1\\OneDrive - T-Mobile USA\\UW_2019_PythonProjects\\Assignment 05_Jasneet\\Todo.txt',"r")
strData = ""
dicRow = {}
lstTable = []

for line in objInputFile:
    strData = line.split(",")
    dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
    lstTable.append(dicRow)
objInputFile.close()

# Step 2 - Display a menu of choices to the user
while(True):

    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("******* TO DO LIST CONTAINS *******")
        for row in lstTable:
            print(row["Task"].upper() + " HAS A " + row["Priority"].upper() + " PRIORITY")
        print("*******************************************")

    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is the new task you want to add? - ")).strip()
        strPriority = str(input("What is priority does it hold? [high|low] - ")).strip()
        dicRow = {"Task":strTask.upper(),"Priority":strPriority.upper()}
        lstTable.append(dicRow)
        print("Current Data in table:")
        for dicRow in lstTable:
            print(dicRow)

        #4a Show the current items in the table
        print("******* TO DO LIST CONTAINS *******")
        for row in lstTable:
            print(row["Task"].upper() + " HAS A " + row["Priority"].upper() + " PRIORITY")
        print("*******************************************")

    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        #5a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? (name of the task)- ")
        blnItemRemoved = False #Creating a boolean Flag
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            if(strKeyToRemove.upper() == str(list(dict(lstTable[intRowNumber]).values())[0])): #the values function creates a list!
                del lstTable[intRowNumber]
                blnItemRemoved = True
            #end if
            intRowNumber += 1
        #end for loop
        #5b-Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        #5c Show the current items in the table
        print("******* TO DO LIST CONTAINS *******")
        for row in lstTable:
            print(row["Task"].upper() + " HAS A " + row["Priority"].upper() + " PRIORITY")
        print("*******************************************")
        continue #to show the menu

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        #5a Show the current items in the table
        print("******* TO DO LIST CONTAINS *******")
        for row in lstTable:
            print(row["Task"].upper() + " HAS A " + row["Priority"].upper() + " PRIORITY")
        print("*******************************************")
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open('C:\\Users\\jchando1\\OneDrive - T-Mobile USA\\UW_2019_PythonProjects\\Assignment 05_Jasneet\\Todo.txt', "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"].upper() + "," + dicRow["Priority"].upper() + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue #to show the menu
    elif (strChoice == '5'):
        break #and Exit the program

