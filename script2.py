import requests
import json

# === Configurazione ===
MODEL_ID = "qwen3-8b"
API_URL = "http://127.0.0.1:1234/v1/chat/completions"

# === Carica il prompt iniziale dell’utente ===
with open("user_prompt.txt", "r") as f:
    user_prompt = f.read().strip()

# === Carica la checklist ===
with open("checklist.json", "r") as f:
    checklist = json.load(f)["checklist"]

# Prompt di verifica completamento
verify_prompt = (
    "Verifica se la seguente checklist è completamente soddisfatta dal prompt utente. "
    "Rispondi SOLO con 'Yes' o 'No'.\n\n" +
    "Checklist:\n" + "\n".join(f"- {item}" for item in checklist) +
    "\n\nPrompt attuale:\n" + user_prompt
)

# Prompt per richiedere informazioni mancanti
fill_prompt_base = (
    "La checklist non è completa. "
    "Chiedi all'utente una sola informazione mancante alla volta, "
    "proponendo, se necessario, dei valori di default e chiedendo conferma."
)

while True:
    # 1) Verifica completamento checklist
    resp_check = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": MODEL_ID,
            "messages": [{"role": "system", "content": verify_prompt}],
            "temperature": 0.0
        }
    )
    answer = resp_check.json()["choices"][0]["message"]["content"].strip()
    print(f"🤖 Verifica checklist: {answer}")

    if answer.lower().startswith("yes"):
        # Tutto completo: riscrivi il prompt in forma tecnica
        rewrite_system = (
            "Checklist completed.\n" +
            "Rewrites the user prompt in a clearer, more technical form for a multi-agent web dev system:\n" +
            user_prompt
        )
        resp_rewrite = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": MODEL_ID,
                "messages": [{"role": "system", "content": rewrite_system}],
                "temperature": 0.7
            }
        )
        final = resp_rewrite.json()["choices"][0]["message"]["content"]
        with open("prompt_chatdev.txt", "w") as f:
            f.write(final)
        print("\n[✓] Prompt finale salvato in prompt_chatdev.txt")
        break

    # 2) Richiesta di chiarimento o default
    fill_prompt = (
        fill_prompt_base + "\n\n" +
        "Checklist:\n" + "\n".join(f"- {item}" for item in checklist) +
        "\n\nPrompt attuale:\n" + user_prompt
    )
    resp_fill = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": MODEL_ID,
            "messages": [{"role": "system", "content": fill_prompt}],
            "temperature": 0.7
        }
    )
    question = resp_fill.json()["choices"][0]["message"]["content"].strip()
    print(f"\n🤖 Domanda per utente:\n{question}")

    # Ricevi risposta utente
    user_input = input("\n👤 Tu: ")
    # Aggiorna il prompt utente
    user_prompt += "\n" + user_input

    # Ricostruisci verify_prompt con il prompt aggiornato
    verify_prompt = (
        "Verifica se la seguente checklist è completamente soddisfatta dal prompt utente. "
        "Rispondi SOLO con 'Yes' o 'No'.\n\n" +
        "Checklist:\n" + "\n".join(f"- {item}" for item in checklist) +
        "\n\nPrompt attuale:\n" + user_prompt
    )
