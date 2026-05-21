from src.polytoria.api_client import APIClient
from pydantic import BaseModel, Field

class User(BaseModel):

    id: int
    username: str
    description: str | None = None
    
    # Thumbnail fields
    thumbnail: dict | None = None
    
    playing: bool | None = None
    net_worth: int = Field(alias="netWorth")
    place_visits: int = Field(alias="placeVisits")
    forum_posts: int = Field(alias="forumPosts")
    asset_sales: int = Field(alias="assetSales")
    membership_type: str = Field(alias="membershipType")
    is_staff: bool = Field(alias="isStaff")
    user_role_class: str = Field(alias="userRoleClass")
    join_date: str = Field(alias="registeredAt")
    last_seen: str = Field(alias="lastSeenAt")

    _client: object = PrivateAttr(default=None)
    
class Item:
    def __init__(self, data:dict, client):

        id: int
        type: str
        accessory_type: Optional[str] = Field(None, alias="accessoryType")
        name: str
        description: Optional[str] = None
        tags: List[str] = Field(default_factory=list)
        creator: Creator
        thumbnail: Optional[str] = None
        price: Optional[int] = None
        stud_price: Optional[int] = Field(None, alias="priceInStuds")
        average_price: Optional[int] = Field(None, alias="averagePrice")
        version: Optional[int] = None
        sales: Optional[int] = None
        favorites: Optional[int] = None

    async def owners(self):
        if self._owners == None:
            self._owners = await self.client.fetch_data(f"store/{self.id}/owners", base_url="https://api.polytoria.com/v1/")
        return self._owners
    
class Place: # /api/places /v1/api/places/{id}
    def __init__(self, data:dict, client):
        self.client = client

        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.creator = data["creator"]["name"]
        self.thumbnail = data.get("thumbnail")
        self.genre = data.get("genre")
        self.maxplayers = data.get("maxPlayers")
        self.isactive = data.get("isActive")
        self.istoolsenabled = data.get("isToolsEnabled")
        self.iscopyable = data.get("isCopyable")
        self.visits = data.get("visits")
        self.uniquevisits = data.get("uniqueVisits")
        self.playing = data.get("playing")
        self.rating = data.get("rating")
        self.accesstype = data.get("accessType")
        self.accessprice = data.get("accessPrice")
        self.createdat = data.get("createdAt")
        self.updatedat = data.get("updatedAt")

    def __repr__(self):
        return f""
    
class Guild: # /api/guilds/{id} /v1/guilds/{id}
    def __init__(self, data:dict, client):
        self.client = client

        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.creator = data["creator"]["name"]
        self.thumbnail = data.get("thumbnail")
        self.banner = data.get("banner")
        self.color = data.get("color")
        self.jointype = data.get("joinType")
        self.membercount = data.get("memberCount")
        self.vaultbalance = data.get("vaultBalance")
        self.isverified = data.get("isVerified")
        self.createdat = data.get("createdAt")

    def __repr__(self):
        return f""

class Forum: # /v1/forum
    def __init__(self, data:dict, client):
        self.client = client

    def __repr__(self):
        return f""