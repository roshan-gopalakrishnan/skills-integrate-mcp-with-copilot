chore(docs): DB persistence docs and Alembic guidance

This PR updates the docs to reflect DB-backed storage and provides steps to set up Alembic migrations and local testing with pytest. It complements PR #17 which added SQLAlchemy persistence.

Files changed:
- src/README.md
- ALEMBIC_README.md
- CHANGES.md
- requirements.txt

Next steps: Add Alembic config and migrations, and a test suite.