#Mencetak Menu
def menu():
    print ("Tabung")
    print ("Kerucut")
    print ("Bola")
    
def tabung():
    print ("Menghitung Volume Tabung")
    t = 10
    r = 7
    v = 22/7*r**2*t

    print ("Apabila tabung memiliki")
    print ("tinggi",t)
    print ("jari-jari lingkaran",r)
    print ("maka tabung memiliki volume",v)


def kerucut():
    print ("Menghitung Volume Kerucut")
    t = 10 
    r = 7
    v = 1/3*22/7*r**2*t

    print ("Apabila kerucut memiliki")
    print ("tinggi",t)
    print ("jari-jari lingkaran",r)
    print ("maka kerucut memiliki volume",v)

def bola():
    print ("Menghitung Volume Bola")
    r = 7
    v = 4/3*22/7*r**3

    print ("Apabila bola memiliki")
    print ("jari-jari lingkaran",r)
    print ("maka bola memiliki volume",v)
