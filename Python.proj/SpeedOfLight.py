# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the variables
# defined below.    

speed_of_light = 299792458   # meters per second
meter = 100                  # one meter is 100 centimeters
nanosecond = 1.0/1000000000  # one billionth of a second
print 'light travels ',(1.0/1000000000) * 299792458 * 100, 'centimetres in one nanosecond.'

# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
cycle_dist_metres = speed_of_light / cycles_per_second
cycle_dist_centimetres = cycle_dist_metres * 100
print 'distance in metres =', cycle_dist_metres
print 'distance in centimetres =', cycle_dist_centimetres
