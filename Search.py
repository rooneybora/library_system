from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import os,glob
import mysql.connector
from mysql.connector import Error

class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Book")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500)
        self.canvas.pack()
        self.iconbitmap(r'libico.ico')
        self.resizable(0,0)
        j=0
        r=200
        for i in range(5):
            c=str(224499+r)
            Frame(self,width=1370,height =768,bg ="#"+c ).place(x=j,y=0)
            j=j+100
            r=r+1000

        
        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where name LIKE %s",['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","something is wrong")
            elif g.get() == 'Book No':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where book_no LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Book No Name not found")
                except Error:
                    messagebox.showerror("Error","something is wrong")
            elif g.get() == 'Book Id':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where book_id LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","something is wrong")
        img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_search (3).png'))
        b=Button(self,image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, bd = 0,command=ge)
        b.photo = img
        b.place(x=460,y=140)
        combo=ttk.Combobox(self,textvariable=g,values=["Book Name","Book No","Book Id"],width=40,state="readonly").place(x = 180, y = 100)
       

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"

        en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self, text="Enter",bg="#"+c, font=("Calibri", 15, 'bold')).place(x=100, y=150)

        l1=Label(self,text="Search Library",bg="#"+c, font=("Calibri",20,'bold')).place(x=290,y=20)
        l = Label(self, text="Search By",bg="#"+c, font=("Calibri", 15, 'bold')).place(x=60, y=96)


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book No', 'Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Book ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book No", text='Book No')
        self.listTree.column("Book No", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=763,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Calibri', 15))

Search().mainloop()