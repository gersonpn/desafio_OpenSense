# Projeto de Extração e Organização de Dados de Patentes

Este projeto realiza a extração, organização e exibição de informações de patentes a partir de arquivos HTML armazenados em um diretório. O resultado final é apresentado em um arquivo HTML contendo uma tabela formatada com os dados extraídos.

## Estrutura do Projeto

- **Pasta de entrada:** Contém os arquivos HTML com os dados a serem extraídos.
- **Código principal:** Script Python que realiza a leitura dos arquivos, extração dos dados, e geração do arquivo HTML.
- **Arquivo de saída:** `PATENTES.HTML`, onde os dados organizados são salvos.

## Funcionalidades

1. **Renomeação de Arquivos:** Verifica se os arquivos seguem o padrão `Arq<number>.html` e renomeia, se necessário.
2. **Extração de Dados:** Usa BeautifulSoup para obter informações de tabelas e outros elementos dos arquivos HTML.
3. **Tratamento de Dados:** Preenche valores ausentes ou inválidos com `...`.
4. **Ordenação:** Ordena os arquivos e dados de forma natural (ex.: `Arq1`, `Arq2`, ..., `Arq10`).
5. **Exportação:** Gera um arquivo HTML com os dados extraídos e organizados.

## Dependências

Certifique-se de instalar as bibliotecas necessárias antes de executar o projeto:

```bash
pip install pandas beautifulsoup4 natsort
```

## Como Executar

1. Coloque os arquivos HTML na pasta especificada no código.
2. Configure o caminho da pasta na variável `pasta` do script Python.
3. Execute o script:

```bash
python nome_do_script.py
```

4. O arquivo `PATENTES.HTML` será gerado no mesmo diretório.

## Estrutura da Tabela de Saída

A tabela contém as seguintes colunas:

- **Arquivo:** Nome do arquivo de origem.
- **CNPJ:** Número do CNPJ extraído do texto.
- **RESULTADO:** Contagem de entradas na tabela.
- **NÚMERO DO PEDIDO:** Número do pedido de patente.
- **DATA DO DEPÓSITO:** Data do depósito.
- **Título:** Título do registro de patente (truncado em 10 caracteres, se necessário).
- **IPC:** Código IPC (International Patent Classification).

## Exemplo de Uso

Um exemplo da tabela gerada:

<div style="display: flex; justify-content: center;">
<table border="1" class="dataframe" style="text-align: center;">
  <thead>
    <tr>
      <th>Arquivo</th>
      <th>CNPJ</th>
      <th>RESULTADO</th>
      <th>NÚMERO DO PEDIDO</th>
      <th>DATA DO DEPÓSITO</th>
      <th>Título</th>
      <th>IPC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Arq1.html</td>
      <td>00000000000191</td>
      <td>2</td>
      <td>BR 1</td>
      <td>24/10/2018</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>Arq2.html</td>
      <td>00001180000126</td>
      <td>0</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
</div>
