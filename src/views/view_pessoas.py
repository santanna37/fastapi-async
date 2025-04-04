from src.controllers.finder_pessoas import PessoasFinder

class PessoasFinderView:
    def __init__(self):
        self.__controller = PessoasFinder()

    async def handle_find_pessoas(self, http_request = None) -> dict:
        response = await self.__controller.find_pessoas()
        http_response = {
            "body": response,
            "status_code": 200
        }
        return http_response