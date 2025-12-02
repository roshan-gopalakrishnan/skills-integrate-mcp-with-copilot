chore(docs): DB persistence docs & Alembic guidance

This PR updates the docs to reflect the SQLite-backed persistence and adds a migration guide for Alembic. It complements PR #17 which added SQLAlchemy models and endpoints.

Files updated:
- `src/README.md` (DB persistence + run steps)
- `ALEMBIC_README.md` (migration setup guide)
- `CHANGES.md`
- `requirements.txt` (add dev deps: alembic, pytest)

Next steps suggested: add Alembic config and migrations, and add test suite if desired.
