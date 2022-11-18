import os
import shutil
def convertToTable(filename):
    results = open(filename)
    table = []
    for line in results:
        line = line.strip()
        line = line.replace("  ",":")
        line = line.split(":")
        line = filter(None, line) 
        
        record = []
        for item in line:
            item = item.strip()
            record.append(item)
        table.append(record)
    return table

def getPrettyString(record):
    string = ""
    for i in range(len(record)):
        if i == 0:
            string += '{:<23}'.format(record[i])
        else:
            string += '{:>8}'.format(record[i])
    return string
    
def isCorrect():
    if not os.path.isfile("FIFA_stats.txt"):
        print("FIFA_stats.txt not found.")
        return False

    if not os.path.isfile("expected_FIFA_stats.txt"):
        print("expected_FIFA_stats.txt not found.")
        return False
    
    results = convertToTable("FIFA_stats.txt")
    expected = convertToTable("expected_FIFA_stats.txt")
    
    if len(results) != len(expected):
        print("The tables do not have same number of records")
        return False
    for i in range(len(results)):
        if results[i] != expected[i]:
            print("The records do no match. The first record that does not match is given below.")
            
            print("Your record: \n", getPrettyString(results[i]))
            print("Correct solution: \n", getPrettyString(expected[i]))
            return False
    return True
    

def deleteFile(filename):
    if os.path.isfile(filename):
        os.remove(filename)


def checkTestCase(testcase):
    print("Deleting files")
    # delete the file if it exists
    deleteFile("FIFA_stats.txt") 
       
    print("Running your code")
    os.system("task1.py")

       
    print("checking results...")
    if isCorrect():
        print("The result is correct")
    else:
        print("The result is not correct")
    




checkTestCase("matches.txt")



