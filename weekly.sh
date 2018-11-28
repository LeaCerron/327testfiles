#!/bin/bash


for (( i = 1; i <= 5; i++ )); do
	cat transactionSession/day${i}.txt | ./dailyRun.sh
done