#LOL, NO I DONT WANNA WAIT FOR YOUR CONSENT TO RAGEQUIT!
import keyboard as key
import subprocess as sub
import os,sys

proc_list=["BsSndRpt.exe","LeagueClient.exe","LeagueClientUx.exe","LeagueClientUxRender.exe","jpatch.exe","LeagueofLegends.exe","LeagueCrashHandler.exe","RiotClientServices.exe","RiotClientUx.exe","RiotClientUxRender.exe","RiotClientCrashHandler.exe","VALORANT-Win64-Shipping.exe","VALORANT.exe","UnrealCEFSubProcess.exe"]
drive_letter_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","W"]
generic_riot_path="\\Riot Games\\Riot Client\\RiotClientServices.exe"
t='"'
def terminate():
    count=0
    try:
        for p in proc_list:
            try:
                sub.call([f'taskkill', '/F', '/IM', f'{proc_list[count]}'])
            except:
                pass
            count=count+1
    except:
        pass
def find_lol_path():
    count=0
    for d in drive_letter_list:
        lolpath=drive_letter_list[count]+":"+generic_riot_path
        if os.path.exists(lolpath):
            return lolpath
        else:
            count=count+1
def execute():
    lolpath=find_lol_path()
    try:
        os.system(f"start /b {t}LeagueOfLegends{t} {t}{lolpath}{t} --launch-product=league_of_legends --launch-patchline=live")
    except:
        pass
def chk():
    if key.is_pressed("f9"):
        terminate()
    elif key.is_pressed("f10"):
        execute()
if __name__ == "__main__":
    while True:
        chk()
