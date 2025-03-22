from airflow.decorators import dag, task
from datetime import datetime, timedelta
import psycopg2

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 17),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    default_args=default_args,
    schedule_interval=None,  # Executar manualmente
    catchup=False,
    description="DAG para configurar o banco de dados PostgreSQL"
)
def setup_postgres_dag():
    
    @task()
    def create_database_and_table():
        connection = psycopg2.connect(
            host="postgres",
            database="postgres",  # Conectar ao banco de dados padrão
            user="postgres",
            password="postgres"
        )
        connection.autocommit = True
        cursor = connection.cursor()

        # Criar banco de dados
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'pokemons'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute("CREATE DATABASE pokemons")

        # Conectar ao banco de dados 'pokemons' e criar a tabela
        connection.close()
        connection = psycopg2.connect(
            host="postgres",
            database="pokemons",
            user="postgres",
            password="postgres"
        )
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemons (
            id SERIAL PRIMARY KEY,
            pokemon_name VARCHAR(50),
            gender VARCHAR(10),
            types VARCHAR(50),
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            speed INTEGER,
            evolution VARCHAR(50),
            habitat VARCHAR(50)
        )
        """)
        connection.commit()
        cursor.close()
        connection.close()

    create_database_and_table()

setup_postgres_dag()