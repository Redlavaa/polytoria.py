from src.polytoria.wrapper import Polytoria
import asyncio

async def main():

    polytoria = Polytoria()


    user = await polytoria.user(22783)
    linked = await user.linked()
    item = await polytoria.item(170053)
    place = await polytoria.place(1)
    guild = await polytoria.guild(1)

    print(item.name)
    print(place.name)
    print(guild.name)
    print(linked)

if __name__ == "__main__":
    asyncio.run(main())