from enumutils import Types 

# TODO: Give this a good name that helps understand 
# what this does and what parameters it receives
def _SeparateAndRequest(dictionary, which):
	"""
	Receives a dictionary `dictionary` 
	and a Types enum member that specifices which type of word to get
	Returns a list of words from the dictionary that are of type `which`
	"""
	words = []
	i     = 0
	text  = dictionary.split('\n')

	for l in range(0,len(text)):
		line = text[l].split(' ')
		if line[0] == which:
			words[i] = line[1]
			i += 1

	return words

class Dictionary:
	def __init__(self, filename):
		with open(filename, 'r') as dfile:
			self.dictionary = dfile.read()
	def LoadWords(self, which):
		return _SeparateAndRequest(self.dictionary, which)
