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

def make_simulation(weight_a, weight_b, c):
    round_numbers = []
    wins = []

    a = 10
    b = 20 - a

    round_counter = 0
    win_counter = 0

    while True:
        if a == 0:
            break
        if a == 20:
            break

        round_counter = round_counter + 1

        a_prev = a
        a, b = make_round(a, b, weight_a, weight_b)

        if (a_prev < a) :
            round_numbers.append(round_counter)
            wins.append(win_counter)

            win_counter = win_counter+1

            round_numbers.append(round_counter)
            wins.append(win_counter)
        else:
            round_numbers.append(round_counter)
            wins.append(win_counter)

    plt.plot(round_numbers, wins, color=c, label="Punkty")
    plt.title("Trajektoria liczby wygranych dla jednego z dwóch graczy A,B")
    plt.xlabel("Numer tury")
    plt.ylabel("Liczba wygranych przez wybranego gracza")
    plt.legend()
    plt.grid(True)



make_simulation(1, 5, "green")
make_simulation(1, 2, "orange")
make_simulation(4, 5, "blue")



plt.show()

