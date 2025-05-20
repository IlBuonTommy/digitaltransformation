from flask import Flask, render_template_string
import webbrowser

def create_app():
    app = Flask(__name__)

    HTML = '''
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Configuratore Sito Web</title>
</head>
<body>
  <h1>Configuratore Sito Web</h1>
  <form id="multiStepForm">
  <div class="step-indicator">
    <div class="step-circle active">1</div>
    <div class="step-circle">2</div>
    <div class="step-circle">3</div>
    <div class="step-circle">4</div>
  </div>
  
    <!-- Step 1 -->
    <div id="step1" class="step active">
      <h2>Step 1: Informazioni di base</h2>
      <label>Nome sito: <input type="text" id="siteName" required></label><br>
      <label>Target di riferimento: <input type="text" id="target" required></label><br>
      <label>Tema/Argomenti: <input type="text" id="theme" required></label><br>
      <label>Colore sfondo: <input type="color" id="bgColor" required></label><br>
      <label>Colore testo: <input type="color" id="textColor" required></label><br>
      <label>Stile:
        <select id="styleSelect" required>
          <option value="moderno">Moderno</option>
          <option value="creativo">Creativo</option>
          <option value="minimal">Minimal</option>
          <option value="corporate">Corporate</option>
        </select>
      </label>
    </div>

    <!-- Step 2 -->
    <div id="step2" class="step">
      <h2>Step 2: Struttura pagine</h2>
      <label>
        <input type="radio" name="pageType" value="single" checked> Monopagina
      </label>
      <label>
        <input type="radio" name="pageType" value="multi"> Multipagina
      </label>
      <div id="multiOptions" style="display:none; margin-top:10px;">
        <label>Numero di pagine: <input type="number" id="pageCount" min="2" max="20"></label>
        <div id="pagesContainer"></div>
      </div>
      <div id="singleOptions" style="margin-top:10px;">
        <h3>Dettagli Pagina</h3>
        <label>Titolo: <input type="text" class="pageTitle"></label><br>
        <label>Info: <textarea class="pageInfo"></textarea></label><br>
        <label>Immagini (url): <input type="text" class="pageImages" placeholder="url1,url2,..."></label><br>
      </div>
    </div>

    <!-- Step 3 -->
    <div id="step3" class="step">
      <h2>Step 3: Contatti</h2>
      <label><input type="radio" name="userType" value="company" checked> Azienda</label>
      <label><input type="radio" name="userType" value="private"> Privato</label>
      <div id="companyFields" style="margin-top:10px;">
        <label>Partita IVA: <input type="text" id="vat"></label><br>
        <label>Sede legale: <input type="text" id="hq"></label><br>
        <label>Altri contatti (email/telefono): <input type="text" id="otherContacts"></label>
      </div>
      <div id="privateFields" style="display:none; margin-top:10px;">
        <label>Email (opzionale): <input type="email" id="privEmail"></label><br>
        <label>Telefono (opzionale): <input type="tel" id="privPhone"></label>
      </div>
    </div>

    <!-- Step 4 -->
    <div id="step4" class="step">
      <h2>Step 4: Altre informazioni</h2>
      <textarea id="otherInfo" rows="5" placeholder="Inserisci qualunque altra informazione..."></textarea>
    </div>

    <div class="navigation">
      <button type="button" id="prevBtn" onclick="nextPrev(-1)">
        <i class="fas fa-arrow-left"></i> Indietro
      </button>
      <button type="button" id="nextBtn" onclick="nextPrev(1)">
        Avanti <i class="fas fa-arrow-right"></i>
    </button>
    </div>
  </form>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Riferimenti a elementi
      const pageTypeRadios = document.getElementsByName('pageType');
      const singleOptions    = document.getElementById('singleOptions');
      const multiOptions     = document.getElementById('multiOptions');
      const pageCountInput   = document.getElementById('pageCount');
      const pagesContainer   = document.getElementById('pagesContainer');

      const userTypeRadios   = document.getElementsByName('userType');
      const companyFields    = document.getElementById('companyFields');
      const privateFields    = document.getElementById('privateFields');

      // Funzione per costruire i campi delle pagine
      function buildPages() {
        const count = parseInt(pageCountInput.value, 10) || 0;
        pagesContainer.innerHTML = '';
        for (let i = 1; i <= count; i++) {
          const div = document.createElement('div');
          div.innerHTML = `
            <h4>Pagina ${i}</h4>
            <label>Titolo: <input type="text" name="pageTitle_${i}" required></label><br>
            <label>Info: <textarea name="pageInfo_${i}" required></textarea></label><br>
            <label>Immagini (url): <input type="text" name="pageImages_${i}" placeholder="url1,url2,..."></label><br>
          `;
          pagesContainer.appendChild(div);
        }
      }

      // Callback al cambio monopagina/multipagina
      function onPageTypeChange() {
        const mt = document.querySelector('input[name="pageType"]:checked').value;
        if (mt === 'single') {
          singleOptions.style.display = 'block';
          multiOptions.style.display  = 'none';
        } else {
          singleOptions.style.display = 'none';
          multiOptions.style.display  = 'block';
          buildPages();
        }
      }

      // Callback al cambio azienda/privato
      function onUserTypeChange() {
        const ut = document.querySelector('input[name="userType"]:checked').value;
        if (ut === 'company') {
          companyFields.style.display = 'block';
          privateFields.style.display = 'none';
        } else {
          companyFields.style.display = 'none';
          privateFields.style.display = 'block';
        }
      }

      // Registra gli event listener
      pageTypeRadios.forEach(r => r.addEventListener('change', onPageTypeChange));
      pageCountInput.addEventListener('input', () => {
        if (document.querySelector('input[name="pageType"]:checked').value === 'multi') {
          buildPages();
        }
      });
      userTypeRadios.forEach(r => r.addEventListener('change', onUserTypeChange));

      // Inizializza lo stato delle sezioni
      onPageTypeChange();
      onUserTypeChange();
    });
  </script>
</body>
</html>
    '''

    @app.route('/')
    def index():
        return render_template_string(HTML)

    return app

if __name__ == '__main__':
    app = create_app()
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
