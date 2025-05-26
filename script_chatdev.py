import requests
import json
import subprocess
import shlex
import os
import re

# === Configurazione ===
MODEL_ID = "qwen3-8b"
API_URL = "http://127.0.0.1:1234/v1/chat/completions"
DATI_UTENTE_PATH = "dati_utente.txt"
PROMPT_CHATDEV_PATH = "prompt_chatdev.txt"
CHATDEV_RUN_FILE = "run.py"
PYTHON_EXECUTABLE = "python3"  # Cambia in "python3" o percorso completo se necessario
PROJECT_NAME = "progetto_sito_generato" # Nome di default per il progetto ChatDev

def chatdev_invoke(final_prompt: str, project_name: str = PROJECT_NAME):
    """
    Invoca chat_dev (run.py) con il prompt fornito.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    chatdev_script_path = CHATDEV_RUN_FILE
    if not os.path.isabs(chatdev_script_path):
        chatdev_script_path = os.path.join(script_dir, chatdev_script_path)

    chatdev_base_dir = os.path.dirname(chatdev_script_path)
    if not chatdev_base_dir:
        chatdev_base_dir = script_dir
    
    # Sanitize project_name
    project_name_slug = "".join(c if c.isalnum() or c in ['_','-'] else '_' for c in project_name.replace(' ', '_')).lower()
    if not project_name_slug: # Fallback se il nome diventa vuoto
        project_name_slug = "progetto_default"


    cmd = [
        PYTHON_EXECUTABLE,
        chatdev_script_path,
        "--task", final_prompt,
        "--name", project_name_slug
    ]
    try:
        print(f"[CHATDEV] Invocazione: {' '.join(shlex.quote(c) for c in cmd)}")
        print(f"[CHATDEV] Directory di lavoro per ChatDev: {chatdev_base_dir}")
        
        #process = subprocess.Popen(
        #    cmd,
        #    stdout=subprocess.PIPE,
        #    stderr=subprocess.PIPE,
        #    text=True,
        #   creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0,
        #    cwd=chatdev_base_dir
        #)
        process = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"[CHATDEV] Processo ChatDev avviato con PID: {process.pid}. Monitorare la console per output e completamento.")
        return True, f"Processo completato con codice {process.returncode} per il progetto '{project_name_slug}'."
        # Se vuoi attendere e catturare l'output (bloccherà lo script):
        # stdout, stderr = process.communicate()
        # print(f"[CHATDEV] Output:\n{stdout}")
        # if stderr:
        #     print(f"[CHATDEV] Errori (stderr):\n{stderr}")
        #return True, f"Processo ChatDev avviato con PID {process.pid} per il progetto '{project_name_slug}'."
    except FileNotFoundError:
        error_message = f"[CHATDEV] File '{chatdev_script_path}' non trovato o '{PYTHON_EXECUTABLE}' non installato/nel PATH."
        print(error_message)
        return False, error_message
    except subprocess.CalledProcessError as e:
        print(f"[✗] Errore durante l'invocazione di chat_dev (rc={e.returncode}):")
        print(e.stdout)
        print(e.stderr)
    except Exception as e:
        error_message = f"[CHATDEV] Errore generico durante l'invocazione di ChatDev: {str(e)}"
        print(error_message)
        return False, error_message
    # Fallback: nel caso improbabile in cui nessun return sia stato eseguito
    return False, "[CHATDEV] Return fallback: chatdev_invoke non ha restituito valori."

def main():
    # 1. Leggi dati_utente.txt
    try:
        with open(DATI_UTENTE_PATH, "r", encoding="utf-8") as f:
            dati_utente_content = f.read()
        if not dati_utente_content.strip():
            print(f"[AVVISO] Il file '{DATI_UTENTE_PATH}' è vuoto. Impossibile procedere.")
            return
        print(f"[INFO] Contenuto di '{DATI_UTENTE_PATH}' letto.")
    except FileNotFoundError:
        print(f"[ERRORE] File '{DATI_UTENTE_PATH}' non trovato. Crealo prima con il form web.")
        return
    except Exception as e:
        print(f"[ERRORE] Errore durante la lettura di '{DATI_UTENTE_PATH}': {e}")
        return

    # Estrai nome_sito da dati_utente.txt per usarlo come project_name
    current_project_name = PROJECT_NAME # Default
    for line in dati_utente_content.splitlines():
        if line.lower().startswith("nome_sito:"):
            parsed_name = line.split(":", 1)[1].strip()
            if parsed_name:
                current_project_name = parsed_name
                break
    
    # 2. Crea il prompt per LM Studio
    rewrite_prompt_text = (
        "Riscrivi le informazioni raccolte in una forma tecnica, chiara e schematica, adatta a un sistema multi-agente per lo sviluppo web.\n\n" +
        dati_utente_content
    )
    print("[INFO] Prompt per LM Studio preparato.")

    # 3. Invia il prompt all'API di LM Studio
    try:
        print(f"[API] Invio richiesta a LM Studio (Modello: {MODEL_ID})...")
        api_payload = {
            "model": MODEL_ID,
            "messages": [{"role": "user", "content": rewrite_prompt_text}],
            "temperature": 0.2,
        }
        
        api_response = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json=api_payload,
            timeout=180 
        )
        api_response.raise_for_status()
        
        response_json = api_response.json()
        
        if not response_json.get("choices") or \
           not response_json["choices"][0].get("message") or \
           not response_json["choices"][0]["message"].get("content"):
            print("[API ERRORE] La risposta dell'API non contiene il contenuto atteso.")
            error_detail = response_json.get("error", {}).get("message", "Struttura risposta API inattesa.")
            print(f"Dettaglio: {error_detail}")
            return
            
        technical_prompt = response_json["choices"][0]["message"]["content"].strip()
        # Rimuovi automaticamente eventuali sezioni tra <think> e </think>
        technical_prompt = re.sub(r'<think>.*?</think>', '', technical_prompt, flags=re.DOTALL).strip()
        
        if not technical_prompt:
            print("[API ERRORE] Il prompt tecnico generato dall'API è vuoto. Impossibile procedere.")
            return
        print("[API] Prompt tecnico ricevuto da LM Studio.")

    except requests.exceptions.Timeout:
        print(f"[API ERRORE] Timeout durante la richiesta a LM Studio.")
        return
    except requests.exceptions.RequestException as e:
        print(f"[API ERRORE] Errore di connessione/richiesta API LM Studio: {e}")
        return
    except Exception as e:
        import traceback
        tb_str = traceback.format_exc()
        print(f"[ERRORE] Errore generico durante l'interazione con LM Studio: {e}\n{tb_str}")
        return

    # 4. Salva il prompt tecnico in prompt_chatdev.txt
    try:
        with open(PROMPT_CHATDEV_PATH, "w", encoding="utf-8") as f:
            f.write(technical_prompt)
        print(f"[INFO] Prompt tecnico salvato in '{PROMPT_CHATDEV_PATH}'.")
    except Exception as e:
        print(f"[ERRORE] Errore durante il salvataggio di '{PROMPT_CHATDEV_PATH}': {e}")
        return

    # 5. Esegui ChatDev con il nuovo prompt
    print(f"[INFO] Avvio di ChatDev per il progetto basato su: '{current_project_name}'...")
    chatdev_success, chatdev_message = chatdev_invoke(technical_prompt, current_project_name)

    if chatdev_success:
        print(f"[INFO] {chatdev_message}")
    else:
        print(f"[ERRORE] {chatdev_message}")

if __name__ == "__main__":
    main()