str = 'X-DSPAM-Confidence:'
dfile = "mbox-short.txt"
fname = raw_input('Enter filename: ')
if len(fname) < 1 : fname = dfile
try :
    fhand = open(fname)
except :
	print 'File cannot be opened:', fname
	exit()
count = 0
spam_sum = 0
for line in fhand :
    line = line.rstrip()
    if line.startswith(str) :
        col = line.find(':')
        str_num = line[col+1:]
        num = float(str_num)
        spam_sum += num
        count += 1
spam_conf = spam_sum / count

print 'Average spam confidence:', spam_conf
