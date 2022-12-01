Set WshShell = CreateObject("WScript.Shell")
TempPath = WshShell.ExpandEnvironmentStrings("%localappdata%\Temp")
WshShell.Run chr(34) & TempPath + "\between.bat" & Chr(34), 0
Set WshShell = Nothing
