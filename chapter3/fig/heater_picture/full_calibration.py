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
    data=map(load_data, ['../fringe/data/out_h%d.txt' % i for i in range(8)])

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
    plt.figure(figsize=(18, 17))
    plt.rc('font', size=20)
    gs = gridspec.GridSpec(8, 3, width_ratios=[3,1,2], wspace=.08)
    for heater_index, pattern in fringes.items():
        # Bits and pieces
        parameters=calibration_table.get_parameters(heater_index)
        voltages=data[heater_index]['v']
        counts=get_summed_counts(data[heater_index], pattern)
        label='Heater %d (%s)' % (heater_index, pattern.upper())

        # Make the three plots
        offset=offsets[heater_index]
        plotting.show_fit(plt.subplot(gs[heater_index, 0]), voltages, counts, parameters, label, offset)
        plotting.show_phase_voltage(plt.subplot(gs[heater_index, 1]), parameters, offset)
        plotting.show_counts_phase(plt.subplot(gs[heater_index, 2]), parameters, voltages, counts, offset)

    # Save to pdf
    plt.savefig('full_calibration.pdf', bbox_inches='tight')

