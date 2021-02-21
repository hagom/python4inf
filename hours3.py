def computepay(hours,rate):
	if hours <= 40:
		pay = hours * rate
	if hours > 40:
		pay = 40 * rate + (rate * 1.5 * (hours - 40))
	return pay

try:
	inp = raw_input("Enter number of hours: ")
	hours = float(inp)
	inp = raw_input("Enter rate: ")
	rate = float(inp)
except:
	print "Enter a numeric value"
	quit()

pay = computepay(hours,rate)
print pay