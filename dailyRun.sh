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

#gets rid of old service list
rm serviceList.txt

#runs backend with merged file
python3 code/backend.py mergedTransactions.txt oldCentralFile.txt newCentralFile.txt serviceList.txt

#check if crashed
crashStatus=$?

#if crash failed don't delete old central service file as no new file created
if [[ $crashStatus == 0 ]]; then
    #get rid of old file
    rm oldCentralFile.txt

    #newly created central service file renamed
    mv newCentralFile.txt oldCentralFile.txt
fi

