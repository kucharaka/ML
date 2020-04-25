import random as rnd
import matplotlib.pyplot as plt

s, s1, k, b = 0, 0, 1, 1
y1 = []
x = [l for l in range(16, 100)]
y = [108 + rnd.randint(-25, 25) + 2 * l for l in x]
for i in range(60000):
    for j in range(0, 84):
        s += ((b + k * x[j]) - y[j]) * x[j]
        s1 += ((b + k * x[j]) - y[j])
    k -= (0.0006 * 0.01 * s)
    b -= (0.0006 * 0.01 * s1)
    s, s1 = 0, 0
for i in x:
    y1.append(b + k * i)

plt.plot(x, y, 'ro', x, y1)
plt.show()
