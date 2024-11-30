from tkinter import *
#provides classes and functions for creating files / directories
from tkinter.filedialog import * 

master = Tk()
master.title('Memorizer')
master.minsize(700, 500)

def openFile():
    fin = askopenfile(title = 'openFile')
    if fin is not None: 
        listbox.delete(0,END) # delete item from listbox
        items = fin.readlines() #read from file
        for item in items:
            listbox.insert(END, item.strip())

# to add itens to listbox
def addItem():
    listbox.insert(END, item.get())
    item.delete(0, END) #deletes item from textbox

# to delete item from listbox
def deleteItem():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

def saveFile():
    pass


openfilebtn = Button(master, text = 'OPEN', command = openFile, width = 20)
dellistbtn = Button(master, text = 'DELETE', command = deleteItem, width = 20)
savefilebtn = Button(master, text = 'SAVE', command = None, width = 20)
addlistbtn = Button(master, text = 'ADD', command = None, width = 20)
item = Entry(master, width = 20)

openfilebtn.pack()
dellistbtn.pack()
savefilebtn.pack()
addlistbtn.pack()
item.pack()

frame = Frame(master)
scrollbar = Scrollbar(frame, orient = 'vertical')
listbox = Listbox(frame, width = 75, yscrollcommand = scrollbar.set, bg = 'red')

for i in range(1,16):
    listbox.insert(END, 'LIST ITEM  '+str(i))


listbox.pack(side = LEFT, padx = 5)
scrollbar.pack(side = RIGHT, fill = Y)
scrollbar.config(command = listbox.yview)
frame.pack()

master.mainloop()
