def _SeparateAndRequest(dictionary, char):
	words = []
	i     = 0
	text  = dictionary.split('\n')

	for l in range(0,len(lines)):
		line = text[l].split(' ')
		if line[0] == char:
			words[i] = line[1]
			i = i + 1

	return words

class Dictionary:
	def __init__(self, filename):
		with open(filename, 'r') as dfile:
			dictionary = dfile.read()
	def LoadNouns():
		return _SeparateAndRequest(dictionary, 'N')
	def LoadVerbs():
		return _SeparateAndRequest(dictionary, 'V')
	def LoadCuss():
		return _SeparateAndRequest(dictionary, 'C')
