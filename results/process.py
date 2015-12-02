#!/usr/bin/env python

print "\nProcessing..."

import os 
import glob

try:
    import numpy as np # Numeric calculation
    import pandas as pd # General purpose data analysis library
    import squeak # For mouse data
except:
    raise Exception("\
Whoops, you're missing some of the dependencies you need to run this script.\n\
You need to have numpy, pandas, and squeak installed.")

this_dir = os.path.abspath('.')
print "Running in %s\n\
Checking for .csv files in %s" % (this_dir, os.path.join(this_dir, 'data'))

datafiles = glob.glob('data/*.csv')
print "%i files found:" % len(datafiles)
print '\n'.join(datafiles)



data = pd.concat(
    [pd.DataFrame(pd.read_csv(datafile)) 
     for datafile in datafiles])

data['t'] = data.tTrajectory.map(squeak.list_from_string)
data['x'] = data.xTrajectory.map(squeak.list_from_string)
data['y'] = data.yTrajectory.map(squeak.list_from_string)

data['y'] = data.y * -1 # Reverse y axis
data['x'] = data.x.map(squeak.remap_right) # Flip the leftward responses
data['x'] = data.x.map(squeak.normalize_space)
data['y'] = data.y.map(squeak.normalize_space) * 1.5


# Normalized time
data['nx'], data['ny'] = zip(*[squeak.even_time_steps(x, y, t) 
                               for x, y, t, in zip(data.x, data.y, data.t)])

# Real time
max_time = 5000 # Alternatively, max_time = data.rt.max()
data['rx'] = [squeak.uniform_time(x, t, max_duration=5000) for x, t in zip(data.x, data.t)]
data['ry'] = [squeak.uniform_time(y, t, max_duration=5000) for y, t in zip(data.y, data.t)] 

# Mouse Stats
data['md'] = data.apply(lambda trial: squeak.max_deviation(trial['nx'], trial['ny']), axis=1)
data['auc'] = data.apply(lambda trial: squeak.auc(trial['nx'], trial['ny']), axis=1)
data['xflips'] = data.nx.map(squeak.count_x_flips)
data['init_time'] = data.ry.map(lambda y: y.index[np.where(y > .05)][0])


# Seperate data frames
nx = pd.concat(list(data.nx), axis=1).T
ny = pd.concat(list(data.ny), axis=1).T

rx = pd.concat(list(data.rx), axis=1).T
ry = pd.concat(list(data.ry), axis=1).T

redundant = ['xTrajectory', 'yTrajectory', 'tTrajectory',
             'x', 'y', 't', 'nx', 'ny', 'rx', 'ry']
data = data.drop(redundant, axis=1)

print "Done!\n"

# Save data
data.to_csv('processed.csv', index=False)
print "Summary statistics saved to %s" % os.path.join(this_dir, 'processed.csv')
nx.to_csv('nx.csv', index=False)
ny.to_csv('ny.csv', index=False)
rx.to_csv('rx.csv', index=False)
ry.to_csv('ry.csv', index=False)

for n in ['nx', 'ny', 'rx', 'ry']:
    print "Mouse trajectories saved to %s.csv" % os.path.join(this_dir, n)
