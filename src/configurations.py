import os

class DBConfigurations :
    postgres_username = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    postgres_server = os.getenv('POSTGRES_SERVER')
    postgres_port = int(os.getenv('POSTGRES_PORT', 5432))
    postgres_db = os.getenv('POSTGRES_DB')
    sql_alchemy_databaase_url = (
        f'postgresql://{postgres_username}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}'
    )

class APIConfigurations :
    title = os.getenv('API_TITLE', 'Model_DB_Service')
    description = os.getenv('API_DESCRIPTION', 'machine learning system training patterns')
    version = os.getenv('API_VERSION', '0.1')