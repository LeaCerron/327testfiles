import sys
import re

#vfile names given when run file
mergedTransactionFile = sys.argv[1]
oldCentralFile = sys.argv[2]
newCentralFile = sys.argv[3]
validServiceFile = sys.argv[4]

#reading in central file to object, only valaue check on capacity
#should I check number of sold tickets too?
objectList = []

centralFile = open(oldCentralFile, "r")
for line in centralFile:
    lineElements = line.split()
    if int(lineElements[1]) < 1000 and int(lineElements[1]) > 0:
        print("successful line") #temp until can uncomment rest
        #tempObject = object call(lineElements[0], lineElements[1], lineElements[2], lineElements[3], lineElements[4])
        #objectList.append(tempObject)
    else:
        print("crash program here")
        #crash
centralFile.close()

#reading in merged transaction file
#assuming ends with 00000
#currently no processing at all, could easily separate out string elements later

transactionList = []

transactionFile = open(mergedTransactionFile, "r")
line = transactionFile.readline().rstrip() #get rid of newline
while line != "00000":
    transactionList.append(line)
    line = transactionFile.readline().rstrip()
transactionFile.close()
print(transactionList)