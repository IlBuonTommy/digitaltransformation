'''
Functions for generating HTML content of the F1 website pages.
These functions create the static and dynamic content as per the task requirements.
'''
def generate_home_html():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Races F1 - Home</title>
    <style>
        body {
            background-color: #ff2600;
            color: white;
            font-family: sans-serif;
        }
        .pannello_centrale {
            border: 5px solid #ff2600;
            margin: auto;
            padding: 2rem;
            max-width: 800px;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="pannello_centrale">
        <h1>Storia della Formula Uno</h1>
        <p>La Formula 1 è una serie di gare automobilistiche che si svolgono su piste chiuse. La competizione ha iniziato nel 1950 e oggi conta circa 20 squadre, con piloti provenienti da tutto il mondo.</p>
        <img src="https://upload.wikimedia.org/wikipedia/en/4/4d/Ferrari_1961.jpg" alt="Auto storica Ferrari">
    </div>
</body>
</html>
"""
def generate_charles_html():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Races F1 - Charles Leclerc</title>
    <style>
        body {
            background-color: #ff2600;
            color: white;
            font-family: sans-serif;
        }
        .pannello_centrale {
            border: 5px solid #ff2600;
            margin: auto;
            padding: 2rem;
            max-width: 800px;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="pannello_centrale">
        <h1>Charles Leclerc</h1>
        <p>Charles Leclerc è un pilota monegasco che ha vinto il campionato mondiale di Formula 1 nel 2021 con la squadra Ferrari. È noto per le sue abilità in pista e la sua capacità di gestire le gare in modo strategico.</p>
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Charles_Leclerc_2023.jpg" alt="Charles Leclerc">
    </div>
</body>
</html>
"""
def generate_lewis_html():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Races F1 - Lewis Hamilton</title>
    <style>
        body {
            background-color: #ff2600;
            color: white;
            font-family: sans-serif;
        }
        .pannello_centrale {
            border: 5px solid #ff2600;
            margin: auto;
            padding: 2rem;
            max-width: 800px;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="pannello_centrale">
        <h1>Lewis Hamilton</h1>
        <p>Lewis Hamilton è un pilota britannico che ha vinto il campionato mondiale di Formula 1 sette volte. È noto per la sua determinazione e capacità di vincere gare anche in condizioni difficili.</p>
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/3e/Lewis_Hamilton_2023.jpg" alt="Lewis Hamilton">
    </div>
</body>
</html>
"""