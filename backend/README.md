# EvePlanetHub Backend

This is the Python FastAPI backend for the EvePlanetHub platform with PostgreSQL integration.

## Project Structure

```
.
├── api/           # API endpoint definitions
├── src/           # Source code
│   ├── database/  # Database connection and migration logic  
│   ├── models/    # SQLAlchemy models
│   └── services/  # Business logic
├── tests/         # Test suite
└── alembic/       # Migration scripts
```

## Database Migrations

Database migrations are automatically applied when the backend starts up. The system uses Alembic to manage schema changes.

### Running Migrations

Migrations can be run manually using:

```bash
# Run all pending migrations
python -m alembic upgrade head

# Rollback last migration 
python -m alembic downgrade -1

# Create a new migration
python -m alembic revision --autogenerate -m "Description of changes"
```

### Migration Process

1. When the application starts, `startup` event triggers database checks
2. The system verifies database connection is available  
3. All pending migrations are applied automatically
4. Application continues to serve requests after successful migration

## Dependencies

- FastAPI
- SQLAlchemy (async)
- Alembic (for migrations) 
- PostgreSQL driver (psycopg2)

The setup handles database connection management and migration in a production-ready way.