This PR documents our new SQLite-backed persistence and provides migration guidance.

Summary of changes:
- Updated `src/README.md` to reflect the new database-backed storage and running steps
- Added `ALEMBIC_README.md` with instructions for setting up Alembic migrations and further deployment notes
- Added `alembic` and `pytest` to `requirements.txt` as development dependencies

This complements PR #17 (merged) which added SQLAlchemy models and DB-backed endpoints.