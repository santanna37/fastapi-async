from src.model.repositories.reposotory_pessoas import PessoasRepository


class PessoasFinder:
    def __init__(self):
        self.__pessoas_repo = PessoasRepository()

    async def find_pessoas(self) -> dict:
        pessoas = await self.__pessoas_repo.get_all_pessoas()
        
        formatted_pessoas = []
        for pessoa in pessoas:
            formatted_pessoas.append(
                { "id": pessoa.id, "nome": pessoa.name}
            )

        return{
            "type": "pessoa",
            "arributes": formatted_pessoas
        }