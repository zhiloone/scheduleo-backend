run:
	docker compose up --build --watch

check:
	uv run ruff check

fix:
	uv run ruff check --fix

format:
	uv run ruff format