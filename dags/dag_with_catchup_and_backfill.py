from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'busragokceli',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_catchup_backfill_v02',
    description='Our first dag using python operator',
    start_date=datetime(2021, 11, 1),
    schedule_interval='@daily',
    catchup=False
    ) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command'
    )
    task1