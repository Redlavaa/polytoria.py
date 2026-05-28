from .api_client import APIClient
from .models import User, Item, Place, Guild, User2id

class Polytoria:
    def __init__(self, browser: str = "chrome"):
        self._client = APIClient(browser=browser)

    async def user(self, user_id: int) -> User:
 
        raw_data = await self._client.fetch_data(f"users/{user_id}", base_url="https://api.polytoria.com/v1/")
        
        return User(raw_data, self._client)
    
    async def item(self, item_id: int) -> Item:
 
        raw_data = await self._client.fetch_data(f"store/{item_id}", base_url="https://api.polytoria.com/v1/")
        
        return Item(raw_data, self._client)
    
    async def place(self, place_id: int) -> Place:
 
        raw_data = await self._client.fetch_data(f"places/{place_id}", base_url="https://api.polytoria.com/v1/")
        
        return Place(raw_data, self._client)
    
    async def guild(self, guild_id: int) -> Guild:
 
        raw_data = await self._client.fetch_data(f"guilds/{guild_id}", base_url="https://api.polytoria.com/v1/")
        
        return Guild(raw_data, self._client)

    async def user2id(self, username: str) -> User2id:
        raw_data = await self._client.fetch_data(f"users/find?username={username}", base_url="https://api.polytoria.com/v1/")
        
        return User2id(raw_data, self._client)
