import random
import numpy as np
from matplotlib import pyplot as plt


P = np.array([[0.64, 0.32, 0.04], [0.4, 0.5, 0.1], [0.25, 0.5, 0.25]])

def exp_r_g(startNode):

        count0 = 0
        count1 = 0
        count2 = 0

        currentNode = startNode

        prop_list0 = P[0]
        prop_list1 = P[1]
        prop_list2 = P[2]

        x = []

        prop_by_n0 = []
        prop_by_n1 = []
        prop_by_n2 = []


        for i in range(0, 10000):

            x.append(i+1)

            if currentNode == 0:
                count0 = count0+1
                currentNode = random.choices([0, 1, 2], weights=prop_list0)[0]
            elif currentNode == 1:
                count1 = count1+1
                currentNode = random.choices([0, 1, 2], weights=prop_list1)[0]
            elif currentNode == 2:
                count2 = count2+1
                currentNode = random.choices([0, 1, 2], weights=prop_list2)[0]

            if count0 == 0:
                prop_by_n0.append(0)
            else:
                prop_by_n0.append(count0/(i + 1))
            if count1 == 0:
                prop_by_n1.append(0)
            else:
                prop_by_n1.append(count1/(i + 1))
            if count2 == 0:
                prop_by_n2.append(0)
            else:
                prop_by_n2.append(count2/(i + 1))

        rg = np.array([count0/10000, count1/10000, count2/10000])

        print(f"Rozkład graniczny: {rg}")

        y = np.full(len(x), rg[0])
        plt.plot(x, y, linestyle='--', color="orange")
        plt.plot(x, prop_by_n0, color="blue")
        plt.title(f"Stan 0 przy starcie z {startNode}")
        plt.xlabel("N")
        plt.ylabel("P")
        plt.grid(True)
        plt.show()

        y = np.full(len(x), rg[1])
        plt.plot(x, y, linestyle='--', color="orange")
        plt.plot(x, prop_by_n1, color="red")
        plt.title(f"Stan 1 przy starcie z {startNode}")
        plt.xlabel("N")
        plt.ylabel("P")
        plt.grid(True)
        plt.show()

        y = np.full(len(x), rg[2])
        plt.plot(x, y, linestyle='--', color="orange")
        plt.plot(x, prop_by_n2, color="green")
        plt.title(f"Stan 2 przy starcie z {startNode}")
        plt.xlabel("N")
        plt.ylabel("P")
        plt.grid(True)
        plt.show()

exp_r_g(0)
#exp_r_g(1)
#exp_r_g(2)

