from numpy import *
from matplotlib import pyplot as plt

plt.figure(figsize=(7,4))

for i in range(8):
    data=loadtxt(open("data/a%d.csv" % i, "rb"), delimiter="\t", skiprows=1)
    voltage, current=data.T
    plt.plot(voltage, current*1000, 'k.')
    plt.plot(voltage, current*1000, 'k-', alpha=.5)

plt.xlabel('Voltage, V')
plt.yticks(range(0, 100, 20))
plt.ylabel('Current, mA')
plt.savefig('iv_curves.pdf', bbox_inches='tight')
