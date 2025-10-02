import requests
import time
import json
from pathlib import Path

# --- CONFIG ---
TOKEN = "7876971776:AAHvR0R6pOx_CFPEYmS3ewx3JtHchvfxqlA"
CHAT_ID = "-4963899081"
CHECK_INTERVAL = 30  # segundos entre checagens
ALERTS_FILE = Path("alerts.json")
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# --- Estado global ---
last_price = None  # guarda o último preço checado

# --- Helpers ---
def load_alerts():
    if not ALERTS_FILE.exists():
        example = [
            # alertas de teto/piso (vermelho)
            {"id": 1, "type": "above", "price": 116000, "active": True, "once": False},
            {"id": 2, "type": "below", "price": 108000, "active": True, "once": False}
        ]
        ALERTS_FILE.write_text(json.dumps(example, indent=2))
        return example
    return json.loads(ALERTS_FILE.read_text())

def save_alerts(alerts):
    ALERTS_FILE.write_text(json.dumps(alerts, indent=2))

def get_btc_price_usd():
    r = requests.get(COINGECKO_URL, timeout=10)
    r.raise_for_status()
    return r.json()["bitcoin"]["usd"]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    try:
        resp = requests.post(url, data=data, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print("Erro ao enviar Telegram:", e)

# --- Lógica de alertas ---
def check_alerts(alerts, price):
    global last_price
    triggered = False

    # Alerta amarelo: toda atualização
    if last_price is None or price != last_price:
        send_telegram(f"⚡ Atualização: BTC agora está {price} USD")
        triggered = True

    # Alertas vermelho: teto/piso
    for a in alerts:
        if not a.get("active", True):
            continue
        typ = a.get("type")
        target = a.get("price")

        if last_price is not None:
            if typ == "above" and last_price < target <= price:
                send_telegram(f"🚨 BTC ultrapassou {target} USD — preço atual: {price} USD. (alert id {a['id']})")
                triggered = True
                if a.get("once", True):
                    a["active"] = False
            elif typ == "below" and last_price > target >= price:
                send_telegram(f"🚨 BTC caiu abaixo de {target} USD — preço atual: {price} USD. (alert id {a['id']})")
                triggered = True
                if a.get("once", True):
                    a["active"] = False

    last_price = price
    return triggered

# --- Main loop ---
def main():
    print("Carregando alertas...")
    alerts = load_alerts()
    print(f"{len(alerts)} alertas carregados. Checando a cada {CHECK_INTERVAL}s.")
    while True:
        try:
            price = get_btc_price_usd()
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] BTC = {price} USD")
            changed = check_alerts(alerts, price)
            if changed:
                save_alerts(alerts)
        except Exception as err:
            print("Erro (ignorando):", err)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
