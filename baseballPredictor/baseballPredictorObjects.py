#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:25:04 This

@author: douglasfamularo
"""

from copy import copy, deepcopy
from xlrd import open_workbook    
    
class mlbTeam(object):
     def __init__(self,initials,winHomeLast,winAwayLast,winLeftLast,totalLeftLast,winRightLast,totalRightLast,runsScoredPer9_Last):
         self.initials = initials;
         
         self.winHomeLast = winHomeLast;
         self.winAwayLast = winAwayLast;
         self.winLast = self.winAwayLast+self.winHomeLast;
         self.winLeftLast = winLeftLast;
         self.totalLeftLast = totalLeftLast;
         self.winRightLast = winRightLast;
         self.totalRightLast = totalRightLast;

         if self.winLast != self.winLeftLast+self.winRightLast:
            raise("R/L Wins not matching Home/Away Wins");
         
         self.winHomeThis = 0;
         self.totalHomeThis = 0;
         self.winAwayThis = 0;
         self.totalAwayThis = 0;
         self.winThis = self.winAwayThis+self.winHomeThis;
         self.nOf162 = self.totalAwayThis+self.totalHomeThis;
         self.winLeftThis = 0;
         self.totalLeftThis = 0;
         self.winRightThis = 0;
         self.totalRightThis = 0;
         
         self.runsScoredPer9_Last = runsScoredPer9_Last;
         self.runsScoredPer9_This = 0;
         
     def setWinHomeThis(self,ipt):
         self.winHomeThis = ipt;
         
         if self.winAwayThis != 0:
             self.winThis = self.winHomeThis+self.winAwayThis;
             
     def setWinAwayThis(self,ipt):
         self.winAwayThis = ipt;
         
         if self.winHomeThis != 0:
             self.winThis = self.winHomeThis+self.winAwayThis;
             
     def setTotalHomeThis(self,ipt):
         self.totalHomeThis = ipt;
             
     def setTotalAwayThis(self,ipt):
         self.totalAwayThis = ipt;

     def setWinLeftThis(self,ipt):
         self.winLeftThis = ipt;
         
     def setWinRightThis(self,ipt):
         self.winRightThis = ipt;
         
     def setTotalLeftThis(self,ipt):
         self.totalLeftThis = ipt;
         
     def setTotalRightThis(self,ipt):
         self.totalRightThis = ipt;
                     
     def setRunsScoredPer9_This(self,ipt):
         self.runsScoredPer9_This = ipt;


         
class mlbGame(object):
    def __init__(self,homeTeam,awayTeam,homeSp,awaySp):
         if homeTeam == awayTeam:
             raise ("Home team and Away team must be different");
        
         self.homeTeam = homeTeam;
         self.awayTeam = awayTeam;
         self.homeSp = homeSp;
         self.awaySp = awaySp;
         

         temp = self.predictGame();
         
         self.predictedWinner = temp[0];
         self.predictedLoser = temp[1];
         self.predictionRatio = temp[2];
         self.predictionPercent = temp[3];

         self.actualWinner = ""
         self.actualLoser = ""

    def setActualWinner(self,ipt):
        if ipt != self.homeTeam or ipt != self.awayTeam:
            raise ('Input not a participant in this game.')

        if ipt == self.homeTeam:
            self.actualWinner = ipt;
            self.actualLoser = self.awayTeam;

        if ipt == self.awayTeam:
            self.actualWinner = ipt;
            self.actualLoser = self.homeTeam;


    def setActualLoser(self,ipt):
        if ipt != self.homeTeam or ipt != self.awayTeam:
            raise ('Input not a participant in this game.')

        if ipt == self.homeTeam:
            self.actualLoser = ipt;
            self.actualWinner = self.awayTeam;

        if ipt == self.awayTeam:
            self.actualLoser = ipt;
            self.actualWinner = self.homeTeam; 


    def getHaSplits(self,team):

        if team == self.homeTeam:
            lastHaSplit = float(team.winHomeLast/81);
            thisHaSplit = safeDivide(team.winHomeThis,team.totalHomeThis)
        else:
            lastHaSplit = float(team.winAwayLast/81);
            thisHaSplit = safeDivide(team.winAwayThis,team.totalAwayThis)

        return (lastHaSplit,thisHaSplit)

    def getLrSplits(self,team):
        if team == self.homeTeam:
            if self.awaySp.arm == "R":
                lastLrSplit = team.winRightLast/team.totalRightLast;
                thisLrSplit = safeDivide(team.winRightThis,team.totalRightThis)

            else:
                lastLrSplit = team.winLeftLast/team.totalLeftLast;
                thisLrSplit = safeDivide(team.winLeftThis,team.totalLeftThis)

        else:
            if self.homeSp.arm == "R":
                lastLrSplit = team.winRightLast/team.totalRightLast;
                thisLrSplit = safeDivide(team.winRightThis,team.totalRightThis)
            else:
                lastLrSplit = team.winLeftLast/team.totalLeftLast;
                thisLrSplit = safeDivide(team.winLeftThis,team.totalLeftThis)

        return (lastLrSplit,thisLrSplit)


    def calcPredictedScore(self,team):
        (lastHaSplit,thisHaSplit) = self.getHaSplits(team);
        (lastLrSplit,thisLrSplit) = self.getLrSplits(team);
        thisYearRecord = safeDivide(team.winThis,team.nOf162);
           
        lastYearRecord = float(team.winLast/162);            
        lastYearRuns = float(team.runsScoredPer9_Last/10);
        thisYearRuns = float(team.runsScoredPer9_This/10);

        predictedScore = (1-(team.nOf162/162))*(lastHaSplit+lastLrSplit+lastYearRecord+lastYearRuns)+(team.nOf162/162)*(thisHaSplit+thisLrSplit+thisYearRecord+thisYearRuns);

        return predictedScore

    def predictGame(self):
        homeScore = self.calcPredictedScore(self.homeTeam);
        awayScore = self.calcPredictedScore(self.awayTeam);

        if homeScore > awayScore:
            predictedWinner = self.homeTeam.initials;
            predictedLoser = self.awayTeam.initials;
            predictionRatio = predictedWinner+": "+str(homeScore)+", "+ predictedLoser+str(awayScore);
            predictionPercent = predictedWinner+": "+str(homeScore/(homeScore+awayScore))+"%, "+ predictedLoser+": "+str(awayScore/(homeScore+awayScore))+"%";
        else:
            predictedWinner = self.awayTeam.initials;
            predictedLoser = self.homeTeam.initials;
            predictionRatio = predictedWinner+": "+str(awayScore)+", "+ predictedLoser+str(homeScore);
            predictionPercent = predictedWinner+": "+str(awayScore/(homeScore+awayScore))+"%, "+ predictedLoser+": "+str(homeScore/(homeScore+awayScore))+"%";

        temp = (predictedWinner,predictedLoser,predictionRatio,predictionPercent);

        return temp 

    def wasPredictionRight(self):
        if self.actualWinner == "" or self.actualLoser == "":
            raise('Actual Winner or Loser not populated')

        if self.actualWinner == self.predictedWinner:
            return true
        else:
            return false

class startingPitcher(object):
    def __init__(self,name,arm):
         if arm != "R" of arm != "L":
             raise ("Input 'R' for right-handed and 'L' for left-handed");

         self.name = name;
         self.arm = arm; 

def safeDivide(num,denom):
    if denom == 0:
        ans = 0;
    else:
        ans = num/denom;

    return ans





             
             

         