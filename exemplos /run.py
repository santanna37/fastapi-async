import asyncio
import httpx

async def fetch_get(client: any, pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = await client.get(url)
    data = response.json()

    name = data["name"]
    hability = data["moves"][0]["move"]
    print(f"name: {name} /  move: {hability}")
    print()


async def main():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            fetch_get(client, "ditto"),
            fetch_get(client, "pikachu"),
            fetch_get(client, "mew"),
            fetch_get(client, "vulpix")
        )

asyncio.run(main())