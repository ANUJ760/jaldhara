.PHONY: dev build clean test lint migrate

dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

build:
	docker compose build

clean:
	docker compose down -v
	rm -rf data/*

test:
	docker compose exec backend pytest

lint:
	docker compose exec backend ruff check .
	docker compose exec frontend npm run lint

migrate:
	docker compose exec backend alembic upgrade head
