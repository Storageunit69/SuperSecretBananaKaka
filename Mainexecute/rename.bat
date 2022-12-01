@echo off
cls
Powershell.exe -executionpolicy remotesigned -File "%~dp0rename.ps1"
pause
exit