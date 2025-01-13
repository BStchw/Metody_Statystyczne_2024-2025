import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson


def get_times(lambd, num_of_times):
    t = []

    for i in range(num_of_times):

        u = random.random()
        t_i = -math.log(1 - u) / lambd

        t.append(t_i)

    return t


'''Pierwsza część'''

def trajectory(num_of_times):
    jump = []
    actual_time = 0
    actual_jump = 0
    times_s = []

    t = get_times(1, num_of_times)

    for t_i in t:

        actual_time += t_i
        actual_jump += 1

        times_s.append(actual_time)
        jump.append(actual_jump)

    return times_s, jump


times_s, jump = trajectory(10)

plt.step(times_s, jump, color="red")
plt.title("Trajektoria procesu Poissona")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)
plt.show()

'''Druga część'''


def get_jump_count(trajectories, t_i):
    results = []

    for times_s, jumps in trajectories:
        for i in range(len(times_s)):
            if times_s[i] > t_i:  # Pierwszy moment przekroczenia t
                results.append(jumps[i])  # Dodajemy liczbę skoków przed przekroczeniem
                break

    return results



def draw_hist(results, t):

    plt.hist(results, bins=np.arange(0, max(results) + 2) - 0.5, density=True, color='blue', align='mid')
    plt.title(f"Histogram t={t}")
    plt.xlabel("Skok")
    plt.ylabel("Gęstość prawdopodobieństwa")

    k_values = np.arange(0, max(results) + 1)
    poisson_pmf = poisson.pmf(k_values, t)
    plt.plot(k_values, poisson_pmf, color='red', linestyle='-', label='Rozkład Poissona')

    # Rysowanie wykresu
    plt.plot(k_values, poisson_pmf, color='red')
    plt.title(f"Rozkład Poissona (t = {t})")
    plt.xlabel("Liczba zdarzeń (k)")
    plt.ylabel("Prawdopodobieństwo P(k)")

    plt.show()


def r_prop():
    trajectories = []

    for i in range(10000):
        times_s, jumps = trajectory(200)
        trajectories.append((times_s, jumps))

    result_1 = get_jump_count(trajectories, 1)
    result_20 = get_jump_count(trajectories, 20)
    result_90 = get_jump_count(trajectories, 90)

    draw_hist(result_1, 1)
    draw_hist(result_20, 20)
    draw_hist(result_90, 90)


r_prop()


