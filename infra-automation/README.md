# DevOps Infrastructure Provisioning & Configuration Automation

## Overview

This is a rolling project that aims to simulate infrastructure provisioning and service configuration through automation. The project will evolve over time, with future enhancements planned to integrate AWS and Terraform to provision real infrastructure resources. For now, the provisioning process is simulated, and the focus is on building a robust foundation for automation.

## Project Objective

The goal is to develop a Python-based automation tool that:
- Simulates infrastructure provisioning, specifically virtual machine (VM) creation.
- Accepts user inputs for defining VMs.
- Validates user inputs using Python, ensuring correct data format and types.
- Automates service installation (such as Nginx) using Bash scripts.
- Implements logging and error handling for both the Python code and Bash scripts.

## Features

- **User Input Validation**: The tool accepts inputs for creating virtual machines and validates them using Python libraries like Pydantic.
- **VM Configuration**: Collects data for defining VMs, including parameters like name, OS, CPU, and RAM.
- **Service Automation**: Bash scripts are used to install services (e.g., Nginx) on the provisioned VMs.
- **Logging and Error Handling**: All actions and errors are logged into a log file for troubleshooting.

## Setup & Repository Initialization

1. **Create a GitHub repository** for the project.
2. **Set up a virtual environment**:
   - Make sure Python 3.x is installed.
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```
3. **Repository structure**:
   ```
   infra-automation/
   |-- scripts/
   |-- configs/
   |-- logs/
   |-- src/
   |-- README.md
   ```

4. Push the initial setup to GitHub.

## Dependencies

To run the project, you will need to install the following Python libraries:

- `pydantic`: Used for validating VM configurations.
- `logging`: Standard Python module for logging.
- `json`: Standard Python module for working with JSON data.

If you don't have them already, you can install the dependencies via:

```bash
pip install pydantic
```

## Simulating Infrastructure Provisioning

The main goal of this project is to simulate infrastructure provisioning, so the tool will ask the user for input regarding the creation of virtual machines.

### VM Configuration

The Python code will prompt users for inputs like VM name, OS, CPU count, and RAM size. These values will be validated using Pydantic and stored in a configuration file (`instances.json`).

Example:

```json
{
    "name": "vm1",
    "os": "Ubuntu",
    "cpu": 2,
    "ram": 4096
}
```

### Validating Input

To ensure the input is correct:
- CPU must be at least 1.
- RAM must be a positive number greater than 0.

### Bash Scripts for Service Installation

Once the VM configuration is complete, a Bash script will be triggered to install a service (e.g., Nginx) on the VM.

Example Bash Script (`install_nginx.sh`):

### Bash Scripts for Service Installation

Once the VM configuration is complete, a Bash script will be triggered to install a service (e.g., Nginx) on the VM.

Example Bash Script (`install_nginx.sh`):

```bash
#!/bin/bash
LOGFILE="/var/log/installation.log" # Use an absolute path for the log file

# Ensure the script has proper permissions to write to the log file
if [ ! -d "$(dirname "$LOGFILE")" ] || [ ! -w "$(dirname "$LOGFILE")" ]; then
    echo "Error: Cannot write to log directory. Please run the script with appropriate permissions."
    exit 1
fi

# Ensure the log file exists and is writable
if [ ! -f "$LOGFILE" ]; then
    if ! sudo touch "$LOGFILE"; then
        echo "Error: Failed to create the log file. Please check permissions."
        exit 1
    fi
    if ! sudo chmod 664 "$LOGFILE"; then
        echo "Error: Failed to set permissions for the log file. Please check permissions."
        exit 1
    fi
fi

{
    if ! command -v nginx &> /dev/null
    then
        echo "$(date) - Nginx is not installed. Installing..."
        if sudo apt update && sudo apt install -y nginx; then
            echo "$(date) - Nginx installed successfully."
        else
            echo "$(date) - Failed to install Nginx. Please check the logs for details."
            exit 1
        fi
    else
        echo "$(date) - Nginx is already installed."
    fi
} >> "$LOGFILE" 2>&1

## Logging & Error Handling

All actions and errors will be logged to a `logs/provisioning.log` file, providing a detailed history of each action.

### Example log entries:
- When provisioning starts and ends.
- When errors occur (e.g., missing packages, validation failures).
- Successful installation of services.

## Example Usage

To start provisioning a new VM and installing services, simply run the Python script:

```bash
python infra_simulator.py
```

### Example Output:

```
Enter VM name: vm1
Enter OS type: Ubuntu
Enter number of CPUs: 2
Enter amount of RAM (in MB): 4096

VM Configuration: {'name': 'vm1', 'os': 'Ubuntu', 'cpu': 2, 'ram': 4096, 'created_at': '2025-04-01T08:00:00'}
```

Once the configuration is valid, the system will attempt to install Nginx using the corresponding Bash script.

### Logs Example:
```
2025-04-01 08:00:00 - Nginx is not installed. Installing...
2025-04-01 08:00:01 - Nginx installed successfully.
```

## Future Enhancements

This project is designed to evolve, and future enhancements may include:
- **AWS Integration**: Replace the mock provisioning process with real AWS instances using AWS SDK (Boto3).
- **Terraform Integration**: Automate infrastructure management with Terraform.
- **Advanced Service Configuration**: Include more complex services and configurations in future versions.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **Pydantic**: For providing a powerful and easy way to validate and manage data models in Python.
- **Bash**: For automating the service installation.

---
