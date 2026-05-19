from src.wrapper import Polytoria
import asyncio

async def main():

    polytoria = Polytoria()
    
    item = await polytoria.item(170053)

    print(item.name)
    print(item.price)

    owners = await item.owners()
    print(owners)

if __name__ == "__main__":
    asyncio.run(main())