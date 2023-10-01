# HOT LAVA STATS CHECKER.
# MADE BY - GAMEPLANETWORLD
# https://github.com/gameplanetworld
# https://www.youtube.com/@gameplanetworld

# IMPORTS

import os 
import webbrowser 

with open ("stats.txt", "r") as file:
    file_contents = file.read()
    
def fileselect():
    os.system("cls")
    print("Please copy the contents of your HLPlayerStatistics.json file to the stats.txt file!\n")
    print("For more info go to the HOT LAVA STATS CHECKER github page.")
    input("\npress enter to quit")
    exit() 
    
# START

start = True

while start == True:
    os.system("cls")
    print("""
(Type "q" and press enter to quit!)
(Type "c" and press enter to get more information for checking a different profile)
(Type "o" and press enter to open the github page)

Gym Class:
    [1] Gym Jam
    [2] Trampoline Trouble
    [3] Livin' on the Ledge
    [4] Surfing Surfaces
    [5] Pole Vault
    [6] Chase Your Sister
    [7] All Course Marathon (Gym Class)
    [8] Pogo trial
    [9] Tiny toy trial
    [10] Jetpack trial
    
Playground:
    [11] Recess
    [12] Big kids side
    [13] Bouncy castle
    [14] Back to Class
    [15] Sports Day
    [16] Chase the Big Kid
    [17] All Course Marathon (Playground)
    [18] Pogo trial (1 - 2)
    [19] Tiny Toy trial (1)
    [20] Tiny Toy trial (2)
    [21] Jetpack trial
    [22] Chase the Grade
    
School:
    [23] ABCs and 123s
    [24] Middle School Mischief
    [25] Repeat the Grade
    [26] Senior Trip
    [27] Freshman Frenzy
    [28] Chase Your Sister
    [29] Chase the Grade
    [30] Pogo trial 1
    [31] Pogo trial 2
    [32] Pogo trial 3
    [33] Jetpack trial
    [34] Tiny Toy trial
    [35] All Course Marathon (School)
    
Wholesale:
    [36] To the Top
    [37] Duct and Cover
    [38] Meat Market
    [39] Returns
    [40] Meat Grinder
    [41] Chase Through the Store
    [42] Pogo trial 1
    [43] Pogo trial 2
    [44] Pogo trial 3
    [45] Chase the Grade
    [46] Jetpack trial
    [47] Tiny Toy trial
    [48] All Course Marathon (Wholesale)
    
Masterclass:
    [49] Air Control Mastery
    [50] Wall Jump Mastery
    [51] Surf Mastery
    [52] Boosting Mastery
    [53] Wind Tunnel Mastery
    [54] Honor Gym Class
    [55] Pogo trial
    [56] Tiny Toy trial
    [57] Jetpack trial
    [58] All Course Marathon (Masterclass)
    
Basement:
    [59] Race to the Summit
    [60] Lights Out
    [61] Temple Sprint
    [62] Fancy Footwork
    [63] Minecart Carnage
    [64] Chase The Meaning
    [65] Jetpack trial
    [66] Tiny Toy trial
    [67] Pogo trial
    [68] All Course Marathon (Basement)
    
Rocco's Arcade:
    [69] Arcade Action
    [70] Rocco's Rumpus Room
    [71] Employees Only
    [72] Storage Room Spree
    [73] Birthday Blowout
    [74] Chase to the Arcade
    [75] Pogo trial 1
    [76] Pogo trial 2
    [77] Jetpack trial
    [78] Tiny Toy trial
    [79] All Course Marathon (Arcade)
    
BlueBox:
    [80] Windmill Valley
    [81] Big Rock Canyon
    [82] Rooftop Rush
    [83] Giant's Garage
    [84] Snowy-Mountain Sliding
    [85] All Star Marathon (BlueBox)
    
Parkour Island:
    [86] The Gauntlet
    
Sunshine Shore:
    [87] Sand Structure Scaling
    [88] Gem Grabbing
    [89] Castle Caper
    [90] Tanning Trek
    [91] Beacon Boarding
    [92] Water Wading
    [93] Pogo trial 1
    [94] Pogo trial 2
    [95] Pogo trial 3
    [96] Tiny Toy trial 1
    [97] Tiny Toy trial 2
    [98] Tiny Toy trial 3

G.A.T HQ:
    [99] The Mount Vile Gauntlet trial
    [100] Poizone's Perlisous Pit
    [101] T.O.X.I.C. Trampolines of Terror
    
Journey:
    [102] City
    [102] Farm
    [103] Forest
    [104] Harbor
    [105] Island
    [106] Volcano
        
    """)
    
    userinput = input()

    # Gym Jam
    if userinput == "1":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Jump")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Trampoline Trouble    
    if userinput == "2":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Course 3")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Livin' on the Ledge
    if userinput == "3":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Course 5")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Surfing Surfaces
    if userinput == "4":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Course 4")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Pole Vault
    if userinput == "5":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Course 2")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Chase Your Sister
    if userinput == "6":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # All Course Marathon
    if userinput == "7":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.All Course")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial
    if userinput == "8":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Pogo Trial")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Tiny toy trial
    if userinput == "9":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Tiny Toy Trial")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Jetpack trial
    if userinput == "10":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("tutorial.Jetpack")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Recess
    if userinput == "11":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Recess")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Big kids side
    if userinput == "12":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Intermediate")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # bouncy castle
    if userinput == "13":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Bouncy Castle")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Back to Class
    if userinput == "14":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Back To Class")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Sports Day
    if userinput == "15":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Sports Day")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Chase the Big Kid
    if userinput == "16":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Grounders")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # All Course Marathon (Playground)
    if userinput == "17":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.All Course")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Pogo trial (1 - 2)
    if userinput == "18":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Pogo 2-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Tiny Toy trial (1)
    if userinput == "19":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Tiny Toy 1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial (2)
    if userinput == "20":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Tiny Toy 2")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Jetpack trial
    if userinput == "21":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Jetpack 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Chase the Grade
    if userinput == "22":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("playground.Chase Grade")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # ABCs and 123s
    if userinput == "23":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Participation")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Middle School Mischief
    if userinput == "24":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Alternate Path")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Repeat the Grade
    if userinput == "25":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Reverse")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Senior Trip
    if userinput == "26":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Scavenger")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Freshman Frenzy
    if userinput == "27":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Head Rush")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Chase Your Sister
    if userinput == "28":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Chase Sue")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Chase the Grade 
    if userinput == "29":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Pursuit")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 1
    if userinput == "30":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Pogo 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 2
    if userinput == "31":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Pogo 2-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Pogo trial 3
    if userinput == "32":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Pogo 3-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Jetpack trial
    if userinput == "33":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Jetpack 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial
    if userinput == "34":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.Tiny Toy")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # All Course Marathon (School)
    if userinput == "35":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("school.All Courses")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # To the Top
    if userinput == "36":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.To The Top")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Duct and Cover
    if userinput == "37":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Fort")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Meat Market
    if userinput == "38":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Break")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Returns
    if userinput == "39":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Returns")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue        

    # Meat Grinder
    if userinput == "40":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Meat Grinder")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Chase Through the Store
    if userinput == "41":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Chase the Dollar")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 1
    if userinput == "42":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Pogo Trial 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 2
    if userinput == "43":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Pogo Trial 2-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 3
    if userinput == "44":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Pogo Trial 3-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Chase the Grade
    if userinput == "45":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Chase Grade")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Jetpack trial
    if userinput == "46":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Jetpack Trial 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial
    if userinput == "47":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.Tiny Toy")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # All Course Marathon (Wholesale)
    if userinput == "48":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("wholesale_expanded.All Courses")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Air Control Mastery
    if userinput == "49":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Air Control Training")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Wall Jump Mastery
    if userinput == "50":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Wall Run Training")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Surf Mastery
    if userinput == "51":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Surf Training")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Boosting Mastery
    if userinput == "52":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Bhop Open")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Wind Tunnel Mastery
    if userinput == "53":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Fan Training")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Honor Gym Class
    if userinput == "54":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Masters")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial
    if userinput == "55":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Pogo 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial
    if userinput == "56":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Tiny Toy")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue  
        
    # Jetpack trial
    if userinput == "57":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.Jetpack 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # All Course Marathon
    if userinput == "58":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("mastery_gym.All Course")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Race to the Summit
    if userinput == "59":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Course One")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Lights Out
    if userinput == "60":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Course Two")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Temple Sprint
    if userinput == "61":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Course Three")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Fancy Footwork
    if userinput == "62":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Course Four")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Minecart Carnage
    if userinput == "63":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Course Five")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Chase The Meaning
    if userinput == "64":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Course Six")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Jetpack trial
    if userinput == "65":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Jetpack 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial
    if userinput == "66":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Tiny Toy")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial
    if userinput == "67":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.Pogo")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # All Course Marathon
    if userinput == "68":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("basement.All Course")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Arcade Action
    if userinput == "69":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.Arcade")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Rocco's Rumpus Room
    if userinput == "70":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.Restaurant")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Employees Only
    if userinput == "71":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.Staff Only")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Storage Room Spree
    if userinput == "72":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.course 4")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Birthday Blowout
    if userinput == "73":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.Course 5")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Chase to the Arcade
    if userinput == "74":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.Course 6")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Pogo trial 1
    if userinput == "75":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.pogo")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Pogo trial 2
    if userinput == "76":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.pogo 2")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Jetpack trial
    if userinput == "77":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.Jetpack")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Tiny Toy trial
    if userinput == "78":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.TinyToy")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # All Course Marathon (Arcade)
    if userinput == "79":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("fun_centre.All Course")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
    
    # Windmill Valley
    if userinput == "80":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("The Blue Box.Windmill Valley")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Big Rock Canyon   
    if userinput == "81":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("The Blue Box.Big Rock Canyon")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Rooftop Rush   
    if userinput == "82":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("The Blue Box.Rooftop Rush")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Giant's Garage   
    if userinput == "83":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("The Blue Box.Giant's Garage")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Snowy-Mountain Sliding   
    if userinput == "84":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("The Blue Box.Snowy-Mountain Sliding")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # All Star Marathon (BlueBox)   
    if userinput == "85":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("The Blue Box.All Star Marathon")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # The Gauntlet
    if userinput == "86":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Parkour_Island.Gauntlet")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Sand Structure Scaling
    if userinput == "87":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Sand Structure Scaling")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Gem Grabbing
    if userinput == "88":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Gem Grabbing")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Castle Caper
    if userinput == "89":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Castle Caper")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tanning Trek
    if userinput == "90":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Tanning Trek")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Beacon Boarding
    if userinput == "91":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Beacon Boarding")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Water Wading
    if userinput == "92":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Water Wading")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 1
    if userinput == "93":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Pogo 1-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 2
    if userinput == "94":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Pogo 2-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Pogo trial 3
    if userinput == "95":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Pogo 3-1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial 1
    if userinput == "96":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Tiny Toy Trial 1")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial 2
    if userinput == "97":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Tiny Toy Trial 2")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Tiny Toy trial 3
    if userinput == "98":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Sunshine.Tiny Toy Trial 3")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # The Mount Vile Gauntlet trial
    if userinput == "99":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("gat_hq.gauntlet")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Poizone's Perlisous Pit
    if userinput == "100":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("gat_hq.don't look down")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # T.O.X.I.C. Trampolines of Terror
    if userinput == "101":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("gat_hq.toxic work enviroment")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # City
    if userinput == "102":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Jpurney.City")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Farm
    if userinput == "103":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Jpurney.Farm")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Forest
    if userinput == "104":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Jpurney.Forest")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Harbor
    if userinput == "105":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Jpurney.Harbor")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue

    # Island
    if userinput == "106":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Jpurney.Island")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue
        
    # Volcano
    if userinput == "107":
        os.system("cls")
        def extract_statistics(text):
            start_index = text.find("Jpurney.Volcano")  
            end_index = text.find("}}", start_index)  

            if start_index != -1 and end_index != -1:
                return text[start_index:end_index + 2]
            else:
                return None

        statistics_text = extract_statistics(file_contents)

        if statistics_text:
            statistics_text = statistics_text.replace(",", "\n")
            statistics_text = statistics_text.replace('''"m_LeaderboardVersion":''', "LeaderboardVersion: ")
            statistics_text = statistics_text.replace('''tutorial.Jump":{"m_Statistics":{"m_LevelVersion":0''', "")
            statistics_text = statistics_text.replace('''"m_BestTime":''', "\nBestTime: ")
            statistics_text = statistics_text.replace('''"m_DistanceTraveled":''', "\nDistanceTraveled: ")
            statistics_text = statistics_text.replace('''"m_PlayTime":''', "\nPlayTime: ")
            statistics_text = statistics_text.replace('''"m_MaxVelocity":''', "\nMaxVelocity: ")
            statistics_text = statistics_text.replace('''"m_DeathInformation":{''', "\nDeathInformation:\n")
            statistics_text = statistics_text.replace('''}''', "")
            statistics_text = statistics_text.replace('''"m_FewestDeaths":''', "\nFewestDeaths: ")
            statistics_text = statistics_text.replace('''"m_TotalSurfTime":''', "\nTotalSurfTime: ")
            statistics_text = statistics_text.replace('''"m_TotalSwingTime":''', "\nTotalSwingTime: ")
            statistics_text = statistics_text.replace('''"m_TotalAirTime":''', "\nTotalAirTime: ")
            statistics_text = statistics_text.replace('''"m_TotalGroundedTime":''', "\nTotalGroundedTime: ")
            statistics_text = statistics_text.replace('''"m_TotalTimeTouchingPursuit":''', "\nTotalTimeTouchingPursuit: ")
            statistics_text = statistics_text.replace('''"m_TotalJumps":''', "\nTotalJumps: ")
            statistics_text = statistics_text.replace('''"m_TotalLateJumps":''', "\nTotalLateJumps: ")
            statistics_text = statistics_text.replace('''}}''', "\n")
            print("Result:")
            print(statistics_text)
        else:
            print("No 'm_Statistics' and '}}' found in the input.")
        
        uinput = input("press enter to return")
        if uinput == "":
            continue
        else: 
            continue        
        
    # QUIT
    if userinput == "q":
        start = False
        continue
    if userinput == "c":
        fileselect()
    if userinput == "o":
        webbrowser.open("https://github.com/gameplanetworld/Hot-Lava-stats-Checker/tree/main")
    else:
        continue
