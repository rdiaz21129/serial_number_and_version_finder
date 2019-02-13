#!/usr/local/bin/python3

# By: Andrew Moriarty, modified by Ricardo Diaz
# Date: 20190212
# Python3
# Name: serial_number_and_version_finder_ver_1_02.py
# Purpose: Program goes through files (show inventory output) and obtains serial number

# Resources
# https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith


# ~~~~~~~~~~
# Import modules
# ~~~~~~~~~~
import csv
import re
import os
import sys
import pprint

#   Print a list of stacked switches, their model number, serial number, and mac-address

# ~~~~~~~~~~
# Define variables
# ~~~~~~~~~~
testline = ('-' * 15 + 'TESTING LINE' + '-' * 15)
devices =[]
device_type = []
file_list = []

#os.chdir('H:\duracel\switches') #on windows os
path = sys.argv[1]
#path = input('Enter path of site directory: ')

# Change directory to folder that has the switch files (show inventory outputs)
try:
    os.chdir(path)
except:
    print ('No such file or directory. Please check your path is entered correctly')
    sys.exit(1)


# search through a given path (".") for all files that endswith ".txt".

files = (os.listdir())


####################

for file in files:
	if file.endswith('.txt'):
		file_list.append(file)

'''
print (testline)
print (list_files)
sys.exit(1)
'''
####################

# 1. Creates file. Will be writing to this file
with open('output_stacks.txt', 'w') as f_output_config:
	f_output_config.close()

f_output=''


for file in file_list:
	#mac_address = []
	switch_model = []
	switch_sn = []
	switch_version = [] 
	with open(file, 'r') as f_device:
		for line in f_device.readlines():
			'''
			if 'Master' in line or 'Member' in line or 'Active' in line or 'Standby' in line:
				# Match -  2       Member ecc8.8224.b980     10     0       Ready
				# Don't match -  5       Member 0000.0000.0000     0      0       Provisioned
				if 'Provisioned' not in line:
					s_mac=re.search('[a-fA-F0-9]{4}.[a-fA-F0-9]{4}.[a-fA-F0-9]{4}',line)
				if s_mac:
					mac_address.append(s_mac.group(0))
					s_mac=''
			'''
			if 'PID' in line:
				# Match - PID: WS-C3750V2-48PS-S , VID: V05, SN: FDO1441X2GC
				# Match - PID: WS-C3850-24P      , VID: V07  , SN: FCW2010D19W
				s_model=re.search('WS[-][\w\-]+',line)
				if s_model:
					s_sn=re.search('[\w|\d]{11}',line) 
					#s_sn=re.search('[\w]{3}[\d]{4}[\w]{4}',line)
					switch_model.append(s_model.group(0))
					switch_sn.append(s_sn.group(0))
                    
            # At this point we should have 2 lists, switch_model and switch_sn.  #NEW_CODE_
            # We need to now enter the contents of the lists and build a dictionary. #NEW_CODE_
            sn_model_dict = {} #NEW_CODE_
            switch_sn_entries = len(switch_sn) #NEW_CODE_
            entries_count = (0) #NEW_CODE_
            while entries_count < switch_sn_entries: #NEW_CODE_
                sn_model_dict[switch_sn[entries_count]] = switch_model[entries_count] #NEW_CODE_
                entries_count +=1 #NEW_CODE_
            print (pprint.pprint(sn_model_dict, width=10)  #NEW_CODE_
            

			 # Add if statement here matching "Cisco IOS Software".. add regex match followed by another if statment (matching regex)
			 
			s_version=re.search('Cisco IOS Software.*',line)
			if s_version:
				switch_version.append(s_version.group(0))
                #TEST
		try:
			if switch_model:
				h_name = file.replace('heist_serial_numbers_','')
				h_name = h_name.replace('.txt','')
				with open('output_stacks.txt', 'a') as f_output_config:
					f_output_config.write('\n')
					f_output_config.write(h_name)
					f_output_config.write('\n')
					loop = 0
					ver_loop = 0
					for line in switch_model:
						if switch_model[loop] and switch_sn[loop]:
							out_line = (switch_model[loop] + '\t' + switch_sn[loop])
							f_output_config.write(out_line)
							f_output_config.write('\n')
							#f_output_config.write(switch_version[ver_loop]) 
							#f_output_config.write('\n') 
						loop+=1
						#ver_loop+=1 
					
					for version_line in switch_version:
						if switch_version[ver_loop]:
							f_output_config.write(switch_version[ver_loop]) 
							f_output_config.write('\n') 
						ver_loop+=1 

				f_output_config.close()

		except:
			print ('=======Issues with ', + file, + ' Check output')

	f_device.close()
