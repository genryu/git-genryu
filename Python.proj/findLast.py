def find_last(s,t):
	last_pos=-1
	while True:
		pos = s.find(t,last_pos+1)
		if pos == -1:
			return last_pos
		last_pos = pos
		
print find_last('aaaa', 'a')
		#>>> 3

print find_last('aaaaa', 'aa')
		#>>> 3

print find_last('aaaa', 'b')
		#>>> -1

print find_last("111111111", "1")
		#>>> 8
print find_last("222222222", "")
		#>>> 9

		#print find_last("", "3")
		#>>> -1

		#print find_last("", "")
		#>>> 0
