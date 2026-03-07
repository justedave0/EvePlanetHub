# EvePlanetHub

A platform for managing planetary resources and space exploration.

## Project Structure

- `backend/` - Python Flask API with PostgreSQL database
- `frontend/` - React.js single page application  
- `docs/` - Documentation files
- `scripts/` - Helper scripts

## Development Setup

### Prerequisites

- Docker and Docker Compose

### Getting Started

1. Clone the repository
2. Run `docker-compose up --build` to start all services

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Directory Structure

```
.
├── backend/           # Python Flask API
│   ├── api/           # API endpoints
│   ├── src/           # Source code
│   └── tests/         # Test suite
├── frontend/          # React frontend 
│   ├── public/        # Static files
│   └── src/           # React components
├── docs/              # Documentation
└── scripts/           # Helper scripts
```

## Notes

- The frontend uses a multi-stage Docker build to create a lightweight production environment
- The backend API is configured with PostgreSQL database