#!/bin/bash

#make sure have parameter
if [[ $# < 2 ]]; then
    echo "missing required parameter"
    exit 0
fi

#times run frontend per day
RUNS=$1
#the day that is run
DAY=$2


#clear out any old runs
rm actualoutput/* 2> /dev/null #if nothing to remove then no errors


#remove the old merged transaction file
rm mergedTransactions.txt 2> /dev/null #if nothing to remove then no errors

#get rid of any files with same name
rm tempfile* 2> /dev/null #if nothing to remove then no errors


#if there was an input piped through the script
if [[ ! -t 0 ]]; then
    #loop through input file and separate it into temporary files for each run of the frontend
    num=1
    while read -r line; do
        echo "$line" >> tempfile$num
        if [[ $line == "logout" ]]; then
            ((num+=1))
        fi
    done

    #putting num back to the number of files that exist
    ((num-=1))
    if [[ $num != $RUNS ]]; then
        echo "input file does not have an equal number of runs as requested daily runs"
        rm tempfile* #clean up incomplete run
        exit 0
    fi

    #run the frontend for the day
    for (( i = 1; i <= $RUNS; i++ )); do
        python3 code/frontEnd.py serviceList.txt actualoutput/${i}.txt < tempfile$i > /dev/null #if automated input do not see prompts
        rm tempfile$i
    done


else
    #run the frontend for the day with user input
    for (( i = 1; i <= $RUNS; i++ )); do
        python3 code/frontEnd.py serviceList.txt actualoutput/${i}.txt
    done
    
fi


#concatenate all output files to a merged transaction file
for file in actualoutput/*; do
    cat $file >> mergedTransactions.txt
done

#makes a seperate merged transaction file for each day
if [[ -f mergedTransactions.txt ]]; then
	cat mergedTransactions.txt >| mergedTransactions$DAY.txt
fi

#runs backend with merged file
python3 code/backend.py mergedTransactions$DAY.txt centralFile.txt centralFile.txt serviceList.txt


