# sito.py
from flask import Flask, render_template_string, request, redirect, url_for
import webbrowser

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>BENVENUTO SU WEB-AI!</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: Arial, sans-serif; background: #333333; color: #f0f0f0; padding: 2rem; }
    .container { background: #444444; color: #f0f0f0; max-width: 600px; margin: auto; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    .step { display: none; }
    .step.active { display: block; }
    .buttons { margin-top: 1.5rem; display: flex; justify-content: space-between; }
    select, textarea { width: 97%; padding: .5rem; margin: .5rem 0 1rem; border: 1px solid #666; border-radius: 4px; background-color: #555; color: #f0f0f0; resize: vertical; overflow: auto; max-width: 100%;}
    input { width: 97%; padding: .5rem; margin: .5rem 0 1rem; border: 1px solid #666; border-radius: 4px; background-color: #555; color: #f0f0f0; }
    select {
      background-color: #ffffff;
      color: #333333;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    /* QUADRATI PER I COLOR PICKER */
    input[type="color"] {
        vertical-align: middle;
        margin-right: 5px;
        padding: 0;
        height: 25px;
        width: auto;
        border: 1px solid #666;
        border-radius: 6px;
        aspect-ratio: 1 / 1;
        box-sizing: border-box;
    }
    .color-preview {
      display: inline-block;
      width: 22px;
      height: 22px;
      border: 1px solid #888;
      vertical-align: middle;
      margin-right: 5px;
    }
    label > span {
        vertical-align: middle;
    }
    input[type="radio"] {
      /* Remove default appearance */
      -webkit-appearance: none;
      appearance: none;
      /* Custom styling */
      background-color: #555; /* Same as other inputs */
      border: 1px solid #666; /* Same as other inputs */
      border-radius: 4px; /* Same as other inputs, or 0 for a sharper square */
      width: 16px; /* Adjust size as needed */
      height: 16px;
      margin-right: 8px; /* Increased margin for better spacing */
      vertical-align: middle;
      position: relative; /* For positioning the checkmark */
      cursor: pointer;
    }
    input[type="radio"]:checked {
      background-color: #5cb85c; /* Same as button background */
      border-color: #4cae4c; /* Slightly darker border for checked state */
    }
    /* Optional: Add a visual checkmark for the checked state */
    input[type="radio"]:checked::after {
      content: '';
      position: absolute;
      left: 5px;
      top: 2px;
      width: 4px;
      height: 8px;
      border: solid white;
      border-width: 0 2px 2px 0;
      transform: rotate(45deg);
    }
    
    label { font-weight: bold; display: block; margin-bottom: 0.5rem; }
    button { background-color: #5cb85c; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
    button:disabled { background-color: #777; cursor: not-allowed; }
    h1 { text-align: center; font-weight: bold; color: #f0f0f0; }
    h2 { color: #f0f0f0; }
    .subtitle { text-align: center; font-size: 1em; color: #ccc; margin-bottom: 1rem; }

    .form-group-ai {
      display: flex;
      align-items: center;
      margin-bottom: 1rem; /* Matches input/textarea margin */
    }
    .form-group-ai label {
      margin-bottom: 0; /* Override default label margin */
      margin-right: 0.5rem;
      flex-shrink: 0; /* Prevent label from shrinking */
    }
    .form-group-ai input[type="color"] {
      width: auto; /* Override general input width */
      margin-bottom: 0;
      flex-shrink: 0;
    }
    .form-group-ai textarea {
      flex-grow: 1;
      width: auto; /* Let flexbox handle width */
      margin-bottom: 0;
    }
    .ai-btn {
      background-color: #6c757d; /* Neutral gray */
      color: white;
      border: none;
      padding: 0.3rem 0.6rem;
      font-size: 0.85em;
      margin-left: 8px;
      border-radius: 4px;
      cursor: pointer;
      vertical-align: middle;
      flex-shrink: 0;
    }
    .ai-btn.active {
      background-color: #5a6268; /* Darker gray for active state */
    }
    .ai-btn:hover {
      background-color: #545b62;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>BENVENUTO SU WEB-AI!</h1>
    <p class="subtitle">Compila il seguente form con le caratteristiche che vorresti avesse il tuo sito web. Dove possibile, clicca &quot;Usa AI&quot; per lasciarti ispirare dall'intelligenza artificiale</p>
    <form id="wizardForm" method="post" action="/">
      <!-- STEP 1 -->
      <div class="step active" id="step1">
        <h2>Step 1: Dati generali</h2>
        <label>Nome sito*<input type="text" name="nome_sito" required></label>
        <label>Target di riferimento<input type="text" name="target">
        <label>Tema/Argomenti trattati*<textarea name="tema" rows="2" required></textarea></label>
        
        <div class="form-group-ai">
          <label for="colore_sfondo_input">Colore sfondo:</label>
          <input type="color" name="colore_sfondo" id="colore_sfondo_input" value="#ffffff">
          <button type="button" class="ai-btn" data-target="colore_sfondo_input">Usa AI</button>
        </div>
        
        <div class="form-group-ai">
          <label for="colore_testo_input">Colore testo:</label>
          <input type="color" name="colore_testo" id="colore_testo_input" value="#000000">
          <button type="button" class="ai-btn" data-target="colore_testo_input">Usa AI</button>
        </div>
        
        <label>Stile del sito
          <select name="stile">
            <option value="Generico" selected>Generico</option>
            <option value="Moderno">Moderno</option>
            <option value="Creativo">Creativo</option>
            <option value="Minimal">Minimal</option>
            <option value="Corporate">Corporate</option>
          </select>
        </label>
        <p style="font-size:0.95em; color:#ccc; margin-bottom:1rem;">* testo obbligatorio</p>
      </div>
      <!-- STEP 2 -->
      <div class="step" id="step2">
        <h2>Step 2: Struttura pagine</h2>
        <p style="font-size:0.95em; color:#ccc; margin-bottom:1rem;">Un sito monopagina mostra tutte le informazioni su un’unica pagina a scorrimento.<br>Un sito multipagina è diviso in più pagine interattive, ognuna con contenuti diversi (es. Home, Contatti, Servizi).</p>
        <label><input type="radio" name="mode" value="single" checked> Monopagina</label>
        <label><input type="radio" name="mode" value="multi"> Multipagina</label>
        
        <div id="singlePageConfig">
          <fieldset style="border:1px solid #ccc; padding:1rem; margin:1rem 0;">
            <legend>Dettagli Pagina</legend>
            <label>Titolo*<input type="text" name="single_page_title" required></label>
            <div class="form-group-ai">
              <label for="single_page_info">Info:*</label>
              <textarea name="single_page_info" id="single_page_info" rows="2" required></textarea>
              <button type="button" class="ai-btn" data-target="single_page_info">Usa AI</button>
            </div>
            <div class="form-group-ai">
              <label for="single_page_img">Immagini? (descrizione):</label>
              <textarea name="single_page_img" id="single_page_img" rows="1"></textarea>
              <button type="button" class="ai-btn" data-target="single_page_img">Usa AI</button>
            </div>
          </fieldset>
        </div>

        <div id="multiConfig" style="display:none;">
          <label>Numero di pagine<input type="number" name="num_pages" id="num_pages" min="2" value="2"></label>
          <div id="pagesContainer"></div>
        </div>
        <p style="font-size:0.95em; color:#ccc; margin-bottom:1rem;">* testo obbligatorio</p>
      </div>
      <!-- STEP 3 -->
      <div class="step" id="step3">
        <h2>Step 3: Tipo utente</h2>
        <label><input type="radio" name="user_type" value="azienda" checked> Azienda</label>
        <label><input type="radio" name="user_type" value="privato"> Privato</label>
        <div id="aziendaFields">
          <label>Partita IVA*<input type="text" name="piva" required></label>
          <label>Sede legale*<input type="text" name="sede" required></label>
          <label>Email<input type="email" name="email_azienda"></label>
          <label>Telefono<input type="tel" name="tel_azienda"></label>
          <label>Altro<textarea name="altro_azienda" rows="2"></textarea></label> 
        </div>
        <div id="privatoFields" style="display:none;">
          <label>Email<input type="email" name="email_privato"></label>
          <label>Telefono<input type="tel" name="tel_privato"></label>
          <label>Altro<textarea name="altro_privato" rows="2"></textarea></label>
        </div>
        <p style="font-size:0.95em; color:#ccc; margin-bottom:1rem;">* testo obbligatorio</p>
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
    const pagesContainer = document.getElementById('pagesContainer'); // Reference pagesContainer
    const numPagesInput = document.getElementById('num_pages'); // Reference num_pages input

    function showStep(n) {
      steps.forEach((s,i)=> s.classList.toggle('active', i===n));
      prevBtn.disabled = n===0;
      nextBtn.innerHTML = (n===steps.length-1)? 'Invia' : '&rarr;';
    }

    function nextPrev(n) {
      const currentStepElement = steps[currentStep];
      if (n === 1) {
        const inputs = currentStepElement.querySelectorAll('input, select, textarea');
        let allValid = true;
        for (const inp of inputs) {
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
        // Re-enable AI-controlled fields before submitting so their values are included
        const aiButtonsActive = document.querySelectorAll('.ai-btn.active');
        aiButtonsActive.forEach(button => {
          const targetInputId = button.dataset.target;
          const targetInput = document.getElementById(targetInputId);
          if (targetInput && targetInput.disabled) {
            targetInput.disabled = false; 
            // Il valore di targetInput è già "Fai generare all'AI"
          }
        });
        document.getElementById('wizardForm').submit();
        return;
      }
      showStep(currentStep);
    }

    function generatePageFields(count) {
      pagesContainer.innerHTML = ''; // Clear previous fields
      if (isNaN(count) || count < 1) {
          return; // Do nothing if count is not a positive number
      }
      for(let i=1; i<=count; i++){
        const pageInfoId = `page_${i}_info`;
        const pageImgId = `page_${i}_img`;
        pagesContainer.insertAdjacentHTML('beforeend', `
          <fieldset style="border:1px solid #ccc; padding:1rem; margin:1rem 0;">
            <legend>Pagina ${i}</legend>
            <label>Titolo<input type="text" name="page_${i}_title"></label>
            <div class="form-group-ai">
              <label for="${pageInfoId}">Info:</label>
              <textarea name="${pageInfoId}" id="${pageInfoId}" rows="2"></textarea>
              <button type="button" class="ai-btn" data-target="${pageInfoId}">Usa AI</button>
            </div>
            <div class="form-group-ai">
              <label for="${pageImgId}">Immagini? (descrizione):</label>
              <textarea name="${pageImgId}" id="${pageImgId}" rows="1"></textarea>
              <button type="button" class="ai-btn" data-target="${pageImgId}">Usa AI</button>
            </div>
          </fieldset>
        `);
      }
    }

    
    coloreSfondoInput.addEventListener('input', function(event) {
      const newColor = event.target.value;
      if (coloreSfondoPreview) coloreSfondoPreview.style.backgroundColor = newColor;
    });

    coloreTestoInput.addEventListener('input', function(event) {
      const newColor = event.target.value;
      if (coloreTestoPreview) coloreTestoPreview.style.backgroundColor = newColor;
    });

    document.getElementsByName('mode').forEach(radio => {
      radio.addEventListener('change', e => {
        if (e.target.value === 'multi') {
          multiConfigDiv.style.display = 'block';
          singlePageConfigDiv.style.display = 'none';
          if (parseInt(numPagesInput.value) < 2) {
            numPagesInput.value = "2";
          }
          const numPagesValue = parseInt(numPagesInput.value);
          generatePageFields(numPagesValue); // Generate fields when multi is selected
        } else {
          multiConfigDiv.style.display = 'none';
          singlePageConfigDiv.style.display = 'block';
          // pagesContainer.innerHTML = ''; // Optionally clear multi-page fields
        }
      });
    });

    numPagesInput.addEventListener('input', e => { // Changed from getElementById('num_pages') to use the variable
      let numPagesValue = parseInt(e.target.value);
      if (document.querySelector('input[name="mode"]:checked').value === 'multi' && numPagesValue < 2) {
        e.target.value = "2"; // Corregge se l'utente prova a scendere sotto 2
        numPagesValue = 2;
      }
      if (numPagesValue < 1 && document.querySelector('input[name="mode"]:checked').value === 'single') {
        // Se per qualche motivo si potesse scendere sotto 1 in single page (non dovrebbe con min="1")
         e.target.value = "1";
         numPagesValue = 1; // Anche se per single page non usiamo numPagesValue per generare fields
      }
      generatePageFields(numPagesValue);
    });


    document.getElementsByName('user_type').forEach(radio=>{
      radio.addEventListener('change', e=>{
        document.getElementById('aziendaFields').style.display = (e.target.value==='azienda')? 'block':'none';
        document.getElementById('privatoFields').style.display = (e.target.value==='privato')? 'block':'none';
      });
    });

    showStep(currentStep);

    const initialModeChecked = document.querySelector('input[name="mode"]:checked');
    if (initialModeChecked) {
        if (initialModeChecked.value === 'single') {
            singlePageConfigDiv.style.display = 'block';
            multiConfigDiv.style.display = 'none';
        } else { // 'multi' is checked
            singlePageConfigDiv.style.display = 'none';
            multiConfigDiv.style.display = 'block';
            if (parseInt(numPagesInput.value) < 2) {
                numPagesInput.value = "2";
            }
            const numPagesValue = parseInt(numPagesInput.value); // Use the variable
            generatePageFields(numPagesValue); // Generate fields on initial load if multi is selected
        }
    }

    // Funzione per generare contenuto AI per i campi "Info pagina"
    async function generateAiContentForPageInfo(targetTextarea, aiButton) {
      const originalButtonText = aiButton.textContent; // Should be "Usa AI" when called
      aiButton.textContent = 'Generazione...';
      aiButton.disabled = true;

      // 1. Collect form data
      const nomeSito = document.querySelector('input[name="nome_sito"]').value || "Non specificato";
      const targetUtenti = document.querySelector('input[name="target"]').value || "Non specificato";
      const temaSito = document.querySelector('textarea[name="tema"]').value || "Non specificato";
      const coloreSfondo = document.getElementById('colore_sfondo_input').value;
      const coloreTesto = document.getElementById('colore_testo_input').value;
      const stileSito = document.querySelector('select[name="stile"]').value;

      let pageTitle = "Informazioni generali della pagina"; 
      if (targetTextarea.id === 'single_page_info') {
        const singlePageTitleInput = document.querySelector('input[name="single_page_title"]');
        if (singlePageTitleInput && singlePageTitleInput.value) {
          pageTitle = singlePageTitleInput.value;
        }
      } else if (targetTextarea.id.startsWith('page_') && targetTextarea.id.endsWith('_info')) {
        const pageIdParts = targetTextarea.id.split('_'); 
        const pageNumber = pageIdParts[1];
        const multiPageTitleInput = document.querySelector(`input[name="page_${pageNumber}_title"]`);
        if (multiPageTitleInput && multiPageTitleInput.value) {
          pageTitle = multiPageTitleInput.value;
        } else {
          pageTitle = `Pagina ${pageNumber}`;
        }
      }

      const promptLines = [
        "Basandoti sulle seguenti informazioni, ma soprattutto in base a quanto riportato nel titolo della pagina, che è il seguente: '${pageTitle}'",
        " genera un elenco di argomenti (massimo 6) che devono essere trattati nella pagina.",
        "Non includere il titolo della pagina nella descrizione, solo l'elenco richiesto.",
        "Caratteristiche del sito:",
        `- Nome del Sito: ${nomeSito}`,
        `- Target di riferimento: ${targetUtenti}`,
        `- Tema/Argomenti trattati: ${temaSito}`,
        `- Stile del Sito: ${stileSito}`,
        `Informazioni specifiche per questa pagina (dal titolo '${pageTitle}'):`
      ];
      const prompt = promptLines.join('\\n');

      try {
        const response = await fetch('http://127.0.0.1:1234/v1/chat/completions', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', },
          body: JSON.stringify({
            model: "qwen3-4b", // IMPORTANTE: Cambia se il nome del modello in LM Studio è diverso!
            messages: [
              { role: "system", content: "Sei un assistente AI specializzato nel generare testi brevi e persuasivi per sezioni di pagine web. Rispondi solo con il testo generato, senza frasi introduttive o conclusive." },
              { role: "user", content: prompt }
            ],
            temperature: 0.7,
            max_tokens: 2000 
          }),
        });

        if (!response.ok) {
          const errorData = await response.text();
          throw new Error(`Errore API: ${response.status} ${response.statusText}. Dettagli: ${errorData}`);
        }

        const data = await response.json();
        if (data.choices && data.choices.length > 0 && data.choices[0].message && data.choices[0].message.content) {
          targetTextarea.value = data.choices[0].message.content.replace(/<think\\s*>[\\s\\S]*?<\\/think\\s*>/gi, '').trim();
          targetTextarea.disabled = false; 
          aiButton.classList.add('active'); 
          aiButton.textContent = 'Manuale'; 
        } else {
          throw new Error("Risposta AI non valida o vuota.");
        }
      } catch (error) {
        console.error("Errore chiamata LLM:", error);
        alert(`Errore durante la generazione del testo con AI: ${error.message}\\nControlla che LM Studio sia in esecuzione, che un modello sia caricato, e che l'indirizzo (http://127.0.0.1:1234) e il nome del modello ('local-model') siano corretti.`);
        aiButton.textContent = 'Usa AI'; 
        aiButton.classList.remove('active');
      } finally {
        aiButton.disabled = false;
      }
    }

    function handleAiButtonClick(event) {
      const aiButton = event.target;
      const targetInputId = aiButton.dataset.target;
      const targetInput = document.getElementById(targetInputId);

      if (!targetInput) return;

      const isInfoTextArea = targetInput.id === 'single_page_info' || 
                             (targetInput.id && targetInput.id.startsWith('page_') && targetInput.id.endsWith('_info'));

      if (isInfoTextArea) {
        if (aiButton.textContent === 'Manuale') { 
          // AI content is present, user wants to revert to manual
          targetInput.disabled = false;
          if (targetInput.dataset.originalValueForAi !== undefined) {
            targetInput.value = targetInput.dataset.originalValueForAi;
          } else {
            targetInput.value = ''; 
          }
          aiButton.classList.remove('active');
          aiButton.textContent = 'Usa AI';
        } else if (aiButton.textContent === 'Usa AI') { 
          // User wants to generate AI content
          targetInput.dataset.originalValueForAi = targetInput.value; // Save current manual content
          generateAiContentForPageInfo(targetInput, aiButton); 
        }
        // If button text is "Generazione...", it's disabled, so no click event handled here.
        return; 
      }

      // Original logic for other AI buttons (colors, etc.)
      const aiMarkerText = "Fai generare all'AI";

      if (aiButton.classList.contains('active')) {
        // Deactivate AI for non-info fields: Switch back to manual
        targetInput.disabled = false;
        const originalType = targetInput.dataset.originalType;
        const originalValue = targetInput.dataset.originalValue;

        if (originalType) {
            targetInput.type = originalType;
            delete targetInput.dataset.originalType;
        }
        if (originalValue !== undefined) {
            targetInput.value = originalValue;
        } else if (targetInput.type === 'color') {
            targetInput.value = targetInput.defaultValue || '#ffffff'; 
        } else {
            targetInput.value = '';
        }
        if (targetInput.dataset.originalValue !== undefined) {
            delete targetInput.dataset.originalValue;
        }
        aiButton.classList.remove('active');
        aiButton.textContent = 'Usa AI';
      } else {
        // Activate AI for non-info fields
        targetInput.dataset.originalValue = targetInput.value; 
        if (targetInput.type === 'color') {
            targetInput.dataset.originalType = targetInput.type;
            targetInput.type = 'text';
        }
        targetInput.value = aiMarkerText;
        targetInput.disabled = true;
        aiButton.classList.add('active');
        aiButton.textContent = 'Manuale';
      }
    }

    document.getElementById('wizardForm').addEventListener('click', function(event) {
      if (event.target.classList.contains('ai-btn')) {
        handleAiButtonClick(event);
      }
    });

  </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def wizard():
    if request.method == 'POST':
        # Converto form in dict
        data = request.form.to_dict(flat=False)
        # Preparo il contenuto da scrivere, filtrando i campi vuoti
        lines = []
        for key, vals in data.items():
            # vals è lista (magari radio o multipli), uniscila in stringa
            # Rimuovi spazi bianchi all'inizio e alla fine per considerare "   " come vuoto
            value = ', '.join(vals).strip() 
            
            # Il valore del campo sarà "Fai generare all'AI" se l'AI è stata attivata
            # e il campo riabilitato dal JS prima del submit.
            
            # Aggiungi la linea solo se il valore non è vuoto
            if value: 
                lines.append(f"{key}: {value}")
        
        if lines: # Se ci sono righe da scrivere
            content = "\n".join(lines) + "\n" + ("-"*40) + "\n";
        else: # Se tutti i campi erano vuoti (o non inviati e filtrati)
            content = "Nessun dato compilato.\n" + ("-"*40) + "\n";

        # Apro (o creo) il file in write mode e scrivo
        with open("dati_utente.txt", "w", encoding="utf-8") as f:
            f.write(content);

        print(data)  # opzionale, per debug in console 
        return "<h2>Modulo inviato con successo!</h2><p>Controlla il terminale e il file dati_utente.txt</p>"
    return render_template_string(HTML)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)