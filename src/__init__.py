# main.py
import asyncio
from src.wrapper import Polytoria

async def main():

    polytoria = Polytoria(browser="chrome") 
    
    user = await polytoria.user(22783)
    print(user.username)

if __name__ == "__main__":
    asyncio.run(main())