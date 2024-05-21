
import subprocess

def gather_facts():
    try:
       
        with open('facts.txt', 'w') as output_file:
            result = subprocess.run(['ansible', 'all', '-m', 'gather_facts'], stdout=output_file, stderr=subprocess.PIPE)
        
        
        if result.returncode == 0:
            print("Ansible facts stored into 'facts.txt' file")
        else:
            print("An error occurred:", result.stderr)
            
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


gather_facts()

