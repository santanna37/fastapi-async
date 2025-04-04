from src.model.settings.db_connection_handler import db_connection_handler
from src.model.entities.entitie_pessoas import Pessoas

class PessoasRepository:
    def __init__(self):
        self.__conn = db_connection_handler.get_db_conn()

    
    async def get_all_pessoas(self) -> list:
        query = Pessoas.select()
        result = await self.__conn.fetch_all(query)
        return result 