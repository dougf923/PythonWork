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
        Team1Button = self.buildMenuButton(mainframe,Team1Str,Team1Int,3,3,7,"Team");
        
        ttk.Label(mainframe, text="Team 2: ").grid(column=5, row=3, sticky=(W,E));
        Team2Button = self.buildMenuButton(mainframe,Team2Str,Team2Int,3,7,7,"Team");
        
        
        
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        
    def buildMenuButton(self,frame,textvar,intvar,rownum,colnum,widthnum,menutype):
        menubutton = ttk.Menubutton(frame, width=widthnum, textvariable = textvar);
        menu = self.buildMenu(menubutton, intvar, textvar, menutype);
        menubutton.config(menu=menu);
        menubutton.grid(column=colnum, row=rownum, sticky=(W, E));
        
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
            teams = self.League; 
            ct = 0;
            for item in teams:
                ct += 1;
                menu.add_radiobutton(label=item, var=varInt, value=ct, command = lambda: self.setMenuLabel(varInt,textvar,menutype))
       
        return menu
    
    
    def setMenuLabel(self,intvar,stringvar,menutype): 
        value = intvar.get();
        if menutype == "Month":
            stringvar.set(self.months[value-1]);
        elif menutype == "Day":
            stringvar.set(str(value+1));
        elif menutype == "Year":
            stringvar.set(self.years[value-1]);
        elif menutype == "Team":
            stringvar.set(self.League[value-1]);


            
         
League = ['Team1','Team2'];
root = Tk();

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