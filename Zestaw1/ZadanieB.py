import random
import matplotlib.pyplot as plt



def make_round(a, b, weight_a, weight_b):

    prop_list = [weight_a, weight_b]

    won = random.choices(["A", "B"], weights=prop_list)[0]

    if won == "A":
        a += 1
        b -= 1
    else:
        a -= 1
        b += 1

    return a, b


def count_r_i(a, M, p):
    q = 1 - p
    if p == q:
        return (M - a) / M
    elif p == 0 or q == 0:
        return 0 if p == 0 else 1
    else:
        return (((q / p)**a) - ((q / p)**M)) / (1 - (q / p)**M)



def make_simulation():
    a_values = []
    r = []


    for a_first in range(0, 101):
        counter = 0

        for i in range(0, 100):

            a = a_first
            b = 100 - a_first

            while True:
                if a == 0:
                    counter = counter+1
                    break
                if a == 100:
                    break

                a, b = make_round(a, b, 1, 1)

        a_values.append(a_first)
        r.append(counter/100)

    plt.scatter(a_values, r, color="red", label="Punkty")
    plt.title("Wykres symulacji")
    plt.xlabel("a")
    plt.ylabel("Prawdopodobieństwo ruiny A")
    plt.legend()
    plt.grid(True)
    plt.show()

def make_analitic_simulation():
    a_values = []
    r = []

    for a in range(0, 101):

        b = 100 - a


        a_values.append(a)
        r.append(count_r_i(a, a+b, 0.5))

    plt.scatter(a_values, r, color="blue", label="Punkty")
    plt.title("Wykres symulacji")
    plt.xlabel("a")
    plt.ylabel("Prawdopodobieństwo ruiny A")
    plt.legend()
    plt.grid(True)
    plt.show()



make_simulation()
make_analitic_simulation()
