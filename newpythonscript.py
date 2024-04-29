


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
            question_system = input("Would you like me to give you more information on the system? yes/no:\n ")
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

def dockercheck():
    askquestion = input("Would you like me to check if Docker is installed? yes/no:\n")
    if askquestion == 'yes':
        try:
            result = subprocess.Popen(['docker', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, _ = result.communicate()
            if result.returncode == 0:
                print("Docker is already installed on the system")
                return True
            else:
                print("Docker is not installed")
                return False
        except FileNotFoundError:
            print("Docker is not installed")
            return False

def instdocker():
    inst = input("Would you like me to install Docker for you? yes/no:\n")
    if inst == 'yes':
        print("Installing Docker for you. Give me a moment...")
        time.sleep(4)
        if os.path.isfile('/etc/redhat-release'):
            subprocess.run(["sudo", "yum", "install", "yum-utils", "-y"])
            subprocess.run(["sudo", "yum-config-manager", "--add-repo", "https://download.docker.com/linux/centos/docker-ce.repo"])
            subprocess.run(["sudo", "yum", "install", "docker-ce", "-y"])
        else:
            subprocess.run(["sudo", "dnf", "config-manager", "--add-repo", "https://download.docker.com/linux/centos/docker-ce.repo"])
            subprocess.run(["sudo", "dnf", "install", "docker-ce", "-y"])

        print("Docker is now installed on the machine.")
        print("Now starting Docker")
        subprocess.run(['systemctl', 'start', 'docker'])
    else:
        print("Okay, Docker will not be installed.")

if dockercheck():
    pass
else:
    instdocker()



docker_question = input("Would you like me to check for the current docker images? yes/no:\n")

if docker_question == 'yes':
    print("Checking for images...")
    time.sleep(3)
    print("Here are some of the docker images, I was able to find:\n")
    subprocess.call(['docker', 'images'])

else:
    print("Okay, we keep going.")



def dockercontainerz():

    docker_question = input("Would you like me to pull a specific image from dockerhub? yes/no:\n")
    if docker_question == 'yes':
        print("What is the image in question?\n")
        imagename = input()
        print("Okay, I'm gonna get this image for you. Give me a second...")
        time.sleep(4)
        subprocess.call(['docker', 'pull', imagename])
        print("The image you liked me to pull is now successfully downloaded")

    else:
        print("Okay, we keep on going.")

dockercontainerz()

