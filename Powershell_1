# Script PowerShell pour afficher les informations système

Write-Host "Informations Système :`n"

# Nom de l'ordinateur
$ComputerName = $env:COMPUTERNAME
Write-Host "Nom de l'ordinateur : $ComputerName"

# Nom de l'utilisateur
$UserName = $env:USERNAME
Write-Host "Nom de l'utilisateur : $UserName"

# Version de Windows
$OSVersion = (Get-CimInstance Win32_OperatingSystem).Caption
Write-Host "Version de Windows : $OSVersion"

# Processeur
$CPU = (Get-CimInstance Win32_Processor).Name
Write-Host "Processeur : $CPU"

# Mémoire RAM totale
$RAM = (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB
Write-Host ("Mémoire RAM Totale : {0:N2} GB" -f $RAM)

# Espace disque disponible
$Disk = Get-PSDrive -Name C | Select-Object Used, Free
Write-Host ("Espace disque utilisé : {0:N2} GB" -f ($Disk.Used / 1GB))
Write-Host ("Espace disque libre : {0:N2} GB" -f ($Disk.Free / 1GB))

Write-Host "`nFin du script."
