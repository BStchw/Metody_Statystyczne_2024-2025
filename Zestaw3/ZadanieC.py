import random
import time

import numpy as np


# Funkcja gęstości rozkładu normalnego
def normal_pdf(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Maksymalna wartość funkcji gęstości rozkładu normalnego dla N(0,1)
f_max = normal_pdf(0)


'''Pierwszy krok'''

def acceptance_rejection_1(xmin=-5, xmax=5):
    accepted_points = []

    for i in range(10000):
        # Generowanie zmiennych losowych zgodnie z podanym wzorem
        U1, U2 = random.random(), random.random()
        x = xmin + (xmax - xmin) * U1
        r = U2

        # Kryterium akceptacji: r < f(x) / f_max
        if r < normal_pdf(x) / f_max:
            accepted_points.append(x)

    return accepted_points

# Symulacja i pomiar czasu
start_time = time.time()
accepted_points = acceptance_rejection_1()
elapsed_time = time.time() - start_time

# Obliczanie procentowego udziału zaakceptowanych punktów
percent_accepted = (len(accepted_points) / 10000) * 100

# Wyniki
print(f"Liczba zaakceptowanych punktów: {len(accepted_points)}")
print(f"Całkowita liczba wygenerowanych punktów: 10000")
print(f"Procent zaakceptowanych punktów: {percent_accepted:.2f}%")
print(f"Czas symulacji: {elapsed_time:.4f} s")
print("\n")


'''Drugi krok'''

def acceptance_rejection_2(n_points, xmin=-5, xmax=5):
    accepted_points = []
    count = 0
    while len(accepted_points) < n_points:
        # Generowanie zmiennych losowych zgodnie z podanym wzorem
        U1, U2 = random.random(), random.random()
        x = xmin + (xmax - xmin) * U1
        r = U2

        # Kryterium akceptacji: r < f(x) / f_max
        if r < normal_pdf(x) / f_max:
            accepted_points.append(x)
        count += 1

    return accepted_points, count

# Symulacja i pomiar czasu
n_points = 10000
start_time = time.time()
accepted_points, total_generated = acceptance_rejection_2(n_points)
elapsed_time = time.time() - start_time

# Obliczanie procentowego udziału zaakceptowanych punktów
percent_accepted = (n_points / total_generated) * 100

# Wyniki
print(f"Liczba zaakceptowanych punktów: {n_points}")
print(f"Całkowita liczba wygenerowanych punktów: {total_generated}")
print(f"Procent zaakceptowanych punktów: {percent_accepted:.2f}%")
print(f"Czas symulacji: {elapsed_time:.4f} s")


