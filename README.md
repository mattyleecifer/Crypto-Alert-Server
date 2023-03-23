# Crypto-Alert-Server
A small server that runs a script to check binance prices and sends an alert through a Telegram bot when the price crosses the alert line

# Usage
- Set up a Telegram bot by texting @BotFather and following the instructions. You will also need a Binance API key. 
  - Enter your Telegram/Binance keys into alert.py where it says 'telegramkey', 'apikey', and 'secretkey'
- Install Flask and the python-binance package
- To run the server just run server.py
- To connect to the page just got to <yourip>:8089/alert eg 127.0.0.1:8089/alert

# Why
Tradingview only lets me have one alert for free. This way I can just set up a small server (AWS free tier) and get unlimited alerts.
