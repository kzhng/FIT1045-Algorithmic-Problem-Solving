
#IMPORTANT: DO NOT CHANGE ANY LINE IN getPrettyString() and writeTable() functions

# This function takes stats of a team and returns a string in the required format
def getPrettyString(record):
    string = ""
    for i in range(len(record)):
        if i == 0:
            string += '{:<23}'.format(record[i])
        else:
            string += '{:>8}'.format(record[i])
    return string

# This functions prints (and writes to the outputfile) the table in the requied format
def writeTable(table):
    
    outfile = open("FIFA_stats.txt",'w')
    header = ["Team", "Played", "Won", "Drawn", "Lost", "GS", "GA", "GD", "Points"]
    record = getPrettyString(header)
    outfile.write(record +"\n")
    print(record)

    for team in table:
        record = getPrettyString(team)
        print(record)
        outfile.write(record+"\n")
    outfile.close()


################################################################
# Write your code below this. At the end, call writeTable(tablename)
# where tablename is the name of your table that has been sorted
# according to the criteria.
################################################################

# Name: Kerry Yue Song Zheng
# Student ID: 28794346

# This function reads the input file and splits each line into the appropriate format and returns a table
def convertMatchesToList(file):
    matches = open(file)
    matchList = []
    for line in matches:
        line = line.strip()
        line = line.split(":")
        line[2] = int(line[2])
        line[3] = int(line[3])
        matchList.append(line)
    return matchList

# This function finds how many matches a team has played
def matchesPlayed(teamname, matchesList):
    played = 0
    length = len(matchesList)
    for i in range(length):
        if matchesList[i][0] == teamname or matchesList[i][1] == teamname:
            played += 1
    return played

# This function finds how many matches a team has won
def matchesWon(teamname, matchesList):
    won = 0
    length = len(matchesList)
    for i in range(length):
        if matchesList[i][0] == teamname:
            if matchesList[i][2] > matchesList[i][3]:
                won += 1
        if matchesList[i][1] == teamname:
            if matchesList[i][3] > matchesList[i][2]:
                won += 1
    return won

# This function finds how many matches a team has lost
def matchesLost(teamname, matchesList):
    lost = 0
    length = len(matchesList)
    for i in range(length):
        if matchesList[i][0] == teamname:
            if matchesList[i][2] < matchesList[i][3]:
                lost += 1
        if matchesList[i][1] == teamname:
            if matchesList[i][3] < matchesList[i][2]:
                lost += 1
    return lost

# This function finds how many matches a team drew
def matchesDrawn(teamname, matchesList):
    """

    :param teamname: 
    :param matchesList: 
    :return: 
    """
    drawn = 0
    length = len(matchesList)
    for i in range(length):
        if matchesList[i][0] == teamname or matchesList[i][1] == teamname:
            if matchesList[i][2] == matchesList[i][3]:
                drawn += 1
    return drawn

# This function finds the total amount of goals scored by a team
def goalsScored(teamname, matchesList):
    scored = 0
    length = len(matchesList)
    for i in range(length):
        if matchesList[i][0] == teamname:
            scored += matchesList[i][2]
        if matchesList[i][1] == teamname:
            scored += matchesList[i][3]
    return scored

# This function finds the total amount of goals scored against a team
def goalsAgainst(teamname, matchesList):
    against = 0
    length = len(matchesList)
    for i in range(length):
        if matchesList[i][0] == teamname:
            against += matchesList[i][3]
        if matchesList[i][1] == teamname:
            against += matchesList[i][2]
    return against

# This function finds the total goal difference of a team
def goalsDifference(teamname, matchesList):
    totalDifference = 0
    length = len(matchesList)
    for i in range(length):
        if matchesList[i][0] == teamname:
            difference = matchesList[i][2] - matchesList[i][3]
            totalDifference += difference
        if matchesList[i][1] == teamname:
            difference = matchesList[i][3] - matchesList[i][2]
            totalDifference += difference
    return totalDifference
            
# This function finds how many points a team has
def points(teamname, matchesList):
    won = matchesWon(teamname, matchesList)
    drawn = matchesDrawn(teamname, matchesList)
    totalPoints = 3*won + drawn
    return totalPoints

#This function finds and returns a list of teams playing in the FIFA world cup
def getTeamsList(matchesList):
    teamList = []
    length = len(matchesList)
    for i in range(length):
        teamOne = matchesList[i][0]
        teamTwo = matchesList[i][1]
        if teamOne not in teamList:
            teamList.append(teamOne)
        if teamTwo not in teamList:
            teamList.append(teamTwo)
    return teamList

# This function finds every team's statistics and returns a table of every team's statistics in the appropriate format
def getTeamTable(file):
    teamTable = []
    matchesList = convertMatchesToList(file)
    teamsList = getTeamsList(matchesList)
    numberOfTeams = len(teamsList)
    for i in range(numberOfTeams):
        teamStatistics = []
        team = teamsList[i]
        played = matchesPlayed(team, matchesList)
        won = matchesWon(team, matchesList)
        drawn = matchesDrawn(team, matchesList)
        lost = matchesLost(team, matchesList)
        scored = goalsScored(team, matchesList)
        against = goalsAgainst(team, matchesList)
        totalDifference = goalsDifference(team, matchesList)
        totalPoints = points(team, matchesList)
        teamStatistics = [team, played, won, drawn, lost, scored, against, totalDifference, totalPoints]
        teamTable.append(teamStatistics)
    return teamTable

# swapping elements function
def swapTeams(aList, i, j):
    temp = aList[i]
    aList[i] = aList[j]
    aList[j] = temp

# uses insertion sort to sort the team standings
def sortTeamTable(filename):
    table = getTeamTable(filename)
    numberOfTeams = len(table)
    for k in range(1, numberOfTeams):
        i = k
        while table[i-1][8] < table[i][8] and i > 0: # sorting by total number of points
            swapTeams(table, i-1, i)
            i = i-1
        while table[i-1][8] == table[i][8] and i > 0: # sorting by fewer matches played
            if table[i-1][1] > table[i][1]:
                swapTeams(table, i-1, i)
                i = i-1
            else:
                break
        while table[i-1][8] == table[i][8] and table[i-1][1] == table[i][1] and i > 0: # sorting by higher goal difference
            if table[i-1][7] < table[i][7]:
                swapTeams(table, i-1, i)
                i = i-1
            else:
                break
        while table[i-1][8] == table[i][8] and table[i-1][1] == table[i][1] and table[i-1][7] == table[i][7] and i > 0: # sorting by more goals scored
            if table[i-1][5] < table[i][5]:
                swapTeams(table, i-1, i)
                i = i-1
            else:
                break
        while table[i-1][8] == table[i][8] and table[i-1][1] == table[i][1] and table[i-1][7] == table[i][7] and table[i-1][5] == table[i][5] and i > 0: # sorting by team's alphabetical order
            if table[i-1][0] > table[i][0]:
                swapTeams(table, i-1, i)
                i = i-1
            else:
                break
    
    return table

table = sortTeamTable("matches.txt")
writeTable(table)
