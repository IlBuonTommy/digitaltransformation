def generate_home_html():
    # Static content for home page
    html = """
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
            margin: 0;
            padding: 0;
        }
        .pannello_centrale {
            border: 5px solid #ff2600;
            margin: auto;
            padding: 2rem;
            max-width: 800px;
            background-color: white;
            color: black;
            text-align: center;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="pannello_centrale">
        <h1>Home - Storia della Formula Uno</h1>
        <p>This is the home page of Races F1, dedicated to the history and excitement of Formula 1 racing.</p>
        <img src="https://picsum.photos/seed/history/800/600" alt="Auto storiche di F1">
    </div>
</body>
</html>
"""
    return html
def generate_charles_html():
    # Dynamic content for Charles Leclerc page
    charles_text = generate_charles_text()
    charles_image_url = get_charles_image_url()
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Races F1 - Charles Leclerc</title>
    <style>
        body {{
            background-color: #ff2600;
            color: white;
            font-family: sans-serif;
            margin: 0;
            padding: 0;
        }}
        .pannello_centrale {{
            border: 5px solid #ff2600;
            margin: auto;
            padding: 2rem;
            max-width: 800px;
            background-color: white;
            color: black;
            text-align: center;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
    <div class="pannello_centrale">
        <h1>Charles Leclerc</h1>
        <p>{charles_text}</p>
        <img src="{charles_image_url}" alt="Foto di Charles Leclerc">
    </div>
</body>
</html>
"""
    return html
def generate_lewis_html():
    # Dynamic content for Lewis Hamilton page
    lewis_text = generate_lewis_text()
    lewis_image_url = get_lewis_image_url()
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Races F1 - Lewis Hamilton</title>
    <style>
        body {{
            background-color: #ff2600;
            color: white;
            font-family: sans-serif;
            margin: 0;
            padding: 0;
        }}
        .pannello_centrale {{
            border: 5px solid #ff2600;
            margin: auto;
            padding: 2rem;
            max-width: 800px;
            background-color: white;
            color: black;
            text-align: center;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
    <div class="pannello_centrale">
        <h1>Lewis Hamilton</h1>
        <p>{lewis_text}</p>
        <img src="{lewis_image_url}" alt="Foto di Lewis Hamilton">
    </div>
</body>
</html>
"""
    return html