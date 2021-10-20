from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import sys
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

py=sys.executable

#creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.canvas = Canvas(self,width=1366, height=768)
        self.canvas.pack()
        self.maxsize(1370, 768)
        self.minsize(1370,768)
        self.state('zoomed')
        self.title('LIBRARY MANAGEMENT SYSTEM')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
        self.resizable(0,0)
        j=0
        r=200
        for i in range(5):
            c=str(224499+r)
            Frame(self,width=1370,height =768,bg ="#"+c ).place(x=j,y=0)
            j=j+100
            r=r+1000




#calling scripts
        def a_s():
            os.system('%s %s' % (py, 'Add_Student.py'))

        def a_b():
            os.system('%s %s' % (py, 'Add_Books.py'))

        def r_b():
            os.system('%s %s' % (py, 'remove_book.py'))

        def r_s():
            os.system('%s %s' % (py, 'Remove_student.py'))

        def ib():
            os.system('%s %s' % (py, 'issueTable.py'))

        def ret():
            os.system('%s %s' % (py, 'ret.py'))

        def sea():
            os.system('%s %s' % (py,'Search.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to Logout?")
            if conf:
             self.destroy()
             os.system('%s %s' % (py, 'Main.py'))



      # def handle(event):
        #     if self.listTree.identify_region(event.x,event.y) == "separator":
        #         return "break"
        def add_user():
            os.system('%s %s' % (py, 'Reg.py'))
        def rem_user():
            os.system('%s %s' % (py, 'Rem.py'))
        def sest():
            os.system('%s %s' % (py,'Search_Student.py'))


#creating table

        self.listTree = ttk.Treeview(self,height=14,columns=('Student','Book','Issue Date','Return Date'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='ID')
        self.listTree.column("#0", width=50,minwidth=50,anchor='center')
        self.listTree.heading("Student", text='Student')
        self.listTree.column("Student", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Book", text='Book')
        self.listTree.column("Book", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Issue Date", text='Issue Date')
        self.listTree.column("Issue Date", width=125, minwidth=125,anchor='center')
        self.listTree.heading("Return Date", text='Return Date')
        self.listTree.column("Return Date", width=125, minwidth=125, anchor='center')
        self.listTree.place(x=320,y=360)
        self.vsb.place(x=1028,y=361,height=287)
        self.hsb.place(x=320,y=650,width=700)
        ttk.Style().configure("Treeview",font=('Calibri',15))

        list1 = Menu(self)
        list1.add_command(label="Student", command=a_s)
        list1.add_command(label="Book", command=a_b)

        list3 = Menu(self)
        list3.add_command(label = "Add User",command = add_user)
        list3.add_command(label = "Remove User",command = rem_user)


        self.mymenu.add_cascade(label='Add', menu=list1)
        self.mymenu.add_cascade(label = 'Admin Tools', menu = list3)

        self.config(menu=self.mymenu)

        def ser():
            if(len(self.studid.get())==0):
                messagebox.showinfo("Error", "Empty Field!")
            else:

             try:
                conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
        
                cursor = conn.cursor()
                change = int(self.studid.get())
                cursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.admission = bi.admission and b.book_no = bi.book_no and s.admission = %s",[change])
                pc = cursor.fetchall()
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4]))
                else:
                    messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
             except Error:
                #print(Error)
              messagebox.showerror("Error","something is wrong")
        def ent():
            if (len(self.bookid.get()) == 0):
                messagebox.showinfo("Error", "Empty Field!")
            else:
             try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                self.myCursor = self.conn.cursor()
                book = int(self.bookid.get())
                self.myCursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.admission = bi.admission and b.book_no = bi.book_no and b.book_no = %s",[book])
                self.pc = self.myCursor.fetchall()
                if self.pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in self.pc:
                        self.listTree.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4]))
                else:
                    messagebox.showinfo("Error", "Either Book No is wrong or The book is not yet issued")
             except Error:
                messagebox.showerror("Error", "something is wrong")

        def check():
            try:
                conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm","Do you want to register a user")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'Reg.py'))
                else:
                    #label and input box
                    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_search (3).png'))
                    img2 = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_find (6).png'))
                    img3 = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_search-student (4).png'))
                    img4 = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_search-book (4).png'))
                    img5 = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_issue-book (4).png'))
                    img6 = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_return-book (4).png'))
                    img7 = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_logout (7).png'))

                   

                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM',fg='black',bg ="#"+c,font=('Calibri', 30, 'bold'))
                    self.label3.place(x=350, y=22)
                    self.label4 = Label(self, text="ENTER STUDENT ADM",bg ="#"+c, font=('Calibri', 18, 'bold'))
                    self.label4.place(x=130, y=105)
                    self.studid = Entry(self, textvariable=self.a, width=90)
                    self.studid.place(x=405, y=110)
                    self.srt = Button(self, image = img,borderwidth = "0",highlightthickness = 0,bg ="#"+c, bd = 0,command = ser)
                    self.srt.photo = img
                    self.srt.place(x=1000, y=100)
                    self.label5 = Label(self, text="ENTER THE BOOK NO",bg ="#"+c, font=('Calibri', 18, 'bold'))
                    self.label5.place(x=130, y=175)
                    self.bookid = Entry(self, textvariable=self.b, width=90)
                    self.bookid.place(x=405, y=180)
                    self.brt = Button(self, image = img2,borderwidth = "0",highlightthickness = 0,bg ="#"+c, bd = 0,command = ent)
                    self.brt.photo = img2
                    self.brt.place(x=1000, y=165)
                    self.brt1 = Button(self,image = img3,borderwidth = "0",highlightthickness = 0,bg ="#"+c, bd = 0, command=sest)
                    self.brt1.photo =img3
                    self.brt1.place(x=240,y=250)
                    self.button = Button(self, image = img4,borderwidth = "0",highlightthickness = 0,bg ="#"+c, bd = 0, command=sea)
                    self.button.photo = img4
                    self.button.place(x=520,y=250)
                    self.brt = Button(self, image = img5,borderwidth = "0",highlightthickness = 0,bg ="#"+c, bd = 0, command=ib)
                    self.brt.photo = img5
                    self.brt.place(x=800, y=250)
                    self.brt = Button(self, image = img6,borderwidth = "0",highlightthickness = 0,bg ="#"+c, bd = 0, command=ret)
                    self.brt.photo = img6
                    self.brt.place(x=1000, y=250)
                    self.brt = Button(self, image = img7,borderwidth = "0",highlightthickness = 0,bg ="#"+c, bd = 0, command=log)
                    self.brt.photo = img7
                    self.brt.place(x=1150, y=95)
            except Error:
                messagebox.showerror("Error", "something is wrong")
        check()

MainWin().mainloop()
