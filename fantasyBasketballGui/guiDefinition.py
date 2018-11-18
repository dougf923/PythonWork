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
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
             
        # Set up Start Date Menus
        StartEnd.set("Start")
        
        ttk.Label(mainframe, text="Start Date: ").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Month").grid(column=2, row=1)
        ttk.Label(mainframe, text="Day").grid(column=3, row=1)
        ttk.Label(mainframe, text="Year").grid(column=4, row=1)
               
        DayMonthYear.set("Month")
        monthStartButton = self.buildMenuButton(mainframe,monthStartStr,monthStartInt,2,2,7,"Date");
        DayMonthYear.set("Day")
        dayStartButton = self.buildMenuButton(mainframe,dayStartStr,dayStartInt,2,3,7,"Date");        
        DayMonthYear.set("Year")
        yearStartButton = self.buildMenuButton(mainframe,yearStartStr,yearStartInt,2,4,7,"Date");
               
        # Set up End Date Menus
        StartEnd.set("End")
        
        ttk.Label(mainframe, text="End Date: ").grid(column=5, row=2, sticky=E)
        ttk.Label(mainframe, text="Month").grid(column=6, row=1)
        ttk.Label(mainframe, text="Day").grid(column=7, row=1)
        ttk.Label(mainframe, text="Year").grid(column=8, row=1)
        
        DayMonthYear.set("Month")
        monthEndButton = self.buildMenuButton(mainframe,monthEndStr,monthEndInt,2,6,7,"Date");      
        DayMonthYear.set("Day")
        dayEndButton = self.buildMenuButton(mainframe,dayEndStr,dayEndInt,2,7,7,"Date");       
        DayMonthYear.set("Year")
        yearEndButton = self.buildMenuButton(mainframe,yearEndStr,yearEndInt,2,8,7,"Date");
        
        #Set up Fantasy Team Menu's
        TeamNum.set(1);
        ttk.Label(mainframe, text="Team 1: ").grid(column=1, row=3, sticky=E);
        Team1Button = self.buildMenuButton(mainframe,Team1Str,Team1Int,3,3,7,"Team");
        
        TeamNum.set(2);
        ttk.Label(mainframe, text="Team 2: ").grid(column=5, row=3, sticky=E);
        Team2Button = self.buildMenuButton(mainframe,Team2Str,Team2Int,3,7,7,"Team");
        
        
        
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        
    def buildMenuButton(self,frame,textvar,intvar,rownum,colnum,widthnum,menutype):
        menubutton = ttk.Menubutton(frame, width=widthnum, textvariable = textvar);
        if menutype == "Date":
            menu = self.buildDateMenu(menubutton, intvar);
        elif menutype == "Team":
            menu = self.buildTeamMenu(menubutton, intvar);
        menubutton.config(menu=menu);
        menubutton.grid(column=colnum, row=rownum, sticky=(W, E));
        
        return menubutton
    
    def buildDateMenu(self,menubutton,varInt):
                     
        menu = Menu(menubutton)        
        
        
        if DayMonthYear.get() == "Month":
            
            
            ct = 0;
            for item in self.months:
                ct += 1;
                if StartEnd.get() == "Start":
                    menu.add_radiobutton(label=item, var=varInt, value=ct, command = self.setStartMonth)
                else:
                    menu.add_radiobutton(label=item, var=varInt, value=ct, command = self.setEndMonth)
                
        elif DayMonthYear.get() == "Day":

            for num in range(31):
                if StartEnd.get() == "Start":
                    menu.add_radiobutton(label=str(num+1), var=varInt, value=num, command = self.setStartDay)
                else:
                    menu.add_radiobutton(label=str(num+1), var=varInt, value=num, command = self.setEndDay)
                
        else:
            ct = 0;
            for item in self.years:
                ct += 1;
                if StartEnd.get() == "Start":
                    menu.add_radiobutton(label=item, var=varInt, value=ct, command = self.setStartYear)
                else:
                    menu.add_radiobutton(label=item, var=varInt, value=ct, command = self.setEndYear)
        return menu
    
    def buildTeamMenu(self,menubutton,varInt):
                     
        menu = Menu(menubutton)        
        
        teams = self.League; 
        ct = 0;
        for item in teams:
            ct += 1;
            if TeamNum.get() == 1:
                menu.add_radiobutton(label=item, var=varInt, value=ct, command = self.setTeam1)
            else:
                menu.add_radiobutton(label=item, var=varInt, value=ct, command = self.setTeam2)
            
        return menu
        
         
    def setStartMonth(self,*args):          
            value = monthStartInt.get();
            monthStartStr.set(self.months[value-1]);
               
    def setEndMonth(self,*args):
        value = monthEndInt.get();
        monthEndStr.set(self.months[value-1]);
            
    def setStartDay(*args):
        value = dayStartInt.get();
        dayStartStr.set(str(value+1));
        
    def setEndDay(*args):
        value = dayEndInt.get();
        dayEndStr.set(str(value+1));
            
    def setStartYear(self,*args):
        value = yearStartInt.get();
        yearStartStr.set(self.years[value-1]);
        
    def setEndYear(self,*args):
        value = yearEndInt.get();
        yearEndStr.set(self.years[value-1]);
        
    def setTeam1(self,*args):          
        value = Team1Int.get();
        Team1Str.set(self.League[value-1]);
        
    def setTeam2(self,*args):         
        value = Team2Int.get();
        Team2Str.set(self.League[value-1]);

            
         
League = ['Team1','Team2'];
root = Tk();

StartEnd = StringVar()
DayMonthYear = StringVar()
TeamNum = IntVar()

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


A = GameCounterApp(root, League);
root.mainloop();