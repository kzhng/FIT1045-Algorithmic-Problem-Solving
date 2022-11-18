# Do not change any line in writeResults and haversine functions
import math
def writeResults(results):
    outfile = open("walkable.txt", "w")
    string = "Location of the most walkable house: "+ str(results[0]) + ", " + str(results[1])
    print(string)
    outfile.write(string+"\n")

    string = "Walkability Score: " + str(results[2])
    print(string)
    outfile.write(string+"\n")
    
    TYPES = ['','','','school', 'fast food', 'post office', 'hospital']
    for i in range(3,len(results)):
        string = "The closest " + TYPES[i] + " is " + str(results[i]) +" km"
        print(string)
        outfile.write(string+"\n")
    
    outfile.close()
    

# using function from http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(point1, point2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = point1[1],point1[0],point2[1],point2[0]
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) *  math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. 
    return c * r

window = input("Enter the window: ")
################################################################
# DO NOT CHANGE ANYTHING ABOVE THIS LINE. At the end, call writeResults(results)
# where results is the name of the list that stores the latitude, longitude
# and other stats for the most walkable house as described in the
# assignment description.
################################################################

# Name: Kerry Yue Song Zheng
# Student ID: 28794346


# this function reads the input file and splits each line into the appropriate format and returns a list of it
def getDataFromFile(file):
    data = open(file)
    dataList = []
    for line in data:
        line = line.strip()
        line = line.split(":")
        line[0] = int(line[0])
        line[1] = float(line[1])
        line[2] = float(line[2])
        dataList.append(line)
    return dataList

# This function puts all POI's that are houses into a list
def getHouseList(dataList):
    houseList = [x for x in dataList if x[3] == "house"]
    return houseList

# This function puts all POI's that are schools into a list
def getSchoolList(dataList):
    schoolList = [x for x in dataList if x[3] == "school"]
    return schoolList

# This function puts all POI's that are fast foods into a list
def getFastFoodList(dataList):
    fastFoodList = [x for x in dataList if x[3] == "fast food"]
    return fastFoodList

# This function puts all POI's that are post offices into a list
def getPostOfficeList(dataList):
    postOfficeList = [x for x in dataList if x[3] == "post office"]
    return postOfficeList


# This function puts all POI's that are hospitals into a list
def getHospitalList(dataList):
    hospitalList = [x for x in dataList if x[3] == "hospital"]
    return hospitalList

# This function takes the window coordinates input and returns the window input into a list of floats
def getWindowCoordinates(coordinates):
    coordinates = coordinates.strip()
    coordinates = coordinates.split(":")
    coordinates = [float(x) for x in coordinates]
    return coordinates

# This function finds every house that are inside the window and returns a list of it
def getHouseWithinWindow(houseList, window):
    windowList = getWindowCoordinates(window)
    housesWithinWindow = [x for x in houseList if x[1] >= windowList[0] and x[1] <= windowList[2] and x[2] >= windowList[1] and x[2] <= windowList[3]]
    return housesWithinWindow

# Implementing selection sort, we can find the minimum value in a list
def getMinDistance(myList):
    n = len(myList)
    minIndex = 0
    for i in range(n):
        if myList[i] < myList[minIndex]:
            minIndex = i
    return myList[minIndex]

# This function finds the closest school to a house
def getDistanceFromSchool(house, schoolList):
    distanceList = []
    n = len(schoolList)
    for x in range(n):
        school = [schoolList[x][1], schoolList[x][2]]
        distance = haversine(house, school)
        distanceList.append(distance)
    minDistanceOfSchool = getMinDistance(distanceList)
    return minDistanceOfSchool

# This function finds the closest fast food to a house
def getDistanceFromFastFood(house, fastFoodList):
    distanceList = []
    n = len(fastFoodList)
    for x in range(n):
        fastFood= [fastFoodList[x][1], fastFoodList[x][2]]
        distance = haversine(house, fastFood)
        distanceList.append(distance)
    minDistanceOfFastFood = getMinDistance(distanceList)
    return minDistanceOfFastFood
    
# This function finds the closest post office to a house
def getDistanceFromPostOffice(house, postOfficeList):
    distanceList = []
    n = len(postOfficeList)
    for x in range(n):
        postOffice = [postOfficeList[x][1], postOfficeList[x][2]]
        distance = haversine(house, postOffice)
        distanceList.append(distance)
    minDistanceOfPostOffice = getMinDistance(distanceList)
    return minDistanceOfPostOffice
    
# This function finds the closest hospital to a house
def getDistanceFromHospital(house, hospitalList):
    distanceList = []
    n = len(hospitalList)
    for x in range(n):
        hospital = [hospitalList[x][1], hospitalList[x][2]]
        distance = haversine(house, hospital)
        distanceList.append(distance)
    minDistanceOfHospital = getMinDistance(distanceList)
    return minDistanceOfHospital

# This function finds the walkability score of a house
def getWalkabilityScore(school, fastFood, postOffice, hospital):
    walkabilityScore = school + fastFood + postOffice + hospital
    return walkabilityScore

# This function finds the house with the lowest walkabilityscore in the houses within the window coordinates
def getMinWalkabilityScore(housesList):
    n = len(housesList)
    minIndex = 0
    for i in range(n):
        if housesList[i][2] < housesList[minIndex][2]:
            minIndex = i
    return housesList[minIndex]

# If there are no houses output false,
# otherwise return a list containing the location of the most walkable house in the window, its walkability score and its closest POI's of each type
def getMostWalkableHouse(file,window):
    dataList = getDataFromFile(file)
    houseList = getHouseList(dataList)
    schoolList = getSchoolList(dataList)
    fastFoodList = getFastFoodList(dataList)
    postOfficeList = getPostOfficeList(dataList)
    hospitalList = getHospitalList(dataList)
    housesWithinWindow = getHouseWithinWindow(houseList, window)
    if housesWithinWindow == []:
        return False
    n = len(housesWithinWindow)
    housesStatisticsList = []
    for x in range(n):
        house = housesWithinWindow[x]
        houseCoordinate = [house[1], house[2]]
        closestSchool = getDistanceFromSchool(houseCoordinate, schoolList)
        closestFastFood = getDistanceFromFastFood(houseCoordinate, fastFoodList)
        closestPostOffice = getDistanceFromPostOffice(houseCoordinate, postOfficeList)
        closestHospital = getDistanceFromPostOffice(houseCoordinate, hospitalList)
        walkabilityScore = getWalkabilityScore(closestSchool, closestFastFood, closestPostOffice, closestHospital)
        houseStatistics = [houseCoordinate[0], houseCoordinate[1], walkabilityScore, closestSchool, closestFastFood, closestPostOffice, closestHospital]
        housesStatisticsList.append(houseStatistics)
    mostWalkableHouse = getMinWalkabilityScore(housesStatisticsList)
    return mostWalkableHouse

# if there are no houses, print there are no houses in the window, otherwise print the most walkable house
mostWalkableHouse = getMostWalkableHouse("POI.txt", window)
if mostWalkableHouse == False:
    print("No house found in the window")
else:
    writeResults(mostWalkableHouse)
            














