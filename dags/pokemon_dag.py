from airflow.decorators import dag, task
from datetime import datetime, timedelta
import random
from pokemon import pokemon_capture
from database import insert_pokemon_data

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 17),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    default_args=default_args,
    schedule_interval=timedelta(minutes=1),  
    catchup=False,
    description="DAG para capturar Pokémon e armazenar no PostgreSQL"
)
def capture_pokemon_dag():
    
    @task()
    def capture_and_store_pokemon():
        pokemon_id = random.randint(1, 1025)
        pokemon_data = pokemon_capture(pokemon_id)
        insert_pokemon_data(pokemon_data)

    capture_and_store_pokemon()

capture_pokemon_dag()
