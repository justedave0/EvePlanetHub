# EvePlanetHub Frontend

## Requirements

- Docker Desktop installed
- Node.js 18+ (for local development, not required for Docker)

## Setup

### Using Docker (Recommended)
```bash
# Build and start containers
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

## Environment Variables

Set these in your environment or `.env` file:
- `REACT_APP_API_URL` - Backend API URL (default: http://localhost:8000)

## Architecture

The frontend is containerized with nginx serving the built React application. The Dockerfile:

1. Installs Node.js dependencies
2. Builds the React app using `npm run build`
3. Serves static files with nginx

## API Integration

The frontend communicates with the backend at:
- http://localhost:8000/api/ (for API endpoints)