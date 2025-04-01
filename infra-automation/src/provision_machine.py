import subprocess
import logging
import os
from src.machine import Machine

# Ensure logging is set up before using logging calls
logging.basicConfig(
    filename='logs/provisioning.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def provision_machine(vm_data):
    """
    Provision a machine and install necessary services (e.g., Nginx) via a bash script.

    Parameters:
        vm_data (dict): A dictionary containing the VM's attributes like name, OS, CPU, RAM.
    """

    # Ensure the necessary fields are present in the input data
    required_fields = ['name', 'operating_system', 'cpu', 'ram']
    for field in required_fields:
        if field not in vm_data:
            logging.error(f"Missing required field: {field}")
            return

    # Create a machine object from the input data
    vm = Machine(**vm_data)
    
    # Log the VM creation
    vm.log_creation()

    # Resolve the absolute path to the Bash script
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts/install_nginx.sh"))

    # Ensure the script exists and is executable
    if not os.path.isfile(script_path):
        logging.error(f"Bash script not found at {script_path}. Please check the path.")
        return
    if not os.access(script_path, os.X_OK):
        logging.error(f"Bash script at {script_path} is not executable. Please check permissions.")
        return

    # Run the Bash script to install Nginx
    try:
        subprocess.run(["bash", script_path], check=True)
        logging.info(f"Service installation for {vm.name} completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during service installation for {vm.name}: {e}")

