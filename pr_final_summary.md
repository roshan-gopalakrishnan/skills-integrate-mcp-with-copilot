This PR: chore(docs): DB persistence docs & Alembic guidance

This follow-up PR complements PR #17 (SQLite persistence + SQLAlchemy). The PR updates documentation to reflect the DB-backed storage and provides instructions for migration setup using Alembic. It also adds `alembic`/`pytest` to the repository `requirements.txt` for developer workflows.

Files changed:
- src/README.md  (doc updates for DB-backed storage)
- CHANGES.md
- ALEMBIC_README.md
- requirements.txt: add alembic & pytest as dev dependencies

Next steps (optional):
- Add a configured Alembic environment with migrations in a follow-up PR
- Add a basic test suite with pytest
