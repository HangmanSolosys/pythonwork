

import subprocess
import time
import os
import platform

name = input("Hello, what is your name?\n")

print("Nice meeting you " + name )

print("Your current working directory is:\n", os.getcwd())

os_name = platform.system()

print("You are currently working on:\n", os_name)

print("Listing all available files in the current directory")
time.sleep(1)

if os_name == 'Windows':
    print("Listing the files in the current working directory:\n", os.system('dir'))

else:
    print("Listing the files in the current working directory:\n", os.system('ls -lah'))


def largestfiles():
    bigfiles = input("Would you like me to show you the largest files in the system? yes/no:\n ")
    if bigfiles == 'yes':
        print("The largest files in your current working machine are:\n ")
        time.sleep(2)
        if os_name == 'Linux':
            info_files = os.system('find / -type f -size +100M')
            print(info_files)
            question_system = input("Would you like me to give you more information on the system?: yes/no ")
            if question_system == 'yes':
                time.sleep(2)
                print("This is some basic information on what is going on: \n FILE SYSTEM INFO: \n", os.system('df -hi'))
                print("Who is on that system:\n ", os.system('w'))
                print("Basic info on the system itself:\n", os.system('uname -a && cat /etc/os-release && uptime'))


        else:
            info_files = os.system(r'powershell.exe -Command "Get-ChildItem -Path C:\ -Recurse -File | Where-Object {$_.Length -gt 100MB}"')

    else:
        print("No worries, we keep on going!")

largestfiles()

askforservice = input("Should we check any service? yes/no:\n")

if askforservice == 'yes':
    
    svc = input("Which service should we check?\n")

    service_check = subprocess.call(['systemctl', 'status', svc], stdout=subprocess.PIPE)

def actiontaken():
    if service_check == 0:
        print("The " + svc + " is currently running")
    else: 
        print("The " + svc + " is NOT running")
        action = input("Would you like me to start this process? yes/no: \n ")
        if action.lower() == 'yes':
            print("Starting " + svc + ", give me a second...")
            time.sleep(3)
            subprocess.call(['systemctl', 'enable', svc])
            subprocess.call(['systemctl', 'start', svc])
            service_check2 = subprocess.call(['systemctl', 'status', svc], stdout=subprocess.PIPE)
            print(subprocess.check_output(['systemctl', 'status', svc]).decode())  # Print the status of the process
            if service_check2 == 0:
                print("The " + svc + " is now running")

actiontaken()

