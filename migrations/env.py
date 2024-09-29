from logging.config import fileConfig
import os
import asyncio

from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine
from app.core.base import Base

from alembic import context

load_dotenv(".env")

# Получаем конфигурацию Alembic
config = context.config

# Устанавливаем URL подключения к базе данных
config.set_main_option("sqlalchemy.url", os.environ["DATABASE_URL"])

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Указываем целевую метадату для автогенерации
target_metadata = Base.metadata


def run_migrations_offline():
    """Запуск миграций в 'офлайн' режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Выполнение миграций с использованием соединения."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Запуск миграций в 'онлайн' режиме."""
    connectable = AsyncEngine(
        engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
