from qy.simulation import linear_optics as lo
from matplotlib import pyplot as plt
from matplotlib import cm
from numpy import *

w=lo.quantum_walk(51)
s=lo.simulator(w, nphotons=2)
s.set_input_state([w.nmodes/2, w.nmodes/2+1])

# compute data
data=[]
maxt=38
w.set_time(18)

data=zeros((w.nmodes, w.nmodes))
for i in range(w.nmodes):
    for j in range(w.nmodes):
        data[i,j]=s.get_probabilities(patterns=[sorted([i,j])])
#save('data.npy', data)
#data=load('data.npy')

plt.matshow(sqrt(data), cmap=cm.Reds, interpolation='nearest')

plt.axis('off')
plt.gca().set_aspect(1)
plt.savefig('two_photon.png', bbox_inches='tight', dpi=150)
