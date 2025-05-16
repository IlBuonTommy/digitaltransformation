# pages/index.html
'''
HTML file for the main page with four sections about the farm.
'''
<!DOCTYPE html>
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
            background-color: #dda0dd; /* Violet */
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
        <h1>Benvenuti nella Fattoria</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="about-mooches.html">Mucche</a>
            <a href="products.html">Prodotti</a>
        </nav>
    </header>
    <section id="storia">
        <h2>Storia della Fattoria</h2>
        <p>Nata nel 1900, la nostra fattoria è orgogliosa di aver allevato 150 mucche di diverse razze.</p>
        <a href="about-mooches.html" style="display: inline-block; margin-top: 10px;">Scopri di più sulle razze</a>
    </section>
    <section id="prodotti">
        <h2>Prodotti Caseari</h2>
        <p>Siamo specializzati nella produzione di formaggi, latte, burro e mozzarella.</p>
    </section>
    <section id="contatti">
        <h2>Contatti</h2>
        <p>Telefono: 345234<br>Email: pippogmail.com</p>
    </section>
    <section id="residenza">
        <h2>Residenza</h2>
        <p>Via Volturno 59, CAP 25689</p>
    </section>
    <footer>
        &copy; 2023 Fattoria del 1900
    </footer>
</body>
</html>