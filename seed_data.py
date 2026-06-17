import asyncio
from tortoise import Tortoise, run_async
from database.models.dimensions import (
    TipoEntrada, PPL, PopSitRua, ProfSaude, Imigrante, BenefGoverno, Forma,
    ExtraPulm1, Aids, Alcoolismo, Diabetes, DoencaMental, DrogasIlicitas,
    Tabagismo, OutraDoenca, RaioX, HIV, Antirretroviral, CulturaEscarro,
    TesteMolec, TesteSensibilidade, SituacaoEncerra, Sexo, Raca, FaixaEtar, UF
)
import os
from config import Config

config = Config()

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": config.DB_HOST,
                "port": 5432,
                "user": config.DB_USER,
                "password": config.DB_PASS,
                "database": config.DB_DATABASE,
            },
        },
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "database.models.dimensions",
                "database.models.general"
            ],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}

async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)

async def seed_data():
    await init_db()

    # TipoEntrada
    await TipoEntrada.bulk_create([
        TipoEntrada(id=1, nome='Caso Novo'),
        TipoEntrada(id=2, nome='Recidiva'),
        TipoEntrada(id=3, nome='Reingresso após Abandono'),
        TipoEntrada(id=4, nome='Não Sabe'),
        TipoEntrada(id=5, nome='Transferência'),
        TipoEntrada(id=6, nome='Pós-óbito')
    ])

    # PPL
    await PPL.bulk_create([
        PPL(id=1, nome='Sim'),
        PPL(id=2, nome='Não'),
        PPL(id=9, nome='Ignorado')
    ])

    # PopSitRua
    await PopSitRua.bulk_create([
        PopSitRua(id=1, nome='Sim'),
        PopSitRua(id=2, nome='Não'),
        PopSitRua(id=9, nome='Ignorado')
    ])

    # ProfSaude
    await ProfSaude.bulk_create([
        ProfSaude(id=1, nome='Sim'),
        ProfSaude(id=2, nome='Não'),
        ProfSaude(id=9, nome='Ignorado')
    ])

    # Imigrante
    await Imigrante.bulk_create([
        Imigrante(id=1, nome='Sim'),
        Imigrante(id=2, nome='Não'),
        Imigrante(id=9, nome='Ignorado')
    ])

    # BenefGoverno
    await BenefGoverno.bulk_create([
        BenefGoverno(id=1, nome='Sim'),
        BenefGoverno(id=2, nome='Não'),
        BenefGoverno(id=9, nome='Ignorado')
    ])

    # Forma
    await Forma.bulk_create([
        Forma(id=1, nome='Pulmonar'),
        Forma(id=2, nome='Extrapulmonar'),
        Forma(id=3, nome='Pulmonar + Extrapulmonar'),
        Forma(id=9, nome='Ignorado')
    ])

    # ExtraPulm1
    await ExtraPulm1.bulk_create([
        ExtraPulm1(id=1, nome='Pleural'),
        ExtraPulm1(id=2, nome='Gang. Perif.'),
        ExtraPulm1(id=3, nome='Geniturinária'),
        ExtraPulm1(id=4, nome='Óssea'),
        ExtraPulm1(id=5, nome='Ocular'),
        ExtraPulm1(id=6, nome='Miliar'),
        ExtraPulm1(id=7, nome='Meningoencefálico'),
        ExtraPulm1(id=8, nome='Cutânea'),
        ExtraPulm1(id=9, nome='Laringea'),
        ExtraPulm1(id=10, nome='Outra')
    ])

    # Aids
    await Aids.bulk_create([
        Aids(id=1, nome='Sim'),
        Aids(id=2, nome='Não'),
        Aids(id=9, nome='Ignorado')
    ])

    # Alcoolismo
    await Alcoolismo.bulk_create([
        Alcoolismo(id=1, nome='Sim'),
        Alcoolismo(id=2, nome='Não'),
        Alcoolismo(id=9, nome='Ignorado')
    ])

    # Diabetes
    await Diabetes.bulk_create([
        Diabetes(id=1, nome='Sim'),
        Diabetes(id=2, nome='Não'),
        Diabetes(id=9, nome='Ignorado')
    ])

    # DoencaMental
    await DoencaMental.bulk_create([
        DoencaMental(id=1, nome='Sim'),
        DoencaMental(id=2, nome='Não'),
        DoencaMental(id=9, nome='Ignorado')
    ])

    # DrogasIlicitas
    await DrogasIlicitas.bulk_create([
        DrogasIlicitas(id=1, nome='Sim'),
        DrogasIlicitas(id=2, nome='Não'),
        DrogasIlicitas(id=9, nome='Ignorado')
    ])

    # Tabagismo
    await Tabagismo.bulk_create([
        Tabagismo(id=1, nome='Sim'),
        Tabagismo(id=2, nome='Não'),
        Tabagismo(id=9, nome='Ignorado')
    ])

    # OutraDoenca
    await OutraDoenca.bulk_create([
        OutraDoenca(id=1, nome='Sim'),
        OutraDoenca(id=2, nome='Não'),
        OutraDoenca(id=9, nome='Ignorado')
    ])

    # RaioX
    await RaioX.bulk_create([
        RaioX(id=1, nome='Suspeito'),
        RaioX(id=2, nome='Normal'),
        RaioX(id=3, nome='Outra patologia'),
        RaioX(id=4, nome='Não realizado'),
        RaioX(id=9, nome='Ignorado')
    ])

    # HIV
    await HIV.bulk_create([
        HIV(id=1, nome='Positivo'),
        HIV(id=2, nome='Negativo'),
        HIV(id=3, nome='Em andamento'),
        HIV(id=4, nome='Não realizado'),
        HIV(id=9, nome='Ignorado')
    ])

    # Antirretroviral
    await Antirretroviral.bulk_create([
        Antirretroviral(id=1, nome='Sim'),
        Antirretroviral(id=2, nome='Não'),
        Antirretroviral(id=9, nome='Ignorado')
    ])

    # CulturaEscarro
    await CulturaEscarro.bulk_create([
        CulturaEscarro(id=1, nome='Positiva'),
        CulturaEscarro(id=2, nome='Negativa'),
        CulturaEscarro(id=3, nome='Em andamento'),
        CulturaEscarro(id=4, nome='Não realizada'),
        CulturaEscarro(id=9, nome='Ignorado')
    ])

    # TesteMolec
    await TesteMolec.bulk_create([
        TesteMolec(id=1, nome='Detectável sensível à Rifampicina'),
        TesteMolec(id=2, nome='Detectável resistente à Rifampicina'),
        TesteMolec(id=3, nome='Não detectável'),
        TesteMolec(id=4, nome='Inconclusivo'),
        TesteMolec(id=5, nome='Não realizado'),
        TesteMolec(id=9, nome='Ignorado')
    ])

    # TesteSensibilidade
    await TesteSensibilidade.bulk_create([
        TesteSensibilidade(id=1, nome='Resistente somente à Isoniazida'),
        TesteSensibilidade(id=2, nome='Resistente somente à Rifampicina'),
        TesteSensibilidade(id=3, nome='Resistente à Isoniazida e Rifampicina'),
        TesteSensibilidade(id=4, nome='Resistente a outras drogas de 1ª linha'),
        TesteSensibilidade(id=5, nome='Sensível'),
        TesteSensibilidade(id=6, nome='Em andamento'),
        TesteSensibilidade(id=7, nome='Não realizado'),
        TesteSensibilidade(id=9, nome='Ignorado')
    ])

    # SituacaoEncerra
    await SituacaoEncerra.bulk_create([
        SituacaoEncerra(id=1, nome='Cura'),
        SituacaoEncerra(id=2, nome='Abandono'),
        SituacaoEncerra(id=3, nome='Falência'),
        SituacaoEncerra(id=4, nome='Óbito por tuberculose'),
        SituacaoEncerra(id=5, nome='Óbito por outras causas'),
        SituacaoEncerra(id=7, nome='Transferência'),
        SituacaoEncerra(id=8, nome='Mudança de diagnóstico'),
        SituacaoEncerra(id=9, nome='Drogas resistentes'),
        SituacaoEncerra(id=10, nome='Não encerrado'),
        SituacaoEncerra(id=99, nome='Ignorado') 
    ])

    # Sexo
    await Sexo.bulk_create([
        Sexo(id=1, nome='Masculino'),
        Sexo(id=2, nome='Feminino'),
        Sexo(id=9, nome='Ignorado')
    ])

    # Raca
    await Raca.bulk_create([
        Raca(id=1, nome='Branca'),
        Raca(id=2, nome='Preta'),
        Raca(id=3, nome='Amarela'),
        Raca(id=4, nome='Parda'),
        Raca(id=5, nome='Indígena'),
        Raca(id=9, nome='Ignorado')
    ])

    # FaixaEtar
    await FaixaEtar.bulk_create([
        FaixaEtar(id=1, nome='Ignorado'),
        FaixaEtar(id=2, nome='<1 Ano'),
        FaixaEtar(id=3, nome='1-4'),
        FaixaEtar(id=4, nome='5-9'),
        FaixaEtar(id=5, nome='10-14'),
        FaixaEtar(id=6, nome='15-19'),
        FaixaEtar(id=7, nome='20-39'),
        FaixaEtar(id=8, nome='40-59'),
        FaixaEtar(id=9, nome='60-64'),
        FaixaEtar(id=10, nome='65-69'),
        FaixaEtar(id=11, nome='70-79'),
        FaixaEtar(id=12, nome='80+')
    ])

    # UF
    await UF.bulk_create([
        UF(id=12, nome='Acre'),
        UF(id=27, nome='Alagoas'),
        UF(id=13, nome='Amazonas'),
        UF(id=16, nome='Amapá'),
        UF(id=29, nome='Bahia'),
        UF(id=23, nome='Ceará'),
        UF(id=53, nome='Distrito Federal'),
        UF(id=32, nome='Espírito Santo'),
        UF(id=52, nome='Goiás'),
        UF(id=21, nome='Maranhão'),
        UF(id=31, nome='Minas Gerais'),
        UF(id=50, nome='Mato Grosso do Sul'),
        UF(id=51, nome='Mato Grosso'),
        UF(id=15, nome='Pará'),
        UF(id=25, nome='Paraíba'),
        UF(id=26, nome='Pernambuco'),
        UF(id=22, nome='Piauí'),
        UF(id=41, nome='Paraná'),
        UF(id=33, nome='Rio de Janeiro'),
        UF(id=24, nome='Rio Grande do Norte'),
        UF(id=43, nome='Rio Grande do Sul'),
        UF(id=11, nome='Rondônia'),
        UF(id=14, nome='Roraima'),
        UF(id=42, nome='Santa Catarina'),
        UF(id=28, nome='Sergipe'),
        UF(id=35, nome='São Paulo'),
        UF(id=17, nome='Tocantins')
    ])

    print("Seed concluído com sucesso!")

if __name__ == '__main__':
    run_async(seed_data())