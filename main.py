from flask import Flask, render_template_string

app = Flask(__name__)

# Google Drive project links
projects = [
("project 1", "https://drive.google.com/file/d/1VkzeAwn-r2rfkX1MkhUTEdujmWZqXlGX/view?usp=sharing"),
("project 2", "https://drive.google.com/file/d/1kR-Uy4nLIOgKBttblok9r_s8QyK2gWYD/view?usp=sharing"),
("project 3", "https://drive.google.com/file/d/1fSnrXAQ2aQNeN8XhCdyfCkEXwLpMgckt/view?usp=sharing"),
("project 4", "https://drive.google.com/file/d/118CZPVBhCqfY87E_GJJim09vj526XSNA/view?usp=sharing"),
("project 5", "https://drive.google.com/file/d/14KA-LladQ041wEaI8dLoSoyDJ2m6wTXO/view?usp=sharing"),
("project 6", "https://drive.google.com/file/d/1LjMGmIiUqbt_rzvfDU1aq0BTdit5CgfM/view?usp=sharing"),
    ("ann", "https://drive.google.com/file/d/18GTCceLzBvDmP9CFnUUzIhEESxtrNpi4/view?usp=sharing"),
    ("A*", "https://drive.google.com/file/d/1-Rf6XYg6UNMzgCPohrudqWZSrs9h9Cdg/view?usp=sharing"),
    ("Candidate Eliminate Algorithm", "https://drive.google.com/file/d/1wirCsSM8Q3gJPGEmdhxuLNekRDyqm_mK/view?usp=sharing"),
    ("Decision tree", "https://drive.google.com/file/d/1k3GUIMXQCLLEYTi2JxLGI-ZMSOTmmPKP/view?usp=sharing"),
    ("Decision Tree 2", "https://drive.google.com/file/d/1N9yVlKjKaVG1VLex2HiyyFkqqAIGE3fe/view?usp=sharing"),
    ("em", "https://drive.google.com/file/d/1KIPY4QF9oeGLijyobHn2BL7WWwI9Xpil/view?usp=sharing"),
("KMeans", "https://drive.google.com/file/d/10dxf4upFwjq1aS_5SI8FDy6MBPQquEVS/view?usp=sharing"),
("KNN", "https://drive.google.com/file/d/1mQs1az6L2z6f4hwEvsDLKEK5ujcQdrRk/view?usp=sharing"),
("multivar", "https://drive.google.com/file/d/1bUBwa6U5a8P0EBvNSR_zjwVCmnBOBdfG/view?usp=sharing"),
    ("navie","https://drive.google.com/file/d/1qzyD8SRdaoEH77xjcHiRM5irhytJiwCj/view?usp=sharing"),
    ("svm","https://drive.google.com/file/d/1ozGbjBkXZbYskc4YmVLQ7zArJpQYVSE6/view?usp=sharing"),
    ("lab1","https://drive.google.com/file/d/1yr4VW4Q4sZXl2ZMFCeKs8tOqoriFv0GU/view?usp=sharing")
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
