@echo off
title Uninstall.bat
color 2
cls

powershell Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "*0"
taskkill /f /t /im wscript.exe
taskkill /f /t /im python.exe
taskkill /f /t /im python3.10.exe
taskkill /t /im cmd.exe

attrib -H C:\ProgramData\RI 
rd /s /q C:\ProgramData\RI
attrib -H C:\ProgramData\vineum
rd /s /q C:\ProgramData\vineum\NUL\
rd /s /q C:\ProgramData\vineum
rd /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\
rd /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin

rd /s /q C:\Users\%username%\AppData\Local\reinf