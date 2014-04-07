import Tkinter
from Tkinter import Label
from Tkinter import Entry
import tkMessageBox
print "this is my first version of planet tracker its pretty basic but can still make the calculations (press next to continue)'
a=raw_input()
if a == "next":

    def convertString(str):
        try:
            returnValue = int(str)
        except ValueError:
            returnValue = float(str)
        return returnValue

    print 'welcome to sattrack 0.2.1'
    print 'what object would you like find the orbit around?'
    print '     1: earth'
    print '     2: the sun'
    print '     *note as of now this is not 100% accurate*'
    a = raw_input()

    if a == '1':
        print 'what is the mass of the satilite (kg):'
        m=input()
        print 'what is the vilosity of the satilite (m/s):'
        v=input()
        print 'how far is the satilite from earth (km):'
        d=input()
        print 'how  long has the object been in orbit (days):'
        t=input()
        r=d+6378.1
        f=(m*v**2)/r
        print 'the net centripital force is:', f, 'newtons'
        G=6.673*10**(0-11)*r**2/m**2
        l=(4*3.14**2)/G*(5.97219*10**24)
        k=l/r**3
        T=k**.5
        e=T/365
        print 'the orbital period of the object is:', e, 'days'
        F=(e*k)*t
        h=2*3.14*r
        H=h*F
        print 'the object has traveled', H , 'km'

    if a == '2':
        print 'what is the mass of the satilite (kg):'
        m=input()
        print 'what is the vilosity of the satilite (m/s):'
        v=input()
        print 'how far is the satilite from the sun (km):'
        d=input()
        print 'how  long has the object been in orbit (days):'
        t=input()
        r=d+695500
        f=(m*v**2)/r
        print 'the net centripital force is:', f, 'newtons'
        G=6.673*10**(0-11)*r**2/m**2
        l=(4*3.14**2)/G*(1.1891*10**30)
        k=l/r**3
        T=k**.5
        e=T/365
        print 'the orbital period of the object is:', T, 'days'
        F=(e*k)*t
        h=2*3.14*r
        H=h*F
        print 'the object has traveled', H , 'km'
        
        print 'now this is my GUI (graphical user interface) version to make it more user freindly"
        print 'type next to continue'
        b = raw_input()
        if b == 'next':

    top = Tkinter.Tk()

    def earth():
        try:
            global massboxEarth
            global vilosityboxEarth
            global distanceboxEarth
            global timeboxEarth
        except:
            print 'oh my you have to use numbers!"
    
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
 
        Gravity = 6.673*10**(0-11)*radius**2/mass**2
        l=(4*3.14**2)/Gravity*(1.9891*10**30)
        k=l/radius**3
        years=k**.5
        days=years/365
 
        F = (days*k)*time
        orbitcircum = 2*3.14*radius
        distancetraveled = orbitcircum*F
 
        force1 = "The net centrpital force is %.6f (newtons),\nthe orbital period is %.2f (days),\nthe satellite has travelled %.2f (km)" % (force, days, distancetraveled)
    
        label = Label(top, text = force1).grid(row = 7)

    def sun():
        try:
            global massboxSun
            global vilosityboxSun
            global distanceboxSun
            global timeboxSun
        except: 
            print 'oh my you have to use numbers!'
    
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

        Gravity = 6.673*10**(0-11)*radius**2/mass**2
        l=(4*3.14**2)/Gravity*(5.97219*10**24)
        k=l/radius**3
        years=k**.5
        days=years/365
    
        F = (days*k)*time
        orbitcircum = 2*3.14*radius
        distancetraveled = orbitcircum*F
    
        force1 = "The net centrpital force is %.6f,\nthe orbital period is %.2f,\nand the satellite has travelled %.2f" % (force, days, distancetraveled)
        label = Label(top, text = force1) 
    
    
    a = Tkinter.Button (top, text = "satilite in orbit around earth", command = earth).grid (row = 1, column = 0)
    b = Tkinter.Button (top, text = "satilite in orbit around the Sun", command = sun).grid (row = 1, column = 2)

    top.mainloop()


===================
