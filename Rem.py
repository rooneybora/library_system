from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image,ImageTk
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(450, 200)
        self.minsize(450, 200)
        self.title("Remove User")
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        self.resizable(0,0)
        j=0
        r=200
        for i in range(5):
            c=str(224499+r)
            Frame(self,width=1370,height =768,bg ="#"+c ).place(x=j,y=0)
            j=j+100
            r=r+1000
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Username")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where user = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","something is wrong")

        img = ImageTk.PhotoImage(Image.open('C:\\Users\\Administrator\\Documents\\library_system\\images\\button_remove (1).png'))
        Label(self, text = "Enter Username: ",bg="#"+c,fg='black',font=('Calibri', 15, 'bold')).place(x = 5,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 180,y = 44)
        self.btn = Button(self, image = img,borderwidth = "0",highlightthickness = 0,bg="#"+c, bd = 0,command = ent)
        self.btn.photo = img
        self.btn.place(x=200, y = 90)



Rem().mainloop()