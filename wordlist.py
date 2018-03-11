import sys


def import_file(fname):
	# read line by line and make a frequency dictionary
	frequency = {}
	with open(fname) as f:
		for line in f.readlines():
			row = line.split(': ')
			frequency[row[0].strip()] = int(row[1].strip())
	return frequency

def add_another_file(fname, dictionary):
	# if in dictionary: += frequency
	# if not in dictionary: add
	frequency = dictionary
	with open(fname) as f:
		for line in f.readlines():
			line = line.strip()
			row = line.split(': ')
			#print(row)
			if row[0].strip() in frequency:
				#print(row[0].strip())
				#print(row[1].strip())
				frequency[row[0]] += int(row[1])
			else:
				frequency[row[0].strip()] = int(row[1].strip())
	return frequency

def output(dictionary):
	# write the dictionary into a file
	frequency_list = ''
	for i in sorted(dictionary, key=dictionary.get, reverse=True):
		frequency_list += i
		frequency_list += '\t'
		frequency_list += str(dictionary[i])
		frequency_list += '\n'
	return frequency_list

def main():
	sys.stdout.write(output(add_another_file('wordlist-kaveshtiebel.txt',
	import_file('wordlist-ivelt.txt'))))


main()
