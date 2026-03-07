#!/bin/bash

# Cross-Platform Docker Verification Script
# This script verifies the EvePlanetHub application works correctly across Windows and Linux

echo "=== EvePlanetHub Cross-Platform Docker Verification ==="

# Check if docker-compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "ERROR: docker-compose is not installed or not in PATH"
    exit 1
fi

echo "1. Checking Docker setup:"
docker --version
docker-compose --version

echo ""
echo "2. Validating docker-compose configuration:"
docker-compose config

echo ""
echo "3. Starting all services:"
docker-compose up -d

echo ""
echo "4. Waiting for services to start (30 seconds):"
sleep 30

echo ""
echo "5. Checking service status:"
docker-compose ps

echo ""
echo "6. Testing backend health endpoint:"
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "SUCCESS: Backend health check passed"
else
    echo "ERROR: Backend health check failed"
fi

echo ""
echo "7. Testing frontend accessibility:"
if curl -f http://localhost:3000 > /dev/null 2>&1; then
    echo "SUCCESS: Frontend accessibility check passed"
else
    echo "ERROR: Frontend accessibility check failed"
fi

echo ""
echo "8. Checking all service logs for errors:"
for service in backend frontend db; do
    echo "=== Logs for $service ==="
    docker-compose logs --tail=20 "$service" 2>/dev/null || echo "No logs available for $service"
done

echo ""
echo "=== Verification Complete ==="

# Cleanup - comment out if you want to keep containers running
# docker-compose down