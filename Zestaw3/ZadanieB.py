import random
import math

from matplotlib import pyplot as plt

'''a) rozkład normalny'''

def polar_method():
    x1 = 1
    x2 = 1

    while((x1*x1)+(x2*x2) > 1):
        x1 = random.random()
        x2 = random.random()

    R2 = (x1*x1)+(x2*x2)
    R = math.sqrt(R2)

    y1 = (math.sqrt((-2)*math.log(R2)))*x1/R
    y2 = (math.sqrt((-2)*math.log(R2)))*x2/R

    return y1, y2

def get_sums_10N():
    number_of_sum = 1000
    s = []

    for j in range(number_of_sum):
        sum = 0
        for i in range(5):
            y1, y2 = polar_method()
            sum = sum + y1 + y2
        s.append(sum)
    print(len(s))
    print((s[1]))
    return s



def get_sums_100N():
    number_of_sum = 1000
    s = []

    for j in range(number_of_sum):
        sum = 0
        for i in range(50):
            y1, y2 = polar_method()
            sum = sum + y1 + y2
        s.append(sum)

    print(len(s))
    print((s[100]))

    return s



def draw_hist_s(s, c, n, name):


    plt.hist(s, bins=30, density=True, color=c)
    plt.title(f"Histogram dla rozkładu {name} i sumy {n} liczb")
    plt.xlabel("Y1")
    plt.ylabel("Gęstość prawdopodobieństwa")

    plt.show()


s10N = get_sums_10N()
s100N = get_sums_100N()


draw_hist_s(s10N, "blue", 10, "normelnego")
draw_hist_s(s100N, "blue", 100, "normalnego")


'''b) rozkład wykładniczy'''

def get_sums_10W(lambd):
    s = []

    for i in range(1000):
        sum = 0
        for i in range(10):
            u = random.random()
            number = -math.log(1 - u) / lambd
            sum = sum+number

        s.append(sum)

    return s


def get_sums_100W(lambd):
    s = []

    for i in range(1000):
        sum = 0
        for i in range(100):
            u = random.random()
            number = -math.log(1 - u) / lambd
            sum = sum + number

        s.append(sum)

    return s


s10J = get_sums_10W(4)
s100J = get_sums_100W(4)

draw_hist_s(s10J, "green", 10, "jednostajnego")
draw_hist_s(s100J, "green", 100, "jednostajnego")


'''c) rozkład jednorodny'''

def get_sums_10J(a, b):
    s = []

    for i in range(1000):
        sum = 0
        for i in range(10):
            number = a + (b - a) * random.random()
            sum = sum+number
        s.append(sum)

    return s


def get_sums_100J(a, b):
    s = []

    for i in range(1000):
        sum = 0
        for i in range(100):
            number = a + (b - a) * random.random()
            sum = sum + number
        s.append(sum)

    return s


s10J = get_sums_10J(1, 6)
s100J = get_sums_100J(1, 6)

draw_hist_s(s10J, "red", 10, "jednostajnego")
draw_hist_s(s100J, "red", 100, "jednostajnego")



'''Twierdzenie opisujące wyniki to centralne twierdzenie graniczne'''


'''Część druga zadania'''


'''a) rozkład normalny'''


def draw_hist_d_log(s, c, name):


    plt.hist(s, bins=50, density=True, color=c)
    plt.title(f"Histogram różnic kolejnych liczb losowych dla rozkładu {name} ze skalą logarytmiczną")
    plt.xlabel("Y1")
    plt.ylabel("Gęstość prawdopodobieństwa")
    plt.yscale('log')

    plt.show()

def draw_hist_d(s, c, name):


    plt.hist(s, bins=50, density=True, color=c)
    plt.title(f"Histogram różnic kolejnych liczb losowych dla rozkładu {name}")
    plt.xlabel("Y1")
    plt.ylabel("Gęstość prawdopodobieństwa")

    plt.show()

def hist_of_diff_n():
    n_set = []

    for i in range(500):
        y1, y2 = polar_method()
        n_set.append(y1)
        n_set.append(y2)


    n_set.sort()

    diff_set = []

    for index in range(len(n_set)):
        if index == len(n_set)-1:
            continue

        diff_set.append(n_set[index+1] - n_set[index])

    draw_hist_d(diff_set, "blue", "normalnego")
    draw_hist_d_log(diff_set, "blue", "normalnego")



hist_of_diff_n()


'''b) rozkład wykładniczy'''

def hist_of_diff_w(lambd):
    n_set = []

    for i in range(1000):
        u = random.random()
        number = -math.log(1 - u) / lambd
        n_set.append(number)


    n_set.sort()

    diff_set = []

    for index in range(len(n_set)):
        if index == len(n_set)-1:
            continue

        diff_set.append(n_set[index+1] - n_set[index])

    draw_hist_d(diff_set, "green", "wykładniczego")
    draw_hist_d_log(diff_set, "green", "wykładniczego")



hist_of_diff_w(4)


'''c) rozkład jednostajny'''

def hist_of_diff_j(a, b):
    n_set = []

    for i in range(1000):
        number = a + (b - a) * random.random()
        n_set.append(number)


    n_set.sort()

    diff_set = []

    for index in range(len(n_set)):
        if index == len(n_set)-1:
            continue

        diff_set.append(n_set[index+1] - n_set[index])

    draw_hist_d(diff_set, "red", "wykładniczego")
    draw_hist_d_log(diff_set, "red", "wykładniczego")


hist_of_diff_j(1, 6)
