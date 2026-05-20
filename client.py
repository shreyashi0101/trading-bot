from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

client = Client(
    API_KEY,
    API_SECRET,
    testnet=True
)

# Correct Futures Testnet URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"