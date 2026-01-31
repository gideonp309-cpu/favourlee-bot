import hashlib
import random
import time
from telegram.helpers import escape_markdown

class SimulationEngine:
    def __init__(self):
        self.balance = 24500.50
        # Realistic 2026 Price
        self.btc_price = 82450.75 

    def get_market_data(self):
        # Adds a bit of random "live" movement
        fluctuation = random.uniform(-50.5, 50.5)
        return self.btc_price + fluctuation

    def generate_tx_hash(self):
        raw_str = f"TX-{random.random()}-{time.time()}"
        return hashlib.sha256(raw_str.encode()).hexdigest()

    def generate_access_code(self):
        # 2026 security-style format
        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        code = "".join(random.choices(chars, k=8))
        return f"VX-{code[:4]}-{code[4:]}"

    def get_scan_link(self, tx_hash):
        return f"https://www.blockchain.com/explorer/transactions/btc/{tx_hash}"

    def safe(self, text):
        """Escapes text for Telegram MarkdownV2"""
        return escape_markdown(str(text), version=2)
