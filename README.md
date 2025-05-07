# 📊 Projeto Comex (desafio SeuBoné)

Este projeto realiza o processo de **ETL (Extração, Transformação e Carga)** dos dados de exportação e importação do Brasil dos anos de 2020 e 2021, armazena-os em um banco de dados SQLite e disponibiliza um dashboard interativo construído no Power BI.

## 🗂 Estrutura do Projeto

├── dados/ # Arquivos CSV de entrada
│ ├── EXP_2020.csv
│ ├── EXP_2021.csv
│ ├── IMP_2020.csv
│ └── IMP_2021.csv
│
├── database/
│ └── comex.db # Banco SQLite gerado
│
├── etl/
│ └── verificacao_qualidade.py # Verificação da qualidade dos dados
│
├── dashboards/
│ └── comex_dashboard.pbix # Dashboard Power BI (offline)
│
├── executar_etl.py # Script principal de carregamento
├── requirements.txt # Dependências do projeto
└── README.md

## ⚙️ Pré-requisitos

- Python 3.9 ou superior
- [Power BI Desktop (versão offline)]

## 📥 Instalação

```bash
python -m venv venv

source venv/bin/activate  # Ou `venv\Scripts\activate` no Windows

pip install -r requirements.txt

## Rodar
```bash
Python main.py
