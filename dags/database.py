import psycopg2

def connect_db():
    
    return psycopg2.connect(
        host="postgres",
        database="pokemons",  
        user="postgres",      
        password="postgres" 
    )

def insert_pokemon_data(pokemon_data):
    
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO pokemons (pokemon_name, gender, types, hp, attack, defense, speed, evolution, habitat)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        pokemon_data['pokemon_name'],
        pokemon_data['gender'],
        pokemon_data['types'],
        pokemon_data['stats']['hp'],
        pokemon_data['stats']['attack'],
        pokemon_data['stats']['defense'],
        pokemon_data['stats']['speed'],
        pokemon_data['evolution'],
        pokemon_data['habitat']
    ))

    connection.commit()
    cursor.close()
    connection.close()
