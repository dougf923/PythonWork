#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 08:47:53 2018

@author: douglasfamularo
"""
from copy import copy, deepcopy
from xlrd import open_workbook

class NBAGame(object):
    
    def __init__(self,home,away,date):
        self.home = home; # name of home team (not object)
        self.away = away; # name of away team (not object)
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
        if (player.getTeam() == self.gethome or player.getTeam() == self.getaway()) and not player.getInjuryStatus() and player.getStarting():
            return True
        return False
    
class NBATeam(object):
    
    def __init__(self,initials,name,NBASchedule):
        self.initials = initials;
        self.name = name;
        
        self.schedule = deepcopy(NBASchedule);
        self.schedule.filterByTeam(self.name);
        
    def getinitials(self):
        return self.initials
    
    def getname(self):
        return self.name
    
    def getSched(self):
        return self.schedule
    
    
class NBAPlayer(object):
    
    def __init__(self,name,position,team,injured,starter):
        self.name = name;
        self.position = position;
        self.team = team;
        self.injured = injured;
        self.starter = starter;
        
    def __str__(self):
        return self.getname()
    
    def getname(self):
        return self.name
    
    def getteam(self):
        return self.team   
    
    def playerGamesBetween(self,startDate,endDate):
        temp = deepcopy(self.getteam().getSched());
        temp.filterByDate(startDate,endDate);
        
        return len(temp.getgames())
    
class FantasyTeam(object):
    
    def __init__(self,name,roster):
        self.name = name;
        self.roster = roster;
        
    def getroster(self):
        return self.roster;
    
    def getname(self):
        return self.name;
        
    def addplayer(self,player):
        self.roster.append(player);
        
    def teamGamesBetween(self,startDate,endDate):
        temp = copy(self.getroster());
        ct = 0;
        
        for player in temp:
            ct += player.playerGamesBetween(startDate,endDate);
            
        return ct
    
class FantasyLeague(object):
    
    def __init__(self,fantasyteams):
        self.fantasyteams = fantasyteams;
        
    def setFantasyTeams(self,teamlist):
        self.fantasyteams = teamlist;
        
    def getFantasyteams(self):
        return self.fantasyteams;
        
        
        
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

def getPlayerObject(playerlist,name):
    for player in playerlist:
        if player.getname() == name:
            return player
        
    return ValueError

def createRoster(filename,playerList):
    rosterList = [];
    filestream = open_workbook(filename)     
    for s in filestream.sheets():
        for row in range(s.nrows):
            if row > 0:
                playerName = str(s.cell_value(row,0));
                rosterList.append(getPlayerObject(playerList,playerName));
                
    return rosterList


