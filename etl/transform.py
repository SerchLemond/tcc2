import pandas as pd
from datetime import datetime
from database.enums import DimensionEnum

class Transformer():
    def parse(self, data):
        column_mapping = DimensionEnum.get_column_mapping()

        valid_columns = list(set(column_mapping.keys()) & set(data.columns))
        df_filtered = data[valid_columns].copy()
        df_renamed = df_filtered.rename(columns=column_mapping)

        current_year = datetime.now().year

        for col in df_renamed.columns:
            df_renamed[col] = df_renamed[col].astype(str).str.strip()

            if col == "data":
                continue

            if col == "ano_nasc":
                df_renamed['idade'] = pd.to_numeric(df_renamed[col], errors='coerce').apply(
                    lambda x: current_year - x if pd.notnull(x) else None
                )
                continue 

            if col == "sexo_id":
                df_renamed[col] = df_renamed[col].map({"M": 1, "F": 2}).fillna(9)
            elif col == "raca_id":
                df_renamed[col] = df_renamed[col].replace("6", "9")
                df_renamed[col] = df_renamed[col].replace("", "9")
                df_renamed[col] = pd.to_numeric(df_renamed[col], errors="coerce").astype("Int64")
            elif col == "situacao_encerra_id":
                df_renamed[col] = df_renamed[col].replace("", "99")
                df_renamed[col] = pd.to_numeric(df_renamed[col], errors="coerce").astype("Int64")
            else:
                df_renamed[col] = df_renamed[col].replace("", "9")
                df_renamed[col] = pd.to_numeric(df_renamed[col], errors="coerce").astype("Int64")

        def idade_para_faixa_id(idade):
            if pd.isna(idade):
                return 1  
            elif idade < 1:
                return 2 
            elif 1 <= idade <= 4:
                return 3
            elif 5 <= idade <= 9:
                return 4
            elif 10 <= idade <= 14:
                return 5
            elif 15 <= idade <= 19:
                return 6
            elif 20 <= idade <= 39:
                return 7
            elif 40 <= idade <= 59:
                return 8
            elif 60 <= idade <= 64:
                return 9
            elif 65 <= idade <= 69:
                return 10
            elif 70 <= idade <= 79:
                return 11
            elif idade >= 80:
                return 12
            else:
                return 1 

        df_renamed['faixa_etar_id'] = df_renamed['idade'].apply(idade_para_faixa_id)

        df_renamed.drop(columns=['idade'], inplace=True)

        return df_renamed.to_dict(orient='records')
