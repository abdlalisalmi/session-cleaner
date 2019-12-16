#!bin/sh

import time
import os
import sys

def slowprint(string):
    for c in string + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10 / 100)


def logo():
	logo = """\033[1;32;40m
                 _|  _|_|_|    _|_|_|    _|_|_|_|_|  
               _|_|        _|        _|          _|  
                 _|    _|_|      _|_|          _|    
                 _|        _|        _|      _|      
                 _|  _|_|_|    _|_|_|      _|        

      for other scripts : https://github.com/salmiabdlali
"""
	print(logo)


def main():
	os.system("clear")
	logo()
	slowprint("[+] Cleaning your session... √")
	os.system("rm -rf ~/Library/*42*")
	print("[+] Your computer is clean   √")
	




if __name__ == '__main__':
	main()