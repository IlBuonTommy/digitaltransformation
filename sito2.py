# sito.py
from flask import Flask, render_template_string, request, redirect, url_for
import webbrowser

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>Wizard Creazione Sito</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: Arial, sans-serif; background: #333333; color: #f0f0f0; padding: 2rem; } /* Sfondo grigio scuro, testo chiaro */
    .container { background: #444444; color: #f0f0f0; max-width: 600px; margin: auto; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    .step { display: none; }
    .step.active { display: block; }
    .buttons { margin-top: 1.5rem; display: flex; justify-content: space-between; }
    input, select, textarea { width: 100%; padding: .5rem; margin: .5rem 0 1rem; border: 1px solid #666; border-radius: 4px; background-color: #555; color: #f0f0f0; }
    /* Override specifico per il menu a tendina: renderlo bianco, con testo scuro e bordi arrotondati */
    select {
      background-color: #ffffff;
      color: #333333;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    input[type="radio"] {
      width: auto;
      margin-right: 5px;
      vertical-align: middle;
    }
    label { font-weight: bold; display: block; margin-bottom: 0.5rem; }
    input[type="color"] {
        vertical-align: middle;
        margin-right: 5px;
        padding: 0;
        height: 25px;
        width: 40px;
        border: 1px solid #666; /* Bordo per visibilità su sfondo scuro */
    }
    .color-preview {
      display: inline-block;
      width: 22px;
      height: 22px;
      border: 1px solid #888; /* Bordo per visibilità */
      vertical-align: middle;
      margin-right: 5px;
    }
    label > span {
        vertical-align: middle;
    }
    button { background-color: #5cb85c; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
    button:disabled { background-color: #777; cursor: not-allowed; }
    h1, h2 { color: #f0f0f0; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Creazione Sito Web</h1>
    <form id="wizardForm" method="post" action="/">
      <!-- STEP 1 -->
      <div class="step active" id="step1">
        <h2>Step 1: Dati generali</h2>
        <label>Nome sito (obbligatorio)<input type="text" name="nome_sito" required></label>
        <label>Target di riferimento<input type="text" name="target">
        <label>Tema/Argomenti (obbligatorio)<textarea name="tema" rows="2" required></textarea></label>
        
        <label for="colore_sfondo_input">Colore sfondo
          <input type="color" name="colore_sfondo" id="colore_sfondo_input" value="#ffffff">
        </label>
        
        <label for="colore_testo_input">Colore testo
          <input type="color" name="colore_testo" id="colore_testo_input" value="#000000">
        </label>
        
        <label>Stile del sito
          <select name="stile">
            <option value="generico" selected>Generico</option>
            <option value="moderno">Moderno</option>
            <option value="creativo">Creativo</option>
            <option value="minimal">Minimal</option>
            <option value="corporate">Corporate</option>
          </select>
        </label>
      </div>
      <!-- STEP 2 -->
      <div class="step" id="step2">
        <h2>Step 2: Struttura pagine</h2>
        <label><input type="radio" name="mode" value="single" checked> Monopagina</label>
        <label><input type="radio" name="mode" value="multi"> Multipagina</label>
        
        <div id="singlePageConfig"> <!-- Visibile se 'single' è selezionato -->
          <fieldset style="border:1px solid #ccc; padding:1rem; margin:1rem 0;">
            <legend>Dettagli Pagina</legend>
            <label>Titolo<input type="text" name="single_page_title"></label>
            <label>Info<textarea name="single_page_info" rows="2"></textarea></label>
            <label>Immagini? (descrizione)<textarea name="single_page_img" rows="1"></textarea></label>
          </fieldset>
        </div>

        <div id="multiConfig" style="display:none;">
          <label>Numero di pagine<input type="number" name="num_pages" id="num_pages" min="1" value="1"></label>
          <div id="pagesContainer"></div>
        </div>
      </div>
      <!-- STEP 3 -->
      <div class="step" id="step3">
        <h2>Step 3: Tipo utente</h2>
        <label><input type="radio" name="user_type" value="azienda" checked> Azienda</label>
        <label><input type="radio" name="user_type" value="privato"> Privato</label>
        <div id="aziendaFields">
          <label>Partita IVA<input type="text" name="piva"></label>
          <label>Sede legale<input type="text" name="sede"></label>
          <label>Email<input type="email" name="email_azienda"></label>
          <label>Telefono<input type="tel" name="tel_azienda"></label>
          <label>Altro<textarea name="altro_azienda" rows="2"></textarea></label> 
        </div>
        <div id="privatoFields" style="display:none;">
          <label>Email<input type="email" name="email_privato"></label>
          <label>Telefono<input type="tel" name="tel_privato"></label>
          <label>Altro<textarea name="altro_privato" rows="2"></textarea></label>
        </div>
      </div>
      <!-- STEP 4 -->
      <div class="step" id="step4">
        <h2>Step 4: Altre informazioni</h2>
        <label>Note aggiuntive<textarea name="altre_info" rows="4"></textarea></label>
      </div>
      <div class="buttons">
        <button type="button" id="prevBtn" onclick="nextPrev(-1)" disabled>&larr;</button>
        <button type="button" id="nextBtn" onclick="nextPrev(1)">&rarr;</button>
      </div>
    </form>
  </div>
  <script>
    let currentStep = 0;
    const steps = document.querySelectorAll('.step');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    // Riferimenti per i colori
    const coloreSfondoInput = document.getElementById('colore_sfondo_input');
    const coloreSfondoPreview = document.getElementById('colore_sfondo_preview');
    const coloreTestoInput = document.getElementById('colore_testo_input');
    const coloreTestoPreview = document.getElementById('colore_testo_preview');

    // Riferimenti ai div per configurazione pagina singola/multipla
    const singlePageConfigDiv = document.getElementById('singlePageConfig');
    const multiConfigDiv = document.getElementById('multiConfig');

    function showStep(n) {
      steps.forEach((s,i)=> s.classList.toggle('active', i===n));
      prevBtn.disabled = n===0;
      nextBtn.innerHTML = (n===steps.length-1)? 'Invia' : '&rarr;'; // Modificato per usare freccia
    }

    function nextPrev(n) {
      const currentStepElement = steps[currentStep];
      if (n === 1) { // Solo in avanti
        const inputs = currentStepElement.querySelectorAll('input, select, textarea');
        let allValid = true;
        for (const inp of inputs) {
            // Un input è considerato per la validazione 'required' solo se è visibile
            const isVisible = inp.offsetParent !== null; 
            if (inp.hasAttribute('required') && !inp.value && isVisible) {
                allValid = false;
                break;
            }
        }
        if (!allValid) {
          alert('Compila tutti i campi obbligatori visibili.');
          return;
        }
      }
      currentStep += n;
      if (currentStep >= steps.length) {
        document.getElementById('wizardForm').submit();
        return;
      }
      showStep(currentStep);
    }

    // Aggiorna valore e anteprima colore sfondo
    coloreSfondoInput.addEventListener('input', function(event) {
      const newColor = event.target.value;
      coloreSfondoPreview.style.backgroundColor = newColor; // Aggiorna anteprima
    });

    // Aggiorna valore e anteprima colore testo
    coloreTestoInput.addEventListener('input', function(event) {
      const newColor = event.target.value;
      coloreTestoPreview.style.backgroundColor = newColor; // Aggiorna anteprima
    });

    // gestione cambio modalità monopagina/multipagina
    document.getElementsByName('mode').forEach(radio => {
      radio.addEventListener('change', e => {
        if (e.target.value === 'multi') {
          multiConfigDiv.style.display = 'block';
          singlePageConfigDiv.style.display = 'none';
        } else { // 'single'
          multiConfigDiv.style.display = 'none';
          singlePageConfigDiv.style.display = 'block';
        }
      });
    });

    // genera campi per ogni pagina extra
    document.getElementById('num_pages').addEventListener('input', e=>{
      const cnt = document.getElementById('pagesContainer');
      cnt.innerHTML = '';
      for(let i=1; i<=e.target.value; i++){
        cnt.insertAdjacentHTML('beforeend', `
          <fieldset style="border:1px solid #ccc; padding:1rem; margin:1rem 0;">
            <legend>Pagina ${i}</legend>
            <label>Titolo<input type="text" name="page_${i}_title"></label>
            <label>Info<textarea name="page_${i}_info" rows="2"></textarea></label>
            <label>Immagini? (descrizione)<textarea name="page_${i}_img" rows="1"></textarea></label>
          </fieldset>
        `);
      }
    });

    // gestione tipologia utente
    document.getElementsByName('user_type').forEach(radio=>{
      radio.addEventListener('change', e=>{
        document.getElementById('aziendaFields').style.display = (e.target.value==='azienda')? 'block':'none';
        document.getElementById('privatoFields').style.display = (e.target.value==='privato')? 'block':'none';
      });
    });

    // inizializzazione
    showStep(currentStep);

    // Imposta la visibilità iniziale dei div single/multi page config
    // basandosi sul radio button checkato al caricamento
    const initialModeChecked = document.querySelector('input[name="mode"]:checked');
    if (initialModeChecked) { // Assicura che ci sia un elemento checkato
        if (initialModeChecked.value === 'single') {
            singlePageConfigDiv.style.display = 'block';
            multiConfigDiv.style.display = 'none';
        } else { // 'multi'
            singlePageConfigDiv.style.display = 'none';
            multiConfigDiv.style.display = 'block';
            // Opzionale: se num_pages ha un valore, triggerare la generazione campi
            // const numPagesInput = document.getElementById('num_pages');
            // if (numPagesInput.value && parseInt(numPagesInput.value) > 0) {
            //    numPagesInput.dispatchEvent(new Event('input'));
            // }
        }
    }
  </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def wizard():
    if request.method == 'POST':
        # Converto form in dict
        data = request.form.to_dict(flat=False)
        # Preparo il contenuto da scrivere
        lines = []
        for key, vals in data.items():
            # vals è lista (magari radio o multipli), uniscila in stringa
            value = ', '.join(vals)
            
            # Se esiste una checkbox associata ed è spuntata sovrascrivi con "inventalo tu"
            ai_flag = f"{key}_ai"
            if ai_flag in data:
                value = "inventalo tu"
            
            lines.append(f"{key}: {value}")
        content = "\n".join(lines) + "\n" + ("-"*40) + "\n"

        # Apro (o creo) il file in append mode e scrivo
        with open("dati_utente.txt", "a", encoding="utf-8") as f:
            f.write(content)

        print(data)  # opzionale, per debug in console
        return "<h2>Modulo inviato con successo!</h2><p>Controlla il terminale e il file dati_utente.txt</p>"
    return render_template_string(HTML)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
