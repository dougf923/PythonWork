#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 08:47:53 2018

@author: douglasfamularo
"""
from copy import copy, deepcopy

class NBAGame(object):
    
    def __init__(self,home,away,date):
        self.home = home;
        self.away = away;
        self.date = date;
        
    def __str__(self):
        return self.gethome()+" vs "+self.getaway()+", "+self.getdate()[0]+" "+self.getdate()[1]+", "+self.getdate()[2];
        
    def gethome(self):
        return self.home;
    
    def getaway(self):
        return self.away;
    
    def getdate(self):
        return self.date
    
    def isGamePlayed(self,player):
        if (player.getTeam() == self.gethome or player.getTeam() == self.getaway) and not player.getInjuryStatus() and player.getStarting():
            return True
        return False
    
class NBAPlayer(object):
    
    def __init__(self,name,position,team,injured,starter):
        self.name = name;
        self.position = position;
        self.team = team;
        self.injured = injured;
        self.starter = starter;
        
    def __str__(self):
        return self.getname();
    
    def getname(self):
        return self.name;
        
class Schedule(object):
    
    def __init__(self,games):
        self.games = games;
        
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
        
    def getgames(self):
        return self.games;
        
    def addgame(self,game):
        self.games.append(game);
        
    def removegame(self,game):
        self.games.remove(game);
        
    def combine(self,other,*args):
        othergames = other.getgames();
        
        for game in othergames:
            self.addgame(game);
            
        for arg in args:
            moregames = arg.getgames();
            
            for game in moregames:
                self.addgame(game);
                
    def filterByTeam(self,team):
        temp_list = copy(self.getgames());
        
        for game in temp_list:
            if not (game.getaway() == team or game.gethome() == team):
                self.removegame(game);
                
    def filterByDate(self,startDate,endDate):
        #filter out games that are before startDate
        startMonth = monthIndex(startDate[0]);
        startDay = int(startDate[1]);
        startYear = int(startDate[2]);
        
        temp_list = copy(self.getgames());
            
        for game in temp_list:
            if int(game.getdate()[2]) < startYear:
                self.removegame(game);
            elif int(game.getdate()[2]) == startYear and monthIndex(game.getdate()[0]) < startMonth:
                self.removegame(game);
            elif int(game.getdate()[2]) == startYear and monthIndex(game.getdate()[0]) == startMonth and int(game.getdate()[1]) < startDay:
                self.removegame(game);
                
        #filter out games that are after endDate
        endMonth = monthIndex(endDate[0]);
        endDay = int(endDate[1]);
        endYear = int(endDate[2]);
        
        temp_list = copy(self.getgames());
            
        for game in temp_list:
            if int(game.getdate()[2]) > endYear:
                self.removegame(game);
            elif int(game.getdate()[2]) == endYear and monthIndex(game.getdate()[0]) > endMonth:
                self.removegame(game);
            elif int(game.getdate()[2]) == endYear and monthIndex(game.getdate()[0]) == endMonth and int(game.getdate()[1]) > endDay:
                self.removegame(game);
            
                

def monthIndex(month):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    # Returns an int representing the month string (1-Jan, 2-Feb, etc.)
    ct = 0;
    for test in months:
        if month == test:
            return ct+1;
        
    return ValueError


#######################


game1 = NBAGame("NY","NJ",["Jan","1","2018"]);
game2 = NBAGame("Phi","Bos",["Jan","2","2018"]);
game3 = NBAGame("Phi","NY",["Jan","3","2018"]);

testSchedule = Schedule([game1,game2,game3]);

testFilteredSchedule = deepcopy(testSchedule);
#testFilteredSchedule.filterByTeam("NY");
testFilteredSchedule.filterByDate(["Jan","3","1994"],["Mar","2","2020"]);

print('#####')
for game in testSchedule.getgames():
    print(str(game))
print('#####')
for game in testFilteredSchedule.getgames():
    print(str(game))
        
        
        
            