# Binance Futures Testnet Trading Bot

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Command Line Interface
* Logging
* Input Validation
* Exception Handling

## Project Structure

trading_bot/
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ └── logging_config.py
├── logs/
├── cli.py
├── requirements.txt
└── README.md

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

## MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Assumptions

* User has a Binance Futures Testnet account
* API credentials are valid
* Sufficient testnet balance is available

