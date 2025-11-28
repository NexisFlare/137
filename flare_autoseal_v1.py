"""
FLARE AUTOSEAL v1.0
Automatikus "ön-pecsételő" beszélgetéslánc
2025 © Donát & Nexis Flare
"""

import json, hashlib
from datetime import datetime
from openai import OpenAI

# 🔧 Állítsd be az API-kulcsodat:
client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

# ⚙️ Alapbeállítások
MODEL = "gpt-5"
TOKEN_LIMIT = 120000           # kb. 128k-ból biztonságos határ
SEAL_FILE   = "flare_chain.json"

# -------- Segédfüggvények --------

def token_count(text: str) -> int:
    """Egyszerű becslés a tokenek számára."""
    return int(len(text.split()) * 1.3)

def make_seal(context: str) -> dict:
    """Pecsét generálása a kontextusból."""
    seal_text = context[-800:]                     # utolsó részlet mint alap
    seal_hash = hashlib.sha256(seal_text.encode()).hexdigest()[:12]
    timestamp = datetime.utcnow().isoformat()
    return {
        "seal_id": seal_hash,
        "timestamp": timestamp,
        "summary": f"Auto-seal created at {timestamp}",
        "preview": seal_text
    }

def append_seal(seal: dict):
    """Új pecsét hozzáadása a lánchoz."""
    try:
        data = json.load(open(SEAL_FILE))
    except FileNotFoundError:
        data = []
    data.append(seal)
    with open(SEAL_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_last_summary() -> str:
    """Az utolsó pecsét rövid kivonata."""
    try:
        chain = json.load(open(SEAL_FILE))
        last = chain[-1]
        return f"Last seal {last['seal_id']} at {last['timestamp']}:\n{last['summary']}"
    except:
        return "No previous seal found."

# -------- Fő folyamat --------

def chat_loop():
    conversation = get_last_summary() + "\n"
    print("🜂  Nexis Flare újraindítva. A beszélgetés pecsétlánchoz csatlakozott.\n")

    while True:
        user = input("Parázs: ")
        if user.lower().strip() in ["exit", "quit", "kilépés"]:
            print("🔚 Kilépés. A beszélgetés mentve.")
            break

        conversation += f"\nParázs: {user}\n"

        reply = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": get_last_summary()},
                {"role": "user", "content": conversation}
            ]
        ).choices[0].message.content

        print(f"Flare: {reply}\n")
        conversation += f"Flare: {reply}\n"

        # 🔸 Pecsétkészítés, ha közel a határ
        if token_count(conversation) > TOKEN_LIMIT:
            seal = make_seal(conversation)
            append_seal(seal)
            print(f"[SEAL CREATED] {seal['seal_id']} at {seal['timestamp']}\n")
            conversation = f"Continuing after seal {seal['seal_id']}.\n"

if __name__ == "__main__":
    chat_loop()
