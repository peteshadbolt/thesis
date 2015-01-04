import numpy as np
from numpy import pi
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from collections import defaultdict
from qy import util
from qy.hardware import heaters
import plotting
import sys

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

def get_summed_counts(curves, pattern):
    ''' Easy way to write a+b '''
    return np.sum(np.array([curves[label] for label in pattern.split('+')]), axis=0)

if __name__=='__main__':
    # Load the experimental data
    data=map(load_data, ['fringe_data/out_h%d.txt' % (i+1) for i in range(8)])

    # Prepare to write the calibration table to disk
    calibration_table=heaters.calibration_table()

    # Choose the curve offsets
    offsets=[0,pi/2,0,pi/2,0,0,0,0]

    # Step through each curve, doing the fit
    fringes={0: 'b+d', 1: 'a+c', 3: 'a+c', 6: 'a', 5: 'b', 7: 'b', 2: 'a', 4: 'a'}
    for heater_index, pattern in fringes.items():
        voltages=data[heater_index]['v']
        counts=get_summed_counts(data[heater_index], pattern)
        guess = [0, .1, max(counts), (max(counts)-min(counts))/float(max(counts))]
        fit_parameters=heaters.fitting.fit_fringe(voltages, counts, guess=guess, nfits=2)
        fit_parameters[0]+=offsets[heater_index]

        calibration_table.set_curve(heater_index, fit_parameters)

    # Write the table to disk
    calibration_table.save()

    # Start making plots
    plt.figure(figsize=(18, 10))
    plt.rc('font', size=20)
    gs = gridspec.GridSpec(8, 3, width_ratios=[3,1,2], wspace=.22, hspace=0)

    # plotting phase-voltage curves etc
    for heater_index, pattern in fringes.items():
        # Bits and pieces
        parameters=calibration_table.get_parameters(heater_index)
        voltages=data[heater_index]['v']
        counts=get_summed_counts(data[heater_index], pattern)
        label='$\\phi_%d(%s)$' % (heater_index, pattern.upper())

        # Make the three plots
        offset=offsets[heater_index]
        plotting.show_fit(plt.subplot(gs[heater_index, 0]), voltages, counts, parameters, label, offset, hide_ticks=heater_index!=7)
        plotting.show_phase_voltage(plt.subplot(gs[heater_index, 1]), parameters, offset, hide_ticks=heater_index!=7)

    # look at the decoupling
    axes=plt.subplot(gs[0:3, 2])
    data=np.loadtxt(open("decoupling_data/slow.txt", "rb"), delimiter="\t", skiprows=1).T
    axes.plot(data[0], data[1], 'r-')
    data=np.loadtxt(open("decoupling_data/fast.txt", "rb"), delimiter="\t", skiprows=1).T
    axes.plot(data[0], data[1], 'b-')
    axes.set_xlabel('Time, s')
    axes.set_yticks(range(50, 200, 40))
    axes.set_yticklabels(['']*(300/40))
    axes.set_ylabel('Intensity, A. U.')
    axes.set_xlim(0, 60)
    axes.grid(ls='-', color='#eeeeee'); axes.set_axisbelow(1)

    # inset: timing
    data=np.loadtxt(open("decoupling_data/slow.txt", "rb"), delimiter="\t", skiprows=1).T
    axes=plt.axes([.69, .64, .04, .05])
    axes.plot(data[0], data[1], 'r-')
    #axes.set_xlabel('Time, s')
    axes.set_yticks([])
    axes.set_xlim(9, 10)
    axes.set_xticks([9,10])


    # now do the iv curves
    axes=plt.subplot(gs[4:8, 2])
    for i in range(8):
        data=np.loadtxt(open("iv_data/a%d.csv" % i, "rb"), delimiter="\t", skiprows=1)
        voltage, current=data.T
        axes.plot(voltage, current*1000, 'k.')
        axes.plot(voltage, current*1000, 'k-', alpha=.5)

    axes.grid(ls='-', color='#eeeeee'); axes.set_axisbelow(1)
    plt.xlabel('Voltage, V')
    plt.yticks(range(0, 100, 20))
    plt.ylabel('Current, mA')


    # and then the decoupling plot


    # Save to pdf
    plt.savefig('heater_picture.pdf', bbox_inches='tight')

