# EvePlanetHub

## Project Overview

EvePlanetHub is a full-stack web application for managing EVE Online planetary interactions.

## Architecture

- **Backend**: FastAPI (Python) running on port 8000
- **Frontend**: React application running on port 3000  
- **Database**: PostgreSQL (PostgreSQL 15) on port 5432
- **Containerization**: Docker Compose

## Setup Instructions

### Prerequisites
- Docker Desktop installed and running
- Git installed

### Getting Started

1. Clone the repository
2. Navigate to project directory: `cd EvePlanetHub`
3. Start all containers: `docker-compose up -d`

### Accessing Services

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Database: postgresql://localhost:5432/eveplanethub

## Troubleshooting

### Common Issues

1. **TypeScript errors with `process.env`**:
   - Solution: The tsconfig.json includes proper Node.js type definitions and api.ts was modified to handle environment variables safely
   - No `npm install` needed for Docker build

2. **Frontend fails on "Could not find index.html"**:
   - Solution: Fixed by creating a proper multistage Dockerfile that builds the React app before serving it with nginx

3. **Docker commands failing in PowerShell**:
   - Use Windows Command Prompt (cmd) instead of PowerShell for better compatibility
   - Run commands one-by-one instead of chaining with `&&`

### Building and Running

Use these commands in Windows Command Prompt (cmd):
```cmd
cd C:\dev\EvePlanetHub
docker-compose up -d
```

To view logs:
```cmd
docker-compose logs -f
```

To stop containers:
```cmd
docker-compose down
```