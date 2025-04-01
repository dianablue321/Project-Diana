from pydantic import BaseModel, Field, field_validator, validator, ValidationError
import json

class VMConfig(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int

    # Adding custom validation for CPU and RAM
    @field_validator('cpu')
    def check_cpu(cls, value):
        if value < 1:
            raise ValueError('CPU must be at least 1')
        return value

    @field_validator('ram')
    def check_ram(cls, value):
        if value <= 0:
            raise ValueError('RAM must be greater than 0')
        return value

    # Optionally, you could add a method to return a dictionary representation
    def to_dict(self):
        return self.model_dump()

def get_user_input():
    while True:
        try:
            name = input("Enter VM name: ")
            os = input("Enter OS type: ")

            # Handle user input for CPU and RAM with error checking
            cpu = int(input("Enter number of CPUs: "))
            ram = int(input("Enter amount of RAM (in MB): "))
            
            # Create a dictionary and validate the VM configuration
            vm_data = {"name": name, "os": os, "cpu": cpu, "ram": ram}
            vm = VMConfig(**vm_data)  # Pydantic automatically validates here

            # If validation passes, return the dictionary
            return vm.to_dict()
        
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        except ValidationError as e:
            print(f"Validation failed: {e}")
            return None

# Example Usage
if __name__ == "__main__":
    vm_config = get_user_input()
    if vm_config:
        print(f"VM Configuration: {vm_config}")