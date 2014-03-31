def convertString(str):

    try:

        returnValue = int(str)

    except ValueError:

        returnValue = float(str)

    return returnValue


print 'welcome to satilite tracker 0.2.1'
print 'what object would you like find the orbit around?'
print '     1: earth'
print '     2: the sun'
print '     3: a custom object (beta)'
print '     *note as of now this is not 100% accurate*'
menue = raw_input()

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
    
if menue == '3'

    
