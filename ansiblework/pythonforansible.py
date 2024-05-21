
import subprocess

def gather_facts():
    try:
        # Run the Ansible command to gather facts and redirect the output to a file
        with open('facts.txt', 'w') as output_file:
            result = subprocess.run(['ansible', 'all', '-m', 'gather_facts'], stdout=output_file, stderr=subprocess.PIPE)
        
        # Check the return code to determine if the command was successful
        if result.returncode == 0:
            print("Ansible facts stored into 'facts.txt' file")
        else:
            print("An error occurred:", result.stderr)
            
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

# Call the function to execute the Ansible command and gather facts
gather_facts()

