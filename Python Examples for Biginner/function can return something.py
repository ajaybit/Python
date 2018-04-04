def add (a,b ):
	print "ADDING %d + %d" % (a, b)
	return a+b

def substract (a, b):
	print "SUBSTRACTION %d - %d "  %(a, b)
	return a-b 

def multiplication(a, b):
	print "MULTIPLICATION %d*%d" % (a, b)
	return a*b 
	
def division (a, b):
	print "DIVISION %d/%d" % (a, b) 
	return a/b

print "Let's do some maths with just fumction"

age = add(30, 5)
height = substract(78, 4)
weight = multiplication(90, 2)
iq = division(100, 2)

print "Age: %d, height: %d ,weight: %d, iq: %d" % (age, height, weight, iq)

what = add( age, substract( height, multiplication(  weight, division(iq, 2))))

print "That becomes:", what, "Can you 	do it by hand?"