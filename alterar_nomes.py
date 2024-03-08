"""
Script para ajudar a renomear arquivos de uma pasta com base em um arquivo Excel.
Autor: Ariel
Versão: 0.1
"""

import os
import pandas as pd

def ler_arquivo_excel(caminho):
    try:
        df = pd.read_excel(caminho)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None

def renomear_arquivos(caminho_pasta_raiz, df):
    if df is None:
        return

    for arquivo in os.listdir(caminho_pasta_raiz):
        arquivo_caminho = os.path.join(caminho_pasta_raiz, arquivo)
        if os.path.isfile(arquivo_caminho):
            codigo, ext = os.path.splitext(arquivo.split('_')[0])
            if codigo in df['Codigo'].values:
                try:
                    nome_correto = df.loc[df['Nome Incorreto'] == codigo, 'Nome Correto'].values[0]
                    os.rename(arquivo_caminho, os.path.join(caminho_pasta_raiz, nome_correto + ext))
                except Exception as e:
                    print(f"Erro ao renomear o arquivo {arquivo}: {e}")

caminho_arquivo_excel = 'nome_do_arquivo.xlsx'
caminho_pasta_raiz = '.'
df = ler_arquivo_excel(os.path.join(caminho_pasta_raiz, caminho_arquivo_excel))
renomear_arquivos(caminho_pasta_raiz, df)