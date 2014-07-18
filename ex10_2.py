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
        time = words[5]
        stime = time.split(":")
        hour = stime[0]
        counts[hour] = counts.get(hour, 0) + 1
 
lst = list()
for key, val in counts.items():
    lst.append((key, val))
    
lst.sort()
for key, val in lst:
    print key, val
