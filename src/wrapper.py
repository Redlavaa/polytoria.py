from src.api_client import APIClient
from src.models import User, Item

class Polytoria:
    def __init__(self, browser: str = "chrome"):
        self._client = APIClient(browser=browser)

    async def user(self, user_id: int) -> User:
 
        raw_data = await self._client.fetch_data(f"users/{user_id}", base_url="https://api.polytoria.com/v1/")
        
        return User(raw_data, self._client)
    
    async def item(self, item_id: int) -> Item:
 
        raw_data = await self._client.fetch_data(f"store/{item_id}", base_url="https://api.polytoria.com/v1/")
        
        return Item(raw_data, self._client)