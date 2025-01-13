import math
import random

from matplotlib import pyplot as plt


def get_times(lambd, num_of_times):
    t = []

    for i in range(num_of_times):

        u = random.random()
        t_i = -math.log(1 - u) / lambd

        t.append(t_i)

    return t

def simulate_queue(lambda_A, lambda_S, sim_time):
    arrival_times = get_times(lambda_A, int(sim_time * lambda_A * 2))
    service_times = get_times(lambda_S, int(sim_time * lambda_A * 2))

    #harmonogram przyjsc zadań
    arrival_har = []
    #harmonogram obsługi zadań
    service_har = []
    #liczba długość kolejki w każdym momencie przyjścia nowego zadania
    queue_lengths = []
    #liczba zakończonych zadań
    completed_tasks = []

    queue = 0
    current_time = 0
    tasks_completed = 0

    for t in arrival_times:
        current_time += t
        arrival_har.append(current_time)

    for i, arrival_time in enumerate(arrival_har):
        # Obsługa pierwszego klienta
        if len(service_har) == 0 or arrival_time >= service_har[-1]:
            service_start_time = arrival_time
        else:
            queue += 1
            service_start_time = service_har[-1]

        service_end_time = service_start_time + service_times[i]
        service_har.append(service_end_time)

        # Aktualizacja liczby zadań w kolejce i wykonanych zadań
        queue_lengths.append(queue)
        tasks_completed += 1
        completed_tasks.append(tasks_completed)

        # Jeśli kolejka ma zadanie, zmniejszamy ją
        while len(service_har) > 0 and service_har[0] <= arrival_time:
            service_har.pop(0)  # Usuwamy zakończone zadanie
            if queue > 0:
                queue -= 1

    return arrival_har, service_har, queue_lengths, completed_tasks


'''λA = 1/20 i λS = 1/15'''

arrival_har, service_har, queue_lengths, completed_tasks = simulate_queue(1/20, 1/15, 1000)

# Wykres liczby zadań w kolejce
plt.step(arrival_har[:len(queue_lengths)], queue_lengths)
plt.title(f"Liczba zadań w kolejce z parametrami: λA = 1/20 i λS = 1/15 \n")
plt.xlabel("Czas")
plt.ylabel("Liczba zadań w kolejce")
plt.grid(True)
plt.show()

# Wykres liczby wykonanych zadań w czasie
plt.step(arrival_har[:len(completed_tasks)], completed_tasks)
plt.title(f"Liczba wykonanych zadań z parametrami: λA = 1/20 i λS = 1/15 \n")
plt.xlabel("Czas")
plt.ylabel("Liczba wykonanych zadań")
plt.grid(True)
plt.show()

'''λA = 1/20 i λS = 1/100'''

arrival_har, service_har, queue_lengths, completed_tasks = simulate_queue(1/20, 1/100, 1000)

# Wykres liczby zadań w kolejce
plt.step(arrival_har[:len(queue_lengths)], queue_lengths)
plt.title(f"Liczba zadań w kolejce w czasie z parametrami: λA = 1/20 i λS = 1/100 \n")
plt.xlabel("Czas")
plt.ylabel("Liczba zadań w kolejce")
plt.grid(True)
plt.show()

# Wykres liczby wykonanych zadań w czasie
plt.step(arrival_har[:len(completed_tasks)], completed_tasks)
plt.title(f"Liczba wykonanych zadań z parametrami: λA = 1/20 i λS = 1/100\n")
plt.xlabel("Czas")
plt.ylabel("Liczba wykonanych zadań")
plt.grid(True)
plt.show()

'''λA = 1/20 i λS = 1/5'''

arrival_har, service_har, queue_lengths, completed_tasks = simulate_queue(1/20, 1/5, 1000)

# Wykres liczby zadań w kolejce
plt.step(arrival_har[:len(queue_lengths)], queue_lengths)
plt.title(f"Liczba zadań w kolejce z parametrami: λA = 1/20 i λS = 1/5 \n")
plt.xlabel("Czas")
plt.ylabel("Liczba zadań w kolejce")
plt.grid(True)
plt.show()

# Wykres liczby wykonanych zadań w czasie
plt.step(arrival_har[:len(completed_tasks)], completed_tasks)
plt.title(f"Liczba wykonanych zadań z parametrami: λA = 1/20 i λS = 1/5\n")
plt.xlabel("Czas")
plt.ylabel("Liczba wykonanych zadań")
plt.grid(True)
plt.show()