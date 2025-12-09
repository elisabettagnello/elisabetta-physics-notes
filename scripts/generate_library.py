import os

html_template = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elisabetta's Physics Notes</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f4f4f9; }
        h1 { color: #333; text-align: center; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); transition: transform 0.2s; }
        .card:hover { transform: translateY(-5px); }
        .btn { display: block; text-align: center; background: #007bff; color: white; padding: 10px; text-decoration: none; border-radius: 4px; margin-top: 10px; }
        .preview { width: 100%; height: 150px; background-color: #eee; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>📚 Appunti Universitari di Fisica </h1>
    <p style="text-align:center">Raccolta open source dei miei appunti universitari (Sapienza, Università di Roma).</p>
    <div class="grid">
        {cards}
    </div>
</body>
</html>
"""

card_template = """
<div class="card">
    <div class="preview">📄 Anteprima</div>
    <h3>{title}</h3>
    <a href="pdfs/{filename}" class="btn" target="_blank">👁️ Leggi / Scarica PDF</a>
</div>
"""

def generate_index():
    pdf_dir = "public/pdfs"
    cards = ""
    
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # Scansiona la cartella dei PDF
    for filename in sorted(os.listdir(pdf_dir)):
        if filename.endswith(".pdf"):
            title = filename.replace("-", " ").replace(".pdf", "").title()
            cards += card_template.format(title=title, filename=filename)
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html_template.replace("{cards}", cards))

if __name__ == "__main__":
    generate_index()