p = 2.70610
a = [1.00, 0.95, 0.90, 0.85, 0.80]
b = [round((i**(1/3))*p, 5) for i in a]
print(b)

for i in range(5):
	InputFile = open("input.in", "rt")
	GenFile = open("input-%d.in" % i, "wt")
	for line in InputFile:
		c = line.replace(str(p), str(b[i]))
		GenFile.write(c)
	InputFile.close()
	GenFile.close()
