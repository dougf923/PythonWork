#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:59:20 2018

@author: douglasfamularo
"""

from FantasyObjects import *   

scheduleDatafiles = ["DecSchedule.xlsx","JanSchedule.xlsx","FebSchedule.xlsx","MarSchedule.xlsx","AprSchedule.xlsx"];
gamelist = [];
for fileString in scheduleDatafiles:
    filestream = open_workbook("ScheduleData/"+fileString)
                
    for s in filestream.sheets():
        for row in range(s.nrows):
            if row > 0:
                dateString = str(s.cell_value(row,0));
                dateStringList = dateString.split(" ");
                date = dateStringList[1:4];
                home = str(s.cell(row,5).value);
                away = str(s.cell(row,3).value);
                gamelist.append(NBAGame(home,away,date))
        
        
NBA2018Schedule = Schedule(gamelist);
## TEST ##
#for game in NBA2018Schedule.getgames():
#    print(game)


teamInitials = ["TOR","MIL","IND","PHI","BOS","DET","ORL","CHO","BRK","MIA","WAS","NYK","CHI","ATL","CLE",\
                "GSW","POR","OKC","LAC","MEM","DEN","NOP","LAL","HOU","SAC","UTA","SAS","DAL","MIN","PHO"];
teamNames = ["Toronto Raptors","Milwaukee Bucks","Indiana Pacers","Philadelphia 76ers","Boston Celtics",\
             "Detroit Pistons","Orlando Magic","Charlotte Hornets","Brooklyn Nets","Miami Heat", "Washington Wizards",\
             "New York Knicks","Chicago Bulls","Atlanta Hawks","Cleveland Cavaliers","Golden State Warriors",\
             "Portland Trailblazers","Oklahoma City Thunder","Los Angeles Clippers","Memphis Grizzlies","Denver Nuggets",\
             "New Orleans Pelicans","Los Angeles Lakers","Houston Rockets","Sacramento Kings","Utah Jazz",\
             "San Antonio Spurs","Dallas Mavericks","Minnesota Timberwolves","Phoenix Suns"];
             

teamlist = [];
for idx in range(len(teamInitials)):
    teamlist.append(NBATeam(teamInitials[idx],teamNames[idx],NBA2018Schedule));

TeamDict = {};
#key: team initials read in from player data sheet
#elems: tuple(team Object, team name used in game Objects)
for team in teamlist:
    TeamDict[team.getinitials()] = team;
    

playerList = [];  
filestream = open_workbook("PlayerData/NBA_players.xlsx")     
for s in filestream.sheets():
    for row in range(s.nrows):
        if row > 0:
            nameString = str(s.cell_value(row,1));
            nameList = nameString.split("\\");
            name = nameList[0];
            position = str(s.cell_value(row,2));
            team = TeamDict[str(s.cell_value(row,4))];
            injured = False;
            starter = True;
            playerList.append(NBAPlayer(name,position,team,injured,starter))
## TEST ##
#for player in playerList:
#    print(player.getteam())
    

    

MOPRoster = createRoster("fantasyTeamData/MainOfficePranksters.xlsx",playerList);
MainOfficePranksters = FantasyTeam("MainOfficePranksters",MOPRoster);

KCRoster = createRoster("fantasyTeamData/Kirilenko Collusion.xlsx",playerList);
KirilenkoCollusion = FantasyTeam("Kirilenko Collusion",KCRoster);
## TEST ##
#for player in KirilenkoCollusion.getroster():
#    print(player.getname())

flatEarthers = FantasyLeague([MainOfficePranksters, KirilenkoCollusion]);



#testFilteredSchedule = deepcopy(testSchedule);
#testFilteredSchedule.filterByTeam("NY");
#testFilteredSchedule.filterByDate(["Jan","3","1994"],["Jan","1","2018"]);

#print('#####')
#for game in testSchedule.getgames():
#    print(str(game))
#print('#####')
#for game in testFilteredSchedule.getgames():
#    print(str(game))
        
        
        