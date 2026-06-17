import os
import asyncio
import json
from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.functions import Count  
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_DATABASE")
DB_PORT = os.getenv("DB_PORT")

DB_URL = f"postgres://{DB_USER}:{DB_PASS}@Postgres:{DB_PORT}/{DB_NAME}"
print(DB_URL)

class Fato(Model):
    id = fields.IntField(pk=True)

    aids_id = fields.IntField(null=True)
    alcoolismo_id = fields.IntField(null=True)
    antirretroviral_id = fields.IntField(null=True)
    bac_escarro1_id = fields.IntField(null=True)
    bac_escarro2_id = fields.IntField(null=True)
    benef_governo_id = fields.IntField(null=True)
    cultura_escarro_id = fields.IntField(null=True)
    diabetes_id = fields.IntField(null=True)
    doenca_mental_id = fields.IntField(null=True)
    droga_ilicita_id = fields.IntField(null=True)
    extra_pulm1_id = fields.IntField(null=True)
    extra_pulm2_id = fields.IntField(null=True)
    forma_id = fields.IntField(null=True)
    hiv_id = fields.IntField(null=True)
    imigrante_id = fields.IntField(null=True)
    municipio_resid_id = fields.IntField(null=True)
    outra_doenca_id = fields.IntField(null=True)
    pop_sit_rua_id = fields.IntField(null=True)
    ppl_id = fields.IntField(null=True)
    prof_saude_id = fields.IntField(null=True)
    raca_id = fields.IntField(null=True)
    sexo_id = fields.IntField(null=True)
    tabagismo_id = fields.IntField(null=True)
    teste_rapido_tb_id = fields.IntField(null=True)
    teste_sensibilidade_id = fields.IntField(null=True)
    tipo_entrada_id = fields.IntField(null=True)
    uf_id = fields.IntField(null=True)

    class Meta:
        table = "fatos"

async def main():
    await Tortoise.init(
        db_url=DB_URL,
        modules={"models": ["__main__"]},
    )
    await Tortoise.generate_schemas()

    fk_columns = [
        "aids_id", "alcoolismo_id", "antirretroviral_id", "bac_escarro1_id", "bac_escarro2_id",
        "benef_governo_id", "cultura_escarro_id", "diabetes_id", "doenca_mental_id", "droga_ilicita_id",
        "extra_pulm1_id", "extra_pulm2_id", "forma_id", "hiv_id", "imigrante_id", "municipio_resid_id",
        "outra_doenca_id", "pop_sit_rua_id", "ppl_id", "prof_saude_id", "raca_id", "sexo_id",
        "tabagismo_id", "teste_rapido_tb_id", "teste_sensibilidade_id", "tipo_entrada_id", "uf_id"
    ]

    result = {}

    for col in fk_columns:
        query = (
            await Fato.annotate(count=Count("id"))
                      .group_by(col)
                      .values(col, "count")
        )
        distrib = {str(row[col]): row["count"] for row in query if row[col] is not None}
        result[col] = distrib

    with open("distribuicoes_importadas_db.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print("Distribuições salvas em 'distribuicoes_fatos.json'.")

    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(main())
