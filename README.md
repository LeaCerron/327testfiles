Commands to run:
While in the 327testfiles directory:
Weekly run: ./weekly.sh 
Daily run with user input: ./dailyRun.sh 3 1 (3 is frontends per day, 1 is which day)
Daily run with input file: ./dailyRun.sh 3 1 <pathToInputFile (3 is frontends per day, 1 is which day)

To run the program for a week, run the script called "weekly.sh". To do this, you need to be sure that there are 5 days worth of input in the transactionSession folder.The input in the folder needs to be called "day[number].txt". By default, this will run 5 days with the number of frontends the input file has available per day.

If you want to run a single day, you can run the "dailyRun.sh". This script takes in two parameters: the number of frontends being run in a single day and which day of the week it is. If no input file is piped into the script, it will prompt the user for input for all the runs for the day. 

The input in the text files needs to have one command per line. The last line of the file needs to be followed by an extra line as it needs a newline at the end. Furthermore, you cannot test errors to do with adding additional "logout" lines as it will not work.

Something to watch out for when running is to have files called "serviceList.txt" (which requires at minimum "00000" at the end of the file) and "centralFile.txt" (which may be completely empty). These files will not change if backend crashes. But if you want to revert the service to an earlier state, it has to be done by hand.

The merged transaction file created will be saved under the name "mergedTransactions[day].txt". If there were any files by the same name previously, the will be overwritten. Similarly, any file with the name "mergedTransactions.txt" will be deleted after a script is run.

Any file put into the directory "actualoutput" will also be deleted after a run.

