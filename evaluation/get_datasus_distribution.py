import pandas as pd
import json
from pysus import SINAN

sinan = SINAN().load()
files = sinan.get_files(dis_code=["TUBE"], year=[2023])
file = files[0]
parquet = sinan.download(file, local_dir="./parquets")
df = parquet.to_dataframe()

cols = [
    'CS_RACA', 'CS_SEXO', 'TRATAMENTO', 'INSTITUCIO', 'POP_LIBER',
    'POP_RUA', 'POP_IMIG', 'BENEF_GOV', 'FORMA', 'EXTRAPU1_N',
    'AGRAVAIDS', 'AGRAVALCOO', 'AGRAVDIABE', 'AGRAVDOENC', 'AGRAVDROGA',
    'AGRAVTABAC', 'AGRAVOUTRA', 'RAIOX_TORA', 'HIV',
    'CULTURA_ES', 'TESTE_TUBE', 'SITUA_ENCE', 'SG_UF_NOT'
]

distros = {}

for col in cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().replace('', '9')

        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(9).astype(int)

        distros[col] = df[col].value_counts(dropna=False).to_dict()

output_path = 'distribuicoes_df_original_datasus.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(distros, f, ensure_ascii=False, indent=2)

print(f"Distribuições salvas em {output_path}")
