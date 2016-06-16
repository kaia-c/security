#First try to find bleeding - run powershell to try to find strange processes with open or listening socket connections
#(save after typing): 
#ProcessToPorts.ps1
Function Map-ProcessToPorts {
    $PS = Get-Process | Select-Object Id, name, Product, ProductVersion, Company
    foreach ($process in $PS){
        $ns=netstat -ano
        $id=$process.id
        if($process.id -gt 5){
            $rgx= "\s+(TCP|UDP|IPv6|TCPv6|UDPv6)\s+.+[0-9]\s+(ESTABLISHED|LISTENING)+\s+$id"
            if ($ns | Select-String -Pattern $rgx){
                echo "-----------------------------------------------------`n"
                $ns | Select-String $process.id
                $process
                gwmi win32_process -filter "processid = '$id'" | select  Path, __PATH, InstallDate, ProcessId, ParentProcessId, ThreadCount
            }
        }
    }
}
#if you find bad ones:
#Taskkill /PID <pid> /F
#or
#Taskkill /IM <process name> /F