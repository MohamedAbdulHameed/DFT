record = open("record.txt", "r+")
stress = []
for line in record:
	stress.append(float(line.strip()))
record.close()


I = input("Iteration number: ")
print(I)
i = int(I)

F1 = open("output-%d.out" %i, "r+")
for line in F1:
	a0 = line.strip()
	a1 = " ".join(a0.split())
	if a1.find("total stress") != -1:
		a2 = a1.replace("total stress (Ry/bohr**3) (kbar) P= ", "")
		stress.append(float(a2))
F1.close()

if len(stress) >= 1:
    record = open("record.txt", "a+")
    record.write(str(stress[len(stress)-1])+"\n")
    record.close()

# Add the value of stress for this iteration to record.txt
try:
    if len(stress) <= 1:
        F1 = open("input-%d.in" %i, "r+")
        NewContent = ""
        for line in F1:
            NewLine = line.replace("%d %d %d" %(i, i, i), "%d %d %d" %(i+1, i+1, i+1))
            NewContent += NewLine + "\n"
        F1.close()
        F2 = open("input-%d.in" %(i+1), "w+")
        F2.write(NewContent)
        F2.close()
    elif round(stress[len(stress)-1], 2) - round(stress[len(stress)-2], 2) <= 0.001:
        F1 = open("input-%d.in" %i, "r+")
        NewContent = ""
        for line in F1:
            NewLine = line.replace("%d %d %d" %(i, i, i), "%d %d %d" %(i+1, i+1, i+1))
            NewContent += NewLine + "\n"
        F1.close()
        F2 = open("input-%d.in" %(i+1), "w+")
        F2.write(NewContent)
        F2.close()
    else:
        print("Covergence is achieved.")
    print(stress)
except:
    print("Program is terminated.")
    exit()
