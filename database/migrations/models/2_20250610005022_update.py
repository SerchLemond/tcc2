from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "faixa_etar" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
        ALTER TABLE "fatos" ADD "faixa_etar_id" BIGINT;
        ALTER TABLE "fatos" ADD CONSTRAINT "fk_fatos_faixa_et_4a010c07" FOREIGN KEY ("faixa_etar_id") REFERENCES "faixa_etar" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "fatos" DROP CONSTRAINT IF EXISTS "fk_fatos_faixa_et_4a010c07";
        ALTER TABLE "fatos" DROP COLUMN "faixa_etar_id";
        DROP TABLE IF EXISTS "faixa_etar";"""
