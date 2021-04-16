import numpy as n
import matplotlib.pyplot as p
from scaled import a
from scipy.optimize import curve_fit

energy = []

for i in range(5):
    F = open("output-%d.out" % i, "rt")
    for line in F:
        a1 = " ".join(line.split())
        if a1.find("! total energy") != -1:
            a2 = a1.replace("! total energy =", "")
            a3 = a2.replace("Ry", "")
            energy.append(float(a3))
    F.close()
print(energy)

V = n.array([n.sqrt(8)*i**3 for i in a])
E = n.array(energy)

p.plot(V, E, "--Db")
p.xlabel("Volume ($a_0^3$)")
p.ylabel("E (Ry)")
p.grid("on")
p.show()
