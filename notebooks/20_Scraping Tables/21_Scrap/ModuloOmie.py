
import os
import pandas as pd

def descargar_omie_ruta(fecha, path=None):
    URL = F'https://www.omip.pt/es/market-data/spot?date={fecha}&commodity=EL&zone=ES'
    dfs = pd.read_html(URL)
    df = dfs[1]
    
    if path:
        filename = f'{fecha}.csv'
        pathfile = os.path.join(path,filename)
        df.to_csv(pathfile, index=False)
    return df


