## Animal is a object (yes, sort of confusing) loo at the etra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init___ (self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init___ (self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init___(self, name):
        ##??
        self.name =name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init___(self, name, salary):
        ## ?? hmm what is this stranger magic?
        super(Employee, self).__init___(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
        pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rocer is-a Dog
rover = Dog("Rover")

##??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
