chore(docs): DB persistence docs and Alembic guidance

This PR updates `src/README.md` to reflect DB-backed storage and provides steps for setting up Alembic migrations.

It also adds `alembic` and `pytest` to `requirements.txt` as dev dependencies (no Alembic env included in this PR).

Related to PR #17 (SQLAlchemy models & endpoints)
