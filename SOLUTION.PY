import pandas as pd
import re
import os
from bs4 import BeautifulSoup

pasta = "D:\\Documents\\teste_open_sense\\PATENTES"

arquivos = os.listdir(pasta)

# alteração do nome dos arquivos conforme solicitação do teste
if any(not arquivo.lower().startswith("arq") for arquivo in arquivos):
  for numero, item in enumerate(arquivos, start=1):
      caminho = os.path.join(pasta,item)
      alteracao = os.path.splitext(item)[1]
      nome = f"Arq{numero}{alteracao}"
      nova_alteracao = os.path.join(pasta, nome)
      os.rename(caminho, nova_alteracao)


# extração das informações de dentro do arquivo
def informacoes(arquivo):
    with open(arquivo, 'r', encoding='utf-8', errors='ignore') as arq:
      soup = BeautifulSoup(arq, 'html.parser')
      texto_arquivo = soup.get_text()
      info_tabela = soup.find('tbody', {'id': 'tituloContext'})

      verificacao_cnpj = r'\d{14}'
      cnpj = re.findall(verificacao_cnpj, texto_arquivo)
      resultado = len(cnpj)



      pedido, deposito, titulo, ipc = [], [], [], []

      if info_tabela is not None:
        tr = info_tabela.find_all('tr')
        for trs in tr:
          colunas = trs.find_all('td')
          pedido.append(colunas[0].text.strip())
          deposito.append(colunas[1].text.strip())
          titulo.append(colunas[2].text.strip())
          ipc.append(colunas[3].text.strip()),

      if info_tabela is None:
        pedido.append('-')
        deposito.append('-')
        titulo.append('-')
        ipc.append('-')

      return cnpj, resultado, pedido, ipc, deposito, titulo


for elementos in arquivos:
    caminho_arquivo = os.path.join(pasta, elementos)
    cnpj, resultado, pedido, ipc, deposito, titulo = informacoes(caminho_arquivo)
    print(f"itens {elementos}: CNPJ: {cnpj}, Total: {resultado}, Pedido: {pedido}, IPC: {ipc}, Data: {deposito}, Título: {titulo}")