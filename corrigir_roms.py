import glob
import re
import so

# Caminho onde suas ROMs estão armazenadas
rom_directory = '/caminho/para/seus/jogos'

# Lista de ROMs encontradas no diretório, usando o padrão de extensão correto (por exemplo, '.iso' ou '.bin')
pattern = '*.chd'  # Você pode ajustar para seu tipo de arquivo específico
rom_files = glob.glob(rom_directory + '/' + pattern)

for file in rom_files:
    # Nome do arquivo sem caminho completo
    filename = os.path.basename(file)

    # Expresse a procura por o sinal (USA)
    regex_pattern = r'\(USA\)'

    # Verifique se a string contém o patrão e mantenha espaços
    if bool(re.search(regex_pattern, filename)):
        print(f'Encontrada ROM com o sinal (USA): {filename}')

        # Remova o texto (USA) do nome do arquivo e mantenha os espaços existentes
        new_filename = re.sub(regex_pattern, '', filename)

        # Renomeie o arquivo original para o novo nome sem o sinal (USA), mantendo os espaços
        if not new_filename.endswith('.chd'):
            new_file = f'{new_filename}.chd'
        else:
            new_file = new_filename

        # Renomeie o arquivo original para o novo nome
        os.rename(file, new_file)

# Imprime as informações de sucesso dos renomeamentos
print("Todos os arquivos foram renomeados com sucesso.")