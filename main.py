from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

ff = ['NAME', 'MOVE', 'VAR']

# file opening process
def open(): 
    global filename
    fn = filedialog.askdirectory()
    for i in os.listdir(fn):
        if i == 'game.txt':
            with open(str(fn) + '/game.txt') as gf: #gamefile
                gfn = gf.read()
                gfnd = gfn.split('', ':')
                for data in gfnd():
                    if data in ff:
                        pass
                        


def credit():
    ct = Toplevel(root)
    ct.geometry('200x300')
    cb = ttk.Label(ct, text='MGMAKER', font='arial')
    cb2 = ttk.Label(ct, text='a - 0.1v, Made by Taegyunyoo9')
    img = Image.open('Graphics/Logo.png')
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)
    cbimg = Label(ct, image=photo)
    cbimg.image = photo
    cb.pack()
    cb2.pack()
    cbimg.pack()

def new2():
    tn.withdraw()
    tv = tb.get()
    tp = filedialog.askdirectory()
    global td
    td = os.path.join(tp, tv)
    os.mkdir(td)

def new():
    global tn
    tn = Toplevel(root)
    tn.geometry('300x100')
    tl = ttk.Label(tn, text='Enter project name.')
    tl2 = ttk.Label(tn, text='(if a tab appears, choose the directory)')
    global tb
    tb = ttk.Entry(tn)
    tb2 = ttk.Button(tn, text='Enter', command=new2)
    tl.pack()
    tl2.pack()
    tb.pack()
    tb2.pack()

# def ko():
#     la.withdraw()
#     global lang
#     lang = 'ko'

# def en():
#     la.withdraw()
#     global lang
#     lang = 'en'
    
root = Tk()
root.iconbitmap(default='Graphics/Logo.ico') 
filename = None
menubar = Menu(root)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label='Open', command=open)
menu1.add_command(label='New', command=new)
menu1.add_command(label='Credit', command=credit)
menubar.add_cascade(label='Edit', menu=menu1)
root.config(menu=menubar)
root.mainloop()

