def _SeparateAndRequest(dictionary, char):
	words = []
	i     = 0
	text  = dictionary.split('\n')

	for l in range(0,len(text)):
		line = text[l].split(' ')
		if line[0] == char:
			words[i] = line[1]
			i += 1

	return words

class Dictionary:
	def __init__(self, filename):
		with open(filename, 'r') as dfile:
			self.dictionary = dfile.read()
	def LoadNouns(self):
		return _SeparateAndRequest(self.dictionary, 'N')
	def LoadVerbs(self):
		return _SeparateAndRequest(self.dictionary, 'V')
	def LoadCuss(self):
		return _SeparateAndRequest(self.dictionary, 'C')
