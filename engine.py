import random

class SimulationEngine:
    def __init__(self):
        # Initial simulated state
        self.balance = 10000.0  # Simulated USDT
        self.portfolio = {}     # { "BTC": 0.5 }

    def get_simulated_price(self, ticker):
        # Mock price generator
        prices = {"BTC": 45000, "ETH": 2500, "SOL": 100}
        return prices.get(ticker.upper(), 1.0) * (1 + random.uniform(-0.01, 0.01))

    def get_wallet_address(self):
        return "0xSimulated_" + "7b2e...9a1c"
