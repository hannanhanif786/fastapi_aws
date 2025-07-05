# 🐳 Docker Commands Quick Reference

## Quick Start
```bash
# Complete development setup and run
make dev

# Quick development start (if already set up)
make dev-quick

# View help
make help
```

## Environment Setup
```bash
# Setup different environments
make setup-dev
make setup-staging
make setup-prod
```

## Docker Development
```bash
# Build Docker image
make docker-build

# Run development environment
make docker-dev

# Run staging environment
make docker-staging

# Run production environment
make docker-prod

# Stop all containers
make docker-stop

# Restart containers
make docker-restart
```

## Monitoring & Logs
```bash
# View development logs
make docker-logs

# View staging logs
make docker-logs-staging

# Access container shell
make docker-shell

# Access database
make docker-db
```

## Database Operations
```bash
# Run migrations locally
make migrate

# Run migrations in development container
make migrate-dev

# Run migrations in staging container
make migrate-staging

# Create database backup
make docker-backup
```

## Cleanup
```bash
# Clean containers and volumes
make docker-clean

# Remove unused Docker resources
make docker-prune

# Clean generated files
make clean
```

## Local Development (without Docker)
```bash
# Install dependencies
make install

# Run locally
make run-dev
make run-staging
make run-prod

# Run tests
make test
```

## Common Workflows

### Development Workflow
```bash
# 1. Setup and start development
make dev

# 2. View logs
make docker-logs

# 3. Run migrations
make migrate-dev

# 4. Stop when done
make docker-stop
```

### Staging Testing
```bash
# 1. Setup staging
make setup-staging

# 2. Run staging environment
make docker-staging

# 3. Run migrations
make migrate-staging

# 4. Test the application
# Open http://localhost:8000

# 5. Stop
make docker-stop
```

### Production Deployment
```bash
# 1. Build production image
make docker-build

# 2. Run production environment
make docker-prod

# 3. Run migrations
make migrate

# 4. Monitor logs
make docker-logs
```

## Troubleshooting

### Container Issues
```bash
# Restart containers
make docker-restart

# Access shell to debug
make docker-shell

# View detailed logs
make docker-logs
```

### Database Issues
```bash
# Access database directly
make docker-db

# Create backup before changes
make docker-backup

# Run migrations
make migrate-dev
```

### Clean Slate
```bash
# Stop and clean everything
make docker-clean
make docker-prune

# Start fresh
make dev
```

## Environment Variables

The Docker containers automatically use the appropriate environment configuration:
- `config.env.development` for development
- `config.env.staging` for staging
- `config.env.production` for production

You can also set the `ENVIRONMENT` variable:
```bash
ENVIRONMENT=staging make docker-dev
``` 