from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import os
import datetime
from tkcalendar import DateEntry

root=Tk()
root.title("G.H.RAISONI POLYTECHNIC")
root.configure(bg='#00d8d6')



TB=Label(root,text="STUDENT RECORD SYSTEM",font=("cambria",15,"bold"),fg="Red" ).place(x=160,y=40,h=45,w=270)

user=StringVar()
pswd=StringVar()

ED=Label(root,text="Enter Student Department",font=("cambria",12,"bold"),fg="Black").place(x=30,y=120,h=30,w=210)
t1=Entry (root,w=30,relief=GROOVE,textvariable=user)
t1.place(x=260,y=120,h=25,w=210)

EE=Label(root,text="Enter Student Enrollment",font=("cambria",12,"bold"),fg="Black").place(x=30,y=180,h=30,w=210)
t2=Entry(root,w=30,relief=GROOVE,textvariable=pswd)
t2.place(x=260,y=180,h=25,w=210)


def dept():
    
    t=("1711760001")
    tg=("2")
    th=("1711760003")
    td=("1711760004")
    tk=("1711760005")
    tv=("1711760006")
    ts=("1711760007")
    ta=("1711760008")
    tz=("1711760009")
    tl=("1711760010")
    tp=("1711760011")
    tj=("1711760012")
    tm=("1711760013")
    
    s1=t1.get()
    s2=t2.get()   
    
    if (s1=="Computer" and s2==t):
       so(),
    elif (s1=="Co" and s2==tg):
      go() ,
    elif (s1=="Computer" and s2==th):
       ho()
    elif (s1=="Computer" and s2==td):
       do()
    elif (s1=="Computer" and s2==tk):
       ko()
    elif (s1=="Computer" and s2==tv):
       vo()
    elif (s1=="Computer" and s2==ts):
       so()
    elif (s1=="Computer" and s2==ta):
       ao()
    elif (s1=="Computer" and s2==tz):
       zo()
    elif (s1=="Computer" and s2==tl):
       lo()
    elif (s1=="Computer" and s2==tp):
       po()
    elif (s1=="Computer" and s2==tj):
       jo()
    elif (s1=="Computer" and s2==tm):
       mo()
    elif (s1 == "IT" and s2 == tm):
       io()
    else:
         messagebox.showerror("Error","Please Enter Valid Department")

 



def so():
    #l=["  Name : Simran Sharma","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]  
    str(root.nm.set("Simran Sharma"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))

    #p1.set("login.jpg")
    im = PhotoImage(file='login.jpg')
    lab = Label(root)
    lab['image'] = im
    im.image = im
    lab.pack(side=RIGHT, padx=25, pady=35)


def go():
  
    str(root.nm.set("Gunvant Chandatre"))
    str(root.mb.set("8989787621"))
    str(root.br.set("Computer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Broooo"))

    #def im():
    img = PhotoImage(file='bold.png')
    label = Label(root , image=img)
    label['image'] = img
    img.image = img
    label.pack(side=RIGHT , padx=25 ,pady=35)





def ho():

    str(root.nm.set("Harshal Hartalkar"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
    
def do():
    ''''l=["  Name : Gayatri Duakhe" ," Mobile: 1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]'''

            
    str(root.nm.set("Gayatri Duakhe"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))

def ko():
    '''l=["  Name : Shivani Kulkarni","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Shivani Kulkarni"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))

def vo():
    '''l=["  Name : Varad Sakhre","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Varad Sakhre"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
def bo():
    '''l=["  Name : Sourav Patil","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Sourav Patil"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
def ao():
    '''l=["  Name : Arshiya Shaikh","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Arshiya Shaikh"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
def zo():
    '''l=["  Name : Sushant Zope","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Sushant Zope"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
def lo():
    '''l=["  Name : Lokesh Bhortake","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Lokesh Bhortake"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
def po():
    '''l=["  Name : Ganesh Patil","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Ganesh Patil"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
def jo():
    '''l=["  Name : Hardik Jain","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Hardik Jain"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
def mo():
    '''l=["  Name : Shruti Badgujar","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Shruti Badgujar"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))

def io():
    '''l=["  Name : Shruti Badgujar","  Mobile:1234567891","  Computer", "  75%", " Shiv Colony Jalgaon", "  Member"]
    for i in l:
             print("\n",i)'''
    str(root.nm.set("Chaitali Bornare"))
    str(root.mb.set("1188776611"))
    str(root.br.set("Compuer"))
    str(root.pr.set("75%"))
    str(root.ad.set("Jalgaon"))
    str(root.pt.set("Member"))
       



root.nm=StringVar()
root.mb=StringVar()
root.br=StringVar()
root.pr=StringVar()
root.ad=StringVar()
root.pt=StringVar()


    
B1=Button(root,text="Go",command=dept,background = "white", fg = "red").place(x=480,y=150)




NL=Label(root,text="Name",font=("cambria",12,"bold"),fg="Black").place(x=30,y=260,h=30,w=210)
e1=Entry(root,relief=GROOVE,textvariable=root.nm).place(x=270,y=260,h=25,w=210)

ML=Label(root,text="Mobile",font=("cambria",12,"bold"),fg="Black").place(x=30,y=310,h=30,w=210)
e2=Entry(root,relief=GROOVE,textvariable=root.mb).place(x=270,y=310,h=25,w=210)

BL=Label(root,text="Branch",font=("cambria",12,"bold"),fg="Black").place(x=30,y=360,h=30,w=210)
e3=Entry(root,relief=GROOVE,textvariable=root.br).place(x=270,y=360,h=25,w=210)

PL=Label(root,text="Percentage",font=("cambria",12,"bold"),fg="Black").place(x=30,y=410,h=30,w=210)
e4=Entry(root,w=32,relief=GROOVE,textvariable=root.pr).place(x=270,y=410,h=25,w=210)

AL=Label(root,text="Address",font=("cambria",12,"bold"),fg="Black").place(x=30,y=460,h=30,w=210)
e5=Entry(root,w=32,relief=GROOVE,textvariable=root.ad).place(x=270,y=460,h=25,w=210)

CL=Label(root,text="Post",font=("cambria",12,"bold"),fg="Black").place(x=30,y=510,h=30,w=210)
e6=Entry(root,w=32,relief=GROOVE,textvariable=root.pt).place(x=270,y=510,h=25,w=210)





root.resizable(0,0)
root.geometry("700x580")
root.mainloop()
