from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from get_files import get_data
from insert_S3 import insert_into_S3
from connectDW import create_conn_sql

default_args = {
    'owner': 'Mariana O',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('primeiroTeste', default_args=default_args, description = 'Desafio Final EDC 2023')

getData = PythonOperator(task_id='get_online_data', python_callable=get_data, dag=dag)

insertS3 = PythonOperator(task_id='insert_data_S3', python_callable=insert_into_S3, dag=dag)

insertSQL = PythonOperator(task_id='insert_into_SQL', python_callable=create_conn_sql, dag=dag)


getData >> insertS3 >> insertSQL

