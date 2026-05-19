from src.api_client import APIClient

class User:
    def __init__(self, data:dict, client):
        self.client = client

        self.id = data.get("id")
        self.username = data.get("username")
        self.description = data.get("description")
        self.thumbnail = data.get("thumbnail")
        if isinstance(self.thumbnail, dict):
            self.avatar = self.thumbnail.get("avatar")
            self.icon = self.thumbnail.get("icon")
        else:
            self.avatar = None
            self.icon = None
        self.playing = data.get("playing")
        self.networth = data.get("netWorth")
        self.placevisits = data.get("placeVisits")
        self.forumposts = data.get("forumPosts")
        self.assetSales = data.get("assetSales")
        self.membershipType = data.get("membershipType")
        self.istaff = data.get("isStaff")
        self.userroleclass = data.get("userRoleClass")
        self.joindate = data.get("registeredAt")
        self.lastseen = data.get("lastSeenAt")

    def __repr__(self):
        return f"id={self.id} username={self.username} description={self.description}"
    
class Item:
    def __init__(self, data:dict, client):
        self.client = client

        self.id = data.get("id")
        self.type = data.get("type")
        self.accessorytype = data.get("accessoryType")
        self.name = data.get("name")
        self.description = data.get("description")
        self.tags = data.get("tags", []) or []
        creator = data.get("creator")
        self.creator = creator if isinstance(creator, dict) else {}
        self.creatorname = self.creator.get("name")
        self.creatorid = self.creator.get("id")
        self.thumbnail = data.get("thumbnail")
        self.price = data.get("price")
        self.studprice = data.get("priceInStuds")
        self.averageprice = data.get("averagePrice")
        self.version = data.get("version")
        self.sales = data.get("sales")
        self.favorites = data.get("favorites")

        self._owners = None

    async def owners(self):
        if self._owners == None:
            self._owners = await self.client.fetch_data(f"store/{self.id}/owners", base_url="https://api.polytoria.com/v1/")
        return self._owners


    def __repr__(self):
        return f"id={self.id} name={self.name} description={self.description}"