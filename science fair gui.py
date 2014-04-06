import Tkinter
from Tkinter import Label
from Tkinter import Entry
import tkMessageBox

top = Tkinter.Tk()

def earth():
    global massboxEarth
    global vilosityboxEarth
    global distanceboxEarth
    global timeboxEarth
    
    label1 = Label (top, text="what is the mass of the satilite (kg)").grid(row=2)
    massboxEarth = Entry (top, bd=5)
    massboxEarth.grid (row=2, column=2, columnspan=3)
    
    label2=Label (top, text="what is the vilosity of the satilite (m/s)").grid(row=3)
    vilosityboxEarth = Entry (top, bd =5)
    vilosityboxEarth.grid (row=3, column=2, columnspan=3)
    
    label3 = Label (top, text="how far is the satilte from earth (km)").grid (row=4)
    distanceboxEarth = Entry (top, bd=5)
    distanceboxEarth.grid (row=4, column=2, columnspan=3)
    
    label4 = Label (top, text="how long has the satilite been in orbit").grid(row=5)
    timeboxEarth = Entry (top, bd=5)
    timeboxEarth.grid (row=5, column=2, columnspan=3)
    
    o = Tkinter.Button (top, text="next", command  = earth1).grid(row=5, column=7)
                                            
def earth1():
    mass = float (Entry.get(massboxEarth))
    vilosity = float (Entry.get(vilosityboxEarth))
    distance = float (Entry.get(distanceboxEarth))
    time = float (Entry.get (timeboxEarth))
   
    radius = distance+6378.1
    force = (mass*vilosity**2)/radius
    force1 = string(force)
    
    label = Label(top, text =  'the net cintripital force is').grid(row = 7)
    label2 = Label(top, textvariable = force).grid(row = 7, column = 5, columnspan = 3)

    Gravity = 6.673*10**(0-11)*r**2/mass**2
    l=(4*3.14**2)/Gravity*(1.9891*10**30)
    k=l/radius**3
    years=k**.5
    days=years/365
    period = string(days)
    
    label3 = Label (top, text = 'the orbital period is,').grid (row = 8)
    label4 = Label (top, textvariable = period).grid (row = 8, column = 5, columnspan = 3)
    
    F = (days*k)*time
    orbitcircum = 2*3.14*radius
    distancetraveled = orbit-circum*F
    dt = string (distancetraveled)
    
    lable5 = Label (top, text = 'the satilite has traveled,').grid (row = 9)
    lable6 = Label (top, textvariable = dt).grid (row = 9, column = 5, columnspan = 3)

def sun():
    global massboxSun
    global vilosityboxSun
    global distanceboxSun
    global timeboxSun
    
    label1 = Label (top, text="what is the mass of the satilite (kg)").grid(row=2)
    massboxSun = Entry (top, bd=5)
    massboxSun.grid (row=2, column=2, columnspan=3)
    
    label2=Label (top, text="what is the vilosity of the satilite (m/s)").grid(row=3)
    vilosityboxSun = Entry (top, bd =5)
    vilosityboxSun.grid (row=3, column=2, columnspan=3)
    
    label3 = Label (top, text="how far is the satilte from earth (km)").grid (row=4)
    distanceboxSun = Entry (top, bd=5)
    distanceboxSun.grid (row=4, column=2, columnspan=3)
    
    label4 = Label (top, text="how long has the satilite been in orbit").grid(row=5)
    timeboxSun = Entry (top, bd=5)
    timeboxSun.grid (row=5, column=2, columnspan=3)
    
    o = Tkinter.Button (top, text="next", command  = earth1).grid(row=5, column=7)
                                            
def sun1():
    mass = float (Entry.get(massboxSun))
    vilosity = float (Entry.get(vilosityboxSun))
    distance = float (Entry.get(distanceboxSun))
    time = float (Entry.get (timeboxSun))
   
    radius = distance+695500 
    force = (mass*vilosity**2)/radius
    force1 = string (force)
    
    label = Label(top, text =  'the net cintripital force is').grid(row = 7)
    label2 = Label(top, textvariable = force).grid(row = 7, column = 5, columnspan = 3)

    Gravity = 6.673*10**(0-11)*r**2/mass**2
    l=(4*3.14**2)/Gravity*(5.97219*10**24)
    k=l/radius**3
    years=k**.5
    days=years/365
    period = string (days)
    
    label3 = Label (top, text = 'the orbital period is,').grid (row = 8)
    label4 = Label (top, textvariable = period).grid (row = 8, column = 5, columnspan = 3)
    
    F = (days*k)*time
    orbitcircum = 2*3.14*radius
    distancetraveled = orbit-circum*F
    dt = string(distancetraveled)
    
    lable5 = Label (top, text = 'the satilite has traveled,').grid (row = 9)
    label6 = Label (top, textvariable = dt).grid (row =9, column = 5, columnspan = 3)
    
a = Tkinter.Button (top, text = "satilite in orbit around earth", command = earth).grid (row = 1, column = 0)
b = Tkinter.Button (top, text = "satilite in orbit around the Sun", command = sun).grid (row = 1, column = 2)

top.mainloop()


===================
