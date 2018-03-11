import codecs


# read the frequency list
def getrealwords(fname):
	realwords = {}
	with open(fname) as f:
		for line in f.readlines(): 
			row = line.split('\t')
			realwords[row[0].strip()] = row[1].strip()
	return realwords

def main():
	realwords = getrealwords('final_wordlist.csv')
	f = codecs.open('found_anglicisms.csv', 'w', 'utf-8')
	with open('potential_anglicisms.txt') as f1:
		for line in f1.readlines():
			row = line.strip().split('\t')
			if row[0] in realwords:
				f.write(line.strip())
				f.write('\t')
				f.write(realwords[row[0]])
				f.write('\n')
	f.close()
	

main()
