# Azure Hosting Deployment Guide

This guide walks you through deploying your application using Gunicorn on an Azure VM.

## Deployment Steps  

```bash
# Clone the repository
git clone https://github.com/Rtarun3606k/Azure-Hostinting/blob/main/guicorn.py
```

# Update the system
```bash
sudo apt update
```

# Navigate to the project directory
```bash
cd Azure-Hosting
```

```bash
# Install required packages
sudo apt install pip
sudo apt install virtualenv
```

# Create and activate virtual environment
```
virtualenv venv
source venv/bin/activate
```


# Install dependencies (if any)
```
pip install -r requirements.txt
```
# Start Gunicorn
```bash
gunicorn -c gunicorn.py app:app
```

# Stop Gunicorn (Ctrl + C)
# Configure inbound rule for port 8000 in the firewall

# Run Gunicorn in the background
```bash
nohup gunicorn -c gunicorn.py app:app > gunicorn.log 2>&1 &
```
# Verify Gunicorn is running
```bash
ps aux | grep gunicorn
```

# Kill Gunicorn if needed
```bash
pkill gunicorn
```
```bash
