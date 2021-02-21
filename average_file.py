# Use the file name mbox-short.txt as the file name
number_count = 0.0 #acumulador
iteration = 0
average = 0.0 #almacenamiento del promedio
while True:
	fname = raw_input("Enter file name: ")

	if len(fname) == 0:
		break

	try:
		fhand = open(fname)
	except:
		print "Invalid file name\n"
		continue

	for line in fhand:
		if not line.startswith("X-DSPAM-Confidence:") : continue
		number = float(line[line.find("0"):len(line)])
		number_count = number_count + number
		iteration = iteration + 1

	average = number_count/iteration
	print "Average spam confidence:", average
	break