# Projeto Comex

Este é um projeto de análise de dados de exportação e importação utilizando Python e Power BI.

## Pré-requisitos

Antes de rodar o projeto, você precisará instalar algumas dependências e configurar um ambiente de desenvolvimento.

### 1. Criando o ambiente virtual

Primeiro, crie um ambiente virtual Python para isolar as dependências do projeto. Isso é recomendado para evitar conflitos com pacotes globais do seu sistema.

No terminal, execute:

```bash
python -m venv venv

2. Instalando as dependências
Depois de ativar o ambiente virtual, instale as dependências do projeto.

Para Windows:

bash
Copiar
Editar
.\venv\Scripts\activate
Para Linux/Mac:

bash
Copiar
Editar
source venv/bin/activate
Com o ambiente ativado, instale as dependências usando o pip:

bash
Copiar
Editar
pip install -r requirements.txt
Se o arquivo requirements.txt não existir, você pode criar um com as bibliotecas que está usando, como:

txt
Copiar
Editar
pandas
sqlalchemy
schedule
gitpython
requests

3. Base de dados
Os arquivos .csv com os dados de importação e exportação (excluídos do Git com .gitignore) precisam ser baixados manualmente e colocados no diretório de dados do projeto. O código depende desses arquivos para funcionar corretamente.

Baixe os arquivos CSV (importação e exportação de 2020 e 2021).

Coloque os arquivos baixados na pasta data/ ou no diretório apropriado do seu projeto.

Por exemplo, o diretório de dados pode ser estruturado assim:

text
Copiar
Editar
/data
  importacao_2020.csv
  importacao_2021.csv
  exportacao_2020.csv
  exportacao_2021.csv
4. Banco de dados
O código usa um banco de dados SQLite (comex.db), que é gerado automaticamente ao rodar o script ETL. Não é necessário adicionar este arquivo ao Git devido ao seu tamanho, mas ele será criado localmente.

5. Rodando o ETL
O processo de ETL pode ser executado manualmente com o seguinte comando:

bash
Copiar
Editar
python etl_pipeline.py
O script de ETL irá carregar os dados CSV para o banco de dados SQLite e realizar as transformações necessárias.

6. Agendamento de Execução
Se você deseja agendar a execução do ETL periodicamente, você pode usar o script main.py com a biblioteca schedule para rodar o ETL automaticamente em intervalos definidos.

Para rodar o agendador, execute:

bash
Copiar
Editar
python main.py