import os
import datetime

# --- DATI DA INSERIRE ---
AUTHOR_NAME = "Elisabetta Agnello"
GITHUB_USER = "elisabettagnello"
SHEEP_LINK = "https://sheeptechnologies.com"
EMAIL_LINK = "agnelloe24@gmail.com"

# Link automatici
GITHUB_LINK = f"https://github.com/{GITHUB_USER}"

card_template = """
<div class="card">
    <div class="card-icon">
        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
    </div>
    <h3>{title}</h3>
    <div class="card-meta">
        <span class="badge">PDF</span>
        <span class="badge">{size}</span>
        <span>{date}</span>
    </div>
    <a href="pdfs/{filename}" class="download-btn" target="_blank">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
        Scarica Appunti
    </a>
</div>
"""

def get_file_size(file_path):
    try:
        size_bytes = os.path.getsize(file_path)
        if size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.0f} KB"
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    except:
        return "Unknown"

def generate_index():
    pdf_dir = "public/pdfs"
    cards = ""
    
    # 1. Genera le Card
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir, exist_ok=True)

    files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    
    if not files:
        cards = "<div class='card' style='grid-column:1/-1; text-align:center;'><h3>Nessun PDF ancora presente</h3></div>"
    
    for filename in sorted(files):
        title = filename.replace("-", " ").replace("_", " ").replace(".pdf", "").title()
        file_path = os.path.join(pdf_dir, filename)
        
        try:
            mod_time = os.path.getmtime(file_path)
            date_str = datetime.datetime.fromtimestamp(mod_time).strftime('%d %b %Y')
            size_str = get_file_size(file_path)
        except:
            date_str = "-"
            size_str = "-"

        cards += card_template.format(
            title=title, filename=filename, date=date_str, size=size_str
        )
    
    # 2. Leggi il template esterno
    template_path = os.path.join(os.path.dirname(__file__), 'template.html')
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 3. Sostituisci i segnaposto
    final_html = html_content.replace("{{AUTHOR_NAME}}", AUTHOR_NAME) \
                             .replace("{{GITHUB_USER}}", GITHUB_USER) \
                             .replace("{{GITHUB_LINK}}", GITHUB_LINK) \
                             .replace("{{SHEEP_LINK}}", SHEEP_LINK) \
                             .replace("{{EMAIL_LINK}}", EMAIL_LINK) \
                             .replace("{{CARDS}}", cards)

    # 4. Scrivi il file finale
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print(" ")

if __name__ == "__main__":
    generate_index()
