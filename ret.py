from tkinter import *
from tkinter import messagebox
import os,sys
from PIL import Image,ImageTk
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
py = sys.executable


class ret(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title("Return")
        self.maxsize(420,280)
        self.canvas = Canvas(width=500, height=417)
        self.canvas.pack()
        self.cal = 0
        self.resizable(0,0)
        j=0
        r=200
        for i in range(5):
            c=str(224499+r)
            Frame(self,width=1370,height =768,bg ="#"+c ).place(x=j,y=0)
            j=j+100
            r=r+1000
        a = StringVar()

        def qui():
            if len(a.get()) == '0':
                messagebox.showerror("Error","Please Enter The Book No")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_no from issue_book where return_date = '' and book_no = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_no = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_no = %s", [idate,a.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Succesfully Returned')
                        d = messagebox.askyesno("Confirm", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'ret.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except Error:
                    messagebox.showerror("Error","something is wrong")

        img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_return-book (4).png'))
        Label(self, text='Return Book', fg='red',font=('Calibri', 35, 'bold')).pack()
        Label(self, text='Enter Book No',bg="#"+c, font=('Calibri', 15, 'bold')).place(x=20, y=120)
        Entry(self, textvariable=a, width=40).place(x=165, y=124)
        self.btn =Button(self, image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, bd = 0, command=qui)
        self.btn.photo = img
        self.btn.place(x=180, y=180)
ret().mainloop()