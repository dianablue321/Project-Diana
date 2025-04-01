import json
from src.user_input import get_user_input

def save_vm_config():
    vm_data = get_user_input()
    if vm_data:
        with open('configs/instances.json', 'a') as f:
            json.dump(vm_data, f, indent=4)
            f.write("\n")
        print("VM configuration saved successfully!")