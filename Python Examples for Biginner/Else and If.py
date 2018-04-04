people = 30
cars = 40
buses = 15

if cars > people:
    print "We Should take the cars."
elif cars < people:
    print "We Should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "Thats too mant buses."
elif buses <cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people> buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
