#!/bin/python3
from pyfiglet import Figlet
import time
import socket

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def connectScan(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	socket.setdefaulttimeout(1)
	conn=s.connect_ex((ip,port))
	if(conn == 0) :
		print(bcolors.GREEN+ f"Port {port} Open On {ip}"+bcolors.ENDC)
	s.close()

if __name__ == "__main__":
	f = Figlet(font='slant')
	print(f.renderText('Simple Port Scanner'))
	
	ip=input(bcolors.BOLD + bcolors.PURPLE + "[+] Enter IP : " + bcolors.ENDC)
	start=int(input(bcolors.BOLD + bcolors.CYAN + "[+] Enter Start Port : " + bcolors.ENDC))
	stop=int(input(bcolors.BOLD + bcolors.RED + "[+] Enter Start Port : " + bcolors.ENDC))

	startTime=time.time()
	print(bcolors.CYAN+f"\n[+] Starting Connect Scan on {ip} from Ports : {start} to {stop}\n")

	while (start<=stop):
		connectScan(ip,start)
		start=start+1
	
	totalTime = time.time() - startTime
	totalTime='%.3f'%totalTime
	print(bcolors.CYAN+f"\n[+] Scan Completed\n[+] Time Taken : {totalTime}s\n")
