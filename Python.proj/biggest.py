# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
#	if a>b:
#		if a>c:
#			return a
#		else:
#			return c
#	else:
#		if b>c:
#			return b
#		else:
#			return c

	return max (a,b,c)


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9


def median (a,b,c):
	big = max(a,b,c)
	if big == a:
		return max(b,c)
	if big == b:
		return max(a,c)
	else:
		return max(a,b)
		
print(median(1,2,3))
		#>>> 2

print(median(9,3,6))
		#>>> 6

print(median(7,8,7))
		#>>> 7
