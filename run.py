
import asyncio
from src.model.settings.db_connection_handler import db_connection_handler
from src.controllers.finder_pessoas import PessoasFinder



async def run_pessoas():
    await db_connection_handler.connect_to_db()

    controller = PessoasFinder()
    response = await controller.find_pessoas()
    
    print(response)

    await db_connection_handler.disconnect_to_db()


asyncio.run(run_pessoas())