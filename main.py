from flask import Flask, render_template_string

app = Flask(__name__)

# Google Drive project links
projects = [
    ("Project 1", "https://drive.google.com/file/d/1VkzeAwn-r2rfkX1MkhUTEdujmWZqXlGX/view?usp=sharing"),
    ("Project 2", "https://drive.google.com/file/d/1kR-Uy4nLIOgKBttblok9r_s8QyK2gWYD/view?usp=sharing"),
    ("Project 3", "https://drive.google.com/file/d/1fSnrXAQ2aQNeN8XhCdyfCkEXwLpMgckt/view?usp=sharing"),
    ("Project 4", "https://drive.google.com/file/d/118CZPVBhCqfY87E_GJJim09vj526XSNA/view?usp=sharing"),
    ("Project 5", "https://drive.google.com/file/d/14KA-LladQ041wEaI8dLoSoyDJ2m6wTXO/view?usp=sharing"),
    ("Project 6", "https://drive.google.com/file/d/1LjMGmIiUqbt_rzvfDU1aq0BTdit5CgfM/view?usp=sharing"),
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Projects</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        a {
            display: block;
            margin: 12px auto;
            padding: 12px 20px;
            width: 250px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 6px;
        }
        a:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h2>My Projects</h2>
    {% for name, link in projects %}
        <a href="{{ link }}" target="_blank">{{ name }}</a>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
