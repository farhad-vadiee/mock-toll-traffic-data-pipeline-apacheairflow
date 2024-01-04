# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Farhad',
    'start_date': days_ago(0),
    'email': ['f.vadei93@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Educational Project',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define the first task

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar zxvf /Users/farhad/airflow/dags/finalassignment/staging/tolldata.tgz -C /Users/farhad/airflow/dags/finalassignment/staging',
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1,2,3,4 /Users/farhad/airflow/dags/finalassignment/staging/vehicle-data.csv > /Users/farhad/airflow/dags/finalassignment/staging/csv_data.csv',
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -f5,6,7 /Users/farhad/airflow/dags/finalassignment/staging/tollplaza-data.tsv | tr "\t" "," > /Users/farhad/airflow/dags/finalassignment/staging/tsv_data.csv',
    dag=dag,
)


extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c 59-62,63-68 /Users/farhad/airflow/dags/finalassignment/staging/payment-data.txt | tr " " "," > /Users/farhad/airflow/dags/finalassignment/staging/fixed_width_data.csv',
    dag=dag,
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command= "paste  -d ',' /Users/farhad/airflow/dags/finalassignment/staging/csv_data.csv /Users/farhad/airflow/dags/finalassignment/staging/tsv_data.csv /Users/farhad/airflow/dags/finalassignment/staging/fixed_width_data.csv  > /Users/farhad/airflow/dags/finalassignment/staging/extracted_data.csv",
    dag=dag,
)

transform_data = BashOperator(
    task_id= 'transform_data',
    bash_command="awk -F',' '{ print $1\",\"$2\",\"$3\",\"toupper($4)\",\"$5\",\"$6\",\"$7\",\"$8\",\"$9; }'  < /Users/farhad/airflow/dags/finalassignment/staging/extracted_data.csv > /Users/farhad/airflow/dags/finalassignment/staging/transformed_data.csv",
    dag=dag,
)


# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data