# EvePlanetHub

A platform for managing planetary resources and space exploration.

## Project Structure

- `backend/` - Python FastAPI with PostgreSQL database
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

## Database Migrations

Database migrations are automatically applied when the backend starts up. 
To manually run migrations, use:

```bash
# Run migrations
python -m alembic upgrade head

# Rollback migrations  
python -m alembic downgrade -1
```

The migration system uses Alembic to manage schema changes and is integrated into the application startup process.

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