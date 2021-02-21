count = 0
lst = list()
email = list()

fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:

	if line.startswith("From") :
		line = line.rstrip()
		lst = line.split()

		if lst[0] == "From:": continue
		email.append(lst[1])
		count = count + 1

for address in email:
	print address

print "There were", count, "lines in the file with From as the first word"