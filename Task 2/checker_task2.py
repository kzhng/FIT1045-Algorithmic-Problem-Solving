import os
import shutil
def getResults(filename):
    infile = open(filename)
    results = []
    for line in infile:
        results.append(line)
    return results

def fileExists(filename):
    if os.path.isfile(filename):
        return True
    else:
        print("File",filename, "does not exist")
        return False
def isCorrect():
    if not fileExists("walkable.txt"):
        return False
    if not fileExists("expected_walkable.txt"):
        return False
    results = getResults("walkable.txt")
    expected = getResults("expected_walkable.txt")
    if len(results) != len(expected):
        print("The two files have different number of lines")
        return False
    for i in range(len(results)):
        if results[i] != expected[i]:
            print("The records do no match. The first record that does not match is given below.")
            print("Your output: \n", results[i])
            print("Correct output: \n", expected[i])
            return False
    return True
    #for line in results:



def deleteFile(filename):
    if os.path.isfile(filename):
        os.remove(filename)


def checkTestCase(testcase):
    print("Deleting files")
    deleteFile("walkable.txt")
   
    

    
    print("CHECKING TESTCASE: ", testcase)
    print("Running your code")
    command = "echo " + testcase + "| task2.py" 
    os.system(command)


    
    
    print("checking results...")
    if isCorrect():
        print("The result is correct")
    else:
        print("The result is not correct")
    


checkTestCase("42.3:-124.2:43.3:-123.3")


