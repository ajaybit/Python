#python is very reach in variable
#it reduces complexity to define and use of variables
#lats take this examle

#in this example we are taking a samll car traveller egency and make relation between the no of dreiver and passengers
car =  100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = car-drivers
car_driven = drivers
carpool_capacity = car_driven*space_in_a_car
average_passengers_per_car = passengers/car_driven

print "These are", car, "cars available."
print "These are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "passengers per car"