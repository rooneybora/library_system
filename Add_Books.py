from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from PIL import Image,ImageTk
import os
import sys
py = sys.executable



#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Add Book')
        self.resizable(0,0)
        j=0
        r=200
        for i in range(5):
            c=str(224499+r)
            Frame(self,width=1370,height =768,bg ="#"+c ).place(x=j,y=0)
            j=j+100
            r=r+1000

            root_color = "#"+c
        self.configure(bg = root_color)
        self.canvas = Canvas(width=500, height=500,bg = root_color)
        self.canvas.pack()
        
        a = StringVar()
        b = StringVar()
        d= StringVar()

         
        #verifying Input
        def b_q():
            if len(b.get()) == 0 or len(d.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'YES'
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(name,book_no,availability) values (%s,%s,%s)",[b.get(),d.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Books.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Check The Details")
        #creating input box and label
        img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_remove.png'))
        style = ttk.Style()
        style.configure('TButton', background = root_color)
        Label(self, text='').pack()
        Label(self, text='Book Details:',bg="#"+c,fg='black',font=('Courier new', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='Book Name:',bg="#"+c,fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=b, width=30).place(x=170, y=182)
        Label(self, text='Book No:',bg="#"+c,fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=d, width=30).place(x=170, y=232)
        self.btn =Button(self, image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, command=b_q)
        self.btn.photo = img
        self.btn.place(x=200, y=300)
Add().mainloop()