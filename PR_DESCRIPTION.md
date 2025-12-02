chore(docs): document DB persistence and Alembic setup

This PR updates the README to reflect database persistence (SQLite by default in dev), includes Alembic migration guidance, and adds `alembic` and `pytest` to `requirements.txt`.

Follow-up actions:
- Set up Alembic configurations (`alembic init`) and add the generated directory to the repo if desired
- Create migrations for existing models and apply them in production

Closes: N/A

