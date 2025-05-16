import requests
import json
import shutil
import subprocess

# === Configurazione ===
MODEL_ID = "qwen3-8b"
API_URL = "http://127.0.0.1:1234/v1/chat/completions"

# === Carica il prompt iniziale dell’utente ===
with open("user_prompt.txt", "r") as f:
    user_prompt = f.read()

# === Carica la checklist ===
with open("checklist.json", "r") as f:
    checklist = json.load(f)["checklist"]

# === Prompt iniziale del sistema ===
system_prompt = (
    "You are a web project analyst. "
    "Check if all the following items are present in the user prompt. "
    "If not, ask questions to complete missing points or suggest defaults, and ask for confirmation. "
    "Once everything is complete, reply with 'Checklist completed.' and rewrite the prompt in a clearer, more technical form for a multi-agent web dev system."
)

# === Cronologia messaggi ===
messages = [{"role": "system", "content": system_prompt}]

# Costruisci messaggio iniziale
initial_message = (
    "Checklist:\n" + "\n".join(f"- {item}" for item in checklist) +
    f"\n\nUser prompt:\n{user_prompt}"
)
messages.append({"role": "user", "content": initial_message})


# === Loop fino a completamento checklist ===
while True:
    # Invia richiesta a LM Studio
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": MODEL_ID,
            "messages": messages,
            "temperature": 0.7
        }
    )

    # Estrai risposta
    reply = response.json()["choices"][0]["message"]["content"]
    print("\n🤖 LM Studio:\n" + reply)

    # Se la checklist è completata, esci dal loop
    if "Checklist completed" in reply:
        # Estrai e salva il prompt finale
        with open("prompt_chatdev.txt", "w") as f:
            f.write(reply)
        print("\n[✓] Prompt finale salvato in prompt_chatdev.txt")
        break

    # Ottieni input dell’utente
    user_reply = input("\n👤 Tu: ")
    messages.append({"role": "assistant", "content": reply})
    messages.append({"role": "user", "content": user_reply})

