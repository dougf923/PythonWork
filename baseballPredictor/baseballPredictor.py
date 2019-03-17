#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:25:04 2019

@author: douglasfamularo
"""

from baseballPredictorObjects import *

# Collect 2018 Data 
initialList = [];
homeWinList = []; 
awayWinList = [];
leftWinList = [];
leftTotalList = [];
rightWinList = [];
rightTotalList = [];
runsList = [];


filestream = open_workbook("baseballPredictor/standings2018.xlsx")     
for s in filestream.sheets():
    for row in range(s.nrows):
        if row > 0 and row <31:
            initialList.append(str(s.cell_value(row,1)));
            
            homeRecord = str(s.cell_value(row,16));
            homeWinList.append(int(homeRecord[0:2]));

            awayRecord = str(s.cell_value(row,17));
            awayWinList.append(int(awayRecord[0:2]));

            rightRecord = str(s.cell_value(row,20));
            rightWin = int(rightRecord[0:2]);
            rightLoss = int(rightRecord[3:5]);
            rightWinList.append(rightWin);
            rightTotalList.append(rightWin+rightLoss);

            leftRecord = str(s.cell_value(row,21));
            leftWin = int(leftRecord[0:2]);
            leftLoss = int(leftRecord[3:5]);
            leftWinList.append(leftWin);
            leftTotalList.append(leftWin+leftLoss);

            runsList.append(float(s.cell_value(row,8)));


#Create Teams and dictionary
teamDict = {};

for nT in range(30):
    team = mlbTeam(initialList[nT],homeWinList[nT],awayWinList[nT],leftWinList[nT],leftTotalList[nT],rightWinList[nT],rightTotalList[nT],runsList[nT]);
    teamDict[team.initials] = team;

#print(teamDict["NYY"].runsScoredPer9_2018)
#print(teamDict["NYM"].lossAway2018)

# Test First Game
homeTeam = "TOR"
awayTeam = "KCR"
yanksFirstGame = mlbGame(teamDict[homeTeam],teamDict[awayTeam],"doug","doug")

print("Predicted Winner: "+yanksFirstGame.predictedWinner)
print("Predicted Loser: "+yanksFirstGame.predictedLoser)
#print(yanksFirstGame.predictionRatio)
print("Percent chance of winning: "+yanksFirstGame.predictionPercent)


