import numpy as np
import random
import math
import matplotlib.pyplot as plt
import os


r = 5
n = 10000000
x = 0
y = 0
d_c = 1
d_s = 1
d = 0
count = 1
p = 0
error = 1
combo = [p, error]
values = [[], []]

interval = np.linspace(-r, r, n)
max = int(input("How many iterations (in millions) you want to perform: "))

while(1):
    for i in range(1000000):
        x = random.choice(interval)
        y = random.choice(interval)
        d = x*x + y*y
        d_s = d_s + 1
        if d<r*r:
            d_c = d_c + 1
    p = 4*(d_c/d_s)
    error = abs((math.pi-p)/math.pi)
    values[0].append(p)
    values[1].append(count)
    if error < combo[1]:
        combo = [p, error]
        print('\nBest Result:')
        print("Iteration " + str(count) + " M : " + str(combo[0]) + "  \tERROR: " + str(combo[1]) + '\n')
    else:
        print("Computing...")
    count = count+1
    if count >= max:
        print('\n----END----\n')
        print("Iterations done: " + str(count) + " M\n" + "Best Result: " + str(combo[0]) + "\nERROR: " + str(combo[1]) + '\n')
        break

plt.plot(values[1], values[0])
plt.xlabel("Iterations (millions)")
plt.ylabel("PI approximation")
plt.show()
