import pandas as pd
import seaborn as sb
low_memory=False
# Apenas no Jupyter
%matplotlib inline

pd.options.display.max_columns = 80
pd.options.display.max_rows = 90

filename = 'fila-publica-2017-11-30.csv'
df = pd.read_csv(filename)

df.shape

df.describe()

df.info()

df.rename(columns={'MUNICÍPIO DE RESIDÊNCIA': 'MUNICÍPIODERESIDÊNCIA',
                'CENTRAL DE REGULAÇÃO/RESPONSÁVEL': 'CENTRALDEREGULAÇÃO/RESPONSÁVEL',
                'TEMPO MÉDIO DE ESPERA(DIAS)': 'TEMPOMÉDIODEESPERA(DIAS)',
                'DATA DA SOLICITAÇÃO': 'DATADASOLICITAÇÃO',
                'DESCRIÇÃO DO PROCEDIMENTO': 'DESCRIÇÃODOPROCEDIMENTO',
                'CNES DA CENTRAL EXECUTANTE': 'CNESDACENTRALEXECUTANTE',
                'CNES DA UNIDADE SOLICITANTE': 'CNESDAUNIDADESOLICITANTE'
                }, inplace=True)

df.sample(10)

df.groupby('SERVIÇO').size().sort_values().plot(kind='barh')

df.groupby('MUNICÍPIODERESIDÊNCIA').size().sort_values().tail(20).plot(kind='barh', figsize=(10,10))

df.query('SERVIÇO == "Exame"')['MUNICÍPIODERESIDÊNCIA'].value_counts().head().plot(kind='barh')

df.query('SERVIÇO == "Exame"')['MUNICÍPIODERESIDÊNCIA'].value_counts().head()

df.query('SERVIÇO == "Exame" and MUNICÍPIODERESIDÊNCIA == "PALHOCA"').DOCUMENTO.value_counts().describe()

df.query('SERVIÇO == "Exame" and MUNICÍPIODERESIDÊNCIA == "PALHOCA"').DOCUMENTO.value_counts().head()

df.query('DOCUMENTO == 704207709501384')[['DESCRIÇÃODOPROCEDIMENTO','DATADASOLICITAÇÃO', 'CENTRALDEREGULAÇÃO/RESPONSÁVEL', 'POSIÇÃO', 'CNESDACENTRALEXECUTANTE', 'CNESDAUNIDADESOLICITANTE']].sort_values(by='DESCRIÇÃODOPROCEDIMENTO').head(10)

df.query('DOCUMENTO == 700603418445267')[['DESCRIÇÃODOPROCEDIMENTO','DATADASOLICITAÇÃO', 'CENTRALDEREGULAÇÃO/RESPONSÁVEL', 'POSIÇÃO', 'CNESDACENTRALEXECUTANTE', 'CNESDAUNIDADESOLICITANTE']].sort_values(by='DESCRIÇÃODOPROCEDIMENTO').head(10)

def deduplicate_stats(query=None):
    if query:
        df_tmp = df.query(query)
    else:
        df_tmp = df
    total_rows = len(df_tmp)
    unique_rows = len(df_tmp.groupby(['DOCUMENTO', 'DESCRIÇÃODOPROCEDIMENTO']))
    unique_rows_same_date = len(df_tmp.groupby(['DOCUMENTO', 'DESCRIÇÃODOPROCEDIMENTO', 'DATADASOLICITAÇÃO']))
    reducao_fila = (total_rows - unique_rows) / total_rows
    print('           registros na fila:', total_rows)
    print('    registros únicos na fila:', unique_rows)
    print('          duplicados (total):', total_rows - unique_rows)
    print('duplicados (mesmo timestamp):', total_rows - unique_rows_same_date)
    print('    redução com deduplicação:', int(100*reducao_fila), '%')

deduplicate_stats('MUNICÍPIODERESIDÊNCIA == "PALHOCA"')

deduplicate_stats()

deduplicate_stats('MUNICÍPIODERESIDÊNCIA == "FLORIANOPOLIS"')

deduplicate_stats('MUNICÍPIODERESIDÊNCIA == "JOINVILLE"')

df['DESCRIÇÃODOPROCEDIMENTO'].value_counts().to_frame().head(10)

df.query('DESCRIÇÃODOPROCEDIMENTO == "CONSULTA EM OFTALMOLOGIA - GERAL"')['MUNICÍPIODERESIDÊNCIA'].value_counts().to_frame().head(10)

"""
Pacientes de Canelinha, ao solicitar uma consulta em oftalmologia, são direcionadas a 4 centrais executantes diferentes, que possuem tempo de espera entre 34 e 417 dias. Sugestão: rotear as pessoas para centrais com menos pacientes.
"""
df.query('DESCRIÇÃODOPROCEDIMENTO == "CONSULTA EM OFTALMOLOGIA - GERAL"').groupby(['CÓDIGO SIGTAP DO PROCEDIMENTO', 'MUNICÍPIODERESIDÊNCIA', 'CNESDACENTRALEXECUTANTE', 'TEMPOMÉDIODEESPERA(DIAS)', 'CLASSIFICAÇÃO']).count()[['POSIÇÃO']].query('MUNICÍPIODERESIDÊNCIA == "CANELINHA"')