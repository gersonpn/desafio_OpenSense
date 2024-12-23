import pandas as pd
import re
import os
from bs4 import BeautifulSoup
from natsort import natsorted as nt

pasta = "D:\\Documents\\teste_open_sense\\PATENTES"

arquivos = os.listdir(pasta)

if any(not arquivo.lower().startswith("arq") for arquivo in arquivos):
  for numero, item in enumerate(arquivos, start=1):
      caminho = os.path.join(pasta,item)
      alteracao = os.path.splitext(item)[1]
      nome = f"Arq{numero}{alteracao}"
      nova_alteracao = os.path.join(pasta, nome)
      os.rename(caminho, nova_alteracao)

def informacoes(arquivo):
    with open(arquivo, 'r', encoding='utf-8', errors='ignore') as arq:
      soup = BeautifulSoup(arq, 'html.parser')
      texto_arquivo = soup.get_text()
      info_tabela = soup.find('tbody', {'id': 'tituloContext'})

      cnpj = re.findall(r'\d{14}', texto_arquivo)
      resultado = 0

      dados_tabela = []

      if info_tabela is not None:
        tr = info_tabela.find_all('tr')
        for trs in tr:
          resultado += 1
          colunas = trs.find_all('td')

          info = {
             "pedido":colunas[0].text.strip()[0:4],
             "deposito":colunas[1].text.strip(),
             "titulo":colunas[2].text.strip()[0:10],
             "ipc":colunas[3].text.strip(),
          }

          if info['pedido'] == '' :
             info['pedido'] = '...'
          if info['deposito'] == '':
             info['deposito'] = '...'
          if info['titulo'] == '':
             info['titulo'] = '...'
          if info['ipc'] in ['', '-']:
             info['ipc'] = '...'

          dados_tabela.append(info)

      if info_tabela is None:
         dados_tabela.append({
            "pedido" : '...',
            "deposito" : '...',
            "titulo" : '...',
            "ipc" : '...'
         })

      return cnpj, resultado, dados_tabela

dados_df = []

for elementos in nt(arquivos):
    caminho_arquivo = os.path.join(pasta, elementos)
    cnpj, resultado, dados_tabela = informacoes(caminho_arquivo)

    for linha in dados_tabela:
        dados_df.append({
            'Arquivo': elementos,
            'CNPJ': cnpj[0],
            'RESULTADO': resultado,
            'NÚMERO DO PEDIDO': linha['pedido'],
            'DATA DO DEPÓSITO': linha['deposito'],
            'Título': linha['titulo'],
            'IPC': linha['ipc']
        })

df = pd.DataFrame(dados_df)
df.to_html("PATENTES.HTML", index=False)