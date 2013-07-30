pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	if "aeiou".find(first) != -1:
	#if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
		pyggy = word + pyg
		print '"' + word + '" ' + 'is ' + pyggy + ' in fuckin PygLatin.'
	else:
		stripped = word[1:]
		pyg = word[0] + pyg
		pyggy = stripped + pyg
		print '"' + word + '" ' + 'is ' + pyggy + ' in fuckin PygLatin.'
else:
	print 'Enter a fuckin word Bitch!!.'