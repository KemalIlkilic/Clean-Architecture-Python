from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def insert(self, table : str, data: dict):
        pass

# The UserEntity class depends on the DatabaseInterface abstraction, not concrete implementations
# The UserEntity class is decoupled from specific database operations, knowing only about the abstract operations defined in DatabaseInterface.
class UserEntity:
    def __init__(self, user_id : str, database: DatabaseInterface):
        self.user_id = user_id
        self.database = database
    def save(self):
        self.database.insert("users", {"id" : self.user_id})

class MySQLDatabase(DatabaseInterface):
    def insert(self, table: str, data: dict):
        print(f"Inserting {data} into {table} table in MySQL")

class PostgreSQLDatabase(DatabaseInterface):
    def insert(self, table: str, data: dict):
        print(f"Inserting {data} into {table} table in PostgreSQL")

# Usage
mysql_db = MySQLDatabase()
user = UserEntity("123", mysql_db)
user.save()
postgres_db = PostgreSQLDatabase()
another_user = UserEntity("456", postgres_db)
another_user.save()

