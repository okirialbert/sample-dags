"""Example DAG demonstrating the usage of the BashOperator."""

from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="example_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
) as dag:

    # [START howto_operator_bash]
    run_this = BashOperator(
        task_id="execute_actuator",
        bash_command="./actuator.exe",
    )

    # [START howto_operator_bash_template]
    also_run_this = BashOperator(
        task_id="execute_shell_script",
        bash_command='./script_file.sh',
    )
    # [END howto_operator_bash_template]

    run_this >> also_run_this

