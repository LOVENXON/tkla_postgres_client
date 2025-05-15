import os
from tkla_postgres_client.core import PostgresClient
from tkla_postgres_client.builder import create_tables

# Reemplaza con tu cadena real o usa variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL_TEST")

schema = {
    "users": {
        "id": {"data_type": "serial", "primary_key": True},
        "name": {"data_type": "varchar", "length": 100, "nullable": False},
        "email": {"data_type": "varchar", "length": 100, "unique": True}
    }
}

def main():
    print("Inicializando cliente...")
    client = PostgresClient(DATABASE_URL)

    print("Creando tablas...")
    print(create_tables(schema, client))

    print("Insertando usuario...")
    result = client.insert_data({
        "users": {"name": "Ana García", "email": "ana@example.com"}
    })
    print(result)

    print("Consultando usuario...")
    result = client.select_data({
        "users": {
            "conditions": {"email": "ana@example.com"},
            "columns": ["id", "name", "email"]
        }
    })
    print(result)

    print("Actualizando nombre...")
    result = client.update_data({
        "users": {
            "values": {"name": "Ana Actualizada"},
            "conditions": {"email": "ana@example.com"}
        }
    })
    print(result)

    print("Verificando existencia...")
    exists = client.exists({
        "users": {"conditions": {"email": "ana@example.com"}}
    })
    print("¿Existe?", exists)

    print("Contando usuarios...")
    count = client.count({
        "users": {"conditions": {}}
    })
    print("Total:", count)

    print("Eliminando usuario...")
    result = client.delete_data({
        "users": {"conditions": {"email": "ana@example.com"}}
    })
    print(result)

    client.close()
    print("Finalizado.")

if __name__ == "__main__":
    main()
