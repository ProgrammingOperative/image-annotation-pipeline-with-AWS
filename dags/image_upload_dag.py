from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import subprocess
import logging

# Default arguments
default_args = {
    'owner': 'Titus Wachira',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'upload_images_to_s3',
    default_args=default_args,
    description='A DAG to upload images to S3 once a day',
    schedule_interval=timedelta(days=1),
)

def run_script():
    script_path = '/home/tito/Desktop/Data_Engineering_2024/Projects/Image_Annotation_Data_Pipeline/image-annotation-pipeline-with-AWS/dags/image_upload_dag.py'
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        logging.info(result.stdout)
        if result.returncode != 0:
            logging.error(result.stderr)
            raise Exception(f"Script failed with return code {result.returncode}")
    except Exception as e:
        logging.error(f"Error running script: {e}")
        raise


run_upload_script = PythonOperator(
    task_id='run_upload_script',
    python_callable=run_script,
    dag=dag,
)


# Define task dependencies
run_upload_script 
