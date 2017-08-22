# -*- coding: utf-8 -*-

import math
#IMAGINARY MODULE, LESS IMPORTANT
import dicthandler

filename = "dict.txt"
string   = "pustema"
song     = ""

dictionary = LoadDictionary(filename) #dicthandler
method     = random.randint(0,3)
length     = len(string)

for i in range(0, len1):
	word1 = ""
	word2 = ""

	if   method == 0:
		dict1 = dictionary.LoadNouns() #dicthandler
		dict2 = dictionary.LoadNouns() #dicthandler
	elif method == 1:
		dict1 = dictionary.LoadNouns() #dicthandler
		dict2 = dictionary.LoadVerbs() #dicthandler
	elif method == 2:
		dict1 = dictionary.LoadVerbs() #dicthandler
		dict2 = dictionary.LoadVerbs() #dicthandler
	elif method == 3:
		dict1 = dictionary.LoadNouns() #dicthandler
		dict2 = dictionary.LoadCuss() #dicthandler
	#if it's impossible to find a first word which has that letter in i position, move on to the next word
	len1 = len(dict1)
	len2 = len(dict2)

	for w in range(0, len1)
		if dict1[w][i] == string[i]:
			word1 = dict1[w]
			w = len1
	if word1 == "":
		word1 = dict1[random.randint(0,len1)]
		for w in range(0, len2):
			if dict2[w][i] == string[i-len1-1]:
				word2 = dict2[w]
	else:
		word2 = dict2[random.randint(0,len2)]

	song += word1
	song += " "
	song += word2
	song += "\n"

print(song)
