import numpy as np
from matplotlib import pyplot as plt

'''
a) Macierz przejść na podstawie grafu
'''

P = np.array([[0.64, 0.32, 0.04], [0.4, 0.5, 0.1], [0.25, 0.5, 0.25]])


'''
b) Wyznaczanie rozkładu granicznego
'''

np.set_printoptions(precision=9)


p0 = np.array([1, 0, 0])

pn = np.array(0)

for i in range(0, 21):
    if i == 0:
        pn = np.dot(p0, P)
        print(f"n={i+1} pn={pn}")
    else:
        pn = np.dot(pn, P)
        print(f"n={i+1} pn={pn}")

print(f"\nRozkład graniczny: {pn}" + "\n")


'''
c) Kryterium zbieznosci
'''
epsilon = 1e-9

pn = p0
for i in range(0, 21):
    if i == 0:
        pn_prev = pn
        pn = np.dot(pn, P)
    else:
        pn_prev = pn
        pn = np.dot(pn, P)

    difference = np.linalg.norm(pn - pn_prev)

    print(f"n={i+1}  e={difference}")

    if difference < epsilon:
        print(f"Zbieżność osiągnięta w {i+1}-tym kroku.")
        break

'''
d) Wykres
'''
np.set_printoptions(precision=9)

x = []

y0 = []

y1 = []

y2 = []


p0 = np.array([1, 0, 0])

pn = np.array(0)

for i in range(0, 20):

    x.append(i+1)

    if i == 0:
        pn = np.dot(p0, P)
        y0.append(pn[0])
        y1.append(pn[1])
        y2.append(pn[2])

    else:
        pn = np.dot(pn, P)
        y0.append(pn[0])
        y1.append(pn[1])
        y2.append(pn[2])

#0
print(pn[0])
y = np.full(len(x), pn[0])
plt.plot(x, y, linestyle='--', color="orange")
plt.plot(x, y0, color="blue")
plt.title("Stan 0")
plt.xlabel("N")
plt.ylabel("P")
plt.xticks(np.arange(1, 21, 1))
plt.grid(True)
plt.show()

#1
print(pn[1])
y = np.full(len(x), pn[1])
plt.plot(x, y, linestyle='--', color="orange")
plt.plot(x, y1, color="red")
plt.title("Stan 1")
plt.xlabel("N")
plt.ylabel("P")
plt.xticks(np.arange(1, 21, 1))
plt.grid(True)
plt.show()

#2
print(pn[2])
y = np.full(len(x), pn[2])
plt.plot(x, y, linestyle='--', color="orange")
plt.plot(x, y2, color="green")
plt.title("Stan 2")
plt.xlabel("N")
plt.ylabel("P")
plt.xticks(np.arange(1, 21, 1))
plt.grid(True)
plt.show()