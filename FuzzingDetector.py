import time
from pathlib import Path
from datetime import datetime

def LogCheck():
    fuzzMone = 0
    check = 0
    fuzzAttck = 1
    lastScanSize = 0
    while fuzzAttck:
        #As seen in the last lab , we can detect if someone tried to fuzz our program via our auth.log , we will receive
        #Alot of connection cloed or errors in that log(more then usual if let's say a user tries to log in and not spam the program)
        with open("/var/log/auth.log","r") as file:
            lines = file.readlines()
            if len(lines) != lastScanSize:
                for line in range(lastScanSize, len(lines)):
                    p =lines[line].split()
                    if ("error:" in p or ("Connection" in p and "closed" in p) or ("banner" in p and "exchange" in p) )and check:
                        fuzzMone += 1
        if fuzzMone >= 5 and check:
            #If we received more then 5 in bad logs , since we started scanning , not before , then a fuzz attack has occured.
            print("Fuzzing Attack via SSH detected!")
            #If detected , close the program.
            exit(0)
        else:
            check = 1
        time.sleep(5)
        lastScanSize = len(lines)

if __name__ == '__main__':
    LogCheck()
