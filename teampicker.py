from random import randrange
from os.path import exists
import os

def remove_common(a,b):
    setA = set(a)
    setB = set(b)
    return list(setA - setB)

def checkForUsedFile():
    used_file_exists = exists("used.txt")
    if not used_file_exists:
        usedFile = open("used.txt", "x") 

def getUniqueTeams(): 
    allTeams = []
    usedTeams = []
    with open("teams.txt") as teamsFile:
        for line in teamsFile:
            allTeams.append(line.replace("\n", ""))
            
    with open("used.txt") as usedFile:
        for line in usedFile:
            usedTeams.append(line.replace("\n", ""))

    possibleTeams = remove_common(allTeams, usedTeams)
    return possibleTeams

def getMatchup(possibleTeams):
    team1 = possibleTeams[randrange(len(possibleTeams))]
    team2 = possibleTeams[randrange(len(possibleTeams))]
    matchupsLeft = int(len(possibleTeams)/2)

    if matchupsLeft == 1:
        print("Final Matchup - resetting 'used' teams")
        os.remove("used.txt")
    else:
        print("Matchups remaining: %s" % matchupsLeft)

    while team1 == team2:
        team2 = possibleTeams[randrange(len(possibleTeams))]
    return team1, team2

def addToUsed(team1, team2):
    usedFile = open("used.txt", "a")
    usedFile.write(team1 + "\n")
    usedFile.write(team2 + "\n")

def main():
    checkForUsedFile()
    possibleTeams = getUniqueTeams()
    team1, team2 = getMatchup(possibleTeams)
    addToUsed(team1, team2)
    print("%s at %s" % (team1, team2))

if __name__ == "__main__":
    main()

