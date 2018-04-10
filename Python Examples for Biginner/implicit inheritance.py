class Parent(object):

    def implicit(self):
        print "PARENT implicit()"
    def child(slef):
        pass #Pass is use you want to make this block empty

class Child(Parent):
    print "Hello ! i'am children !"
    pass #empty block

dad = Parent()
son = Child()

dad.implicit()
son.child()
