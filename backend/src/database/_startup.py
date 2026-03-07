#!/usr/bin/env python3

import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from src.database.session import engine
import os
import time
from config import settings

async def wait_for_db_connection(max_retries=10, delay=5):
    """
    Wait for database connection to be ready
    """
    for attempt in range(max_retries):
        try:
            print(f"Attempting to connect to database (attempt {attempt + 1})...")
            
            # Simple test query to check if DB is available
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            
            print("Database connection successful!")
            return True
            
        except Exception as e:
            print(f"Database connection failed (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {delay} seconds...")
                await asyncio.sleep(delay)
            else:
                print("Max retries reached. Failed to connect to database.")
                return False

async def main():
    """
    Startup script that waits for DB and then starts the application
    """
    try:
        if settings.database_url:
            print("Starting application with database checks...")
            
            # Wait for database connection
            db_ready = await wait_for_db_connection()
            if not db_ready:
                print("Failed to connect to database. Application will exit.")
                return
                
        else:
            print("No database URL configured. Starting without DB check.")
        
        print("Starting FastAPI application...")
        
        # Run the FastAPI app
        import uvicorn
        from main import app
        
        uvicorn.run(app, host="0.0.0.0", port=8000)
        
    except Exception as e:
        print(f"Application startup failed: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())