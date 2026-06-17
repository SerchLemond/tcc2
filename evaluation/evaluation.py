import json
import pandas as pd

with open('distribuicoes_df_original_datasus.json', 'r', encoding='utf-8') as f:
    df_original = json.load(f)

with open('distribuicoes_importadas_db.json', 'r', encoding='utf-8') as f:
    db_data = json.load(f)

mapping = {
    "AGRAVAIDS": "aids_id",
    "AGRAVALCOO": "alcoolismo_id",
    "BENEF_GOV": "benef_governo_id",
    "CULTURA_ES": "cultura_escarro_id",
    "AGRAVDIABE": "diabetes_id",
    "AGRAVDOENC": "doenca_mental_id",
    "AGRAVDROGA": "droga_ilicita_id",
    "EXTRAPU1_N": "extra_pulm1_id",
    "FORMA": "forma_id",
    "HIV": "hiv_id",
    "AGRAVOUTRA": "outra_doenca_id",
    "POP_RUA": "pop_sit_rua_id",
    "POP_LIBER": "ppl_id",
    "AGRAVTABAC": "tabagismo_id",
    "TRATAMENTO": "tipo_entrada_id"
}

def compare_distributions(df_data, db_data, mapping):
    results = []
    for df_col, db_col in mapping.items():
        if df_col not in df_data or db_col not in db_data:
            continue  

        df_dist = pd.Series(df_data[df_col]).astype(float)
        db_dist = pd.Series(db_data[db_col]).astype(float)

        df_total = df_dist.sum()
        db_total = db_dist.sum()

        if df_total == 0 or db_total == 0:
            continue 

        df_percent = df_dist / df_total
        db_percent = db_dist / db_total

        comparison = pd.concat([df_percent, db_percent], axis=1, keys=['original', 'db']).fillna(0)
        comparison['diff'] = (comparison['original'] - comparison['db']).abs()
        comparison['diff_pct'] = comparison['diff'] * 100
        results.append((df_col, comparison.sort_index()))
    
    return results

distribution_comparison = compare_distributions(df_original, db_data, mapping)

for var, comp_df in distribution_comparison:
    print(f"\nComparação para variável: {var}")
    print(comp_df)
