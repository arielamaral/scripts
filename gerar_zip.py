import os
import shutil

def criar_arquivo_zip(pasta, diretorio_atual):
    nome_zip = f"{pasta}.zip"  # Nome do arquivo ZIP baseado no nome da pasta
    caminho_pasta = os.path.join(diretorio_atual, pasta)  # Caminho da pasta a ser compactada
    caminho_zip = os.path.join(diretorio_atual, nome_zip)  # Caminho para o arquivo ZIP a ser criado
    try:
        shutil.make_archive(caminho_zip[:-4], 'zip', caminho_pasta)  # Cria o arquivo ZIP
    except Exception as e:
        print(f"Erro ao criar o arquivo ZIP {nome_zip}: {e}")

def main():
    # Obtém o caminho do diretório atual
    diretorio_atual = os.getcwd()

    # Lista todas as pastas no diretório atual
    pastas = [pasta for pasta in os.listdir(diretorio_atual) if os.path.isdir(os.path.join(diretorio_atual, pasta))]

    # Cria um arquivo ZIP para cada pasta
    for pasta in pastas:
        criar_arquivo_zip(pasta, diretorio_atual)

if __name__ == "__main__":
    main()