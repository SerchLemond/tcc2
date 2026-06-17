import pandas as pd
from pysus import SINAN
import numpy as np

class Extractor:
    async def extract(self, year):
        sinan = SINAN().load()
        
        files = sinan.get_files(dis_code=["TUBE"], year=[year])
       
        file = files[0]
        parquet = sinan.download(file, local_dir="./parquets")
        df = parquet.to_dataframe()


        return df
