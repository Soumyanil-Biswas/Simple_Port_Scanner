#!/usr/bin/python3

import nmap
import time

RED = '\033[91m'
PURPLE = '\033[95m'
ENDC = '\033[0m'

s_port = int(input("Enter Starting port: "))
e_port = int(input("Enter Ending port: "))

trgt_ip = input("Enter target: ")

# input validation -> IP excludes only space from string
trgt_ip = trgt_ip.strip()

scanner = nmap.PortScanner()

#For loop for iteration

print("-"*25)

startTime = time.time()

for i in range(s_port, e_port+1):

    res = scanner.scan(trgt_ip, str(i))

    res = res['scan'][trgt_ip]['tcp'][i]['state']

    # to show the results, we are acessing only 2 values, port
    # and state of port

    if(res == 'closed'):
        print('| Port:',i,' | State:', RED+f'{res}'+ENDC)
        continue

    print('| Port:',i,' | State:', res)

totalTime = time.time() - startTime
totalTime='%.3f'%totalTime
print(PURPLE+f"\n[+] Scan Completed\n[+] Time Taken : {totalTime}s\n")
