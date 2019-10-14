from tkinter import *
import sqlite3
main_screen = Tk()
main_screen.geometry("300x250")
main_screen.title("Movie Recommentation System")

    
 
# Set text variables
Passenger= StringVar()
Survived = StringVar()
Pclass=StringVar()
Name=StringVar()

Sex= StringVar()
Age = StringVar()
SibSP=StringVar()
Parch=StringVar()

Ticket= StringVar()
Fare = StringVar()
Cabin=StringVar()
Embarked=StringVar()

def database():
   Passengerid=Passenger.get()
   Survivedid=Survived.get()
   Pclassid=Pclass.get()
   Nameid=Name.get()
   
   Sexid=Sex.get()
   Ageid=Age.get()
   SibSPid=SibSP.get()
   Parchid=Parch.get()

   Ticketid=Ticket.get()
   Fareid=Fare.get()
   Cabinid=Cabin.get()
   Embarkedid=Embarked.get()
   
   conn = sqlite3.connect('predict.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS predict (Passenger TEXT,Survived TEXT,Pclass TEXT,Name TEXT,Sex TEXT,Age TEXT,SibSP TEXT,Parch TEXT,Ticket TEXT,Fare TEXT,Cabin TEXT,Embarked TEXT)')
   cursor.execute('INSERT INTO  predict(Passenger,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(Passengerid,Survivedid,Pclassid,Nameid,Sexid,Ageid,SibSPid,Parchid,Ticketid,Fareid,Cabinid,Embarkedid,))
   conn.commit()
 
# Set label for user's instruction
Label(main_screen, text="Please enter details below", bg="orange").pack()
Label(main_screen, text="").pack()
    
# Set username label
Passengerid_lable = Label(main_screen, text="Passenger")
Passengerid_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    
Passengerid_entry = Entry(main_screen, textvariable=Passenger)
Passengerid_entry.pack()
   
# Set password label
Survivedid_lable = Label(main_screen, text="Survived  ")
Survivedid_lable.pack()

Survivedid_entry = Entry(main_screen, textvariable=Survived)
Survivedid_entry.pack()

Pclassid_lable = Label(main_screen, text="Pclass  ")
Pclassid_lable.pack()

Pclassid_entry = Entry(main_screen, textvariable=Pclass)
Pclassid_entry.pack()


Nameid_lable = Label(main_screen, text="Name  ")
Nameid_lable.pack()

Nameid_entry = Entry(main_screen, textvariable=Name)
Nameid_entry.pack()




Sexid_lable = Label(main_screen, text="Sex")
Sexid_lable.pack()
Sexid_entry = Entry(main_screen, textvariable= Sex)
Sexid_entry.pack()

Ageid_lable = Label(main_screen, text="Age")
Ageid_lable.pack()
Ageid_entry = Entry(main_screen, textvariable= Age)
Ageid_entry.pack()




SibSPid_lable = Label(main_screen, text="SibSP ")
SibSPid_lable.pack()

SibSPid_entry = Entry(main_screen, textvariable=SibSP)
SibSPid_entry.pack()


Parchid_lable = Label(main_screen, text="Parch")
Parchid_lable.pack()

Parchid_entry = Entry(main_screen, textvariable=Parch)
Parchid_entry.pack()


Ticketid_lable = Label(main_screen, text="Ticket")
Ticketid_lable.pack()
Ticektid_entry = Entry(main_screen, textvariable= Ticket)
Ticektid_entry.pack()

Fareid_lable = Label(main_screen, text="Fare")
Fareid_lable.pack()
Fareid_entry = Entry(main_screen, textvariable= Fare)
Fareid_entry.pack()

Cabinid_lable = Label(main_screen, text="Cabin")
Cabinid_lable.pack()
Cabinid_entry = Entry(main_screen, textvariable= Cabin)
Cabinid_entry.pack()

Embarkedid_lable = Label(main_screen, text="Embarked")
Embarkedid_lable.pack()
Embarkedid_entry = Entry(main_screen, textvariable= Embarked)
Embarkedid_entry.pack()


    
Label(main_screen, text="").pack()
# Set register button
Button(main_screen, text="Submit", width=10, height=1, bg="blue",command=database).pack()


main_screen.mainloop()
