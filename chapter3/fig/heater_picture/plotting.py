from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from numpy import pi
from qy.hardware import heaters

blue='#5555bb'
red='#bb5555'

def show_fit(axes, voltages, counts, parameters, label, offset, hide_ticks=True):
    '''Make a simple plot '''
    axes.text(0.98, 0.9, label, transform=axes.transAxes, va='top', ha='right', fontsize=20)

    fit_voltages=np.linspace(-1, 10, 500)

    # plot without offset
    modparams=list(parameters)
    modparams[0]-=offset
    fit_counts=heaters.fitting.counts_voltage(modparams, fit_voltages)
    axes.plot(fit_voltages, fit_counts, '-', color=blue, lw=1, alpha=.5)

    # plot with offset
    fit_counts=heaters.fitting.counts_voltage(parameters, fit_voltages)
    axes.plot(fit_voltages, fit_counts, '--', color=red, lw=1, alpha=.5)

    # plot the data
    axes.plot(voltages, counts, 'k.', ms=4)

    # organize the axes
    axes.set_xlim(min(fit_voltages), max(fit_voltages))
    axes.set_yticks([])

    if hide_ticks: 
        axes.set_xticklabels(['']*8)
    else:
        axes.set_xlabel('Voltage, V')

    axes.grid(ls='-', color='#eeeeee'); axes.set_axisbelow(1)

def show_phase_voltage(axes, parameters, offset=None, hide_ticks=True):
    ''' Show the phase voltage relation '''
    voltages=np.linspace(0, 7, 500)
    phases=heaters.fitting.phase_voltage(parameters, voltages)
    axes.plot(voltages, phases-offset, '-', color=blue, lw=2)
    axes.plot(voltages, phases, '--', color=red, lw=1)
    axes.set_yticks([i*pi for i in [0, 2]])
    axes.set_yticklabels(['%d$\pi$' % i for i in [0, 2]])
    axes.set_ylim(-pi, pi*3)
    axes.set_xticks(range(0, 8, 2))
    axes.set_ylabel('$\phi$')

    if hide_ticks: 
        axes.set_xticklabels(['']*8)
    else:
        axes.set_xlabel('Voltage, V')

    axes.grid(ls='-', color='#eeeeee')
    axes.set_axisbelow(1)
