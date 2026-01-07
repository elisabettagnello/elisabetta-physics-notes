import os
import json

# --- CONFIGURAZIONE ---
AUTHOR_NAME = "Elisabetta Agnello"
GITHUB_USER = "elisabettagnello"
SHEEP_LINK = "https://sheeptechnologies.com"
EMAIL_LINK = "agnelloe24@gmail.com"
GITHUB_LINK = f"https://github.com/{GITHUB_USER}"

# --- ICONE ---
ICONS = {
    "open_book": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>""",
    "stack_books": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/><path stroke-linecap="round" stroke-linejoin="round" d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2c1.798 0 3.298 1.044 4.5 2.5c1.202-1.456 2.702-2.5 4.5-2.5A2.5 2.5 0 0 1 18 4.5v15"/></svg>""",
    "ruler": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"/></svg>""",
    "closed_book": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25"/></svg>""",
    "atom": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>"""
}

# --- TEMPLATE CARD HTML ---
card_template = """
<div class="card" data-title="{search_title}" data-year="{year}" data-code="{code}">
    <div class="card-icon">
        {icon_svg}
    </div>
    <h3>{title}</h3>
    <div class="card-meta">
        <span class="badge">{code}</span>
        <span class="badge">{year}</span>
    </div>
    <div class="card-meta" style="margin-top:0.5rem; opacity:0.8;">
        <span>PDF • {size}</span>
    </div>
    <a href="pdfs/{filename}" class="download-btn" target="_blank">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="width:18px;height:18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
        Download
    </a>
</div>
"""

def get_icon_for_title(title):
    t = title.lower()
    if "bio" in t or "neur" in t: return ICONS["open_book"]
    elif "disordered" in t or "spin" in t or "glass" in t: return ICONS["ruler"]
    elif "Lab" in t or "micro" in t: return ICONS["closed_book"]
    else: return ICONS["closed_book"]

def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        if size < 1024*1024: return f"{size/1024:.0f} KB"
        return f"{size/(1024*1024):.1f} MB"
    except: return "-"

def load_central_metadata():
    if os.path.exists("metadata.json"):
        try:
            with open("metadata.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Errore JSON: {e}")
    return {}

def get_latest_news():
    news_items = ""
    if os.path.exists("news.txt"):
        with open("news.txt", "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
            for line in lines[:5]:
                news_items += f"<li>{line}</li>\n"
    return news_items if news_items else "<li>Nessuna news recente.</li>"

def generate_index():
    pdf_dir = "public/pdfs"
    if not os.path.exists(pdf_dir): os.makedirs(pdf_dir, exist_ok=True)

    # Pulizia file nascosti (iniziano con _)
    files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    for f in files:
        if f.startswith("_"):
            public_v = f[1:]
            if os.path.join(pdf_dir, public_v) in [os.path.join(pdf_dir, x) for x in files]:
                os.remove(os.path.join(pdf_dir, public_v))

    files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf") and not f.startswith("_")]
    
    # 1. Carica Metadata
    metadata = load_central_metadata()
    
    file_list = []
    for filename in files:
        key = filename.replace(".pdf", "")
        # Se il file ha spazi nel nome (es. Statistical Mechanics...) la chiave deve matchare
        # Il PDF generato da GitHub di solito ha lo stesso nome della cartella src
        
        info = metadata.get(key, {
            "title": key.replace("-", " ").replace("_", " ").title(),
            "code": "Other",
            "year": "Magistrale",
            "order": 999
        })
        
        file_list.append({
            "filename": filename,
            "title": info["title"],
            "code": info["code"],
            "year": info["year"],
            "order": info["order"],
            "search_title": info["title"].lower()
        })
    
    file_list.sort(key=lambda x: (x["order"], x["title"]))

    cards_html = ""
    if not file_list:
        cards_html = "<div style='grid-column:1/-1;text-align:center;'><h3>No PDFs found...</h3></div>"
    
    for item in file_list:
        f_path = os.path.join(pdf_dir, item["filename"])
        cards_html += card_template.format(
            title=item["title"],
            filename=item["filename"],
            size=get_file_size(f_path),
            icon_svg=get_icon_for_title(item["title"]),
            year=item["year"],
            code=item["code"],
            search_title=item["search_title"]
        )

    with open("scripts/template.html", "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("{{AUTHOR_NAME}}", AUTHOR_NAME)\
               .replace("{{GITHUB_USER}}", GITHUB_USER)\
               .replace("{{GITHUB_LINK}}", GITHUB_LINK)\
               .replace("{{SHEEP_LINK}}", SHEEP_LINK)\
               .replace("{{EMAIL_LINK}}", EMAIL_LINK)\
               .replace("{{CARDS}}", cards_html)\
               .replace("{{NEWS_ITEMS}}", get_latest_news())

    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("Libreria aggiornata con metadata centralizzati!")

if __name__ == "__main__":
    generate_index()
