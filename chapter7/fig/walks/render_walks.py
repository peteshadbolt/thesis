from qy.simulation import linear_optics as lo
from matplotlib import pyplot as plt
from matplotlib import cm
from numpy import *

w=lo.quantum_walk(51)
s=lo.simulator(w, nphotons=1)
s.set_input_state([w.nmodes/2])

# compute data
data=[]
maxt=38
#for t in linspace(0, maxt, 500):
    #w.set_time(t)
    #data.append(s.get_probabilities())
#data=array(data)
#save('data.npy', data)
data=load('data.npy')

plt.imshow(pow(data, 1/4.), cm.Reds, interpolation='nearest')

# overlay
for cut_time in arange(20, len(data), 40):
    w.set_time(cut_time)
    q=data[cut_time]/max(data[cut_time])
    plt.plot(arange(w.nmodes), cut_time-26*q, 'k-', lw=1)
    #plt.plot([0, w.nmodes], [maxt-cut_time]*2, '-', alpha=.5)


plt.axis('off')
plt.gca().set_aspect(.2)
plt.savefig('single_photon_walk.png', bbox_inches='tight', dpi=200)
