#LOL, NO I DONT WANNA WAIT FOR YOUR CONSENT TO RAGEQUIT!, League of Legends / Valorant Fast Starter /QUITTER https://github.com/ny4rlk0/RiotGameManager/
import keyboard as key
import subprocess as sub
import os,time

proc_list=["BsSndRpt.exe","LeagueClient.exe","LeagueClientUx.exe","LeagueClientUxRender.exe","jpatch.exe","LeagueofLegends.exe","LeagueCrashHandler.exe","RiotClientServices.exe","RiotClientUx.exe","RiotClientUxRender.exe","RiotClientCrashHandler.exe","VALORANT-Win64-Shipping.exe","VALORANT.exe","UnrealCEFSubProcess.exe"]
drive_letter_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","W"]
generic_riot_path="\\Riot Games\\Riot Client\\RiotClientServices.exe"
t='"'
def kill_process(): #Kill the game process
    i=0
    for i in range(len(proc_list)):
        try: sub.Popen(['taskkill','/T','/F','/IM',f'{proc_list[i]}'], stdout=sub.DEVNULL, stderr = sub.DEVNULL , stdin = sub.DEVNULL)
        except: continue
        i=+1
def find_game_path(): #Find game path
    i=0
    for i in range(len(drive_letter_list)):
        try:
            gamepath=drive_letter_list[i]+":"+generic_riot_path
            if os.path.exists(gamepath): return gamepath
        except: continue
        i=+1
def start_process(game): #Start Game
    gamepath=find_game_path()
    try:
        if game=="lol": os.system(f"start /b {t}LeagueOfLegends{t} {t}{gamepath}{t} --launch-product=league_of_legends --launch-patchline=live")
        elif game=="valorant": os.system(f"start /b {t}Valorant{t} {t}{gamepath}{t} --launch-product=valorant --launch-patchline=live")
    except: pass
def is_any_button_pressed():
    time.sleep(0.1) #Lowers the cpu usage significantly!
    if key.is_pressed("f8"): kill_process()
    elif key.is_pressed("f9"): start_process("lol")
    elif key.is_pressed("f10"): start_process("valorant")
if __name__ == "__main__":
    while True: is_any_button_pressed()
