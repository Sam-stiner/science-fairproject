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
    a=Label(top, text="what is the mass of the satilite (kg)").grid(row=2)
    q=Entry(top, bd=5)
    q.grid(row=2, column=2, columnspan=3)
    mass=q.get()

    a1=Label(top, text="what is the vilosity of the satilite (m/s)").grid(row=3)
    w=Entry(top, bd =5)
    w.grid(row=3, column=2, columnspan=3)
    vilosity=w.get()
    
    


    a2=Label(top, text="how far is the satilte from earth (km)").grid(row=4)
    e=Entry(top, bd=5)
    e.grid(row=4, column=2, columnspan=3)
    distance=e.get()
    


    a3=Label(top, text="how long has the satilite been in orbit").grid(row=5)
    y=Entry(top, bd=5)
    y.grid(row=5, column=2, columnspan=3)
    time=y.get()

    o = Tkinter.Button (top, text="next", command  = earth1).grid(row=5, column=7)

def earth1():
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
