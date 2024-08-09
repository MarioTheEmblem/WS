import pandas as pd

def preprocesamiento_omie (ruta):

    df = pd.read_csv(ruta)
    date = ruta.split('/')[-1].split('.')[0]

    df.columns = ['Hours','Price','Volume']
    df['date'] = date

    solo_hora = df['Hours'].str.extract(r'(\d+)')[0]

    solo_hora = df['date'] + ' ' + solo_hora
    fecha_hora = pd.to_datetime(solo_hora)

    df['datetime'] = fecha_hora

    df = df.drop(columns=['Hours','date'])
    df = df.set_index('datetime')
    return df