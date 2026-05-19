from src.wrapper import Polytoria
import asyncio

async def main():


    polytoria = Polytoria(browser="chrome")



    item = await polytoria.item(170053)

    print(item.price)

if __name__ == "__main__":
    asyncio.run(main())