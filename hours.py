inp = raw_input("Enter number of hours: ")
hours = float(inp)
inp = raw_input("Enter rate: ")
rate = float(inp)

if hours <= 40:
	pay = hours * rate
if hours > 40:
	pay = 40 * rate + (rate * 1.5 * (hours - 40))

print pay
