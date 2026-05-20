# Binance Futures Testnet Trading Bot

This project is a simple command-line trading bot built using Python and the Binance Futures Testnet API. The application allows users to place MARKET and LIMIT orders on Binance USDT-M Futures in a structured and reusable way.

The project was developed as part of a Python developer assessment task and focuses on clean architecture, input validation, logging, and proper exception handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Support for BUY and SELL positions
- Command-line interface using argparse
- Input validation
- Logging of API requests, responses, and errors
- Exception handling for invalid input and API/network failures
- Binance Futures Testnet integration

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── bot.log
│
├── cli.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore

Setup Instructions

1. Clone the Repository
git clone <repository-url>
cd trading_bot
2. Create Virtual Environment
Windows

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

Environment Variables

Create a .env file in the root directory and add your Binance Futures Testnet API credentials.

BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
Binance Futures Testnet

This project uses the Binance Futures Testnet environment and does not place real trades.

Testnet URL:

https://testnet.binancefuture.com

Usage
Place a MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Place a LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
Example Output
===== ORDER REQUEST =====

Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

===== ORDER RESPONSE =====

Order ID: 13168218522
Status: NEW
Executed Qty: 0.0000
Average Price: 0.00

SUCCESS: Order placed successfully
Logging

All API requests, responses, and errors are logged automatically in:

logs/bot.log
Error Handling

The application handles:

Invalid order side
Invalid order type
Invalid quantity
Missing price for LIMIT orders
Binance API exceptions
Network-related exceptions
Technologies Used
Python 3
python-binance
python-dotenv
argparse
logging
Notes
This project is intended for Binance Futures Testnet only.
Test USDT balance is required for order placement.
API keys should never be shared publicly.


The goal of this project is to demonstrate API integration, structured Python code, logging, validation, and CLI-based order execution using Binance Futures Testnet.