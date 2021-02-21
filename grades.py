try:
	inp = raw_input("Enter a grade: ")
	grade = float(inp)
except:
	print "Error, wrong grade. Please enter a valid grade"
	quit()

if grade >= 0.9 and grade <= 1.0:
	print "A"
elif grade >= 0.8 and grade < 0.9:
	print "B"
elif grade >= 0.7 and grade < 0.8:
	print "C"
elif grade >= 0.6 and grade < 0.7:
	print "D"
elif grade >= 0.0 and grade < 0.6:
	print "F"
else:
	print "Grade out of range. Please enter a grade between 0.0 and 1.0"