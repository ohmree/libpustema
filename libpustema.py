#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import dicthandler
import random
from enumutils import Methods, Types

filename = "dict.txt"
string   = "zotzoot"
song     = ""

dictionary = dicthandler.Dictionary(filename)
<<<<<<< HEAD
=======
method = random.randint(0, 3)
>>>>>>> b315ca564b141bd0058d9fa0e310e93374d5e851
length     = len(string)

for i in range(0, length):
	word1 = ''
	word2 = ''

<<<<<<< HEAD
	method = 0 #method     = random.randint(0,3)
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
=======
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
>>>>>>> b315ca564b141bd0058d9fa0e310e93374d5e851

	lend1  = len(dict1)
	lend2  = len(dict2)
	shortl = len(dict1[0])
	shortw = dict1[0]
	longl  = len(dict1[0])
	longw  = dict1[0]
	#word2 will be treated as if word1+space is its prefix
	for w in range(0, lend1):
		if i < len(dict1[w]):
			if dict1[w][i] == string[i]:
				word1 = dict1[w]
				word2 = dict2[random.randint(0,lend2-1)]
			if len(dict1[w]) < shortl:
				shortl = len(dict1[w])
				shortw = dict1[w]
			if len(dict1[w]) > longl:
				longl = len(dict1[w])
				longw = dict1[w]

	if word1 == '':
		for w in range(0, lend2):
			if string[i] in dict2[w]:
				for x in range(0, len(dict2[w])):
					if dict2[w][x] == string[i]:
						position = x
						x = len(dict2[w])
				#word1 = dicthandler.LookFor(i-position, dict1)[random.randint(0,len(dicthandler.LookFor(i-position,dict1))-1)]
				#print(i-position+1)
				word1 = dicthandler.LookFor(i-position+1, dict1)[0]
				word2 = dict2[w]
				w = lend2
	if word1 == '':
		word1 = dict1[random.randint(0,lend1-1)]
		if i >= longl:
			word2 = dicthandler.MakeUp(string[i], i-len(word1))
		else:
			word1 = dicthandler.MakeUp(string[i], i, longl)
			word2 = dict2[random.randint(0,lend2-1)]

	#print(word1 + ' ' + word2)
	print(word1 + " " + word2)
