import tkinter as tk
from tkinter import font
from tkinter import StringVar
from PIL import Image, ImageTk

# Open File
with open ("stats.txt", "r") as file:
    file_contents = file.read()

# Gui Start
root = tk.Tk()
root.title("Hot Lava Stats Checker")
root.resizable(False, False)
root.iconbitmap("bin\\HTSC.ico")

# background
background_image = Image.open("bin\\BackGround.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

def resize_window():
    # Set the desired width and height
    desired_width = 700
    desired_height = 650

    # Get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the center position
    x = (screen_width - desired_width) // 2
    y = (screen_height - desired_height) // 2

    # Set the Tkinter window size and position
    root.geometry(f"{desired_width}x{desired_height}+{x}+{y}")
resize_window()

# Map Select Dropdown
# list
Gym_Jam = "tutorial.Jump"
Trampoline_Trouble = "tutorial.Course 3"

GymClassList = [
    "Gym Jam",
    "Trampoline Trouble",
    "Livin' on the Ledge",
    "Surfing Surfaces",
    "Pole Vault",
    "Chase Your Sister",
    "All Course Marathon",
    "Pogo trial",
    "Tiny toy trial",
    "Jetpack trial"
    ]

PlaygroundList = [
    "Recess",
    "Big kids side",
    "Bouncy castle",
    "Back to Class",
    "Sports Day",
    "Chase the Big Kid",
    "All Course Marathon",
    "Pogo trial (1 - 2)",
    "Tiny Toy trial (1)",
    "Tiny Toy trial (2)",
    "Jetpack trial",
    "Chase the Grade"
]

SchoolList = [
    "ABCs and 123s",
    "Middle School Mischief",
    "Repeat the Grade",
    "Senior Trip",
    "Freshman Frenzy",
    "Chase Your Sister",
    "Chase the Grade",
    "Pogo trial 1",
    "Pogo trial 2",
    "Pogo trial 3",
    "Jetpack trial",
    "Tiny Toy trial",
    "All Course Marathon"
]

WholesaleList = [
    "To the Top",
    "Duct and Cover",
    "Meat Market",
    "Returns",
    "Meat Grinder",
    "Chase Through the Store",
    "Pogo trial 1",
    "Pogo trial 2",
    "Pogo trial 3",
    "Chase the Grade",
    "Jetpack trial",
    "Tiny Toy trial",
    "All Course Marathon"
]
    
MasterclassList = [
    "Air Control Mastery",
    "Wall Jump Mastery",
    "Surf Mastery",
    "Boosting Mastery",
    "Wind Tunnel Mastery",
    "Honor Gym Class",
    "Pogo trial",
    "Tiny Toy trial",
    "Jetpack trial",
    "All Course Marathon"
]
    
BasementList = [
    "Race to the Summit",
    "Lights Out",
    "Temple Sprint",
    "Fancy Footwork",
    "Minecart Carnage",
    "Chase The Meaning",
    "Jetpack trial",
    "Tiny Toy trial",
    "Pogo trial",
    "All Course Marathon"
]

RoccoList = [
    "Arcade Action",
    "Rocco's Rumpus Room",
    "Employees Only",
    "Storage Room Spree",
    "Birthday Blowout",
    "Chase to the Arcade",
    "Pogo trial 1",
    "Pogo trial 2",
    "Jetpack trial",
    "Tiny Toy trial",
    "All Course Marathon"
]
    
BlueBoxList = [
    "Windmill Valley",
    "Big Rock Canyon",
    "Rooftop Rush",
    "Giant's Garage",
    "Snowy-Mountain Sliding",
    "All Star Marathon"
]
    
ParkourIslandList = [
    "The Gauntlet"
]

SunshineShoreList = [
    "Sand Structure Scaling",
    "Gem Grabbing",
    "Castle Caper",
    "Tanning Trek",
    "Beacon Boarding",
    "Water Wading",
    "Pogo trial 1",
    "Pogo trial 2",
    "Pogo trial 3",
    "Tiny Toy trial 1",
    "Tiny Toy trial 2",
    "Tiny Toy trial 3"
]
    
GATList = [
    "The Mount Vile Gauntlet trial",
    "Poizone's Perlisous Pit",
    "T.O.X.I.C. Trampolines of Terror"
]

JourneyList = [
    "City",
    "Farm",
    "Forest",
    "Harbor",
    "Island",
    "Volcano"
]
    
WeeklyList = [
    "Gym Class",
    "Playground",
    "School",
    "Wholesale",
    "Masterclass",
    "Basement",
    "Rocco's Arcade",
    "BlueBox",
    "Sunshine Shore",
    "G.A.T HQ",
    "Journey"
]
    
MapList = [
    "Gym Class",
    "Playground",
    "School",
    "Wholesale",
    "Masterclass",
    "Basement",
    "Rocco's Arcade",
    "BlueBox",
    "Parkour Island",
    "Sunshine Shore",
    "G.A.T HQ",
    "Journey",
    "Weekly Challenge"
    ]

selected_option = StringVar()
options = GymClassList
selected_option.set(options[0])  # Set the default selection


selected_option_Playground = StringVar()
options2 = PlaygroundList
selected_option_Playground.set(options2[0])

selected_option_School = StringVar()
options3 = SchoolList
selected_option_School.set(options3[0])

selected_option_Wholesale = StringVar()
options4 = WholesaleList
selected_option_Wholesale.set(options4[0])

selected_option_Mastery = StringVar()
options5 = MasterclassList
selected_option_Mastery.set(options5[0])

selected_option_Basement = StringVar()
options6 = BasementList
selected_option_Basement.set(options6[0])

selected_option_Rocco = StringVar()
options7 = RoccoList
selected_option_Rocco.set(options7[0])

selected_option_BlueBox = StringVar()
options8 = BlueBoxList
selected_option_BlueBox.set(options8[0])

selected_option_ParkourIsland = StringVar()
options9 = ParkourIslandList
selected_option_ParkourIsland.set(options9[0])

selected_option_SunshineShore = StringVar()
options10 = SunshineShoreList
selected_option_SunshineShore.set(options10[0])

selected_option_GAT = StringVar()
options11 = GATList
selected_option_GAT.set(options11[0])

selected_option_Journey = StringVar()
options12 = JourneyList
selected_option_Journey.set(options12[0])

selected_option_Weekly = StringVar()
options13 = WeeklyList
selected_option_Weekly.set(options13[0])

# Gym Class
def option_gymclass(event):
    print("option_gymclass")
    selected_option.set(event)
    global index
    if event == "Gym Jam":
        print("Selected: Gym Jam")
        index = "tutorial.Jump"
    if event == "Trampoline Trouble":
        print("Selected: Trampoline Trouble")
        index = "tutorial.Course 3"
    if event == "Livin' on the Ledge":
        print("Selected: Livin' on the Ledge")
        index = "tutorial.Course 5"
    if event == "Surfing Surfaces":
        print("Selected: Surfing Surfaces")
        index = "tutorial.Course 4"
    if event == "Pole Vault":
        print("Selected: Pole Vault")
        index = "tutorial.Course 2"
    if event == "Chase Your Sister":
        print("Selected: Chase Your Sister")
        index = "tutorial"
    if event == "All Course Marathon":
        print("Selected: All Course Marathon")
        index = "tutorial.All Course"
    if event == "Pogo trial":
        print("Selected: Pogo trial")
        index = "tutorial.Pogo Trial"
    if event == "Tiny toy trial":
        print("Selected: Tiny toy trial")
        index = "tutorial.Tiny Toy Trial"
    if event == "Jetpack trial":
        print("Selected: Jetpack trial")
        index = "tutorial.Jetpack"   
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")
            
# Playground
def option_Playground(event):
    print("option_Playground")
    selected_option_Playground.set(event)
    global index
    if event == "Recess":
        print("Selected: Recess")
        index = "playground.Recess"
        
    if event == "Big kids side":
        print("Selected: Big kids side")
        index = "playground.Intermediate"
        
    if event == "Bouncy castle":
        print("Selected: Bouncy castle")
        index = "playground.Bouncy Castle"
        
    if event == "Back to Class":
        print("Selected: Back to Class")
        index = "playground.Back To Class"
        
    if event == "Sports Day":
        print("Selected: Sports Day")
        index = "playground.Sports Day"
        
    if event == "Chase the Big Kid":
        print("Selected: Chase the Big Kid")
        index = "playground.Grounders"
        
    if event == "All Course Marathon":
        print("Selected: All Course Marathon")
        index = "playground.All Course"
        
    if event == "Pogo trial (1 - 2)":
        print("Selected: Pogo trial")
        index = "playground.Pogo 2-1"
        
    if event == "Tiny Toy trial (1)":
        print("Selected: Tiny toy trial 1")
        index = "playground.Tiny Toy 1"
        
    if event == "Tiny Toy trial (2)":
        print("Selected: Tiny toy trial 2")
        index = "playground.Tiny Toy 2"
        
    if event == "Jetpack trial":
        print("Selected: Jetpack trial")
        index = "playground.Jetpack 1-1"   
        
    if event == "Chase the Grade":
        print("Selected: Chase the Grade")
        index = "playground.Chase Grade"   
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")
        
# School
def option_School(event):
    print("option_School")
    selected_option_School.set(event)
    global index
    if event == "ABCs and 123s":
        print("Selected: ABCs and 123s")
        index = "school.Participation"
        
    if event == "Middle School Mischief":
        print("Selected: Middle School Mischief")
        index = "school.Alternate Path"
        
    if event == "Repeat the Grade":
        print("Selected: Repeat the Grade")
        index = "school.Reverse"
        
    if event == "Senior Trip":
        print("Selected: Senior Trip")
        index = "school.Scavenger"
        
    if event == "Freshman Frenzy":
        print("Selected: Freshman Frenzy")
        index = "school.Head Rush"
        
    if event == "Chase Your Sister":
        print("Selected: Chase Your Sister")
        index = "school.Chase Sue"
        
    if event == "Chase the Grade":
        print("Selected: Chase the Grade")
        index = "school.Pursuit"
        
    if event == "Pogo trial 1":
        print("Selected: Pogo trial 1")
        index = "school.Pogo 1-1"
        
    if event == "Pogo trial 2":
        print("Selected: Pogo trial 2")
        index = "school.Pogo 2-1"
        
    if event == "Pogo trial 3":
        print("Selected: Pogo trial 3")
        index = "school.Pogo 3-1"
        
    if event == "Jetpack trial":
        print("Selected: Jetpack trial")
        index = "school.Jetpack 1-1"   
        
    if event == "Tiny Toy trial":
        print("Selected: Tiny Toy trial")
        index = "school.Tiny Toy"   
        
    if event == "All Course Marathon":
        print("Selected: All Course Marathon")
        index = "school.All Courses"  
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")

# Wholesale
def option_Wholesale(event):
    print("option_Wholesale")
    selected_option_Wholesale.set(event)
    global index
    if event == "To the Top":
        print("Selected: To the Top")
        index = "wholesale_expanded.To The Top"
        
    if event == "Duct and Cover":
        print("Selected: Duct and Cover")
        index = "wholesale_expanded.Fort"
        
    if event == "Meat Market":
        print("Selected: Meat Market")
        index = "wholesale_expanded.Break"
        
    if event == "Returns":
        print("Selected: Returns")
        index = "wholesale_expanded.Returns"
        
    if event == "Meat Grinder":
        print("Selected: Meat Grinder")
        index = "wholesale_expanded.Meat Grinder"
        
    if event == "Chase Through the Store":
        print("Selected: Chase Through the Store")
        index = "wholesale_expanded.Chase the Dollar"
        
    if event == "Pogo trial 1":
        print("Selected: Pogo trial 1")
        index = "wholesale_expanded.Pogo Trial 1-1"
        
    if event == "Pogo trial 2":
        print("Selected: Pogo trial 2")
        index = "wholesale_expanded.Pogo Trial 2-1"
        
    if event == "Pogo trial 3":
        print("Selected: Pogo trial 3")
        index = "wholesale_expanded.Pogo Trial 3-1"
        
    if event == "Chase the Grade":
        print("Selected: Chase the Grade")
        index = "wholesale_expanded.Chase Grade"
        
    if event == "Jetpack trial":
        print("Selected: Jetpack trial")
        index = "wholesale_expanded.Jetpack Trial 1-1"   
        
    if event == "Tiny Toy trial":
        print("Selected: Tiny Toy trial")
        index = "wholesale_expanded.Tiny Toy"   
        
    if event == "All Course Marathon":
        print("Selected: All Course Marathon")
        index = "wholesale_expanded.All Courses"  
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")

# Masterclass
def option_Mastery(event):
    print("option_Mastery")
    selected_option_Mastery.set(event)
    global index
    if event == "Air Control Mastery":
        print("Selected: Air Control Mastery")
        index = "mastery_gym.Air Control Training"
        
    if event == "Wall Jump Mastery":
        print("Selected: Wall Jump Mastery")
        index = "mastery_gym.Wall Run Training"
        
    if event == "Surf Mastery":
        print("Selected: Surf Mastery")
        index = "mastery_gym.Surf Training"
        
    if event == "Boosting Mastery":
        print("Selected: Boosting Mastery")
        index = "mastery_gym.Bhop Open"
        
    if event == "Wind Tunnel Mastery":
        print("Selected: Wind Tunnel Mastery")
        index = "mastery_gym.Fan Training"
        
    if event == "Honor Gym Class":
        print("Selected: Honor Gym Class")
        index = "mastery_gym.Masters"
        
    if event == "Pogo trial":
        print("Selected: Pogo trial")
        index = "mastery_gym.Pogo 1-1"
        
    if event == "Tiny Toy trial":
        print("Selected: Tiny Toy trial")
        index = "mastery_gym.Tiny Toy"
        
    if event == "Jetpack trial":
        print("Selected: Jetpack trial")
        index = "mastery_gym.Jetpack 1-1"
        
    if event == "All Course Marathon":
        print("Selected: All Course Marathon")
        index = "mastery_gym.All Course"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")
            
# Basement
def option_Basement(event):
    print("option_Basement")
    selected_option_Basement.set(event)
    global index
    if event == "Race to the Summit":
        print("Selected: Race to the Summit")
        index = "basement.Course One"
        
    if event == "Lights Out":
        print("Selected: Lights Out")
        index = "basement.Course Two"
        
    if event == "Temple Sprint":
        print("Selected: Temple Sprint")
        index = "basement.Course Three"
        
    if event == "Fancy Footwork":
        print("Selected: Fancy Footwork")
        index = "basement.Course Four"
        
    if event == "Minecart Carnage":
        print("Selected: Minecart Carnage")
        index = "basement.Course Five"
        
    if event == "Chase The Meaning":
        print("Selected: Chase The Meaning")
        index = "basement.Course Six"
        
    if event == "Jetpack trial":
        print("Selected: Jetpack trial")
        index = "basement.Jetpack 1-1"
        
    if event == "Tiny Toy trial":
        print("Selected: Tiny Toy trial")
        index = "basement.Tiny Toy"
        
    if event == "Pogo trial":
        print("Selected: Pogo trial")
        index = "basement.Pogo"
        
    if event == "All Course Marathon":
        print("Selected: All Course Marathon")
        index = "basement.All Course"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")
            
# Rocco
def option_Rocco(event):
    print("option_Rocco")
    selected_option_Rocco.set(event)
    global index
    if event == "Arcade Action":
        print("Selected: Arcade Action")
        index = "fun_centre.Arcade"
        
    if event == "Rocco's Rumpus Room":
        print("Selected: Rocco's Rumpus Room")
        index = "fun_centre.Restaurant"
        
    if event == "Employees Only":
        print("Selected: Employees Only")
        index = "fun_centre.Staff Only"
        
    if event == "Storage Room Spree":
        print("Selected: Storage Room Spree")
        index = "fun_centre.course 4"
        
    if event == "Birthday Blowout":
        print("Selected: Birthday Blowout")
        index = "fun_centre.Course 5"
        
    if event == "Chase to the Arcade":
        print("Selected: Chase to the Arcade")
        index = "fun_centre.Course 6"
        
    if event == "Pogo trial 1":
        print("Selected: Pogo trial 1")
        index = "fun_centre.pogo"
        
    if event == "Pogo trial 2":
        print("Selected: Pogo trial 2")
        index = "fun_centre.pogo 2"
        
    if event == "Jetpack trial":
        print("Selected: Jetpack trial")
        index = "fun_centre.Jetpack"
        
    if event == "Tiny Toy trial":
        print("Selected: Tiny Toy trial")
        index = "fun_centre.TinyToy"
        
    if event == "All Course Marathon":
        print("Selected: All Course Marathon")
        index = "fun_centre.All Course"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")
            
# BlueBox
def option_BlueBox(event):
    print("option_BlueBox")
    selected_option_BlueBox.set(event)
    global index
    if event == "Windmill Valley":
        print("Selected: Windmill Valley")
        index = "The Blue Box.Windmill Valley"
        
    if event == "Big Rock Canyon":
        print("Selected: Big Rock Canyon")
        index = "The Blue Box.Big Rock Canyon"
        
    if event == "Rooftop Rush":
        print("Selected: Rooftop Rush")
        index = "The Blue Box.Rooftop Rush"
        
    if event == "Giant's Garage":
        print("Selected: Giant's Garage")
        index = "The Blue Box.Giant's Garage"
        
    if event == "Snowy-Mountain Sliding":
        print("Selected: Snowy-Mountain Sliding")
        index = "The Blue Box.Snowy-Mountain Sliding"
        
    if event == "All Star Marathon":
        print("Selected: All Star Marathon")
        index = "The Blue Box.All Star Marathon"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")
            
# ParkourIsland
def option_ParkourIsland(event):
    print("option_ParkourIsland")
    selected_option_ParkourIsland.set(event)
    global index
    if event == "The Gauntlet":
        print("Selected: The Gauntlet")
        index = "Parkour_Island.Gauntlet"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")

# SunshineShore
def option_SunshineShore(event):
    print("option_SunshineShore")
    selected_option_SunshineShore.set(event)
    global index
    if event == "Sand Structure Scaling":
        print("Selected: Sand Structure Scaling")
        index = "Sunshine.Sand Structure Scaling"
        
    if event == "Gem Grabbing":
        print("Selected: Gem Grabbing")
        index = "Sunshine.Gem Grabbing"
        
    if event == "Castle Caper":
        print("Selected: Castle Caper")
        index = "Sunshine.Castle Caper"
        
    if event == "Tanning Trek":
        print("Selected: Tanning Trek")
        index = "Sunshine.Tanning Trek"
        
    if event == "Beacon Boarding":
        print("Selected: Beacon Boarding")
        index = "Sunshine.Beacon Boarding"

    if event == "Water Wading":
        print("Selected: Water Wading")
        index = "Sunshine.Water Wading"

    if event == "Pogo trial 1":
        print("Selected: Pogo trial 1")
        index = "Sunshine.Pogo 1-1"
        
    if event == "Pogo trial 2":
        print("Selected: Pogo trial 2")
        index = "Sunshine.Pogo 2-1"
        
    if event == "Pogo trial 3":
        print("Selected: Pogo trial 3")
        index = "Sunshine.Pogo 3-1"
        
    if event == "Tiny Toy trial 1":
        print("Selected: Tiny Toy trial 1")
        index = "Sunshine.Tiny Toy Trial 1"
        
    if event == "Tiny Toy trial 2":
        print("Selected: Tiny Toy trial 3")
        index = "Sunshine.Tiny Toy Trial 2"
        
    if event == "Tiny Toy trial 3":
        print("Selected: Tiny Toy trial 3")
        index = "Sunshine.Tiny Toy Trial 3"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A")
            
# GAT
def option_GAT(event):
    print("option_GAT")
    selected_option_GAT.set(event)
    global index
    if event == "The Mount Vile Gauntlet trial":
        print("Selected: The Mount Vile Gauntlet trial")
        index = "gat_hq.gauntlet"
        
    if event == "Poizone's Perlisous Pit":
        print("Selected: Poizone's Perlisous Pit")
        index = "gat_hq.don't look down"
        
    if event == "T.O.X.I.C. Trampolines of Terror":
        print("Selected: T.O.X.I.C. Trampolines of Terror")
        index = "gat_hq.toxic work enviroment"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A") 
        
# Journey
def option_Journey(event):
    print("option_Journey")
    selected_option_Journey.set(event)
    global index
    if event == "City":
        print("Selected: City")
        index = "Journey.City"
        
    if event == "Farm":
        print("Selected: Farm")
        index = "Journey.Farm"
        
    if event == "Forest":
        print("Selected: Forest")
        index = "Journey.Forest"
        
    if event == "Harbor":
        print("Selected: Harbor")
        index = "Journey.Harbor"
        
    if event == "Island":
        print("Selected: Island")
        index = "Journey.Island"
        
    if event == "Volcano":
        print("Selected: Volcano")
        index = "Journey.Volcano"
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A") 
            
# Weekly
def option_Weekly(event):
    print("option_Weekly")
    selected_option_Weekly.set(event)
    global index
    if event == "Gym Class":
        print("Selected: Gym Class")
        index = "tutorial.Weekly Challenge"
        
    if event == "Playground":
        print("Selected: Playground")
        index = "playground.Weekly Challenge"
        
    if event == "School":
        print("Selected: School")
        index = "school.Weekly Challenge"
        
    if event == "Wholesale":
        print("Selected: Wholesale")
        index = "wholesale_expanded.Weekly Challenge"
        
    if event == "Masterclass":
        print("Selected: Masterclass")
        index = "mastery_gym.Weekly Challenge"
        
    if event == "Basement":
        print("Selected: Basement")
        index = "basement.Weekly Challenge"
        
    if event == "Rocco's Arcade":
        print("Selected: Rocco's Arcade")
        index = "fun_centre.Weekly Challenge"
        
    if event == "BlueBox":
        print("Selected: BlueBox")
        index = "The Blue Box.Weekly Challenge"
        
    if event == "Sunshine Shore":
        print("Selected: Sunshine Shore")
        index = "Sunshine.Weekly Challenge"
        
    if event == "G.A.T HQ":
        print("Selected: G.A.T HQ")
        index = "gat_hq.Weekly Challenge"
        
    if event == "Journey":
        print("Selected: Journey")
        index = "Journey.Weekly Challenge"
        
    
    def extract_statistics(text):
        start_index = text.find(index)  
        end_index = text.find("}}", start_index)  

        if start_index != -1 and end_index != -1:
            return text[start_index:end_index + 2]
        else:
            return None

    statistics_text = extract_statistics(file_contents)
    with open ("bin\\DONTTOUCH.txt", "w") as file:
        file.write(statistics_text)

        def extract_statistics_DT(text2):
            global DistanceTraveled
            if "DistanceTraveled" in text2:
                global findstart
                findstart = text2.find("DistanceTraveled")  
                DistanceTraveled = True
            else:
                DistanceTraveled = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        statistics_text_DT = extract_statistics_DT(statistics_text)
        
        if DistanceTraveled == True:
            print("DistanceTraveled: ",DistanceTraveled)
            statistics_text_DT = statistics_text_DT.replace('''DistanceTraveled":''', "")
            statistics_text_DT = statistics_text_DT.replace(''',"''', "")
            statistics_text_DT = statistics_text_DT.replace('''}''', "")
            statistics_text_DT = statistics_text_DT.replace('''"''', "")
            parts = statistics_text_DT.split(".")
            statistics_text_DT = parts[0]
            DistanceTravellabel.config(text=statistics_text_DT)
        else:
            print("DistanceTraveled: ",DistanceTraveled)
            DistanceTravellabel.config(text="N/A")
        
        def extract_statistics_TJ(text2):
            global TotalJumps
            if "TotalJumps" in text2:
                global findstart
                findstart = text2.find("TotalJumps")  
                TotalJumps = True
            else:
                TotalJumps = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_TJ = extract_statistics_TJ(statistics_text)
        
        if TotalJumps == True:
            print("TotalJumps:",TotalJumps)
            extract_text_TJ = extract_text_TJ.replace('''TotalJumps":''', "")
            extract_text_TJ = extract_text_TJ.replace(''',"''', "")
            extract_text_TJ = extract_text_TJ.replace('''}''', "")
            extract_text_TJ = extract_text_TJ.replace('''"''', "")
            jumplabel.config(text=extract_text_TJ)
        else:
            print("TotalJumps:",TotalJumps)
            jumplabel.config(text="N/A")
                
        def extract_statistics_LD(text2):
            global Lava
            if "Lava" in text2:
                global findstart
                findstart = text2.find("Lava")
                Lava = True
            else: 
                Lava = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_LD = extract_statistics_LD(statistics_text)
        
        if Lava == True:
            print("Lava: ",Lava)
            extract_text_LD = extract_text_LD.replace('''Lava":''', "")
            extract_text_LD = extract_text_LD.replace(''',"''', "")
            extract_text_LD = extract_text_LD.replace('''}''', "")
            extract_text_LD = extract_text_LD.replace('''"''', "")
            lavalabel.config(text=extract_text_LD)
        else:
            print("Lava: ",Lava)
            lavalabel.config(text="N/A")
        
        def extract_statistics_Restart(text2):
            global Restart
            if "Restart" in text2:
                global findstart
                findstart = text2.find("Restart")
                Restart = True
            else: 
                Restart = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_Restart = extract_statistics_Restart(statistics_text)
        
        if Restart == True:
            print("Restart: ",Restart)
            extract_text_Restart = extract_text_Restart.replace('''Restart":''', "")
            extract_text_Restart = extract_text_Restart.replace(''',"''', "")
            extract_text_Restart = extract_text_Restart.replace('''}''', "")
            extract_text_Restart = extract_text_Restart.replace('''"''', "")
            restartlabel.config(text=extract_text_Restart)
        else:
            print("Restart: ",Restart)
            restartlabel.config(text="N/A")
            
        def extract_statistics_CL(text2):
            global Collision
            if "Collision" in text2:
                global findstart
                findstart = text2.find("Collision")
                Collision = True
            else: 
                Collision = False
            findend = text2.find(''',"''', findstart)  

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CL = extract_statistics_CL(statistics_text)
        
        if Collision == True:
            print("Collision: ", Collision)
            extract_text_CL = extract_text_CL.replace('''Collision":''', "")
            extract_text_CL = extract_text_CL.replace(''',"''', "")
            extract_text_CL = extract_text_CL.replace('''}''', "")
            extract_text_CL = extract_text_CL.replace('''"''', "")
            collisionlabel.config(text=extract_text_CL)
        else:
            print("Collision: ", Collision)
            collisionlabel.config(text="N/A")
        
        
        def extract_statistics_CH(text2):
            global GoToCheckpoint
            if "GoToCheckpoint" in text2:
                global findstart
                findstart = text2.find("GoToCheckpoint")   
                GoToCheckpoint = True
            else:
                GoToCheckpoint = False         
            findend = text2.find(''',''', findstart)

            if findstart != -1 and findend != -1:
                return text2[findstart:findend + 2]
            else:
                return None
            
        extract_text_CH = extract_statistics_CH(statistics_text)
        
        if GoToCheckpoint == True:
            print("GoToCheckpoint: ",GoToCheckpoint)
            extract_text_CH = extract_text_CH.replace('''GoToCheckpoint":''', "")
            extract_text_CH = extract_text_CH.replace(''',''', "")
            extract_text_CH = extract_text_CH.replace('''}''', "")
            extract_text_CH = extract_text_CH.replace('''"''', "")
            checkpointlabel.config(text=extract_text_CH)
        else:
            print("GoToCheckpoint: ",GoToCheckpoint)
            checkpointlabel.config(text="N/A") 
        
        

# GymClass
dropdown1_frame_color = "white"
dropdown1_frame = tk.Frame(root, bg=dropdown1_frame_color, highlightbackground=dropdown1_frame_color, highlightthickness=1)
dropdown1_frame.place(x=20, y=5)

dropdown1_font = font.Font(family="Arial", size=15, weight="bold")
dropdown1 = tk.OptionMenu(dropdown1_frame, selected_option, *GymClassList, command=option_gymclass)
dropdown1.config(width=18, height=1, bg="#313131", fg="white", font=dropdown1_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown1['menu'].config(bg="#313131", fg="white", font=dropdown1_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown1.pack()

# Playground
dropdown2_frame_color = "white"
dropdown2_frame = tk.Frame(root, bg=dropdown2_frame_color, highlightbackground=dropdown2_frame_color, highlightthickness=1)
dropdown2_frame.place(x=20, y=55)

dropdown2_font = font.Font(family="Arial", size=15, weight="bold")
dropdown2 = tk.OptionMenu(dropdown2_frame, selected_option_Playground, *PlaygroundList, command=option_Playground)
dropdown2.config(width=18, height=1, bg="#313131", fg="white", font=dropdown2_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown2['menu'].config(bg="#313131", fg="white", font=dropdown2_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown2.pack()

# School
dropdown3_frame_color = "white"
dropdown3_frame = tk.Frame(root, bg=dropdown3_frame_color, highlightbackground=dropdown3_frame_color, highlightthickness=1)
dropdown3_frame.place(x=20, y=105)

dropdown3_font = font.Font(family="Arial", size=15, weight="bold")
dropdown3 = tk.OptionMenu(dropdown3_frame, selected_option_School, *SchoolList, command=option_School)
dropdown3.config(width=18, height=1, bg="#313131", fg="white", font=dropdown3_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown3['menu'].config(bg="#313131", fg="white", font=dropdown3_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown3.pack()

# Wholesale
dropdown4_frame_color = "white"
dropdown4_frame = tk.Frame(root, bg=dropdown4_frame_color, highlightbackground=dropdown4_frame_color, highlightthickness=1)
dropdown4_frame.place(x=20, y=155)

dropdown4_font = font.Font(family="Arial", size=15, weight="bold")
dropdown4 = tk.OptionMenu(dropdown4_frame, selected_option_Wholesale, *WholesaleList, command=option_Wholesale)
dropdown4.config(width=18, height=1, bg="#313131", fg="white", font=dropdown4_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown4['menu'].config(bg="#313131", fg="white", font=dropdown4_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown4.pack()

# Masterclass
dropdown5_frame_color = "white"
dropdown5_frame = tk.Frame(root, bg=dropdown5_frame_color, highlightbackground=dropdown5_frame_color, highlightthickness=1)
dropdown5_frame.place(x=20, y=205)

dropdown5_font = font.Font(family="Arial", size=15, weight="bold")
dropdown5 = tk.OptionMenu(dropdown5_frame, selected_option_Mastery, *MasterclassList, command=option_Mastery)
dropdown5.config(width=18, height=1, bg="#313131", fg="white", font=dropdown5_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown5['menu'].config(bg="#313131", fg="white", font=dropdown5_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown5.pack()

# Basement
dropdown6_frame_color = "white"
dropdown6_frame = tk.Frame(root, bg=dropdown6_frame_color, highlightbackground=dropdown6_frame_color, highlightthickness=1)
dropdown6_frame.place(x=20, y=255)

dropdown6_font = font.Font(family="Arial", size=15, weight="bold")
dropdown6 = tk.OptionMenu(dropdown6_frame, selected_option_Basement, *BasementList, command=option_Basement)
dropdown6.config(width=18, height=1, bg="#313131", fg="white", font=dropdown6_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown6['menu'].config(bg="#313131", fg="white", font=dropdown6_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown6.pack()

# Rocco
dropdown7_frame_color = "white"
dropdown7_frame = tk.Frame(root, bg=dropdown7_frame_color, highlightbackground=dropdown7_frame_color, highlightthickness=1)
dropdown7_frame.place(x=20, y=305)

dropdown7_font = font.Font(family="Arial", size=15, weight="bold")
dropdown7 = tk.OptionMenu(dropdown7_frame, selected_option_Rocco, *RoccoList, command=option_Rocco)
dropdown7.config(width=18, height=1, bg="#313131", fg="white", font=dropdown7_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown7['menu'].config(bg="#313131", fg="white", font=dropdown7_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown7.pack()

# BlueBox
dropdown8_frame_color = "white"
dropdown8_frame = tk.Frame(root, bg=dropdown8_frame_color, highlightbackground=dropdown8_frame_color, highlightthickness=1)
dropdown8_frame.place(x=20, y=355)

dropdown8_font = font.Font(family="Arial", size=15, weight="bold")
dropdown8 = tk.OptionMenu(dropdown8_frame, selected_option_BlueBox, *BlueBoxList, command=option_BlueBox)
dropdown8.config(width=18, height=1, bg="#313131", fg="white", font=dropdown8_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown8['menu'].config(bg="#313131", fg="white", font=dropdown8_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown8.pack()

# ParkourIsland
dropdown9_frame_color = "white"
dropdown9_frame = tk.Frame(root, bg=dropdown9_frame_color, highlightbackground=dropdown9_frame_color, highlightthickness=1)
dropdown9_frame.place(x=20, y=405)

dropdown9_font = font.Font(family="Arial", size=15, weight="bold")
dropdown9 = tk.OptionMenu(dropdown9_frame, selected_option_ParkourIsland, *ParkourIslandList, command=option_ParkourIsland)
dropdown9.config(width=18, height=1, bg="#313131", fg="white", font=dropdown9_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown9['menu'].config(bg="#313131", fg="white", font=dropdown9_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown9.pack()

# SunshineShore
dropdown10_frame_color = "white"
dropdown10_frame = tk.Frame(root, bg=dropdown10_frame_color, highlightbackground=dropdown10_frame_color, highlightthickness=1)
dropdown10_frame.place(x=20, y=455)

dropdown10_font = font.Font(family="Arial", size=15, weight="bold")
dropdown10 = tk.OptionMenu(dropdown10_frame, selected_option_SunshineShore, *SunshineShoreList, command=option_SunshineShore)
dropdown10.config(width=18, height=1, bg="#313131", fg="white", font=dropdown10_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown10['menu'].config(bg="#313131", fg="white", font=dropdown10_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown10.pack()

# GAT
dropdown11_frame_color = "white"
dropdown11_frame = tk.Frame(root, bg=dropdown11_frame_color, highlightbackground=dropdown11_frame_color, highlightthickness=1)
dropdown11_frame.place(x=20, y=505)

dropdown11_font = font.Font(family="Arial", size=15, weight="bold")
dropdown11 = tk.OptionMenu(dropdown11_frame, selected_option_GAT, *GATList, command=option_GAT)
dropdown11.config(width=18, height=1, bg="#313131", fg="white", font=dropdown11_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown11['menu'].config(bg="#313131", fg="white", font=dropdown11_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown11.pack()

# Journey
dropdown12_frame_color = "white"
dropdown12_frame = tk.Frame(root, bg=dropdown12_frame_color, highlightbackground=dropdown12_frame_color, highlightthickness=1)
dropdown12_frame.place(x=20, y=555)

dropdown12_font = font.Font(family="Arial", size=15, weight="bold")
dropdown12 = tk.OptionMenu(dropdown12_frame, selected_option_Journey, *JourneyList, command=option_Journey)
dropdown12.config(width=18, height=1, bg="#313131", fg="white", font=dropdown12_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown12['menu'].config(bg="#313131", fg="white", font=dropdown12_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown12.pack()

# Weekly
dropdown13_frame_color = "white"
dropdown13_frame = tk.Frame(root, bg=dropdown13_frame_color, highlightbackground=dropdown13_frame_color, highlightthickness=1)
dropdown13_frame.place(x=20, y=605)

dropdown13_font = font.Font(family="Arial", size=15, weight="bold")
dropdown13 = tk.OptionMenu(dropdown13_frame, selected_option_Weekly, *WeeklyList, command=option_Weekly)
dropdown13.config(width=18, height=1, bg="#313131", fg="white", font=dropdown13_font, activebackground="#1D1D1D", activeforeground="white", relief="flat", indicatoron=0)
dropdown13['menu'].config(bg="#313131", fg="white", font=dropdown13_font, activebackground="#1D1D1D", activeforeground="white", relief="flat")
dropdown13.pack()



custom_font = font.Font(family="Impact", size=20, weight="bold")
result_font = font.Font(family="Ariel", size=20)


label = tk.Label(root, text="NOTE: IF THE STATS DONT REFRESH", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=2)

label = tk.Label(root, text="THAT MEANS THAT THERE ARE NONE", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=40)

# DistanceTravel text
label = tk.Label(root, text="DistanceTraveled: ", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=90)

DistanceTravellabel = tk.Label(root, text="0", font=result_font, bg="#090909", fg="white")
DistanceTravellabel.place(x=500, y=92)

# total jump text
label = tk.Label(root, text="Total Jumps: ", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=140)

jumplabel = tk.Label(root, text="0", font=result_font, bg="#090909", fg="white")
jumplabel.place(x=430, y=144)

# death  text
label = tk.Label(root, text="Deathinformation: ", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=260)

# lava death text
label = tk.Label(root, text="Lava: ", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=330)

lavalabel = tk.Label(root, text="0", font=result_font, bg="#090909", fg="white")
lavalabel.place(x=340, y=334)

# restart death text
label = tk.Label(root, text="Restart: ", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=400)

restartlabel = tk.Label(root, text="0", font=result_font, bg="#090909", fg="white")
restartlabel.place(x=375, y=404)

# Collision death text
label = tk.Label(root, text="Collision: ", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=470)

collisionlabel = tk.Label(root, text="0", font=result_font, bg="#090909", fg="white")
collisionlabel.place(x=395, y=474)

# Checkpoint text
label = tk.Label(root, text="Checkpoint: ", font=custom_font, bg="#090909", fg="white")
label.place(x=270, y=540)

checkpointlabel = tk.Label(root, text="0", font=result_font, bg="#090909", fg="white")
checkpointlabel.place(x=420, y=544)

# Gui End
root.mainloop()