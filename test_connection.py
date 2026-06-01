from bot.client import client

try:
    balance = client.futures_account_balance()
    print("Connected successfully!")
    print(balance[:2])
except Exception as e:
    print("Error:", e)
