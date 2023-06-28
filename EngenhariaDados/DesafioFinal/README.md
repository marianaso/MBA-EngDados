##  Desafio final

A proposta do desafio é desenvolver um pipeline que faça a extração de dados no MongoDB e na API do IBGE (https://servicodados.ibge.gov.br/api/docs/localidades) e deposite os dados no Data Lake, além de deixar disponibilizado os dados tratados em um DW. Tanto Data Lake quando DW, foram utilizados na AWS (free tier). Além disso, todas as etapas foram executadas através do Apache Airflow (localmente).

Para instalação e execução do airflow:

```sh
python -m venv venv
source venv/bin/activate

pip install "apache-airflow[postgres,celery,redis]==2.6.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.0/constraints-3.10.txt"

export AIRFLOW_HOME=~/DesafioFinal/

airflow standalone
```

- Pasta dags: contém as dags para o pipeline.

- Pasta dados: contém os arquivos csv com os DataFrames resultantes da extração dos dados do MongoDB e da API do IBGE. Para facilitar os dados já foram tratados assim que extraídos.