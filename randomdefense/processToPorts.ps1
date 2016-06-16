#First try to find bleeding - run powershell to try to find strange processes with open or listening socket connections
#(save after typing) Gives details about processes that run on ports and their parent processes: 
#ProcessToPorts.ps1
Function Map-ProcessToPorts {
    $PS = Get-Process | Select-Object Id, name, Product, ProductVersion, Company
    foreach ($process in $PS){
        $ns=netstat -ano
        $id=$process.id
        if($process.id -gt 5){
            $rgx= "\s+(TCP|UDP|IPv6|TCPv6|UDPv6)\s+.+[0-9]\s+(ESTABLISHED|LISTENING)+\s+$id"
            if ($ns | Select-String -Pattern $rgx){
                echo "------------------------------------------------------------------------------------------------`n"
                $ns | Select-String $process.id
                $process
                $win32ps=gwmi win32_process -filter "processid = '$id'" | select  Path, __PATH, InstallDate, ProcessId, ParentProcessId, ThreadCount
				echo "Immediant Parent Process:`n"
				$ns | Select-String $win32ps.ParentProcessId
				$ps | Select-String $win32ps.ParentProcessId
            }
        }
    }
}
Map-ProcessToPorts > YOU\TYPE\PATH\HERE\processToPorts.txt

