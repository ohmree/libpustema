<<<<<<< HEAD
import random

def _SeparateAndRequest(dictionary, char):
=======
from enumutils import Types 

# TODO: Give this a good name that helps understand 
# what this does and what parameters it receives
def _SeparateAndRequest(dictionary, which):
	"""
	Receives a dictionary `dictionary` 
	and a Types enum member that specifices which type of word to get
	Returns a list of words from the dictionary that are of type `which`
	"""
>>>>>>> b315ca564b141bd0058d9fa0e310e93374d5e851
	words = []
	text  = dictionary.split('\n')

	for l in range(0,len(text)):
		line = text[l].split(' ')
<<<<<<< HEAD
		if line[0] == char:
			words.append(line[1])
=======
		if line[0] == which:
			words[i] = line[1]
			i += 1
>>>>>>> b315ca564b141bd0058d9fa0e310e93374d5e851

	return words

def MakeUp(letter, index, length=0):
	if length == 0:
		length = random.randint(index,index+random.randint(0,5))
	word = ''

	for i in range(0,length):
		char = random.randint(97,122)
		word = word[:i] + chr(char) + word[i+1:]
	word = word[:index] + letter + word[index+1:]

	return word

def LookFor(length, dictionary):
	compat = []
	for w in range(0,len(dictionary)):
		if len(dictionary[w]) == length:
			compat.append(dictionary[w])
	return compat

class Dictionary:
	def __init__(self, filename):
		with open(filename, 'r') as dfile:
			self.dictionary = dfile.read()
<<<<<<< HEAD
	def LoadLetter(self, letter):
		return _SeparateAndRequest(self.dictionary, letter)
	def LoadNouns(self):
		return _SeparateAndRequest(self.dictionary, 'N')
	def LoadVerbs(self):
		return _SeparateAndRequest(self.dictionary, 'V')
	def LoadCuss(self):
		return _SeparateAndRequest(self.dictionary, 'C')
=======
	def LoadWords(self, which):
		return _SeparateAndRequest(self.dictionary, which)
>>>>>>> b315ca564b141bd0058d9fa0e310e93374d5e851
