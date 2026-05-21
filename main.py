from src.polytoria.wrapper import Polytoria
import asyncio

async def main():

    polytoria = Polytoria()
    
    item = await polytoria.item(170053)
    place = await polytoria.place(1)
    guild = await polytoria.guild(1)

    print(item.name)
    print(place.name)
    print(guild.name)

if __name__ == "__main__":
    asyncio.run(main())