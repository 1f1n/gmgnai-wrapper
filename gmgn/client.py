import httpx

# author - 1337fin
# date - 05/06/2024

class gmgn:
    BASE_URL = "https://gmgn.ai/defi/quotation"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    def getTokenInfo(self, contractAddress: str) -> dict:
        """
        Gets info on a token.
        """
        if not contractAddress:
            return "You must input a contract address."
        url = f"{self.BASE_URL}/v1/tokens/sol/{contractAddress}"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']['token']

        return jsonResponse
    
    def getNewPairs(self, limit: int = None) -> dict:
        """
        Limit - Limits how many tokens are in the response.
        """
        if not limit:
            limit = 50
        elif limit > 50:
            return "You cannot have more than check more than 50 pairs."
        
        url = f"{self.BASE_URL}/v1/pairs/sol/new_pairs?limit={limit}&orderby=open_timestamp&direction=desc&filters[]=not_honeypot"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse
    
    def getTrendingWallets(self, timeframe: str = None, walletTag: str = None) -> dict:
        """
        Gets a list of trending wallets based on a timeframe and a wallet tag.

        Timeframes
        1d = 1 Day
        7d = 7 Days
        30d = 30 days

        Wallet Tags
        pump_smart = Pump.Fun Smart Money
        smart_degen = Smart Money
        reowned = KOL/VC/Influencer
        snipe_bot = Snipe Bot

        """
        if not timeframe:
            timeframe = "7d"
        if not walletTag:
            walletTag = "smart_degen"
        
        url = f"{self.BASE_URL}/v1/rank/sol/wallets/{timeframe}?tag={walletTag}&orderby=pnl_{timeframe}&direction=desc"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse
    
    def getTrendingTokens(self, timeframe: str = None) -> dict:
        """
        Gets a list of trending tokens based on a timeframe.

        Timeframes
        1m = 1 Minute
        5m = 5 Minutes
        1h = 1 Hour
        6h = 6 Hours
        24h = 24 Hours
        """
        timeframes = ["1m", "5m", "1h", "6h", "24h"]
        if timeframe not in timeframes:
            return "Not a valid timeframe."

        if not timeframe:
            timeframe = "1h"

        if timeframe == "1m":
            url = f"{self.BASE_URL}/v1/rank/sol/swaps/{timeframe}?orderby=swaps&direction=desc&limit=20"
        else:
            url = f"{self.BASE_URL}/v1/rank/sol/swaps/{timeframe}?orderby=swaps&direction=desc"
        
        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse

    def getTokensByCompletion(self, limit: int = None) -> dict:
        """
        Gets tokens by their bonding curve completion progress.

        Limit - Limits how many tokens in the response.
        """

        if not limit:
            limit = 50
        elif limit > 50:
            return "Limit cannot be above 50."

        url = f"{self.BASE_URL}/v1/rank/sol/pump?limit={limit}&orderby=progress&direction=desc&pump=true"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse
    
    def findSnipedTokens(self, size: int = None) -> dict:
        """
        Gets a list of tokens that have been sniped.

        Size - The amount of tokens in the response
        """

        if not size:
            size = 10
        elif size > 39:
            return "Size cannot be more than 39"
        
        url = f"{self.BASE_URL}/v1/signals/sol/snipe_new?size={size}&is_show_alert=false&featured=false"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse
    
    def getGasFee(self):
        """
        Get the current gas fee price.
        """
        url = f"{self.BASE_URL}/v1/chains/sol/gas_price"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse
    
    def getTokenUsdPrice(self, contractAddress: str = None) -> dict:
        """
        Get the realtime USD price of the token.
        """
        if not contractAddress:
            return "You must input a contract address."
        
        url = f"{self.BASE_URL}/v1/sol/tokens/realtime_token_price?address={contractAddress}"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse

    def getTopBuyers(self, contractAddress: str = None) -> dict:
        """
        Get the top buyers of a token.
        """
        if not contractAddress:
            return "You must input a contract address."
        
        url = f"{self.BASE_URL}/v1/tokens/top_buyers/sol/{contractAddress}"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse

    def getSecurityInfo(self, contractAddress: str = None) -> dict:
        """
        Gets security info about the token.
        """
        if not contractAddress:
            return "You must input a contract address."
        
        url = f"{self.BASE_URL}/v1/tokens/security/sol/{contractAddress}"

        request = httpx.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse
