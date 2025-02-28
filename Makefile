run:
	uv run uvicorn src.main:app --reload

check:
	uv run ruff check

format:
	uv run ruff format