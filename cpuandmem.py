
#This script checks for CPU and Memory usage if they are above a specific number (you can put any number)
#If not it will tell you that both the CPU and the Memory are okay

import psutil

import time


def procfun():
    
    cpu_usage = psutil.cpu_percent(interval=1)

    mem_usage = psutil.virtual_memory().percent
    

    if cpu_usage >= 90 or mem_usage >= 90:

        print(f"The CPU Usage is: {cpu_usage}")
    
        print(f"The Memory Usage is: {mem_usage}")
    
        processes = sorted(psutil.process_iter(), key=lambda proc: proc.cpu_percent(), reverse=True)[:10]
    
        print("The TOP 10 heaviest processes are:\n")
        
        time.sleep(4)
    
        for process in processes:
            print(process.id, process.name(), process.cpu_percent())

    else:
        print("Memory and CPU are under 90")
procfun()
