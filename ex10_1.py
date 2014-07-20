str = 'From'
dfile = "mbox-short.txt"
fname = raw_input('Enter filename: ')
if len(fname) < 1 : fname = dfile
try :
    fhand = open(fname)
except :
	print 'File cannot be opened:', fname
	exit()
counts = dict()
for line in fhand :
    line = line.rstrip()
    if line.startswith(str) and not line.startswith('From:'):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
        
lst = list()
for key, val in counts.items():
    lst.append((val, key))
    
lst.sort(reverse=True)
for val, key in lst[:1]:
    print key, val
