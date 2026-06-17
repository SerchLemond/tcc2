from tortoise.models import Model
from tortoise import fields

class Fatos(Model):
    id = fields.BigIntField(primary_key=True)
    data = fields.DateField()
    ano_nasc = fields.CharField(max_length=50)
    uf = fields.ForeignKeyField("models.UF", related_name="facts", null=True)
    ppl = fields.ForeignKeyField("models.PPL", related_name="facts", null=True)
    raca = fields.ForeignKeyField("models.Raca", related_name="facts", null=True)
    sexo = fields.ForeignKeyField("models.Sexo", related_name="facts", null=True)
    tipo_entrada = fields.ForeignKeyField("models.TipoEntrada", related_name="facts", null=True)
    pop_sit_rua = fields.ForeignKeyField("models.PopSitRua", related_name="facts", null=True)
    imigrante = fields.ForeignKeyField("models.Imigrante", related_name="facts", null=True)
    prof_saude = fields.ForeignKeyField("models.ProfSaude", related_name="facts", null=True)
    benef_governo = fields.ForeignKeyField("models.BenefGoverno", related_name="facts", null=True)
    forma = fields.ForeignKeyField("models.Forma", related_name="facts", null=True)
    extra_pulm1 = fields.ForeignKeyField("models.ExtraPulm1", related_name="facts", null=True)
    extra_pulm2 = fields.ForeignKeyField("models.ExtraPulm2", related_name="facts", null=True)
    aids = fields.ForeignKeyField("models.Aids", related_name="facts", null=True)
    alcoolismo = fields.ForeignKeyField("models.Alcoolismo", related_name="facts", null=True)
    diabetes = fields.ForeignKeyField("models.Diabetes", related_name="facts", null=True)
    doenca_mental = fields.ForeignKeyField("models.DoencaMental", related_name="facts", null=True)
    droga_ilicita = fields.ForeignKeyField("models.DrogasIlicitas", related_name="facts", null=True)
    tabagismo = fields.ForeignKeyField("models.Tabagismo", related_name="facts", null=True)
    outra_doenca = fields.ForeignKeyField("models.OutraDoenca", related_name="facts", null=True)
    bac_escarro1 = fields.ForeignKeyField("models.BacEscarro1", related_name="facts", null=True)
    bac_escarro2 = fields.ForeignKeyField("models.BacEscarro2", related_name="facts", null=True)
    cultura_escarro = fields.ForeignKeyField("models.CulturaEscarro", related_name="facts", null=True)
    teste_rapido_tb = fields.ForeignKeyField("models.TesteRapidoTB", related_name="facts", null=True)
    teste_sensibilidade = fields.ForeignKeyField("models.TesteSensibilidade", related_name="facts", null=True)
    hiv = fields.ForeignKeyField("models.HIV", related_name="facts", null=True)
    antirretroviral = fields.ForeignKeyField("models.Antirretroviral", related_name="facts", null=True)
    #bacilosc_2mes = fields.ForeignKeyField("models.Bacilosc2Mes", related_name="facts", null=True)
    #bacilosc_6mes = fields.ForeignKeyField("models.Bacilosc6Mes", related_name="facts", null=True)
    situacao_encerra = fields.ForeignKeyField("models.SituacaoEncerra", related_name="facts", null=True)
    faixa_etar = fields.ForeignKeyField("models.FaixaEtar", related_name="facts", null=True)
    criado_em = fields.DatetimeField(auto_now_add=True, null=True)

    class Meta:
        table = "fatos"

class BancoMetadados(Model):
    id = fields.BigIntField(primary_key=True)
    nome_tabela = fields.CharField(max_length=5000)
    descricao_tabela = fields.TextField()
    categorias = fields.TextField()
    
    class Meta:
        table = "banco_metadados"

class MensagensChat(Model):
    id = fields.BigIntField(primary_key=True)
    chat_id = fields.BigIntField()
    sender = fields.CharField(max_length=10)
    content = fields.TextField()
    criado_em = fields.DatetimeField(auto_now_add=True, null=True)
    
    class Meta:
        table = "menssagens_chat"

class Logs(Model):
    id = fields.BigIntField(primary_key=True)
    chat_id = fields.BigIntField()
    message = fields.TextField()
    criado_em = fields.DatetimeField(auto_now_add=True, null=True)
    
    class Meta:
        table = "logs"