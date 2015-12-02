@echo off

rem Change this variable to match where ever OpenSesame, and specifically opensesamerun.exe, is installed on your system.
set opensesame=C:\Users\40027000\Desktop\Software\OpenSesame\opensesame_2.8.3-win32-1\opensesamerun.exe

rem Read subject number from the file subject_nr.txt    
set number_path=%~dp0\subject_nr.txt
if exist %number_path% for /f "delims=" %%i in (%number_path%) do set /A subject_nr=%%i
echo Subject number = %subject_nr%.

rem Increment subject number, and save it to the file
set /A next_subject = %subject_nr% + 1
echo %next_subject% > %number_path%

rem Make sure the 'data' folder exists
if not exist %~dp0data mkdir %~dp0data

rem Run experiment, with set subject number, and save location, in fullscreen mode    
echo Starting experiment...
%opensesame% %~dp0Experiment.osexp -s %subject_nr% ^
    -l %~dp0data\subject_%subject_nr%.csv -f > NUL

echo Experiment complete!
echo Goodbye.
pause 
