# Fix style
isort:
	isort .

black:
	black .

fix-style: isort black

# Check
isort-check:
	isort --check-only --diff .

flake8-check:
	flake8 .

check-style: isort-check flake8-check

# RUN
start-db:
	docker-compose up -d

remove-db:
	docker-compose down -v

migrate-postrgress:
	PYTHONPATH=. python3 src/destination/postgres/run_migrations.py

run-script:
	PYTHONPATH=. python src/main.py
