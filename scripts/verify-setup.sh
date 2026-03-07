#!/bin/bash

# Simple verification script to check if all components are working properly
echo "=== EvePlanetHub Setup Verification ==="

# Check docker-compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "ERROR: Docker Compose not found"
    exit 1
fi

echo "Docker Compose version:"
docker-compose --version

# Validate the compose file 
echo "Validating docker-compose.yml..."
if docker-compose config > /dev/null 2>&1; then
    echo "✓ docker-compose.yml is valid"
else
    echo "✗ docker-compose.yml has errors"
    exit 1
fi

# Check if required directories exist
if [ -d "backend" ] && [ -d "frontend" ]; then
    echo "✓ Backend and frontend directories found"
else
    echo "✗ Backend or frontend directory missing"
    exit 1
fi

echo "=== Setup Verification Complete ==="