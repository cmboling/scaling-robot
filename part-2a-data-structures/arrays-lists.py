# part 2
numbers = list(range(100))
binary = [bin(num)[2:] for num in numbers]
new_numbers = [int(b, 2) for b in binary]

print(binary)

# part 3
import time
import matplotlib.pyplot as plt

times = {}
iterations = 1000
numbers = list(range(20))
for i in range(iterations):
    l = []
    for i in numbers:
        start = time.time()
        l.append(i)
        end = time.time()
        if i not in times:
            times[i] = []
        times[i].append(end - start)

avg_times = []
for i in numbers:
    avg_times.append(sum(times[i]))

plt.bar(numbers, avg_times)
