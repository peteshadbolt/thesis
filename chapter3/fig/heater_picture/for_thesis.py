import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from collections import defaultdict
from heater_fitting import *
from qy import util

def load_data(filename):
    ''' Load data from a text file, return as a dict of numpy arrays '''
    text_file=open(filename, 'r')
    curves=defaultdict(list)
    for line in text_file:
        split_point=line.find(',')
        curves['v'].append(float(line[:split_point]))
        for key, value in eval(line[split_point+1:]).items():
            curves[key.lower()].append(value)
    return {key: np.array(value) for key, value in curves.items()}

def fit_and_plot(axes, voltages, counts, label):
    '''Make a simple plot '''
    #axes.text(0.07, 0.95, label, transform=axes.transAxes, va='top', ha='left', fontsize=12)
    fit=get_fit(voltages, counts)
    axes.plot(fit['voltages'], fit['counts'], '-', color='#5555bb', lw=1)
    axes.plot(voltages, counts, 'k.', ms=4)
    #axes.set_ylim(0, max(counts)*1.2)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.grid(ls='-', color='#dddddd')
    axes.set_axisbelow(1)
    return fit['parameters']

def show_phase_voltage(axes, parameters):
    ''' Show the phase voltage relation '''
    voltages=np.linspace(0, 7, 500)
    phases=phasefunc(parameters, voltages)
    axes.plot(voltages, phases, '-', color='#5555bb', lw=2)
    #axes.text(0.5, 0.5, 'Offset = %.3f$\pi$' % (parameters[1]/np.pi), transform=axes.transAxes, va='center', ha='center')
    axes.set_xticks(range(0, 7, 2))
    #axes.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    axes.grid(ls='-', color='#dddddd')
    axes.set_axisbelow(1)
    axes.set_yticks([])
    #axes.set_xlabel('Voltage')
    #axes.set_ylabel('Phase')
    axes.set_ylim(0, 3*np.pi)

def get_pattern(curves, pattern):
    ''' Easy way to write a+b '''
    return np.sum(np.array([curves[label] for label in pattern.split('+')]), axis=0)

if __name__=='__main__':
    data=map(load_data, ['../fringe/data/out_h%d.txt' % i for i in range(8)])
    plt.figure(figsize=(13, 3))
    plt.rc('font', size=13)
    gs = gridspec.GridSpec(2, 8, wspace=.05, hspace=0.05, left=.03, right=.99, top=.98)

    # specify the fringes that we care about
    fringes=[(0, 'b+c'), (1, 'a+c'), (3, 'a+c'), (6, 'a'), (5, 'b'), (7, 'b'), (2, 'a'), (4, 'a')]
    for heater_index, pattern in fringes:
        # bits and pieces
        curves=data[heater_index]
        voltages=curves['v']; counts=get_pattern(curves, pattern)
        label='Heater %d (%s)' % (heater_index, pattern.upper())

        # make the three plots
        axes=plt.subplot(gs[0, heater_index])
        parameters = fit_and_plot(axes, voltages, counts, label)

        if heater_index==0: 
            axes.set_ylabel('Intensity (A.U.)')
            
        axes=plt.subplot(gs[1, heater_index])
        show_phase_voltage(axes, parameters)

        if heater_index==0: 
            axes.set_yticks([i*np.pi for i in range(-5, 5)])
            labs=['$%d\\pi$' % i for i in range(-5, 5)]
            axes.set_yticklabels(labs)
            axes.set_ylim(0, 3*np.pi)
        #show_counts_phase(plt.subplot(gs[heater_index, 2]), parameters, voltages, counts)

    # save to pdf
    plt.savefig('for_thesis.pdf')

