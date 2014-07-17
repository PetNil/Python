fname = 'romeo.txt'
try :
    fhand = open(fname)
except :
	print 'File cannot be opened:', fname
	exit()
word_list = []

for line in fhand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        if word not in word_list :
            word_list.append(word)

word_list.sort()
print word_list
