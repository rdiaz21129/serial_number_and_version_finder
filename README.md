Purpose: Goes through every file (txt) in a directory and parses out the switch(s)' model,serial number, and IOS version
Required: directory/path with files (per switch that include a [show inventory && show version | in Ver] output)

# Below is how to run python script<br/>

	~~~~~~~~~~ START ~~~~~~~~~~
	rdiaz@Ricardo-Mint ~ $ python3.5 serial_number_and_version_finder_ver_1_00.py 
	Enter path of site directory: /home/rdiaz/Documents/prod/serial_number_and_version_finder/site_a/
	~~~~~~~~~~ END ~~~~~~~~~~

# AFTER PYTHON SCRIPT IS RAN<br/>

	rdiaz@Ricardo-Mint ~ $ ll
	-rw-r--r-- 1 rdiaz rdiaz 1.7K Jan 31 10:43 site_a_inventory_version_asw-01_10.40.255.21.txt
	-rw-r--r-- 1 rdiaz rdiaz 2.3K Jan 31 10:48 site_a_inventory_version_csw-01_10.40.255.1.txt
	-rw-r--r-- 1 rdiaz rdiaz  489 Jan 31 11:08 output_stacks.txt
	
	rdiaz@Ricardo-Mint ~ $ cat output_stacks.txt 
	
	site_a_inventory_version_csw-01_10.40.255.1
	WS-C3850-48F-E	AAAAAAAAAA1
	WS-C3850-48F-E	AAAAAAAAAA1
	WS-C3850-48F-E	AAAAAAAAAA2
	Cisco IOS Software [Denali], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 16.3.6, RELEASE SOFTWARE (fc3)
	
	site_a_inventory_version_asw-01_10.40.255.21
	WS-C2960X-48FPS-L	BBBBBBBBBB1
	WS-C2960X-48FPS-L	BBBBBBBBBB2
	WS-C2960X-48FPS-L	BBBBBBBBBB3
	Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.0(2a)EX5, RELEASE SOFTWARE (fc3)

