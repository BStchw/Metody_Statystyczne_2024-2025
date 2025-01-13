import math
import random
import matplotlib.pyplot as plt

def get_times(lambd, num_of_times):
    t = []

    for i in range(num_of_times):

        u = random.random()
        t_i = -math.log(1 - u) / lambd

        t.append(t_i)

    return t

def simulate_queue_with_little_law(lambda_A, lambda_S, sim_time):
    #lista czasów pomiędzy przyjściami kolejnych zadań
    arrival_times = get_times(lambda_A, int(sim_time * lambda_A * 2))
    #lista czasów obslugi zadań
    service_times = get_times(lambda_S, int(sim_time * lambda_A * 2))

    # harmonogram przyjsc zadań
    arrival_har = []
    # harmonogram obsługi zadań
    service_har = []
    # liczba długość kolejki w każdym momencie przyjścia nowego zadania
    queue_lengths = []
    # liczba zakończonych zadań
    completed_tasks = []

    waiting_times = []  # Czas oczekiwania w kolejce
    times_in_system = []  # Czas spędzony w systemie

    queue = 0
    current_time = 0
    tasks_completed = 0

    for t in arrival_times:
        current_time += t
        arrival_har.append(current_time)

    for i, arrival_time in enumerate(arrival_har):
        #jeśli zadanie jest puste to przechodzi do obsługi lub
        # czas przyjścia nowego zadania (arrival_time) jest późniejszy niż zakończenie obsługi poprzedniego zadania (service_har[-1])
        if len(service_har) == 0 or arrival_time >= service_har[-1]:
            service_start_time = arrival_time
            queue = max(queue - 1, 0)
        else:
            queue += 1
            service_start_time = service_har[-1]

        service_end_time = service_start_time + service_times[i]
        service_har.append(service_end_time)

        waiting_time = service_start_time - arrival_time
        waiting_times.append(waiting_time)

        time_in_system = waiting_time + service_times[i]
        times_in_system.append(time_in_system)

        queue_lengths.append(queue)
        tasks_completed += 1
        completed_tasks.append(tasks_completed)

    L = sum(queue_lengths) / len(queue_lengths)
    W = sum(times_in_system) / len(times_in_system)
    lambda_system = len(arrival_times) / sim_time

    return L, W, lambda_system


#λA=1/20, λS=1,15
# a) E(liczba zadań w systemie) od λA
lambda_A_values = []
L_values_A = []

for x in range(1, 21):
    lambda_A = x / 100
    lambda_A_values.append(lambda_A)
    average_queue_length, _, _ = simulate_queue_with_little_law(lambda_A, 1/15, 10000)
    L_values_A.append(average_queue_length)

plt.figure()
plt.plot(lambda_A_values, L_values_A, marker='o')
plt.title('Średnia liczba zadań w systemie od λA')
plt.xlabel('λA')
plt.ylabel('E[L]')
plt.grid(True)
plt.show()

# b) E(liczba zadań w systemie) od λS
lambda_S_values = [x / 100 for x in range(5, 21)]
L_values_S = [simulate_queue_with_little_law(1/20, lambda_S, 10000)[0] for lambda_S in lambda_S_values]

plt.figure()
plt.plot(lambda_S_values, L_values_S, marker='o')
plt.title('Średnia liczba zadań w systemie od λS')
plt.xlabel('λS')
plt.ylabel('E[L]')
plt.grid(True)
plt.show()

# c) E(liczba zadań w systemie) od r = λA/λS
r_values = [x / 100 for x in range(1, 20)]
L_values_r = [simulate_queue_with_little_law(r * (1/15), 1/15, 10000)[0] for r in r_values]

plt.figure()
plt.plot(r_values, L_values_r, marker='o')
plt.title('Średnia liczba zadań w systemie od r = λA/λS')
plt.xlabel('r = λA/λS')
plt.ylabel('E[L]')
plt.grid(True)
plt.show()
