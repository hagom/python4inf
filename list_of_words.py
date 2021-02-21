fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
	line = line.rstrip()
	line = line.split()
		
	for word in line:
		lst.append(word)

lst.sort()
newlst = list()

for words in lst: 
	if words in newlst: continue
	newlst.append(words)

newlst.sort()
print newlst