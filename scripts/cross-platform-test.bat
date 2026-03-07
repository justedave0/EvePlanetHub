@echo off
REM Cross-Platform Docker Verification Script for Windows
REM This script verifies the EvePlanetHub application works correctly across Windows and Linux

echo ============ EvePlanetHub Cross-Platform Docker Verification ============

echo.
echo 1. Checking Docker setup:
docker --version
docker-compose --version

echo.
echo 2. Validating docker-compose configuration:
docker-compose config

echo.
echo 3. Starting all services:
docker-compose up -d

echo.
echo 4. Waiting for services to start (30 seconds):
timeout /t 30 /nobreak >nul

echo.
echo 5. Checking service status:
docker-compose ps

echo.
echo 6. Testing backend health endpoint:
curl -f http://localhost:8000/health > nul
if %errorlevel% equ 0 (
    echo SUCCESS: Backend health check passed
) else (
    echo ERROR: Backend health check failed
)

echo.
echo 7. Testing frontend accessibility:
curl -f http://localhost:3000 > nul
if %errorlevel% equ 0 (
    echo SUCCESS: Frontend accessibility check passed
) else (
    echo ERROR: Frontend accessibility check failed
)

echo.
echo 8. Checking all service logs for errors:
for %%s in (backend frontend db) do (
    echo ===== Logs for %%s =====
    docker-compose logs --tail=20 %%s 2>nul || echo No logs available for %%s
)

echo.
echo ============ Verification Complete ============

REM Cleanup - uncomment if you want to keep containers running
REM docker-compose down