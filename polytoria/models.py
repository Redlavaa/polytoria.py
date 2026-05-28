from .api_client import APIClient

class User:
    def __init__(self, data:dict, client):
        self.client = client

        self.id = data.get("id")
        self.username = data.get("username")
        self.description = data.get("description")
        self.thumbnail = data.get("thumbnail")
        self.avatar = self.thumbnail.get("avatar")
        self.icon = self.thumbnail.get("icon")
        self.playing = data.get("playing")
        self.networth = data.get("netWorth")
        self.placevisits = data.get("placeVisits")
        self.forumposts = data.get("forumPosts")
        self.assetSales = data.get("assetSales")
        self.membershipType = data.get("membershipType")
        self.istaff = data.get("isStaff")
        self.role = data.get("userRoleClass") # for anyone wondering this shows the role of the user like user, admin, item designer
        self.joindate = data.get("registeredAt")
        self.lastseen = data.get("lastSeenAt")

        self._linked = None

    async def linked(self):
        if self._linked == None:
            self._linked = await self.client.fetch_data(f"users/{self.id}/linked", base_url="https://api.polytoria.com/v1/")
        return self._linked


    def __repr__(self): # used for debugging
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
        self.creator = data["creator"]["name"]
        self.thumbnail = data.get("thumbnail")
        self.price = data.get("price")
        self.studprice = data.get("priceInStuds")
        self.averageprice = data.get("averagePrice")
        self.version = data.get("version") # gets if its 2.0 or 1.0 I think?
        self.sales = data.get("sales")
        self.favorites = data.get("favorites")

        self._owners = None

    async def owners(self):
        if self._owners == None:
            self._owners = await self.client.fetch_data(f"store/{self.id}/owners", base_url="https://api.polytoria.com/v1/")
        return self._owners


    def __repr__(self):
        return f"id={self.id} name={self.name} description={self.description}"
    
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
        self.active = data.get("isActive")
        self.toolsenabled = data.get("isToolsEnabled")
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

class user2id:
    def __init__(self, data:dict, client):
        self.client = client

        self.id = data.get("id")

    def __repr__(self):
        return f""
