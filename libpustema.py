# -*- coding: utf-8 -*-

import math
import dicthandler
import random
import enum

filename = "dict.txt"
string   = "da"
song     = ""

dictionary = dicthandler.Dictionary(filename)
#method     = random.randint(0,3)
method = 0
length     = len(string)

for i in range(0, length):
	word1 = ""
	word2 = ""

	if   method == 0:
		dict1 = dictionary.LoadNouns()
		dict2 = dictionary.LoadNouns()
	elif method == 1:
		dict1 = dictionary.LoadNouns()
		dict2 = dictionary.LoadVerbs()
	elif method == 2:
		dict1 = dictionary.LoadVerbs()
		dict2 = dictionary.LoadVerbs()
	elif method == 3:
		dict1 = dictionary.LoadNouns()
		dict2 = dictionary.LoadCuss()

	len1 = len(dict1)
	len2 = len(dict2)

	for w in range(0, len1):
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
