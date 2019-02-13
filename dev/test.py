#!/usr/local/bin/python3

import pprint

#sn = ['sn1', 'sn1', 'sn3']
#model = ['ws-3850', 'ws-3850-48', 'ws-3850']
#dict = {}


def def_test():

    sn = ['sn1', 'sn1', 'sn3']
    model = ['ws-3850', 'ws-3850-48', 'ws-3850']
    test_model = ['1A', '2AA', '3AAA']

    dict = {}
    elements = len(sn)
    count = (0)
    while count < elements:
    	#print ("line")
    	#dict[key] = value
    	#dict[sn[count]] = model[count]
        dict[sn[count]] = test_model[count]
        count +=1
    print ("SN: Model")
    #print (dict)
    pprint.pprint(dict, width=10)
# Call function
def_test()

'''
output
rdiaz@Ricardo-Mint ~/Documents/github/serial_number_and_version_finder/dev $ python3.5 test.py 
SN: Model
{'sn1': '2AA',
 'sn3': '3AAA'}

'''


AA
BB
CC
DD

test
