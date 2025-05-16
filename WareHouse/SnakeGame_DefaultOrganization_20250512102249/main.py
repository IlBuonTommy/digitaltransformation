'''
DOCSTRING
A simple static website about snakes using Python-generated HTML. Displays information, an image of a snake, and interactive elements.
'''
import webbrowser
import os
from PIL import Image
def generate_website():
    '''Generate an HTML file with snake information, including a generated placeholder image, and open it in the default browser'''
    html_content = '''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Serpente - Informazioni</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        .container h2 {
            color: #2980b9;
        }
        .facts {
            margin-top: 30px;
        }
        .facts ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        .image-container {
            text-align: center;
            margin: 40px 0;
        }
        .buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
        }
        button {
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        #learn-more {
            background-color: #2980b9;
            color: white;
        }
        #exit {
            background-color: #e74c3c;
            color: white;
        }
        button:hover {
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <header>
        <h1>Il Serpente</h1>
    </header>
    <div class="container">
        <p>I serpenti sono rettili senza arti, con un corpo snello e una coda che si muove in modo fluido. Svolgono un ruolo chiave nell'ecosistema come predatori e prede. Alcuni specie sono velenosi, mentre altre no.</p>
        <div class="facts">
            <h2>Fatti interessanti:</h2>
            <ul>
                <li>Il serpente più lungo al mondo è il rettiliano di mare (fino a 7.6 m)</li>
                <li>Alcuni serpenti possono dormire per mesi senza mangiare</li>
                <li>I serpenti non hanno orecchie esterne, ma sentono le vibrazioni del suolo</li>
                <li>Il cobra è noto per il suo 'colpo della testa' durante l'attacco</li>
            </ul>
        </div>
        <div class="image-container">
            <!-- Immagine del serpente -->
            <img src="snake.jpg" alt="Serpente" style="max-width: 100%; border-radius: 8px;">
        </div>
        <div class="buttons">
            <button id="learn-more" onclick="window.open('https://www.nationalgeographic.com/animals/reptiles/snake', '_blank')">Scopri di più</button>
            <button id="exit" onclick="window.close()">Esci</button>
        </div>
    </div>
</body>
</html>
'''
    # Verifica e crea la directory
    if not os.path.exists('website'):
        os.makedirs('website')
    # Scrivi il file HTML
    html_file = os.path.join('website', 'snake.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    # Genera immagine placeholder se non esiste
    image_path = os.path.join('website', 'snake.jpg')
    if not os.path.exists(image_path):
        # Crea un'immagine placeholder rossa (simula un serpente)
        img = Image.new('RGB', (400, 250), color='red')
        img.save(image_path)
    # Apri il sito nel browser predefinito
    webbrowser.open(f'file://{os.path.abspath(html_file)}')
if __name__ == "__main__":
    generate_website()