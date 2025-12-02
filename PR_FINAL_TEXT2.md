PR: Update docs to reflect DB persistence & add migration guidance.

This follow-up PR complements merged PR #17 (SQLite persistence).

- Update `src/README.md` to document how to run with DB-backed storage
- Add `ALEMBIC_README.md` with migration steps
- Add `CHANGES.md` and helper files for PR description
- Add `alembic` and `pytest` as dev dependencies in `requirements.txt`

Next steps:
- Optionally add generated Alembic environment and migrations once accepted
