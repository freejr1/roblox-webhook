# rofrom flask import Flask, request
import requests, datetime, os

app = Flask(__name__)

# ⚠️ Configure estas variáveis no painel da Render (ou em .env local)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = os.getenv("CHAT_ID")   # exemplo: -1002607184549

def send_to_telegram(text: str) -> None:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

@app.route("/robloxhook", methods=["POST"])
def roblox_hook():
    data = request.json or {}
    username  = data.get("username", "Desconhecido")
    timestamp = data.get("timestamp") or datetime.datetime.utcnow().isoformat()

    msg = (
        "🖥️ *Script executado*\n"
        f"👤 Usuário: `{username}`\n"
        f"🕒 Data/Hora (UTC): `{timestamp}`"
    )
    # Telegram ignora markdown se não vier como parse_mode, então texto simples:
    send_to_telegram(msg.replace("*", "").replace("`", ""))

    return "OK", 200

if __name__ == "__main__":
    # Render detecta a porta pelo ambiente; localmente use 5000
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)blox-webhook
