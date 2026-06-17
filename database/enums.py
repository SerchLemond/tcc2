from enum import Enum
from typing import Self

import pandas as pd

class DimensionEnum(Enum):
    """
    Each entry is structured as: (name, foreign_key_column)
    """
    TIPO_ENTRADA = "TRATAMENTO", "tipo_entrada_id"
    RACA = "CS_RACA", "raca_id",
    SEXO = "CS_SEXO", "sexo_id"
    POP_LIBER = "POP_LIBER", "ppl_id", 
    POP_RUA = "POP_RUA", "pop_sit_rua_id", 
    FORMA = "FORMA", "forma_id", 
    EXTRAPU1_N = "EXTRAPU1_N", "extra_pulm1_id", 
    AGRAVAIDS = "AGRAVAIDS", "aids_id", 
    AGRAVALCOO = "AGRAVALCOO","alcoolismo_id", 
    AGRAVDIABE =  "AGRAVDIABE","diabetes_id",
    AGRAVDOENC = "AGRAVDOENC", "doenca_mental_id", 
    AGRAVDROGAS = "AGRAVDROGA", "droga_ilicita_id", 
    AGRAVTABACO = "AGRAVTABAC", "tabagismo_id", 
    AGRAVOUTRA = "AGRAVOUTRA", "outra_doenca_id", 
    HIV = "HIV", "hiv_id", 
    CULTURA_ES = "CULTURA_ES", "cultura_escarro_id", 
    SITUA_ENCE = "SITUA_ENCE", "situacao_encerra_id",
    DATA = "DT_NOTIFIC", "data",
    ANO_NASC = "ANO_NASC", "ano_nasc"
    UF = "SG_UF_NOT", "uf_id"
    #BACILOSC_6 = "BACILOSC_6", "bacilosc_6mes_id", 
    #BACILOSC_2 = "BACILOSC_2",  "bacilosc_2mes_id", 
    #ANTIRRETROVIRAL = "ANTIRRETROVIRAL", "antirretroviral_id", 
    #RAIOX_TORA = "RAIOX_TORA","raio_x_id", 
    #TESTE_MOLEC = "TEST_MOLEC", "teste_molec_id", 
    #POP_SAUDE = "POP_SAUDE", "prof_saude_id", 
    #POP_IMIG = "POP_IMIG","imigrante_id", 
    #BENEF_GOV = "BENEF_GOV", "benef_governo_id", 
    #TEST_SENSIBILID = "TEST_SENSI", "teste_sensibilidade_id", 
    
    @property
    def ref(self):
        return self.value[0]

    @property
    def column(self):
        return self.value[1]
    
    @classmethod
    def get_column_mapping(cls):
        return {dim.ref: dim.column for dim in cls}

    @classmethod
    def transform_dataframe(cls, df: pd.DataFrame) -> list:
        """
        Transforma o DataFrame substituindo os nomes das colunas pelos nomes das foreign keys,
        removendo colunas não presentes no Enum e convertendo o DataFrame em uma lista de dicionários.
        """
        column_mapping = cls.get_column_mapping()
        
        # Filtra apenas as colunas que estão no Enum
        valid_columns = list(set(column_mapping.keys()) & set(df.columns))
        df_filtered = df[valid_columns].copy()

        # Renomeia as colunas conforme o mapeamento
        df_renamed = df_filtered.rename(columns=column_mapping)

        return df_renamed.to_dict(orient='records')
