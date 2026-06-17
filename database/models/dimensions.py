from tortoise.models import Model
from tortoise import fields

class UF(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "uf"

    def __str__(self):
        return self.nome
    
class MunicipioResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "municipio_resid"

    def __str__(self):
        return self.nome
    
class Idade(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "idade"

    def __str__(self):
        return self.nome

class Raca(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "raca"

    def __str__(self):
        return self.nome

class Sexo(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "sexo"

    def __str__(self):
        return self.nome

class TipoEntrada(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "tipo_entrada"

    def __str__(self):
        return self.nome

class PopSitRua(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "pop_sit_rua"

    def __str__(self):
        return self.nome

class ProfSaude(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "prof_saude"

    def __str__(self):
        return self.nome

class BenefGoverno(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "benef_governo"

    def __str__(self):
        return self.nome

class Forma(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "forma"

    def __str__(self):
        return self.nome

class ExtraPulm1(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "extra_pulm1"

    def __str__(self):
        return self.nome

class ExtraPulm2(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "extra_pulm2"

    def __str__(self):
        return self.nome

class Aids(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "aids"

    def __str__(self):
        return self.nome

class PPL(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "ppl"

    def __str__(self):
        return self.nome
    
class Alcoolismo(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "alcoolismo"

    def __str__(self):
        return self.nome

class Imigrante(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "imigrante"

    def __str__(self):
        return self.nome

class Diabetes(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "diabetes"

    def __str__(self):
        return self.nome

class DoencaMental(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "doenca_mental"

    def __str__(self):
        return self.nome

class DrogasIlicitas(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "droga_ilicita"

    def __str__(self):
        return self.nome

class Tabagismo(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "tabagismo"

    def __str__(self):
        return self.nome

class OutraDoenca(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "outra_doenca"

    def __str__(self):
        return self.nome

class BacEscarro1(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bac_escarro1"

    def __str__(self):
        return self.nome

class BacEscarro2(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bac_escarro2"

    def __str__(self):
        return self.nome

class CulturaEscarro(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "cultura_escarro"

    def __str__(self):
        return self.nome

class TesteRapidoTB(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "teste_rapido_tb"

    def __str__(self):
        return self.nome

class TesteSensibilidade(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "teste_sensibilidade"

    def __str__(self):
        return self.nome

class HIV(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "hiv"

    def __str__(self):
        return self.nome

class Antirretroviral(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "antirretroviral"

    def __str__(self):
        return self.nome

class Bacilosc2Mes(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bacilosc_2mes"

    def __str__(self):
        return self.nome

class Bacilosc6Mes(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bacilosc_6mes"

    def __str__(self):
        return self.nome

class RaioX(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "raio_x"

    def __str__(self):
        return self.nome

class TesteMolec(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "teste_molec"

    def __str__(self):
        return self.nome

class SituacaoEncerra(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "situacao_encerra"

    def __str__(self):
        return self.nome

class FaixaEtar(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "faixa_etar"

    def __str__(self):
        return self.nome
