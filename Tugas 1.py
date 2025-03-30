class Passenger:
    TITLES = ('Mr', 'Mrs', 'Ms') #class attribute

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s is nt a valid title." % title)
        
        self.title = title #instance attribute
        self.fname = fname
        self.lname = lname
    
#Pembuatan Objek
p1 = Passenger('Mr', 'Kiewlamphone', 'Soulvalinth')
#mengakses class attribute dari object
print(p1.TITLES)
#mengakses class attribute dari class
print(Passenger.TITLES)
#mengakses instance attribute dari object
print(p1.title)
#mengakses instance attribute dari class
print(Passenger.title)