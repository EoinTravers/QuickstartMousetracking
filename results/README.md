This directory takes care of your basic data processing.

- `process.py` is a script which parses the data files in `data/`,
  calculates the relevant summary statistics for each trajectory, and
  saves them to `processed.csv`. It also outputs the processed
  trajectories to `nx.csv`, `ny.csv` (both normalisime time),
  `rx.csv`, and `ry.csv` (both real time), for future
  analysis/plotting.
- `SqueakIntro.ipynb` is an
  [iPython notebook](http://ipython.org/notebook.html ) containing the
  same code as `process.py`, but with a lot of extra documentation
  explaining how it all works. If you're not familiar with iPython,
  notebooks are an incredibly useful way of combining code, text, and
  output like plots and tables into a single document, which allows
  individual code segments to be modified and executed
  interactively. To use it, once you've installed
  [Anaconda](https://store.continuum.io/cshop/anaconda/ ), just open
  up a command prompt, type in `ipyton notebook`, wait for the browser
  window to open, and then use the interface to navigate to this
  folder. You can also just view the notebook by
  [viewing the file on GitHub](https://github.com/EoinTravers/QuickstartMousetracking/blob/master/results/SqueakIntro.ipynb)
- `Plotting.ipynb` is a notebook demonstrating some ways of visualing
  the processed mouse trajectories. Again, you can edit it yourself
  using the iPython notebook, or
  [view it on GitHub](https://github.com/EoinTravers/QuickstartMousetracking/blob/master/results/Plotting.ipynb)



