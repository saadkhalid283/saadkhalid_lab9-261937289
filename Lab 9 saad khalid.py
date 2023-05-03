#Muhammad Saad Khlid
#Roll no 261937289
#Lab 9


class Person:
    
    def __init__(self,person,age):
        self.person = person
        self.age = age

    def display(self):
        return self.person
        return self.age
        
class House:
    
    def __init__(self,address,numOfrooms):
        self.address = address
        self.numOfrooms = numOfrooms
        self.persons = []
        
    def add_person(self,obj):
        self.persons.append(obj)
        
    def remove_person(self,obj):
        for i in self.persons:
            if i == obj:
                self.persons.remove(i)
            else:
                continue
            
    def display(self):
        for i in range(0,len(self.persons)):
            print("Person",i+1,":",self.persons[i].display())
            
Saad = Person("Saad",20)
Mansion = House("Dha Raya",10)
Mansion.add_person(Saad)
Mansion.add_person(Person("Khalid",19))
Mansion.add_person(Person("Muhammad",21))
Mansion.display()
Mansion.remove_person(Saad)
Mansion.display()
