import subprocess
import logging
from src.machine import Machine

def provision_machine(vm_data):
    # Create a machine object
    vm = Machine(**vm_data)
    vm.log_creation()

    # Call the Bash script to install Nginx
    try:
        subprocess.run(["bash", "scripts/install_nginx.sh"], check=True)
        logging.info(f"Service installation for {vm.name} completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during service installation for {vm.name}: {e}")