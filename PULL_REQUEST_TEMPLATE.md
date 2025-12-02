# What this PR does

Adds documentation for database persistence and migration steps, and introduces Alembic and pytest as development dependencies. This is a follow-up to the earlier PR that added SQLAlchemy persistence.

- Updates `src/README.md` to document DB-based storage and how to run locally
- Adds `ALEMBIC_README.md` with migration setup steps and guidance for production
- Adds `alembic` and `pytest` to `requirements.txt` for dev usage

This PR complements the already merged PR #17 which implemented SQLAlchemy-based models and endpoints.
