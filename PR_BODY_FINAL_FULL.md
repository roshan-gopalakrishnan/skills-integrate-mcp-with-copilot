chore(docs): DB persistence docs and Alembic guidance

This follow-up PR complements PR #17 which introduced DB-backed storage using SQLAlchemy. It updates documentation and adds migration guidance for Alembic.

Files changed:
- `src/README.md` — add DB run instructions and seeding behavior
- `ALEMBIC_README.md` — migration setup steps
- `CHANGES.md` — record of follow-up changes
- `requirements.txt` — add `alembic` and `pytest` as dev dependencies

Next steps:
- Add generated Alembic environment for migrations
- Add test suite

