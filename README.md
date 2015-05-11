# QuickstartMousetracking

This repository provides (almost)
everything you need to get started
at mouse tracking research using python/OpenSesame.

Data Collection
---------------

The `procedure` directory contains a temlate for a simple mouse
tracking experiment implemented using the
OpenSesame experiment builder,
which you can install [from here](osdoc.cogsci.nl).
You can also see my tutorial on mousetracking in OpenSesame
[here](http://eointravers.github.io/blog/2014/03/os-mousetracking/)

Data Analysis
-------------

I've completed this experiment a few times myself,
and copied the results into the `results` directory
(in the `data` directory within it).
The `results` directory also contains a python script,
`process.py`, which will parse the individual .csv files in `results/data/`,
merge them, and calculate relevant summary statistics,
as well as saving standardised cursor trajectories
for plotting and analysis.

To do this, you'll need to have a few things installed:

- An interpreter for the [python](https://www.python.org/about/) programming language.
- The SciPy set of python scientific packages. The easiest way to install all of these on Windows is to download the [anaconda scientific pyton distribution](https://store.continuum.io/cshop/anaconda/), which is a version of python which comes with almost all of the scientific tools you could need preinstalled.
- [Squeak](www.github.com/eointravers/squeak/), my python package for
  processing mouse data. The easiest way to install this is to type `pip install squeak` at the command prompt.

Finally, a note on usability: I've tried to make all of this as
user-friendly as possible, but this remains a solution for researchers
with at least some computing know-how. To modify the example
experiment provided, you'l need to be able to at least understand the
python code which powers it. Python is perhaps the easiest programming
language to learn, and a practical application like this is a great
way to start, but it will still be more difficult than clicking on a
magic button.  Running the analyses also requires a little bit of
knowledge about running python scripts, and even just what a script
is, more generally. This is something which isn't difficult to learn though,
and there are plenty of resources online
([here is a good starting point](https://www.python.org/about/gettingstarted/)).

If all of this sounds like a lot of work, I want to stress that Jon
Freeman's [MouseTracker](http://www.mousetracker.org/ ) is an
excellent tool for mouse tracking research, and should be the first
option most people look to. What I provide here is intended for
researchers who want to design experiments which go outside
MouseTracker's capabilities (and if MouseTracker is to be easy to use,
it can't support every conceivable experimental design),
or for those interested in learning a little more about
the fine detail of mouse trajectory recording and analysis.

### Happy tracking!
