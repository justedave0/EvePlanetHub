#!/bin/bash

# Run database migrations for EvePlanetHub backend
cd /home/splashxxx/EvePlanetHub/backend

echo "Applying database migrations..."

# Apply migrations using python alembic command
python -m alembic upgrade head

echo "Database migrations completed!"