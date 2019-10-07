from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'chesswebmarket',
    user='chesswebmarket',
    password='chessmaster',
    host='localhost', port=5300,
    autorollback=True
)
