import matplotlib.pyplot as plt
import random
from statistics import mean
import math
x = []
y = []
m = [random.randint(0, 25), random.randint(0,25)]

x_b = []
y_b = []

x_c = []
y_c = []

x_d = []
y_d = []

k = 3

for i in range(0, k):
    m.append(random.randint(0, 25))
    m.append(random.randint(0, 25))

for i in range(0, 20):
    x.append(random.randint(0, 10))
    y.append(random.randint(0, 10))

plt.scatter(x, y, color='g')

for i in range(20, 40):
    x_b.append(random.randint(0, 10))
    y_b.append(random.randint(15, 25))


plt.scatter(x_b, y_b, color='r')

for i in range(40, 60):
    x_c.append(random.randint(15, 25))
    y_c.append(random.randint(0, 10))

plt.scatter(x_c, y_c, color="b")

for i in range(40, 60):
    x_d.append(random.randint(15, 25))
    y_d.append(random.randint(15, 25))

plt.scatter(x_d, y_d, color="y")


for i in range(0, k):
    plt.scatter(m[i*2],m[(i+1)*2], color='k', marker='x')
##########


list_g = []
list_r = []
list_b = []
list_y = []

for i in range(20):
    list_g.append(abs((x[i] - m[0])^2 - (y[i] - m[1])^2))
    list_r.append(abs((x_b[i] - m[0])^2 - (y_b[i] - m[1])^2))
    list_b.append(abs((x_c[i] - m[0])^2 - (y_c[i] - m[1])^2))
    list_y.append(abs((x_d[i] - m[0])^2 - (y_d[i] - m[1])^2))

list.sort(list_g)
list.sort(list_r)
min_g = 0
min_r = 0
for i in range(5):
    min_g += list_g[i]
    min_r += list_r[i]


if min_g < min_r:
    print("Belongs to Green")
else:
    print("Belongs to Red")


plt.show()
