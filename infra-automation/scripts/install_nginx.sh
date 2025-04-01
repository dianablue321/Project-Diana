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