subject_nr=$(cat subject_nr.txt)
next_subject=$(($subject_nr + 1))

echo "Subject number = $subject_nr"
echo $next_subject > subject_nr.txt

if [ ! -d data ]; then
    mkdir data
fi

echo "Starting experiment..."
opensesamerun experiment.opensesame -s $subject_nr -l "data/subject_$subject_nr.csv" -f

echo Experiment complete!
echo Goodbye.
