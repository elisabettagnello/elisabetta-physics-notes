import os
import datetime

# --- CONFIGURAZIONE ---
AUTHOR_NAME = "Elisabetta Agnello"
GITHUB_USER = "elisabettagnello"
SHEEP_LINK = "https://sheeptechnologies.com"
EMAIL_LINK = "agnelloe24@gmail.com"
GITHUB_LINK = f"https://github.com/{GITHUB_USER}"

# --- COLLEZIONE ICONE (SVG) ---
ICONS = {
    # 1. BATTERIO (Theoretical Biophysics) - Nuovo!
    "bacterium": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="6" y="8" width="12" height="8" rx="4" /><path d="M18 12h2"/><path d="M4 12h2"/><path d="M7 6l1 2"/><path d="M17 6l-1 2"/><path d="M7 18l1-2"/><path d="M17 18l-1-2"/><path d="M22 12c1 0 1-2 2-2"/></svg>""",
    
    # 2. CRITICAL PHENOMENA (Campo/Vortice)
    "feynman": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 12c0-1.66 4-3 9-3s9 1.34 9 3"/><path d="M21 12c0 4.42-4 8-9 8s-9-3.58-9-8"/><path d="M3 12c0-4.42 4-8 9-8s9 3.58 9 8"/><circle cx="12" cy="12" r="3"/></svg>""",
    
    # 3. SPIN GLASS / ISING (Reticolo)
    "ising": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path stroke-linecap="round" stroke-linejoin="round" d="M8 8l0 2m0-4l0 2m8 4l0-2m0 4l0-2m-4 4l0 2m0-4l0 2m-4 4l0 2m0-4l0 2m8-4l0-2m0 4l0-2"/></svg>""",
    
    # 4. MICROSCOPIO (Biosistemi)
    "microscope": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 20v-6h4v6m-2-6V9m-2 0h4l-1-5h-2l-1 5zM3 20h18M14 14l5-5"/><path stroke-linecap="round" stroke-linejoin="round" d="M18 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/></svg>""",
    
    # 5. FISICA GENERICA (Atomo)
    "physics": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>""",
    
    # 6. LIBRO (Default)
    "book": """<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>"""
}

# --- TEMPLATE CARD HTML ---
card_template = """
<div class="card">
    <div class="card-icon">
        {icon_svg}
    </div>
    <h3>{title}</h3>
    <div class="card-meta">
        <span class="badge">PDF</span>
        <span class="badge">{size}</span>
        <span>{date}</span>
    </div>
    <a href="pdfs/{filename}" class="download-btn" target="_blank">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="width:18px;height:18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
        View/Download
    </a>
</div>
"""

def get_icon_for_title(title):
    """Sceglie l'icona in base alle parole chiave nel titolo"""
    t = title.lower()
    
    # Logica di assegnazione
    if "bio" in t or "neur" in t or "life" in t:
        # Se c'è "lab", vince il microscopio, altrimenti batterio per biofisica
        if "lab" in t:
            return ICONS["microscope"]
        return ICONS["bacterium"] 
        
    elif "critical" in t or "phenomena" in t or "field" in t:
        return ICONS["feynman"] 
        
    elif "disordered" in t or "spin" in t or "glass" in t or "ising" in t:
        return ICONS["ising"]
        
    elif "lab" in t or "micro" in t:
        return ICONS["microscope"]
        
    elif "non" in t and "equilibrium" in t:
        return ICONS["physics"]
        
    elif "stat" in t or "mech" in t or "phys" in t:
        return ICONS["physics"]
        
    else:
        return ICONS["book"]

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
    
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir, exist_ok=True)

    files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    
    if not files:
        cards = "<div style='grid-column:1/-1; text-align:center; color:#94a3b8;'><h3>No PDFs found yet...</h3></div>"
    
    for filename in sorted(files):
        # Pulisce il titolo
        title = filename.replace("-", " ").replace("_", " ").replace(".pdf", "").title()
        
        file_path = os.path.join(pdf_dir, filename)
        
        try:
            mod_time = os.path.getmtime(file_path)
            date_str = datetime.datetime.fromtimestamp(mod_time).strftime('%d %b %Y')
            size_str = get_file_size(file_path)
        except:
            date_str = "-"
            size_str = "-"

        # Seleziona icona
        icon_svg = get_icon_for_title(title)

        cards += card_template.format(
            title=title, 
            filename=filename, 
            date=date_str, 
            size=size_str,
            icon_svg=icon_svg
        )
    
    # Leggi e compila template
    template_path = os.path.join(os.path.dirname(__file__), 'template.html')
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    final_html = html_content.replace("{{AUTHOR_NAME}}", AUTHOR_NAME) \
                             .replace("{{GITHUB_USER}}", GITHUB_USER) \
                             .replace("{{GITHUB_LINK}}", GITHUB_LINK) \
                             .replace("{{SHEEP_LINK}}", SHEEP_LINK) \
                             .replace("{{EMAIL_LINK}}", EMAIL_LINK) \
                             .replace("{{CARDS}}", cards)

    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print("✨ Libreria generata con icona Batterio per Biofisica!")

if __name__ == "__main__":
    generate_index()
