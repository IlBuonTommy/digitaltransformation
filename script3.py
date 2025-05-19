import requests
import json
import re

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
    "Chiedi all'utente le informazioni mancanti dalla checklist, confrontandole con il prompt attuale, "
    "proponendo, se necessario, dei valori di default e chiedendo conferma."
)

# Prompt per aggiornare il file con la risposta contestualizzata
def build_update_prompt(existing_prompt, user_response, answer):
    return (
        "Integra i requisiti elencati dall'utente nella sua risposta nel prompt esistente, mantenendo il contesto originale. "
        "Il risultato deve essere un unico prompt coerente e completo. Attieniti alla checklist, ovvero il prompt aggiornato deve contenere anche i nuovi parametri definiti dall'utente e consoni alla checklist se non erano stati definiti nel prompt utente."
        "Se i valori di default della risposta del modello sono stati confermati nella risposta dell'utente, includili nel prompt aggiornato.\n\n" +
        "Prompt esistente:\n" + existing_prompt +
        "\n\nRisposta utente:\n" + user_response +
        "\n\nChecklist:\n" + "\n".join(f"- {item}" for item in checklist) +
        "\n\nRisposta della verifica:\n" + answer
    )

while True:
    # === Rileggi il prompt aggiornato ===
    with open(Prompt_File, "r", encoding="utf-8") as f:
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
    try:
        answer = resp_check.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Errore nella risposta dell'API (verifica checklist):", e)
        print("Risposta API:", resp_check.text)
        break
 
    raw = resp_check.json()["choices"][0]["message"]["content"]
    # rimuovo tutto ciò che sta tra <...>
    clean = re.sub(r"<[^>]*>", "", raw).strip().lower()

    if clean == "yes":
    #if resp_check.json()["choices"][0]["message"]["content"].strip().lower() == "yes":
        print("✅ Checklist completata con successo!")
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
                "temperature": 0.2
            }
        )
        try:
            summary = resp_summary.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print("Errore nella risposta dell'API (riassunto):", e)
            print("Risposta API:", resp_summary.text)
            break
        print(f"\n📋 Riassunto raccolto:\n{summary}")

        # Riscrivi technical prompt
        rewrite_prompt = (
            "Riscrivi le informazioni raccolte in una forma tecnica, chiara e schematica, adatta a un sistema multi-agente per lo sviluppo web:\n" +
            user_prompt
        )
        resp_rewrite = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": MODEL_ID,
                "messages": [{"role": "system", "content": rewrite_prompt}],
                "temperature": 0.2
            }
        )
        try:
            final_prompt = resp_rewrite.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print("Errore nella risposta dell'API (rewrite):", e)
            print("Risposta API:", resp_rewrite.text)
            break

        if final_prompt:
            with open("prompt_chatdev.txt", "w", encoding="utf-8") as f:
                f.write(final_prompt)
            print("\n[✓] Prompt tecnico salvato in prompt_chatdev.txt")
        else:
            print("Attenzione: il prompt tecnico generato è vuoto!")
        break
    else:
        print("❌ Checklist non completata. Procedo con la richiesta di chiarimenti.")
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
                "temperature": 0.2
            }
        )
        try:
            question = resp_fill.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print("Errore nella risposta dell'API (fill):", e)
            print("Risposta API:", resp_fill.text)
            break
        print(f"\n🤖 Domanda per utente:\n{question}")

        # Ricevi risposta utente
        user_response = input("\n👤 Tu: ")

        # 3) Integra la risposta nel prompt esistente
        update_prompt = build_update_prompt(user_prompt, user_response, answer)
        resp_update = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": MODEL_ID,
                "messages": [{"role": "system", "content": update_prompt}],
                "temperature": 0.2
            }
        )
        try:
            updated_prompt = resp_update.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print("Errore nella risposta dell'API (update):", e)
            print("Risposta API:", resp_update.text)
            break

    # Sovrascrivi il file del prompt con il contenuto aggiornato
    with open(Prompt_File, "w", encoding="utf-8") as f:
        f.write(updated_prompt)

    print(f"[+] Prompt aggiornato e salvato su {Prompt_File}.")
#fine del ciclo
