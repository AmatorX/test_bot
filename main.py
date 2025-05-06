# === MarketSignalBot/main.py ===
import asyncio
import logging
import datetime
import requests

TOKEN = "7225103105:AAEYfhrzoWdUJJD9i17SUN8BFP3EPcoGwPE"
CHAT_ID = "498990166"
SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "AVAXUSDT"]

async def get_signal(symbol):
    # Здесь эмуляция логики: сигнал случайный. Заменить подключением к TradingView API или Webhook позже.
    from random import choice
    direction = choice(["long", "short"])
    probability = round(50 + choice(range(0, 51)), 2)
    return f"📊 {symbol} сигнал: {direction.upper()} с вероятностью {probability}%"

async def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        logging.error(f"Ошибка при отправке в Telegram: {e}")

async def main_loop():
    while True:
        now = datetime.datetime.utcnow()
        if now.second == 45:
            for sym in SYMBOLS:
                signal = await get_signal(sym)
                await send_telegram(signal)
            await asyncio.sleep(1.5)
        else:
            await asyncio.sleep(0.5)

if __name__ == "__main__":
    logging.basicConfig(filename='market_bot_log.txt', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    asyncio.run(main_loop())
