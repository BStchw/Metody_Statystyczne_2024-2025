import math
import random
import numpy as np

from matplotlib import pyplot as plt


def polar_method():
    x1 = 1
    x2 = 1

    while((x1*x1)+(x2*x2) > 1):
        x1 = 1 - random.random()*2
        x2 = 1 - random.random()*2

    R2 = (x1*x1)+(x2*x2)
    R = math.sqrt(R2)

    y1 = (math.sqrt((-2)*math.log(R2)))*x1/R
    y2 = (math.sqrt((-2)*math.log(R2)))*x2/R

    return y1, y2


def analitic_method(x):
    return (1/math.sqrt(2*math.pi))*math.exp(-(x*x)/2)



def draw_hist_polar():
    n = 10000

    y1_values = []
    y2_values = []

    for _ in range(n):
        y1, y2 = polar_method()
        y1_values.append(y1)
        y2_values.append(y2)

    plt.figure(figsize=(12, 6))

    plt.hist(y1_values, bins=30, density=True, color='g')
    plt.title("Histogram Y1")
    plt.xlabel("Y1")
    plt.ylabel("Gęstość prawdopodobieństwa")
    draw_func_analitic()

    plt.show()


    plt.hist(y2_values, bins=30, density=True, color='b')
    plt.title("Histogram Y2")
    plt.xlabel("Y2")
    plt.ylabel("Gęstość prawdopodobieństwa")

    draw_func_analitic()

    plt.show()


def draw_func_analitic():

    x_values = np.linspace(-3, 3, 10000)
    y_values = []

    for x in x_values:
        y_values.append(analitic_method(x))

    plt.plot(x_values, y_values, 'r')




draw_hist_polar()
