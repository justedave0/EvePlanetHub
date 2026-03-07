# Frontend Setup Instructions

## Problem
You're experiencing Docker build error:
```
ERROR: failed to build: failed to solve: Internal: stream terminated by RST_STREAM with error code: INTERNAL_ERROR
ERROR: Service 'frontend' failed to build : Build failed
```

This appears to be caused by an internal Docker issue, potentially related to WSL configuration or resource constraints.

## Solution

### Option 1: Simplified Local Development Approach (Recommended)
Instead of using Docker for the frontend, you can develop and test locally:

1. **Install dependencies:**
```bash
cd ./frontend
npm install
```

2. **Run development server:**
```bash
npm start
```

3. **Build for production:**
```bash
npm run build
```

### Option 2: Fixed Dockerfile (If you must use Docker)
Create a simpler, single-stage Dockerfile:

FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm ci --no-audit --no-optional

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

Or for production building:
FROM node:18 AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci --no-audit --no-optional

COPY . .

RUN npm run build

# Serve with nginx for production
FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

### Option 3: Docker Troubleshooting
1. Clean Docker system:
```bash
docker system prune -af
```

2. Restart Docker service:
```bash
sudo systemctl restart docker
```

3. Increase Docker resources in Docker Desktop settings if using Docker Desktop.