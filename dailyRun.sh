#!/bin/bash

#times run frontend per day
RUNS=3

#clear out any old runs
rm actualoutput/*

#remove the old merged transaction file
rm mergedTransactions.txt

#run the frontend for the day
for (( i = 1; i <= $RUNS; i++ )); do
    python3 code/frontEnd.py serviceList.txt actualoutput/${i}.txt
done

#concatenate all output files to a merged transaction file
for file in actualoutput/*; do
    cat $file >> mergedTransactions.txt
done


#runs backend with merged file
python3 code/backend.py mergedTransactions.txt centralFile.txt centralFile.txt serviceList.txt
