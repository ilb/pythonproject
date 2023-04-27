import mysql.connector

from app.webapp.config import config


class DataBaseConnector:

    def __init__(self):
        self.connection = None
        self.connection = mysql.connector.connect(
            host=config.db(),
            password=config.db_password(),
            user=config.db_user(),
            database="pythonproject"
        )

    def build_query(self, sql_query, data):
        """
        Building a SQL query from received SQL-code and values
        :param sql_query: Formed SQL query to execute example (INSERT INTO table_name (col_1, col_2) VALUES || SELECT col_1, col_2 FROM table_name)
        :type sql_query: str
        :param data: Values to be operated in query (values to insert or logical statement for select)
        :type data:
        :return: Cursor (an MySQL-connector example of class)
        :rtype: MySQLCursor
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_query, data)
        return cursor

    def insert(self, sql_query, data):
        """
        Executes a INSERT function to database
        :param sql_query: Formed SQL query to execute example INSERT INTO table_name (col_1, col_2, col_3) VALUES)
        :type sql_query: str
        :param data: Values to be operated in query example ('Name', 'Last name', 'Age')
        :type data: tuple
        :return: Id of last row in table after insertion
        :rtype: int
        """
        cursor = self.build_query(sql_query, data)
        id = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return id

    def insert_many(self, sql_query, data):
        """
        Executes many value insertions into same table
        :param sql_query: Formed SQL query to execute example INSERT INTO table_name (col_1, col_2, col_3) VALUES)
        :type sql_query: str
        :param data: Values to be operated in query example [('Name', 'Last name', 'Age'), ('Name', 'Last name', 'Age'), ...]
        :type data: List
        :return: Count of inserted rows
        :rtype: int
        """
        cursor = self.connection.cursor()
        cursor.executemany(sql_query, data)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount

    def select(self, sql_query, data=""):
        """
        Executes SELECT function
        :param sql_query: Formed SQL query to execute example (SELECT col_1, col_2 FROM table_name)
        :type sql_query: str
        :param data: Optional parameter for logical statement example (WHERE age = 30)
        :type data: str
        :return: All selected data after query execution
        :rtype: Any
        """
        cursor = self.build_query(sql_query, data)
        selected_data = cursor.fetchall()
        cursor.close()
        return selected_data
