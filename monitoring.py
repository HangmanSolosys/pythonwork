

#This script checks the CPU usage, the Disk Usage, the Memory usage and the Network
#All info is being redirected to a file 

import time
import psutil


def monitoring_check():

    while True:
            
        cpu_usage =  psutil.cpu_percent(interval=1)
    
        mem_usage = psutil.virtual_memory().percent
    
        disk_usage = psutil.disk_usage('/').percent
    
        net_io = psutil.net_io_counters()

        
        with open('/var/log/system_monitoring.log', 'a') as log_file:
            
            log_file.write(f"The CPU Usage:{cpu_usage}%\n, The Memory Usage:{mem_usage}%\n, The Disk Usage:{disk_usage}%\n, Network I/O:{net_io}\n")
            
        time.sleep(60)
            
monitoring_check()
