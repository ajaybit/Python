print "Let's practice everything."
print "You\'d need to know \'bout escape with \\that do \newline and \t tab."

poem = """
\t this is the srart of poem
this is another line without newline strock 
this is third line of poem 
thid is fourth kine of poem 
"""
print "----------------------------------"
print poem
print "----------------------------------"

five = 10-2+3-6
print "this is shold be five: %s" % five

def secret_formula(started):
	jelly_beans = started*500
	jar = started/1000
	crates = jar/100
	return jelly_beans, jar, crates
start_point = 10000
beans, jar, crates = secret_formula(start_point)
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jar, and %d crates." % (beans, jar, crates)
start_point = start_point/10

print "We can also do that 	this way:"
print "We'd have %d beans, %d jar, %d  crates." % secret_formula(start_point)