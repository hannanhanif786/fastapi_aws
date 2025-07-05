.PHONY: help dev staging prod setup-dev setup-staging setup-prod run run-dev run-staging run-prod docker-dev docker-staging docker-prod docker-build docker-stop docker-logs docker-clean docker-prune clean install test migrate

help: ## Show this help message
	@echo "FastAPI AWS Services - Environment Management"
	@echo "=============================================="
	@echo ""
	@echo "Environment Setup:"
	@echo "  setup-dev      - Setup development environment"
	@echo "  setup-staging  - Setup staging environment"
	@echo "  setup-prod     - Setup production environment"
	@echo ""
	@echo "Local Development:"
	@echo "  run            - Run the application locally"
	@echo "  run-dev        - Run in development mode"
	@echo "  run-staging    - Run in staging mode"
	@echo "  run-prod       - Run in production mode"
	@echo "  dev            - Complete development setup and run"
	@echo "  dev-quick      - Quick development start"
	@echo ""
	@echo "Docker Commands:"
	@echo "  docker-build   - Build Docker image"
	@echo "  docker-dev     - Run with Docker Compose (development)"
	@echo "  docker-staging - Run with Docker Compose (staging)"
	@echo "  docker-prod    - Run with Docker Compose (production)"
	@echo "  docker-stop    - Stop all Docker containers"
	@echo "  docker-logs    - View Docker logs"
	@echo "  docker-clean   - Clean Docker containers and volumes"
	@echo "  docker-prune   - Remove unused Docker resources"
	@echo "  docker-shell   - Access Docker container shell"
	@echo "  docker-db      - Access database in Docker"
	@echo "  docker-backup  - Create database backup"
	@echo "  docker-restart - Restart Docker containers"
	@echo ""
	@echo "Database:"
	@echo "  migrate        - Run database migrations"
	@echo "  migrate-dev    - Run migrations in development"
	@echo "  migrate-staging - Run migrations in staging"
	@echo ""
	@echo "Utilities:"
	@echo "  clean          - Clean up generated files"
	@echo "  install        - Install dependencies"
	@echo "  test           - Run tests"

setup-dev: ## Setup development environment
	@echo "Setting up development environment..."
	python scripts/setup_env.py development

setup-staging: ## Setup staging environment
	@echo "Setting up staging environment..."
	python scripts/setup_env.py staging

setup-prod: ## Setup production environment
	@echo "Setting up production environment..."
	python scripts/setup_env.py production

run: ## Run the application (uses current .env)
	@echo "Running application..."
	python run.py

run-dev: setup-dev run ## Setup dev environment and run

run-staging: setup-staging run ## Setup staging environment and run

run-prod: setup-prod run ## Setup production environment and run

docker-dev: ## Run with Docker Compose (development)
	@echo "Starting development environment with Docker..."
	docker compose -f docker-compose.dev.yml up --build

docker-staging: ## Run with Docker Compose (staging)
	@echo "Starting staging environment with Docker..."
	docker-compose -f docker-compose.staging.yml up --build

docker-prod: ## Run with Docker Compose (production)
	@echo "Starting production environment with Docker..."
	docker-compose -f docker-compose.yml up --build

docker-build: ## Build Docker image
	@echo "Building Docker image..."
	docker build -t fastapi-aws-services .

docker-stop: ## Stop all Docker containers
	@echo "Stopping all Docker containers..."
	docker-compose -f docker-compose.dev.yml down
	docker-compose -f docker-compose.staging.yml down
	docker-compose -f docker-compose.yml down

docker-logs: ## View Docker logs
	@echo "Viewing Docker logs..."
	docker-compose -f docker-compose.dev.yml logs -f

docker-logs-staging: ## View staging Docker logs
	@echo "Viewing staging Docker logs..."
	docker-compose -f docker-compose.staging.yml logs -f

docker-clean: ## Clean Docker containers and volumes
	@echo "Cleaning Docker containers and volumes..."
	docker-compose -f docker-compose.dev.yml down -v
	docker-compose -f docker-compose.staging.yml down -v
	docker-compose -f docker-compose.yml down -v

docker-prune: ## Remove unused Docker resources
	@echo "Removing unused Docker resources..."
	docker system prune -a -f

docker-shell: ## Access Docker container shell
	@echo "Accessing Docker container shell..."
	docker-compose -f docker-compose.dev.yml exec app /bin/bash

docker-db: ## Access database in Docker
	@echo "Accessing database in Docker..."
	docker-compose -f docker-compose.dev.yml exec db psql -U postgres -d postgres_dev

docker-backup: ## Create database backup
	@echo "Creating database backup..."
	docker-compose -f docker-compose.dev.yml exec db pg_dump -U postgres postgres_dev > backup_$(shell date +%Y%m%d_%H%M%S).sql

docker-restart: ## Restart Docker containers
	@echo "Restarting Docker containers..."
	docker-compose -f docker-compose.dev.yml restart

dev: ## Complete development setup and run
	@echo "Setting up complete development environment..."
	$(MAKE) setup-dev
	$(MAKE) docker-dev

dev-quick: ## Quick development start (assumes setup is done)
	@echo "Quick development start..."
	docker-compose -f docker-compose.dev.yml up -d
	@echo "Application is running at http://localhost:8000"
	@echo "Use 'make docker-logs' to view logs"
	@echo "Use 'make docker-stop' to stop"

migrate: ## Run database migrations
	@echo "Running database migrations..."
	alembic upgrade head

migrate-dev: ## Run migrations in development
	@echo "Running migrations in development..."
	docker-compose -f docker-compose.dev.yml exec app alembic upgrade head

migrate-staging: ## Run migrations in staging
	@echo "Running migrations in staging..."
	docker-compose -f docker-compose.staging.yml exec app alembic upgrade head

test: ## Run tests
	@echo "Running tests..."
	python -m pytest tests/ -v

install: ## Install dependencies
	@echo "Installing dependencies..."
	pip install -r requirements.txt

clean: ## Clean up generated files
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov 