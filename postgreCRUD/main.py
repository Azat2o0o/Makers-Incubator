from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'crud_db',
    user = 'azat',
    password = '1',
    host = 'localhost',
    port = 5432
)
