#here i have function called iverride in both classes
class Parent(object):

    def override(self):
        print "PARENT OVERRIDE()"

class Child(Parent):

    def override(self):
        print "CHILD OERRIDE()"

dad = Parent()
son = Child()

dad.override()
son.override()
