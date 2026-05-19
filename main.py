from src.wrapper import Polytoria
import asyncio

async def main():


    polytoria = Polytoria(browser="chrome")



    User = await polytoria.user(22783)

    print(User.forumposts)

if __name__ == "__main__":
    asyncio.run(main())