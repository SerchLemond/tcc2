from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "logs" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "chat_id" BIGINT NOT NULL,
    "message" TEXT NOT NULL,
    "criado_em" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "logs";"""
