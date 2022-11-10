# ORM (object-relational mapping) - это технология программирования благодаря которой 
# разработчики могут использовать язык программирования для взаимодействия с реляционной 
# базой данных postgres, MySQL, MariaDB) вместо написания операторов SQL вы пишите код на
#  языке программирования. Это очень сильно ускоряет разработку приложения и БД, особенно
#  в начальных этапах разработки.

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm_db',
    user = 'azat',
    password = '1',
    host = 'localhost',
    port = 5432
)