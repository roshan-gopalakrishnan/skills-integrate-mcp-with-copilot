chore(docs): DB persistence docs and Alembic guidance

This PR updates the docs to reflect the SQLite-backed persistence and adds migration guidance.

File highlights:
- `src/README.md` — how to run the app with SQLite and seed DB
- `ALEMBIC_README.md` — steps to initialize and create migrations with Alembic
- `CHANGES.md` — record of noteworthy changes
- `requirements.txt` — added `alembic` and `pytest` as dev dependencies

Next steps:
- Add Alembic config and migrations (not included in this PR)
- Add a basic test suite using pytest
