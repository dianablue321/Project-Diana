#!/bin/bash
LOGFILE="installation.log"
{
    if ! command -v nginx &> /dev/null
    then
        echo "$(date) - Nginx is not installed. Installing..."
        sudo apt update
        sudo apt install -y nginx
        echo "$(date) - Nginx installed successfully."
    else
        echo "$(date) - Nginx is already installed."
    fi
} >> "$LOGFILE" 2>&1