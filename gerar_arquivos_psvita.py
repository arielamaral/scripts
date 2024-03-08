import pandas as pd
import os

def ler_arquivo_excel(caminho):
    try:
        df = pd.read_excel(caminho)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None

def criar_arquivo_psvita(nome, id, diretorio_saida):
    nome_arquivo = os.path.join(diretorio_saida, nome + ".psvita")
    try:
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(f"ID: {id}")
    except Exception as e:
        print(f"Erro ao criar o arquivo {nome_arquivo}: {e}")

def criar_arquivos_psvita(df, diretorio_saida):
    if df is None:
        return

    for indice, linha in df.iterrows():
        nome = linha["Nome"]
        id = linha["ID"]
        criar_arquivo_psvita(nome, id, diretorio_saida)

caminho_arquivo_excel = 'vita.xlsx'
diretorio_saida = '.'
df = ler_arquivo_excel(caminho_arquivo_excel)
criar_arquivos_psvita(df, diretorio_saida)

print("Arquivos criados:")
for arquivo in os.listdir(diretorio_saida):
    print(arquivo)