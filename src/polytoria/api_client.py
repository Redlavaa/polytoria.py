from curl_cffi.requests import AsyncSession

class APIClient:
    def __init__(self, browser: str = "chrome", base_url:str = None):
        self.base_url = base_url or "https://api.polytoria.com/v1"
        self.browser = browser

    async def fetch_data(self, endpoint:str, base_url:str = None, params: dict = None) -> dict:
        url = f"{self.base_url}/{endpoint}"

        async with AsyncSession(impersonate=self.browser) as session:
            try:
                response = await session.get(
                    url,
                    params=params,
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                print(f"API Request failed: {e}")
                raise