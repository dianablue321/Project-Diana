import logging
from datetime import datetime
import os

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        self.creation_time = datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram,
            "created_at": self.creation_time.isoformat()
        }

    def log_creation(self):
        # Ensure the 'logs' directory exists
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Configure logging with log rotation
        logging.basicConfig(
            filename='logs/provisioning.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Log the machine creation
        logging.info(f"Machine {self.name} created with {self.cpu} CPUs, {self.ram}MB RAM, OS: {self.os} at {self.creation_time}")


# Example usage:
if __name__ == "__main__":
    machine = Machine(name="VM-001", os="Ubuntu", cpu=2, ram=4096)
    machine.log_creation()
    print(machine.to_dict())