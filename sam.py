import Tkinter
from Tkinter import Label
from Tkinter import Entry
import tkMessageBox

top = Tkinter.Tk()
global mass
global vilosity
global distance
global time

def earth():
    label1=Label(top, text="what is the mass of the satilite (kg)").grid(row=2)
    mass=Entry(top, bd=5)
    mass.grid(row=2, column=2, columnspan=3)
    
    label2=Label(top, text="what is the vilosity of the satilite (m/s)").grid(row=3)
    vilosity=Entry(top, bd =5)
    vilosity.grid(row=3, column=2, columnspan=3)
    
    label3=Label(top, text="how far is the satilte from earth (km)").grid(row=4)
    distance=Entry(top, bd=5)
    distance.grid(row=4, column=2, columnspan=3)
    
    label4=Label(top, text="how long has the satilite been in orbit").grid(row=5)
    time=Entry(top, bd=5)
    time.grid(row=5, column=2, columnspan=3)
    
    o = Tkinter.Button (top, text="next", command  = earth1).grid(row=5, column=7)

def earth1():
    mass = massbox.get
    vilosity = vilositybox.get
    distance = distancebox.get
    time = timebox.get
    if mass.isdigit():
        mass=int(mass)
    if vilosity.isdigit():
        vilosity=int(vilosity)
    if distance.isdigit():
        distance=int(distance)
    if time.isdigit():
        time=int(time)
   
    f=(m*v**2)/r
    a1=Label(top, text =  'the net cintripital force is').grid(row=7)
    print f


    

    
    

   
a = Tkinter.Button (top, text = "obgect in orbit around earth", command = earth).grid(row=1, column=1)



top.mainloop()

===================
