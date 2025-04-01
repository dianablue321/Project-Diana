import logging
from datetime import datetime
import os

# Ensure the 'logs' directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging globally
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Machine:
    def __init__(self, name, operating_system, cpu, ram):
        self.name = name
        self.operating_system = operating_system  # Renamed from 'os' to 'operating_system'
        self.cpu = cpu
        self.ram = ram
        self.creation_time = datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "operating_system": self.operating_system,
            "cpu": self.cpu,
            "ram": self.ram,
            "created_at": self.creation_time.isoformat()
        }

    def log_creation(self):
        # Log the machine creation
        logging.info(f"Machine {self.name} created with {self.cpu} CPUs, {self.ram}MB RAM, OS: {self.operating_system} at {self.creation_time}")


# Example usage:
if __name__ == "__main__":
    machine = Machine(name="VM-001", operating_system="Ubuntu", cpu=2, ram=4096)
    machine.log_creation()
    print(machine.to_dict())