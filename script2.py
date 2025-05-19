import requests
import json

# === Configurazione ===
MODEL_ID = "qwen3-8b"
API_URL = "http://127.0.0.1:1234/v1/chat/completions"
Prompt_File = "user_prompt.txt"

# === Carica la checklist ===
with open("checklist.json", "r") as f:
    checklist = json.load(f)["checklist"]

# Prompt di verifica completamento
def build_verify_prompt(prompt):
    return (
        "Verifica se la seguente checklist è completamente soddisfatta dal prompt utente. "
        "Rispondi SOLO con 'Yes' o 'No'.\n\n" +
        "Checklist:\n" + "\n".join(f"- {item}" for item in checklist) +
        "\n\nPrompt attuale:\n" + prompt
    )

# Prompt per richiedere informazioni mancanti
fill_prompt_base = (
    "La checklist non è completa. "
    "Chiedi all'utente una sola informazione mancante alla volta, "
    "proponendo, se necessario, dei valori di default e chiedendo conferma."
)

# Prompt per aggiornare il file con la risposta contestualizzata
def build_update_prompt(existing_prompt, user_response):
    return (
        "Integra la seguente risposta dell'utente nel prompt esistente, mantenendo il contesto e la formattazione originale. "
        "Il risultato deve essere un unico prompt coerente e completo.\n\n" +
        "Prompt esistente:\n" + existing_prompt +
        "\n\nRisposta utente:\n" + user_response
    )

while True:
    # === Rileggi il prompt aggiornato ===
    with open(Prompt_File, "r") as f:
        user_prompt = f.read().strip()

    # 1) Verifica completamento checklist
    verify_prompt = build_verify_prompt(user_prompt)
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
        # Genera riassunto per utente
        summary_prompt = (
            "Hai raccolto tutte le informazioni dalla checklist. "
            "Fornisci un breve riassunto schematizzato dei punti raccolti:"
        )
        resp_summary = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": MODEL_ID,
                "messages": [
                    {"role": "system", "content": summary_prompt},
                    {"role": "assistant", "content": user_prompt}
                ],
                "temperature": 0.5
            }
        )
        summary = resp_summary.json()["choices"][0]["message"]["content"].strip()
        print(f"\n📋 Riassunto raccolto:\n{summary}")

        # Riscrivi technical prompt
        rewrite_prompt = (
            "Rewrites the collected information in a clear, technical, schematic form for a multi-agent web dev system:\n" +
            user_prompt
        )
        resp_rewrite = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": MODEL_ID,
                "messages": [{"role": "system", "content": rewrite_prompt}],
                "temperature": 0.7
            }
        )
        final_prompt = resp_rewrite.json()["choices"][0]["message"]["content"].strip()
        with open("prompt_chatdev.txt", "w") as f:
            f.write(final_prompt)
        print("\n[✓] Prompt tecnico salvato in prompt_chatdev.txt")
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
    user_response = input("\n👤 Tu: ")

    # 3) Integra la risposta nel prompt esistente
    update_prompt = build_update_prompt(user_prompt, user_response)
    resp_update = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": MODEL_ID,
            "messages": [{"role": "system", "content": update_prompt}],
            "temperature": 0.7
        }
    )
    updated_prompt = resp_update.json()["choices"][0]["message"]["content"].strip()

    # Sovrascrivi il file del prompt con il contenuto aggiornato
    with open(Prompt_File, "w") as f:
        f.write(updated_prompt)

    print(f"[+] Prompt aggiornato e salvato su {Prompt_File}.")

# Fine del ciclo
    