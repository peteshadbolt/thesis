#!/usr/bin/python
from glob import glob
import os
import subprocess
from datetime import datetime
import anydbm
from matplotlib import pyplot as plt
from numpy import random

def count(filestr):
    ps = subprocess.Popen([r'detex', filestr], stdout=subprocess.PIPE)
    output = subprocess.check_output(('wc'), stdin=ps.stdout)
    newline, word, byte=map(int, filter(lambda x: x!='', output.split(' ')))
    return word

# Write to database
root=os.path.split(__file__)[0]
db = anydbm.open(os.path.join(root, "checkins.db"), "c")
word=count(glob('thesis.tex')[0])
#word=sum(map(count, glob('chapter*/*.tex')))
now=datetime.now().ctime()
db[str(now)]='%d' % word
print 'check_in logged %d words at %s' % (word, str(now))

# Plot
plt.figure(figsize=(10,3))
everything=map(lambda x: [datetime.strptime(x[0], '%a %b %d %H:%M:%S %Y'), x[1]], db.items())
everything=sorted(everything, key=lambda x: x[0])
times, counts=zip(*everything)
plt.plot_date(times, random.normal(0, 1, len(times)), 'k.', ms=6)
plt.xlabel('Date')
plt.xlim(datetime.strptime('14/11/13', '%d/%m/%y'), datetime.strptime('6/1/14', '%d/%m/%y'))
plt.yticks([0], [''])
#plt.yticks([10000, 20000, 30000])
plt.ylim(-10, 10)

import matplotlib.dates as mdates
import matplotlib.cbook as cbook

weeks    = mdates.WeekdayLocator()   # every year
weeksfmt = mdates.DateFormatter('%d/%m')
days      = mdates.DayLocator()  # every month

# Format the ticks
ax=plt.gca()
ax.xaxis.set_major_locator(weeks)
ax.xaxis.set_major_formatter(weeksfmt)
ax.xaxis.set_minor_locator(days)

plt.grid(ls='-', color='#eeeeee', which='minor', alpha=.5, lw=.5)
plt.grid(ls='-', color='#888888', which='major', lw=.5)
#plt.gca().set_axisbelow(1)
plt.savefig('progress.pdf', bbox_inches='tight')

db.close()

