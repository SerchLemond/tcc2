from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "fatos" ADD "situacao_encerra_id" BIGINT;
        ALTER TABLE "fatos" ADD CONSTRAINT "fk_fatos_situacao_cf8a7195" FOREIGN KEY ("situacao_encerra_id") REFERENCES "situacao_encerra" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "fatos" DROP CONSTRAINT IF EXISTS "fk_fatos_situacao_cf8a7195";
        ALTER TABLE "fatos" DROP COLUMN "situacao_encerra_id";"""
