FROM node:20-alpine AS builder

WORKDIR /app

# Placeholder for package.json
COPY package*.json ./
RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi

COPY . /app
RUN if [ -f package.json ]; then npm run build; fi

FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app ./

CMD if [ -f package.json ]; then npm start; else echo "Frontend placeholder container running." && sleep infinity; fi
