# main.py
'''
Main entry point for the website generator. This script creates all necessary HTML files with the specified structure and styling.
'''
import os
def generate_html_files():
    # Create directories if they don't exist
    os.makedirs('pages', exist_ok=True)
    # Generate index.html
    with open('index.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Fattoria</title>
    <style>
        body {
            background-color: #ffcc99; /* Yellow */
            color: #4b0082; /* Purple */
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #ffd700; /* Gold */
            padding: 20px;
            text-align: center;
        }
        section {
            padding: 30px;
            border-bottom: 1px solid #8b4513;
        }
        nav a {
            margin: 0 15px;
            color: #ff6347; /* Tomato */
            text-decoration: none;
        }
        footer {
            background-color: #dda0dd; /* Plum */
            padding: 20px;
            text-align: center;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Fattoria del 1900</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="about-mooches.html">Mucche</a>
            <a href="products.html">Prodotti</a>
        </nav>
    </header>
    <section id="farm-section">
        <h2>La Fattoria</h2>
        <p>Nata nel 1900, la nostra fattoria ospita 150 mucche di diverse razze. Scopri di più sulle nostre razze cliccando qui:</p>
        <a href="about-mooches.html">Dettagli sulle razze</a>
    </section>
    <section id="products-section">
        <h2>Prodotti Caseari</h2>
        <p>Vendiamo formaggi, latte fresco, burro e mozzarella. Scopri i dettagli cliccando qui:</p>
        <a href="products.html">Dettagli sui prodotti</a>
    </section>
    <section id="contact-section">
        <h2>Contatti</h2>
        <p>Telefono: 345234<br>Email: pippogmail.com</p>
    </section>
    <section id="address-section">
        <h2>Residenza</h2>
        <p>Via Volturno 59, CAP 25689</p>
    </section>
    <footer>
        &copy; 2023 Fattoria del 1900
    </footer>
</body>
</html>''')
    # Generate about-mooches.html
    with open('about-mooches.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Razze di Mucche</title>
    <style>
        body {
            background-color: #ffcc99;
            color: #4b0082;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #ffd700;
            padding: 20px;
            text-align: center;
        }
        nav a {
            margin: 0 15px;
            color: #ff6347;
            text-decoration: none;
        }
        footer {
            background-color: #dda0dd;
            padding: 20px;
            text-align: center;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Razze di Mucche</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="about-mooches.html">Mucche</a>
            <a href="products.html">Prodotti</a>
        </nav>
    </header>
    <section>
        <h2>Frisona</h2>
        <p>La razza Frisona è nota per la sua alta produzione di latte e robustezza.</p>
    </section>
    <section>
        <h2>Simental</h2>
        <p>Il Simmental è una razza versatile adatta a diverse condizioni climatiche.</p>
    </section>
    <section>
        <h2>Belga</h2>
        <p>La mucca Belga è riconosciuta per la sua carne di alta qualità e produttività.</p>
    </section>
    <footer>
        &copy; 2023 Fattoria del 1900
    </footer>
</body>
</html>''')
    # Generate products.html
    with open('products.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Prodotti Caseari</title>
    <style>
        body {
            background-color: #ffcc99;
            color: #4b0082;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #ffd700;
            padding: 20px;
            text-align: center;
        }
        nav a {
            margin: 0 15px;
            color: #ff6347;
            text-decoration: none;
        }
        footer {
            background-color: #dda0dd;
            padding: 20px;
            text-align: center;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Prodotti Caseari</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="about-mooches.html">Mucche</a>
            <a href="products.html">Prodotti</a>
        </nav>
    </header>
    <section>
        <h2>Formaggi</h2>
        <p>Siamo specializzati nella produzione di formaggi artigianali con metodi tradizionali.</p>
    </section>
    <section>
        <h2>Latte Fresco</h2>
        <p>Latte fresco giornaliero, sempre disponibile e di alta qualità.</p>
    </section>
    <section>
        <h2>Burro</h2>
        <p>Burro prodotto con latte della nostra fattoria, ricco di sapore e cremoso.</p>
    </section>
    <section>
        <h2>Mozzarella</h2>
        <p>Mozzarella fatta a mano con latte fresco e ingredienti naturali.</p>
    </section>
    <footer>
        &copy; 2023 Fattoria del 1900
    </footer>
</body>
</html>''')
    # Generate contact.html (already included in index.html)
    # Generate address.html (already included in index.html)
if __name__ == "__main__":
    generate_html_files()
    print("Sito web creato con successo! Apri 'index.html' nel browser per visualizzarlo.")