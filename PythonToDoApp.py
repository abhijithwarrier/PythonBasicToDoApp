# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI FOR A BASIC TO-DO APP

# Importing necessary packages
import tkinter as tk
from tkinter import *

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    toDoItemLabel = Label(root, text="NEW ITEM: ", bg="palevioletred4")
    toDoItemLabel.grid(row=0, column=0, padx=5, pady=5)

    root.toDoItemEntry = Entry(root, width=30, bg='snow3', textvariable=toDoItem)
    root.toDoItemEntry.grid(row=0, column=1, padx=5, pady=5)
    root.toDoItemEntry.config(foreground="black")

    addItemButton = Button(root, text="ADD ITEM", command=addItem)
    addItemButton.grid(row=0, column=2, padx=5, pady=5)

    toDoItemsListLabel = Label(root, text="ToDo LIST:", bg="palevioletred4")
    toDoItemsListLabel.grid(row=3, column=0, padx=5, pady=5)
    root.toDoItemsListBox = Listbox(root, width=55, height=20, bg='snow3')
    root.toDoItemsListBox.grid(row=4, column=0, rowspan=12, columnspan=3, padx=5, pady=5)
    # Binding onItemSelect() event to the ListBox Widget
    root.toDoItemsListBox.bind('<<ListboxSelect>>', onItemSelect)
    root.toDoItemsListBox.config(foreground="black")

    doneItemLabel = Label(root, text="DONE ITEM: ", bg="palevioletred4")
    doneItemLabel.grid(row=19, column=0, padx=5, pady=5)

    root.doneItemEntry = Entry(root, width=30, bg='snow3', textvariable=completedItem)
    root.doneItemEntry.grid(row=19, column=1, padx=5, pady=5)
    root.doneItemEntry.config(foreground="black")

    downloadButton = Button(root, text="MARK DONE", command=markDone)
    downloadButton.grid(row=19, column=2, padx=5, pady=15)

    root.notificationLabel = Label(root, bg="palevioletred4", font="'' 20")
    root.notificationLabel.grid(row=20, column=0, padx=5, pady=5, columnspan=3)

# Defining listToDoItems() to list all the to-do items that are added to the list
def listToDoItems():
    # Clearing the list widget and list before displaying the updated list
    root.toDoItemsListBox.delete(0, END)
    # Looping through to-do item list and displaying item in ListBox using insert() method
    for item in toDoItemsList:
        root.toDoItemsListBox.insert("end", item["item"])

# Defining onItemSelect() to display the ListBox Cursor Selection in the Entry widget
def onItemSelect(evt):
    # Fetching the ListBox cursor selection
    selectedItem = root.toDoItemsListBox.get(root.toDoItemsListBox.curselection())
    # Displaying the selected text from ListBox in the widget using tkinter variable
    completedItem.set(selectedItem)

# Defining addItem() function to add user-input item to the to-do list and display it in the ListBox
def addItem():
    # Fetching the user-selected to-do item from the widget using get() of tkinter variable
    newToDoItem = toDoItem.get()
    # Adding the item to the list of to-do items
    try:
        toDoItemsList.append({"item": newToDoItem, "status": 1})
        # Displaying success notification
        root.notificationLabel.config(text="New To-Do Item Added Successfully!", foreground="darkgreen")
        # Clearing the item entry widget
        root.toDoItemEntry.delete(0, END)
        listToDoItems()
    except Exception:
        # Displaying error notification
        root.notificationLabel.config(text="Error While Adding To-Do Item!", foreground="red4")

# Defining markDone() function to mark the selected item as COMPLETED
def markDone():
    # Fetching and storing the user-selected item from the widget using the get() method
    selectedItem = completedItem.get()
    try:
        # Looping through each item in the list and removing the selectedItem from the list
        for item in toDoItemsList:
            if item["item"] == selectedItem:
                toDoItemsList.pop(toDoItemsList.index(item))
        # Displaying success notification
        root.notificationLabel.config(text="Item Marked As Done!", foreground="darkgreen")
        # Clearing the item entry widget
        root.doneItemEntry.delete(0, END)
        listToDoItems()
    except Exception:
        # Displaying error notification
        root.notificationLabel.config(text="Error While Marking Item As Done!", foreground="red4")

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color, windowsize &
# disabling the resizing property
root.title("PythonBasicToDoApp")
root.config(background="palevioletred4")
root.resizable(False, False)

# Creating the tkinter variables
toDoItem = StringVar()
completedItem = StringVar()
# Creating an empty list
toDoItemsList = []

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
