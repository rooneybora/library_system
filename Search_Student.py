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
        self.title("Search Student")
        self.maxsize(850,560)
        self.canvas = Canvas(width=1366, height=768)
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
        l1=Label(self,text="Search Student",bg="#"+c, font=("Calibri",20,'bold')).place(x=290,y=40)
        l = Label(self, text="Search By",bg="#"+c, font=("Calibri", 15, 'bold')).place(x=180, y=100)


        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("","end",text = row[0], values = (row[1],row[2],row[3]))


        def ge():
            if (len(self.entry.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(self.combo.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+self.combo.get())
            elif self.combo.get() == 'Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    name = self.entry.get()
                    self.mycursor.execute("Select * from student where name like %s",['%'+name+'%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's","Name not found")
                except Error:
                    messagebox.showerror("Error", "something is wrong")
            elif self.combo.get() == 'Admission':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    id = self.entry.get()
                    self.mycursor.execute("Select * from student where admission like %s", ['%' +id+ '%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Admission not found")
                except Error:
                    messagebox.showerror("Error", "something is wrong")

        img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_search (3).png'))
        self.b= Button(self,image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, bd = 0,command= ge )
        self.b.photo = img
        self.b.place(x=380,y=170)
        self.combo=ttk.Combobox(self,textvariable=g,values=["Name","Admission"],width=40,state="readonly")
        self.combo.insert(0,"Search By?")
        self.combo.place(x = 310, y = 105)
        self.entry = Entry(self,textvariable=f,width=43)
        self.entry.place(x=310,y=145)
        self.la = Label(self, text="Enter",bg = "#"+c, font=("Calibri", 15, 'bold')).place(x=180, y=140)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Student Name', 'admission', 'Form'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Student ID', anchor='w')
        self.listTree.column("#0", width=100, anchor='w')
        self.listTree.heading("Student Name", text='Student Name')
        self.listTree.column("Student Name", width=200, anchor='center')
        self.listTree.heading("admission", text='admission')
        self.listTree.column("admission", width=200, anchor='center')
        self.listTree.heading("Form", text='Form')
        self.listTree.column("Form", width=200, anchor='center')
        self.listTree.place(x=40, y=240)
        self.vsb.place(x=748,y=240,height=287)
        ttk.Style().configure("Treeview", font=('Calibri', 15))

Search().mainloop()