# EvePlanetHub Backend

FastAPI backend service for EvePlanetHub application.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development
```bash
uvicorn main:app --reload
```

### Docker
```bash
docker build -t eveplanethub-backend .
docker run -p 8000:8000 eveplanethub-backend
```

## Testing

Run tests:
```bash
pytest tests/
```

## API Documentation

The API documentation will be available at:
- `http://localhost:8000/docs`
- `http://localhost:8000/redoc`

## Environment Variables

Create a `.env` file in the root of the backend directory with:
```
DATABASE_URL=postgresql://user:password@db:5432/eveplanethub
ENV=development
```

## Project Structure

```
src/
├── api/              # API routes and endpoints
├── models/           # Data models (ORM)
├── services/         # Business logic
├── database/         # Database connection code
└── utils/            # Utility functions
```