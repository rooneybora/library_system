from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
from PIL import Image,ImageTk
import tkinter as tk
import sys
import mysql.connector
from mysql.connector import Error
py=sys.executable


#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('libico.ico')
        self.geometry('1300x768')
        self.a = StringVar()
        self.b = StringVar()
        self.title("LIBRARY MANAGEMENT SYSTEM")
        j=0
        r=200
        for i in range(5):
            c=str(224499+r)
            Frame(self,width=1370,height =768,bg ="#"+c ).place(x=j,y=0)
            j=j+400
            r=r+1000


            root_color = "#"+c 
        self.configure(bg = root_color)



#verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error',"something is wrong,Try restarting")

        def check():
            
                    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_login.png'))
                    img2 = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\library.png'))

                    style = ttk.Style()
                    style.configure('TButton', background = root_color)
                    self.user_text = Entry(self, textvariable=self.a,font=("Calibri",16,"bold"), width=30)
                    self.user_text.insert(0,"Username...")
                    self.user_text.place(x=480, y=190)
                    self.pass_text = Entry(self, show='.', textvariable=self.b,font=("Calibri",16,"bold"),width=30)
                    self.pass_text.insert(0,"Password")
                    self.pass_text.place(x=480, y=255)
                    self.butt = Button(self,image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, bd = 0,command=chex)
                    self.butt.photo = img
                    self.butt.place(x=580,y=300)
                
                    self.img = Label(self, image = img2,borderwidth = "0",highlightthickness = 0,bg=root_color, bd = 0)
                    self.img.photo = img2
                    self.img.place(x=594,y=30)
                    


        check()

Lib().mainloop()