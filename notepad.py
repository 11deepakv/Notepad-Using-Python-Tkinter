from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file 
    root.title('Untitled - Notepad')
    file = None
    Textarea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file=="":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        Textarea.delete(1.0, END)
        f = open(file, 'r')
        Textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()

def quitapp():
    root.destroy()

def cut():
    Textarea.event_generate("<<Cut>>")

def copy():
    Textarea.event_generate("<<Copy>>")

def paste():
    Textarea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad", "Notepad by Deepak\nApp Version: 2.1.02                 Release 1")

if __name__ == "__main__":
    root = Tk() 
    root.geometry('880x480')
    root.title('Untitled - Notepad')
    root.wm_iconbitmap('notepad.ico')
    root.configure(background="grey")

    Textarea = Text(root, font="lucida 13")
    file = None
    Textarea.pack(fill=BOTH, expand=True)

    # create a menu bar
    Menubar = Menu(root)
    FileMenu = Menu(Menubar, tearoff=0)

    # to open new file
    FileMenu.add_command(label="New", command=newfile)

    # to open already existing file
    FileMenu.add_command(label="Open", command=openfile)

    # To save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitapp)

    Menubar.add_cascade(label="File", menu=FileMenu)

    # Edit menu
    EditMenu = Menu(Menubar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    Menubar.add_cascade(label="Edit", menu=EditMenu)

    # help menu
    HelpMenu = Menu(Menubar, tearoff=0)

    HelpMenu.add_command(label='About Notepad', command=about)
    Menubar.add_cascade(label="help", menu=HelpMenu)

    root.config(menu=Menubar)

    # Adding Scrollbar
    Scroll = Scrollbar(Textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()