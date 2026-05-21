from src.wrapper import Polytoria
import asyncio

async def main():

    polytoria = Polytoria()
    
    item = await polytoria.item(170053)
    place = await polytoria.place(1)

    print(item.name)
    print(item.price)
    print(place.creator)

if __name__ == "__main__":
    asyncio.run(main())