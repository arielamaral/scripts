# Projeto Python

Este projeto contém alguns scripts Python para auxiliar em atividades comuns do dia a dia.

## Script de Renomeação de Arquivos

Este script lê um arquivo Excel que contém um mapeamento de nomes de arquivos incorretos para corretos. Ele então percorre todos os arquivos em um diretório especificado e renomeia os arquivos de acordo com o mapeamento.

O script é dividido em duas funções principais:

- `ler_arquivo_excel(caminho)`: Esta função lê o arquivo Excel especificado e retorna um DataFrame pandas. Se ocorrer um erro durante a leitura do arquivo, a função imprimirá uma mensagem de erro e retornará None.

- `renomear_arquivos(caminho_pasta_raiz, df)`: Esta função percorre todos os arquivos no diretório especificado e renomeia os arquivos de acordo com o mapeamento no DataFrame fornecido. Se ocorrer um erro durante a renomeação de um arquivo, a função imprimirá uma mensagem de erro.

## Script de Criação de Arquivos .psvita

Este script lê um arquivo Excel que contém uma lista de nomes e IDs. Ele então cria um arquivo .psvita para cada linha no arquivo Excel, com o nome do arquivo sendo o nome na linha e o conteúdo do arquivo sendo o ID na linha.

O script é dividido em três funções principais:

- `ler_arquivo_excel(caminho)`: Esta função lê o arquivo Excel especificado e retorna um DataFrame pandas. Se ocorrer um erro durante a leitura do arquivo, a função imprimirá uma mensagem de erro e retornará None.

- `criar_arquivo_psvita(nome, id, diretorio_saida)`: Esta função cria um arquivo .psvita com o nome e ID fornecidos no diretório de saída especificado. Se ocorrer um erro durante a criação do arquivo, a função imprimirá uma mensagem de erro.

- `criar_arquivos_psvita(df, diretorio_saida)`: Esta função percorre todas as linhas no DataFrame fornecido e chama `criar_arquivo_psvita(nome, id, diretorio_saida)` para cada linha.

## Script de Compactação de Arquivos

Este script percorre todas as pastas em um diretório especificado e cria um arquivo .zip para cada pasta.

O script é dividido em duas funções principais:

- `criar_arquivo_zip(pasta, diretorio_atual)`: Esta função cria um arquivo .zip para a pasta especificada no diretório atual. Se ocorrer um erro durante a criação do arquivo .zip, a função imprimirá uma mensagem de erro.

- `main()`: Esta é a função principal que obtém o caminho do diretório atual, lista todas as pastas no diretório atual e chama `criar_arquivo_zip(pasta, diretorio_atual)` para cada pasta.