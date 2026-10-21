from settings.loader import settings
import psycopg2
from psycopg2.extras import RealDictCursor
from database import queries


class BaseManager:
    def __init__(self):
        self.connection = psycopg2.connect(settings.db.url)

    def manage(self, sql: str, *args,
               fetchone: bool = False,
               fetchall: bool = False,
               commit: bool = False):
        with self.connection as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sql, args)

                if fetchone and commit:
                    connection.commit()
                    return cursor.fetchone()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()
                connection.commit()
                return

class TableManager(BaseManager):
    def is_table_exists(self, table_name: str):
        return self.manage(queries.TABLE_EXISTS_SQL, table_name, fetchone=True)

    def create_tables(self):
        for table_name, sql in queries.TABLES_DATA.items():
            if not self.is_table_exists(table_name).get('exists'):
                self.manage(sql, commit=True)
                print(f'Таблица {table_name} создана.')

table_manager = TableManager()