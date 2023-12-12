#!/bin/bash

# Create a virtual environment (if not already created)
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
# Activate the virtual environment
source venv/bin/activate
# Install or upgrade requirements
pip install --no-cache-dir -r requirements.txt

# Run your tests
cd app && python -m pytest tests/ --html=report.html 

# Run your application
python main.py