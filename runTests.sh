#!/bin/bash

#get rid of old run outputs
rm actualoutput/*

#get number of tests to run
num=$(find ./testinputentry -maxdepth 1 -type f -name "*.txt" | wc -l)

#run all the tests
for (( i = 1; i <= $num; i++ )); do #using value of i to use files needed for each test
    echo "running test $i"
    #running code on test inputs, saving output file and terminal output
    python3 code/main.py serviceList.txt actualoutput/${i}.txt < testinputentry/t${i}in.txt > actualoutput/${i}.log
done

#checking actual output with expected output
for (( i = 1; i <= $num; i++ )); do
    echo "checking outputs of test $i"

    #if expected output that is not just empty transcation file, use that instead 
    if [[ -f testoutput/t${i}out.txt ]]; then
        output="t${i}out.txt"
    else
        output="EOS.txt"
    fi

    #name of actual terminal output file
    terminal="t${i}out.log"

    #name of log file which will contain record of which tests fail
    log="log$(date +_%Y_%m_%T)" #uses date so will not be overridden when running tests again

    #this section needs fixed
    filediff="$(diff -wc actualoutput/${i}.txt testoutput/$output)"
    resultfile=$?
    terminaldiff="$(diff -wc actualoutput/${i}.log testoutputterminal/$terminal)"
    resultterminal=$?

    #if either output didn't match then fail test
    if [[ $resultfile != 0 || $resultterminal != 0 ]]; then
        echo "test $i failed" >> logfiles/$log
        echo $filediff >> logfiles/$log 
        echo >> logfiles/$log
        echo $terminaldiff >> logfiles/$log
        echo >> logfiles/$log #make a space for readability 
   fi
   
done
