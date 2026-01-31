import hashlib
import random
import time

class SimulationEngine:
    def __init__(self):
        self.balance = 24500.50
        self.ticker = "BTC"

    def generate_tx_hash(self):
        # Generates a realistic 64-character BTC transaction hash
        raw_str = f"TX-{random.random()}-{time.time()}"
        return hashlib.sha256(raw_str.encode()).hexdigest()

    def generate_access_code(self):
        # 2026-style secure simulated access key
        prefix = random.choice(["X-VOID", "Z-CORE", "ALPHA"])
        suffix = random.randint(1000, 9999)
        return f"{prefix}-{suffix}-TXN"

    def get_scan_link(self, tx_hash):
        return f"https://www.blockchain.com/explorer/transactions/btc/{tx_hash}"
