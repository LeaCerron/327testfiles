#!/bin/bash

#times run frontend per day
RUNS=3

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
        echo "$line yep"
        echo "$line" >> tempfile$num
        if [[ $line == "logout" ]]; then
            ((num+=1))
        fi
    done

    #run the frontend for the day
    for (( i = 1; i <= $RUNS; i++ )); do
        python3 code/frontEnd.py serviceList.txt actualoutput/${i}.txt < tempfile$i
        rm tempfile$i
    done


else
    #run the frontend for the day with user input
    for (( i = 1; i <= $RUNS; i++ )); do
        python3 code/frontEnd.py serviceList.txt actualoutput/${i}.txt < file4
    done
    
fi



#concatenate all output files to a merged transaction file
for file in actualoutput/*; do
    cat $file >> mergedTransactions.txt
done


#runs backend with merged file
python3 code/backend.py mergedTransactions.txt centralFile.txt centralFile.txt serviceList.txt
