import inject

from app.webapp.services.db_connect_service import DataBaseConnector


class SendToDataBase:

    @inject.autoparams()
    def __init__(self, database_connector: DataBaseConnector):
        self.database_connector = database_connector

    def insert(self, sql_query, data):
        return self.database_connector.insert(sql_query, data)

    def insert_many(self, sql_query, data):
        return self.database_connector.insert_many(sql_query, data)

    def select(self, sql_query, data):
        return self.database_connector.select(sql_query, data)
