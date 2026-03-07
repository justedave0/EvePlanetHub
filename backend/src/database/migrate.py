import asyncio
from sqlalchemy import text
from alembic.config import Config
from alembic import command
from src.database.session import engine
from config import settings


async def run_migrations():
    """Run database migrations on startup"""
    try:
        # Check if we're in a development environment and need to apply migrations
        print("Checking for database migrations...")
        
        # Create alembic configuration
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", settings.database_url)
        
        # Run migrations
        command.upgrade(alembic_cfg, "head")
        
        print("Database migrations applied successfully!")
        
    except Exception as e:
        print(f"Error applying database migrations: {e}")
        raise


async def check_database_connection():
    """Check if database is reachable"""
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise