This directory contains everything you need to run your experiment.

`experiment.opensesame` is an [OpenSesame](http://osdoc.cogsci.nl/)
experiment file, which implements a simple mouse tracking experiment.
You'll need to
[download OpenSesame](http://osdoc.cogsci.nl/getting-opensesame/),
which includes two programs: opensesame.exe, which you can use to edit
this file, and opensesamerun.exe, for running the experment.

`Run Experiment.bat` is a Windows script that automates the process of
starting your experiment and assigning subject numbers.  You'll need
to open it up and edit the `opensesame` variable at the top to match
where ever you've installed OpenSesame to on your system.
`RunExperiment.sh` does the same thing on OSX/Linux systems.

You'll want to use OpenSesame to modify `experiment.opensesame` to
implement your own experiment. In particular, take a look at the
`question_script` element in the experiment - it's this which takes
care of stimulus presentation, mouse tracking, and response logging.
