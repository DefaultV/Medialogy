import random
import matplotlib.pyplot as plt
from statistics import mean


x = []
y = []
mod = []


for i in range(10):
    x.append(i)
for j in range(10):
    y.append(j)


for i in range(10):
    mod.append(y[i] + random.randint(-2, 2))

meanmod = 0
for i in range(10):
    meanmod += x[i] * mod[i]

m_mod = (mean(x)*mean(mod)) - (meanmod)/pow((mean(x)),2) - pow(mean(x), 2)
print(m_mod)


err = 0

for i in range(10):
    err += abs(y[i] - mod[i])^2

print(err)
plt.scatter(x, y)
plt.scatter(x, mod)
plt.plot(x, mod)
plt.show()

arr = []

arr.append(100)
for x in range(1, 10):
    arr.append(arr[x-1]*2)

random.shuffle(arr)

#for x in arr:i
#    print(x)



def fun():
    text = input("Choose a briefcase! [ "+ str(len(arr)-1) +" ]\n")
    index = int(text)
    briefcase = arr[index]
    arr.remove(briefcase)
        #for x in arr:
        #    print(x)
    offer = random.randint(0, briefcase - random.randint(briefcase/5, briefcase))
    text = input("Deal or no deal!:\n" + str(offer) + " -> DEBUG : " + str(briefcase) + "\n")
    if (text == "y"):
        print("You got: " + str(offer))
    if (text == "n"):
        fun()
