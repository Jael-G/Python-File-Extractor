from tkinter import *
import os
import platform
from time import sleep
import getpass


"""
File extractor by Jael Gonzalez

Select which folders do you wish to copy and press extract.
The folders will be copied into a folder called COPIES, inside
the directory where the script is being excuted.
"""

userOS = platform.platform()

user = getpass.getuser()

master = Tk()
master.iconbitmap(default='windowicon.ico') #ICON DOWNLOADED FROM GOOGLE IMAGES
master.title("File Extracter")
master.geometry("240x184")
master.resizable(height=False, width=False)

def checking_indicator():
    checking = Label()
    checking.config(text='Extracting')
    checking.grid(row=4, column=2)
    master.after(1000,lambda:var_states(checking))

def var_states(checking):
    if (Documents.get()):
        os.system(f"xcopy C:\\Users\\{user}\\Documents {os.path.dirname(os.path.realpath(__file__))}\\COPIES\\Documents /q /i /h /y /e")
    if (Downloads.get()):
        os.system(f"xcopy C:\\Users\\{user}\\Downloads {os.path.dirname(os.path.realpath(__file__))}\\COPIES\\Downloads /q /i /h /y /e")
    if (Desktop.get()):
        os.system(f"xcopy C:\\Users\\{user}\\Desktop {os.path.dirname(os.path.realpath(__file__))}\\COPIES\\Desktop /q /i /h /y /e")
    if (Pictures.get()):
        os.system(f"xcopy C:\\Users\\{user}\\Pictures {os.path.dirname(os.path.realpath(__file__))}\\COPIES\\Pictures /q /i /h /y /e")
    if (Videos.get()):
        os.system(f"xcopy C:\\Users\\{user}\\Videos {os.path.dirname(os.path.realpath(__file__))}\\COPIES\\Videos /q /i /h /y /e")

    master.after(1, checking.config(text='Files extracted'))
    master.after(2000, lambda:checking.destroy())

Label(master, text=f"System user: {user}").grid(row=0, sticky=W)

Documents = IntVar()
Checkbutton(master, text="Documents", variable=Documents).grid(row=2, sticky=W)

Downloads = IntVar()
Checkbutton(master, text="Downloads", variable=Downloads).grid(row=2, column=2 ,sticky=W)

Desktop = IntVar()
Checkbutton(master, text="Desktop", variable=Desktop).grid(row=3, sticky=W)

Pictures = IntVar()
Checkbutton(master, text="Pictures", variable=Pictures).grid(row=3,column=2, sticky=W)

Videos = IntVar()
Checkbutton(master, text="Videos", variable=Videos).grid(row=4, sticky=W)


Quit = Button(master, text='Quit', command=master.quit)
Quit.place(x=5, y=180, anchor=SW, width=230, height=30)
Check = Button(master, text='Extract', command=checking_indicator)
Check.place(x=5,y=140, anchor=SW, width=230, height=30)
mainloop()