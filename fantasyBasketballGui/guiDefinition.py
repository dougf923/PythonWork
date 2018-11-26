from tkinter import *
from tkinter import ttk

  
    
class GameCounterApp:
    
    def __init__(self,master,League):
        self.master = master;
        self.League = League;
        self.months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
        self.years = ["2018","2019"]
        
        self.master.title("Fantasy Basketball Game Counter")
        
        mainframe = ttk.Frame(self.master, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.frame = mainframe
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
             
        # Set up Start Date Menus        
        ttk.Label(mainframe, text="Start Date: ").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Month").grid(column=2, row=1)
        ttk.Label(mainframe, text="Day").grid(column=3, row=1)
        ttk.Label(mainframe, text="Year").grid(column=4, row=1)
               
        monthStartButton = self.buildMenuButton(mainframe,monthStartStr,monthStartInt,2,2,7,"Month");
        dayStartButton = self.buildMenuButton(mainframe,dayStartStr,dayStartInt,2,3,7,"Day");        
        yearStartButton = self.buildMenuButton(mainframe,yearStartStr,yearStartInt,2,4,7,"Year");
               
        # Set up End Date Menus        
        ttk.Label(mainframe, text="End Date: ").grid(column=5, row=2, sticky=E)
        ttk.Label(mainframe, text="Month").grid(column=6, row=1)
        ttk.Label(mainframe, text="Day").grid(column=7, row=1)
        ttk.Label(mainframe, text="Year").grid(column=8, row=1)
        
        monthEndButton = self.buildMenuButton(mainframe,monthEndStr,monthEndInt,2,6,7,"Month");      
        dayEndButton = self.buildMenuButton(mainframe,dayEndStr,dayEndInt,2,7,7,"Day");       
        yearEndButton = self.buildMenuButton(mainframe,yearEndStr,yearEndInt,2,8,7,"Year");
        
        #Set up Fantasy Team Menu's
        ttk.Label(mainframe, text="Team 1: ").grid(column=1, row=3, sticky=(W,E));
        Team1Button = self.buildMenuButton(mainframe,Team1Str,Team1Int,3,3,21,"Team");
        
        ttk.Label(mainframe, text="Team 2: ").grid(column=5, row=3, sticky=(W,E));
        Team2Button = self.buildMenuButton(mainframe,Team2Str,Team2Int,3,7,21,"Team");
        
        #Setup Roster Variable Lists
        self.team1rosterStrings = [];
        self.team2rosterStrings = [];
        
        self.team1startingInts = [];
        self.team2startingInts = [];
        
        self.team1injuredInts = [];
        self.team2injuredInts = [];
        
        self.team1gameRemainStrings = [];
        self.team2gameRemainStrings = [];
        
        self.Team1TotalStr = StringVar()
        self.Team2TotalStr = StringVar()
        
        
        
        
        

        
        
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        
    def buildMenuButton(self,frame,textvar,intvar,rownum,colnum,widthnum,menutype):
        menubutton = ttk.Menubutton(frame, width=widthnum, textvariable = textvar);
        menu = self.buildMenu(menubutton, intvar, textvar, menutype);
        menubutton.config(menu=menu);
        menubutton.grid(column=colnum, row=rownum, sticky=(W,E));
        
        return menubutton
    
    def buildMenu(self,menubutton,varInt,textvar, menutype):
                     
        menu = Menu(menubutton)        
        
        if menutype == "Month":
            ct = 0;
            for item in self.months:
                ct += 1;
                menu.add_radiobutton(label=item, var=varInt, value=ct, command = lambda: self.setMenuLabel(varInt,textvar,menutype));
 
        elif menutype == "Day":
            for num in range(31):
                menu.add_radiobutton(label=str(num+1), var=varInt, value=num, command = lambda: self.setMenuLabel(varInt,textvar,menutype))
              
        elif menutype == "Year":
            ct = 0;
            for item in self.years:
                ct += 1;
                menu.add_radiobutton(label=item, var=varInt, value=ct, command = lambda: self.setMenuLabel(varInt,textvar,menutype))
                  
        elif menutype == "Team":
            teams = self.League.getFantasyTeams(); 
            ct = 0;
            for item in teams:
                ct += 1;
                menu.add_radiobutton(label=item.getname(), var=varInt, value=ct, command = lambda: self.setMenuLabel(varInt,textvar,menutype))
       
        return menu
    
    def updateGameCount(self,teams,value,oneOrtwo):
        startDate = [monthStartStr.get(),dayStartStr.get(),yearStartStr.get()];
        endDate = [monthEndStr.get(),dayEndStr.get(),yearEndStr.get()];
        if oneOrtwo == "Team 1":
            ct = 0;
            gamecount = 0;
            for player in teams[value-1].getroster():
                if not self.team1startingInts[ct].get() or self.team1injuredInts[ct].get():
                    self.team1gameRemainStrings[ct].set('0');
                else:
                    number = player.playerGamesBetween(startDate,endDate);
                    self.team1gameRemainStrings[ct].set(number)
                    gamecount += number;
                ct += 1;
            self.Team1TotalStr.set(gamecount);
        else:
            ct = 0;
            gamecount = 0;
            for player in teams[value-1].getroster():
                if not self.team2startingInts[ct].get() or self.team2injuredInts[ct].get():
                    self.team2gameRemainStrings[ct].set('0');
                else:
                    number = player.playerGamesBetween(startDate,endDate);
                    self.team2gameRemainStrings[ct].set(number)
                    gamecount += number;
                ct += 1;
            self.Team2TotalStr.set(gamecount)
        
        
        
        
    def setMenuLabel(self,intvar,stringvar,menutype): 
        value = intvar.get();
        if menutype == "Month":
            stringvar.set(self.months[value-1]);
        elif menutype == "Day":
            stringvar.set(str(value+1));
        elif menutype == "Year":
            stringvar.set(self.years[value-1]);
        elif menutype == "Team":
            teams = self.League.getFantasyTeams();
            stringvar.set(teams[value-1].getname());
            
            for team in self.League.getFantasyTeams():
                #print(team.getname());
                #print(Team1Str.get())
                buttonRow = 0;
                if team.getname() == Team1Str.get():
                    #print('here2');
                    ct = 0;
                    ttk.Label(self.frame, text = "ROSTER: ").grid(column=1, row=4)
                    ttk.Label(self.frame, text = "Starting?").grid(column=2, row=4)
                    ttk.Label(self.frame, text = "Injured?").grid(column=3, row=4)
                    ttk.Label(self.frame, text = "Games Remaining").grid(column=4, row=4)
                    for player in team.getroster():
                       self.team1rosterStrings.append(StringVar()); 
                       self.team1startingInts.append(IntVar());
                       self.team1injuredInts.append(IntVar());
                       self.team1gameRemainStrings.append(StringVar());
                       ttk.Label(self.frame, textvariable=self.team1rosterStrings[ct]).grid(column=1, row=5+ct)
                       ttk.Checkbutton(self.frame,variable = self.team1startingInts[ct]).grid(column=2, row=5+ct)
                       ttk.Checkbutton(self.frame,variable = self.team1injuredInts[ct]).grid(column=3, row=5+ct)
                       ttk.Label(self.frame, textvariable=self.team1gameRemainStrings[ct]).grid(column=4, row=5+ct)
                       ct += 1;


                    buttonRow = 5+ct;
                    ttk.Button(self.frame, text='Team 1 Refresh', command = lambda: self.updateGameCount(teams,value,"Team 1")).grid(column=1,row=buttonRow)
                    ttk.Label(self.frame, text = "TOTAL: ").grid(column=3, row=buttonRow+1)
                    ttk.Label(self.frame, textvariable=self.Team1TotalStr).grid(column=4, row=buttonRow+1)
                    
                if team.getname() == Team2Str.get():
                    ct = 0;
                    ttk.Label(self.frame, text= "ROSTER: ").grid(column=5, row=4)
                    ttk.Label(self.frame, text = "Starting?").grid(column=6, row=4)
                    ttk.Label(self.frame, text = "Injured?").grid(column=7, row=4)
                    ttk.Label(self.frame, text = "Games Remaining").grid(column=8, row=4)
                    for player in team.getroster():
                        self.team2rosterStrings.append(StringVar());
                        self.team2startingInts.append(IntVar());
                        self.team2injuredInts.append(IntVar());
                        self.team2gameRemainStrings.append(StringVar());
                        ttk.Label(self.frame, textvariable=self.team2rosterStrings[ct]).grid(column=5, row=5+ct)
                        ttk.Checkbutton(self.frame,variable = self.team2startingInts[ct]).grid(column=6, row=5+ct)
                        ttk.Checkbutton(self.frame,variable = self.team2injuredInts[ct]).grid(column=7, row=5+ct)
                        ttk.Label(self.frame, textvariable=self.team2gameRemainStrings[ct]).grid(column=8, row=5+ct)
                        ct += 1;
                    
                    
                    buttonRow = 5+ct;
                    ttk.Button(self.frame, text='Team 2 Refresh', command = lambda: self.updateGameCount(teams,value,"Team 2")).grid(column=5,row=buttonRow)                        
                    ttk.Label(self.frame, text = "TOTAL: ").grid(column=7, row=buttonRow+1)
                    ttk.Label(self.frame, textvariable=self.Team2TotalStr).grid(column=8, row=buttonRow+1)
            

            if stringvar.get() == Team1Str.get():
                ct = 0;
                for player in teams[value-1].getroster():
                    self.team1rosterStrings[ct].set(player.getname())
#                    if not self.team1startingInts[ct].get() or self.team1injuredInts[ct].get():
#                        self.team1gameRemainStrings[ct].set('0');
#                    else:
#                        self.team1gameRemainStrings[ct].set(player.playerGamesBetween(startDate,endDate))
                    ct += 1;
                    
            if stringvar.get() == Team2Str.get():
                ct = 0;
                for player in teams[value-1].getroster():
                    self.team2rosterStrings[ct].set(player.getname())
                    if not self.team2startingInts[ct].get() or self.team2injuredInts[ct].get():
                        self.team2gameRemainStrings[ct].set('0');
                    else:
                        self.team2gameRemainStrings[ct].set(player.playerGamesBetween(startDate,endDate))
                    ct += 1;


            
         
#League = ['Team1','Team2'];
root = Tk();
#
monthStartInt = IntVar()
monthStartStr = StringVar()
dayStartInt = IntVar()
dayStartStr = StringVar()
yearStartInt = IntVar()
yearStartStr = StringVar()

monthEndInt = IntVar()
monthEndStr = StringVar()
dayEndInt = IntVar()
dayEndStr = StringVar()
yearEndInt = IntVar()
yearEndStr = StringVar()

Team1Int = IntVar()
Team1Str = StringVar()
Team2Int = IntVar()
Team2Str = StringVar()




#def appSetup(fantasyLeague):
#    TeamInts = [];
#    TeamStrs = [];
#    teams = fantasyLeague.getFantasyTeams()
#    
#    for item in teams:
#        TeamInts.append(IntVar());
#        TeamStrs.append(StringVar());
#        
#    return [TeamInts,TeamStrs]


#
#
#A = GameCounterApp(root, League);
#root.mainloop();