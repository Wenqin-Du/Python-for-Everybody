import random
import matplotlib.pyplot as plt

results = []
times = 20
random.seed(102)

for i in range(150):
    total = 0
    for j in range(times):
        total += random.randint(1, 6)
    results.append(total/times)

#  print(results)

#  plt.bar(range(len(results)), results)
#  plt.show()

plt.hist(results, bins=15, density=0, facecolor="blue", edgecolor="yellow", alpha=0.7)
plt.show()
