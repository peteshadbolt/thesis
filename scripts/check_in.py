#!/usr/bin/python
from glob import glob
import os, sys
import subprocess
from datetime import datetime
import anydbm
from matplotlib import pyplot as plt

def count(filestr):
    ps = subprocess.Popen([r'detex', filestr], stdout=subprocess.PIPE)
    output = subprocess.check_output(('wc'), stdin=ps.stdout)
    newline, word, byte=map(int, filter(lambda x: x!='', output.split(' ')))
    return word

# Write to database
root=os.path.split(__file__)[0]
db = anydbm.open(os.path.join(root, "checkins.db"), "c")
word=count(glob(sys.argv[1])[0])
#word=sum(map(count, glob('chapter*/*.tex')))
now=datetime.now().ctime()
db[str(now)]='%d' % word
print 'check_in logged %d words at %s' % (word, str(now))

# Plot
plt.subplot(211)
everything=map(lambda x: [datetime.strptime(x[0], '%a %b %d %H:%M:%S %Y'), x[1]], db.items())
everything=sorted(everything, key=lambda x: x[0])
times, counts=zip(*everything)
plt.plot_date(times, counts, '-', lw=.5, color='#aaaaaa')
plt.plot_date(times, counts, 'k.', ms=2)
plt.xlabel('Date')
plt.ylabel('Words')
plt.xlim(datetime.strptime('14/11/13', '%d/%m/%y'), datetime.strptime('5/2/14', '%d/%m/%y'))
plt.ylim(0, 55000)
plt.yticks([10000, 20000, 30000, 40000, 50000])

import matplotlib.dates as mdates
import matplotlib.cbook as cbook

weeks    = mdates.WeekdayLocator()   # every year
weeksfmt = mdates.DateFormatter('%d/%m')
days      = mdates.DayLocator()  # every month

# format the ticks
ax=plt.gca()
ax.xaxis.set_major_locator(weeks)
ax.xaxis.set_major_formatter(weeksfmt)
ax.xaxis.set_minor_locator(days)

plt.grid(ls='-', color='#eeeeee', which='minor', alpha=.5)
plt.grid(ls='-', color='#888888', which='major', lw=1)
#plt.gca().set_axisbelow(1)
plt.subplot(212)

hours=[t.hour for t in times]
plt.hist(hours, bins=23, color='black', ec='black', histtype='step')
plt.xlim(0, 23)
plt.xticks(range(24))
plt.yticks([0, 45])
plt.xlabel('Time of day')
plt.xlabel('Number of commits')

plt.savefig('progress.pdf', bbox_inches='tight')

db.close()

