import random
import matplotlib.pyplot as plt

'''A - gracz A
B - gracz B
a - kapitał gracza A
b - kapitał gracza B
pA - prawdopodobieństwo wygrania tury przez gracza A
pB - prawdopodobieństwo wygrania tury przez gracza B
qA - prawdopodobieństwo przegrania tury przez gracza A
qB - prawdopodobieństwo przegrania tury przez gracza B
'''


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
    pa = []
    r = []

    for j in range(0, 100):
        counter = 0
        for i in range(0, 100):

            a = 50
            b = 50

            while True:
                if a == 0:
                    counter = counter+1
                    break
                if a == 100:
                    break

                a, b = make_round(a, b, j, 100-j)

        pa.append(j/100)
        r.append(counter/100)

    plt.scatter(pa, r, color="red", label="Punkty")
    plt.title("Wykres symulacji")
    plt.xlabel("Prawdopodobieństwo wygranej rundy A")
    plt.ylabel("Prawdopodobieństwo ruiny A")
    plt.legend()
    plt.grid(True)
    plt.show()


def make_analitic_simulation():
    pa = []
    r = []

    for j in range(0, 100):
        p = j / 100
        counter = 0

        for i in range(100):
            a, b = 50, 50

            while True:
                if a == 0:
                    counter += 1
                    break
                if a == 100:
                    break

                a, b = make_round(a, b, j, 100 - j)

        pa.append(p)
        r.append(count_r_i(50, 100, p))

    plt.scatter(pa, r, color="blue", label="Punkty")
    plt.title("Wykres symulacji analityczny")
    plt.xlabel("Prawdopodobieństwo wygranej rundy A")
    plt.ylabel("Prawdopodobieństwo ruiny A")
    plt.legend()
    plt.grid(True)
    plt.show()


make_simulation()
make_analitic_simulation()
