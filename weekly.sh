#!/bin/bash

#loops 5 times to represent the 5 days of activity
for (( i = 1; i <= 5; i++ )); do
	#counts the number of times logout occurs in the text file for number of frontend runs
	num=$(grep -c 'logout' transactionSession/day${i}.txt)
	#passes the text file to daily run and the number of times the frontend was run
	cat transactionSession/day${i}.txt | ./dailyRun.sh $num $i
	# echo $i
done