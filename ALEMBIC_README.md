# Alembic (migrations)

This project uses SQLAlchemy for ORM. To manage schema migrations in production and across environments, we recommend using Alembic.

1. Install dependencies:

```
pip install alembic
```

2. Initialize Alembic:

```
alembic init alembic
```

3. Edit `alembic/env.py` and configure the database URL and models import.

4. Create migration scripts:

```
alembic revision --autogenerate -m "create tables"
alembic upgrade head
```

Note: For this exercise we haven't committed a generated Alembic environment. This file provides the steps to set it up in your environment and as a follow-up step for production.