import itertools
import codecs
import re


# get words
def getwords(fname): #rewrite later. now there are only some example words
	english_words = {}
	with open(fname) as f:
		for line in f.readlines():
			row = line.split(',\t\t')
			try:
				#if len(row[0].strip()) > 2:
				english_words[row[1].strip()] = row[0].strip()
			except:
				continue
	return english_words

# get graphical correspondencies
def getcorrespondences(fname):
	correspondences = {}
	with open(fname) as f:
		for line in f.readlines():
			row = line.split('\t')
			options = []
			for i in row[1].split(','):
				options.append(i.strip())
			correspondences[row[0].strip()] = options
	return correspondences

# a preparatory stage for generating potential anglicisms
def transliterate(word, correspondences):
	translit_array = []
	while len(word) > 0:
		for i in correspondences:
			if word.startswith(i):
				# add all possible options for a particular phoneme
				translit_array.append(correspondences[i])
				word = word[len(i):]
				#print(word)
				continue
	return translit_array

# generate potential anglicisms (cartesian product)
def potentialanglicisms(translit_array):
	options = []
	for i in itertools.product(*translit_array): # get the lists from it
		word = ''.join(i)
		if word.endswith('מ') == True:
			word = word[:-1] + 'ם'
		if word.endswith('נ') == True:
			word = word[:-1] + 'ן'
		m = re.search('^[יײוױ]', word)
		if m != None:
			word = 'א' + word
		options.append(word) 
	return options

# print the potential anglicisms into a file
def writeanglicisms(words, english_word):
	f = codecs.open('potential_anglicisms.txt', 'a', 'utf-8')
	for i in words:
		f.write(i)
		f.write('\t')
		f.write(english_word)
		f.write('\n')
	f.close()

def main():
	correspondences = (getcorrespondences('correspondences.csv'))
	words = getwords('test.txt')
	n = 0
	for i in words:
		n += 1
		#if n % 1000 == 0:
		print(str(n) + ' words')
		writeanglicisms(potentialanglicisms(transliterate(i, correspondences)), words[i])


main()