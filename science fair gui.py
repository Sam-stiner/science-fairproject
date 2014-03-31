import Tkinter
from Tkinter import Label
from Tkinter import Entry
import tkMessageBox

top = Tkinter.Tk()

def earth():
    global massbox
    global vilositybox
    global distancebox
    global timebox
    
    label1 = Label (top, text="what is the mass of the satilite (kg)").grid(row=2)
    massbox = Entry (top, bd=5)
    massbox.grid (row=2, column=2, columnspan=3)
    
    label2=Label (top, text="what is the vilosity of the satilite (m/s)").grid(row=3)
    vilositybox = Entry (top, bd =5)
    vilositybox.grid (row=3, column=2, columnspan=3)
    
    label3 = Label (top, text="how far is the satilte from earth (km)").grid (row=4)
    distancebox = Entry (top, bd=5)
    distancebox.grid (row=4, column=2, columnspan=3)
    
    label4 = Label (top, text="how long has the satilite been in orbit").grid(row=5)
    timebox = Entry (top, bd=5)
    timebox.grid (row=5, column=2, columnspan=3)
    
    o = Tkinter.Button (top, text="next", command  = earth1).grid(row=5, column=7)

def earth1():
    mass = float (Entry.get(massbox))
    vilosity = float (Entry.get(vilositybox))
    distance = float (Entry.get(distancebox))
    time = float (Entry.get (timebox))
   
    radius = distance+695500 
    force = (mass*vilosity**2)/radius
    a1 = Label(top, text =  'the net cintripital force is').grid(row = 7)
    print f

a = Tkinter.Button (top, text = "obgect in orbit around earth", command = earth).grid (row = 1, column = 1)

top.mainloop()

===================
