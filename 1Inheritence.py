
class person:
    def __init__(self , f_name,l_name):
        self.fName = f_name
        self.lName = l_name
    def printNames(self):
        print("hello programmer: ",self.fName , self.lName)
a = str(input("name: "))
b = str(input("surname: "))

x = person(a,b)
x.printNames()

class student(person):
    def __init__(self, f_name, l_name,year):
        person.__init__(self,f_name , l_name) # вместо этого мы можем использовать: super().__init__(fname, lname)
        self.WhenHeSheFinishUni = year
    def Welcome(self):
        print("Heloo ",self.lName,self.fName,"which finish at ",self.WhenHeSheFinishUni)
y = int(input("Year when you finish KBTU: "))

x = student(a,b,y)
x.Welcome()

    
