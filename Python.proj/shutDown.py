s = raw_input ("Hey fucker, would you like to shut down your damned computer? ")
def shut_down(s):
	if s.lower() =='yes':
		return "Shutting down..."
	elif s.lower() =='no':
		return "Shutdown aborted!"
	else:
		return "You suck, I didn't understand you."
print shut_down(s)