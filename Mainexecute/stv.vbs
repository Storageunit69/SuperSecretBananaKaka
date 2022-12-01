Set WshShell = CreateObject("WScript.Shell")
scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
name = scriptdir + "\stv.bat"
name2 = scriptdir + "\rename.ps1"
name3 = scriptdir + "\backup.vbs"
WshShell.Run chr(34) & name & Chr(34), 0
WshShell.Run chr(34) & name2 & Chr(34), 0
WshShell.Run chr(34) & name3 & Chr(34), 0
Set WshShell = Nothing