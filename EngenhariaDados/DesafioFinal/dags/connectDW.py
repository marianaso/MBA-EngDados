import pandas as pd
from sqlalchemy import create_engine

def create_conn_sql():

    database_type = 'postgresql'
    username = 'seu_usuario'
    password = 'sua_senha'
    host = 'database-igti.cyy6z3ahm75i.us-east-1.rds.amazonaws.com'
    port = '5432'
    database_name = 'database-igti'

    # Crie a string de conexão
    connection = f'{database_type}://{username}:{password}@{host}:{port}/{database_name}'
    engine = create_engine(connection)
    conn = engine.connect()


    dfMongoDB = pd.DataFrame('./dados/dfMongoDB.csv')
    dfIBGE = pd.DataFrame('./dados/dfIBGE.csv')

    dfMongoDB.to_sql('tableMongoDB', conn, if_exists='replace', index=False)
    dfIBGE.to_sql('tableIBGE', conn, if_exists='replace', index=False)

    conn.close()

    
