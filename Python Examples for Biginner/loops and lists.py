#programs also need to do repetitive things very quickly. We are going to use a for loop in this exercise to build and print various lists. When you do the exercise, you will start to figure out what they are.

#making some lists

the_count = [1,2,3,4,5]
fruits = ['apple', 'orange', 'pears','apiricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a lists
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#aso we can go through mixed lists # too
#notice we have to use %r since we don't know what's in it

for i in change:
    print "I got %r" % i

#we can also build lists, first start with an empty one
element = []

#then use the range function to do 0 to 5 count
for i in range(0,6):
    print "Adding %d to the list." % i
    # append is the funtion that lists understand
    element.append(i)

#now we can print them out
for i in element:
    print "Element was: %d" % i



    #perfect working
