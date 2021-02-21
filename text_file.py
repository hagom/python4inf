while True:
	fname = raw_input("Enter a file name: ")
	if fname is "done":
		break

	try:
		file = open(fname,'r')
	except:
		print "Invalid file name.\n"
		continue

	text = file.read()
	text = text.upper().rstrip()
	break
print text