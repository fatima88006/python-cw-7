class Person :
    name = "Fatima"
    age = 17

first_person = Person()
print(first_person.name)
print(first_person.age)

class Person :
    def __init__ (self , name , age):
        self.name = name
        self.age = age

    def adult(self):
        if self.age >= 18:
            print("You have too much responsibilities")
        else:
            print(" Lucky you ")
    def __str__ (self):
        return f"My name is {self.name} and I am {self.age} years old"
first_person = Person("Fatima",17)
print(first_person.name)
print(first_person.age)
print(first_person.adult())