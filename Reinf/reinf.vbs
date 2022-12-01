Set WshShell = CreateObject("WScript.Shell")
scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
name = scriptdir + "\reinf.bat"
WshShell.Run chr(34) & name & Chr(34), 0
Set WshShell = Nothing