#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import dicthandler
import random
from enumutils import Methods, Types

filename = "dict.txt"
string   = "da"
song     = ""

dictionary = dicthandler.Dictionary(filename)
method = random.randint(0, 3)
length     = len(string)

for i in range(0, length):
	word1 = ""
	word2 = ""

	if   method == Methods.NN:
		dict1 = dictionary.LoadWords(Types.NOUN)
		dict2 = dictionary.LoadWords(Types.NOUN)
	elif method == Methods.NV:
		dict1 = dictionary.LoadWords(Types.NOUN)
		dict2 = dictionary.LoadWords(Types.VERB)
	elif method == Methods.VV:
		dict1 = dictionary.LoadWords(Types.VERB)
		dict2 = dictionary.LoadWords(Types.VERB)
	elif method == Methods.NC:
		dict1 = dictionary.LoadWords(Types.NOUN)
		dict2 = dictionary.LoadWords(Types.CUSS)

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
