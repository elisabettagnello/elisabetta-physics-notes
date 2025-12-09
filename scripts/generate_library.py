import os
import datetime

# --- CONFIGURAZIONE PROFILO ---
AUTHOR_NAME = "Elisabetta Agnello"
ROLE_DESC = "M.Sc. Student in Statistical Physics & Complex Systems @ Sapienza | Co-Founder @ Sheep"
GITHUB_USER = "elisabettagnello"
REPO_NAME = "elisabetta-physics-notes"

# Link
GITHUB_LINK = f"https://github.com/{GITHUB_USER}"
REPO_LINK = f"https://github.com/{GITHUB_USER}/{REPO_NAME}"
SHEEP_LINK = "https://sheeptechnologies.com"
EMAIL_LINK = "agnelloe24@gmail.com"

html_template = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Physics Notes | {author}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #4f46e5;
            --primary-glow: #818cf8;
            --secondary: #ec4899;
            --bg-dark: #0f172a;
            --card-bg: rgba(255, 255, 255, 0.85);
            --card-border: rgba(255, 255, 255, 0.5);
            --text-main: #1e293b;
            --text-muted: #64748b;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f0f4f8;
            color: var(--text-main);
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }}

        /* Sfondo Animato "Aurora" */
        .background-gradient {{
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            z-index: -1;
            background: 
                radial-gradient(circle at 15% 50%, rgba(79, 70, 229, 0.15), transparent 25%),
                radial-gradient(circle at 85% 30%, rgba(236, 72, 153, 0.15), transparent 25%);
            filter: blur(40px);
            animation: pulse 10s ease-in-out infinite alternate;
        }}

        @keyframes pulse {{
            0% {{ transform: scale(1); opacity: 0.8; }}
            100% {{ transform: scale(1.1); opacity: 1; }}
        }}

        /* Container */
        .container {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        /* Header */
        header {{
            padding: 80px 0 60px;
            text-align: center;
        }}

        .avatar {{
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-bottom: 20px;
            border: 3px solid white;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            object-fit: cover;
        }}

        h1 {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #1e293b 0%, #4f46e5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            letter-spacing: -0.03em;
        }}

        .role {{
            font-size: 1.1rem;
            color: var(--text-muted);
            font-weight: 400;
            max-width: 600px;
            margin: 0 auto 30px;
            line-height: 1.6;
        }}

        .social-links {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap; /* Fondamentale per mobile */
        }}

        .btn-social {{
            text-decoration: none;
            color: var(--text-main);
            background: white;
            padding: 10px 20px;
            border-radius: 99px;
            font-size: 0.9rem;
            font-weight: 600;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: all 0.2s;
            border: 1px solid rgba(0,0,0,0.05);
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}

        .btn-social:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 15px rgba(0,0,0,0.1);
            color: var(--primary);
            border-color: var(--primary-glow);
        }}

        /* Grid Layout */
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 30px;
            padding-bottom: 80px;
        }}

        /* Card Design */
        .card {{
            background: var(--card-bg);
            border: 1px solid white;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 
                0 4px 6px -1px rgba(0, 0, 0, 0.05), 
                0 2px 4px -1px rgba(0, 0, 0, 0.03),
                inset 0 0 0 1px rgba(255,255,255,0.5);
            backdrop-filter: blur(20px);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }}

        .card:hover {{
            transform: translateY(-8px) scale(1.01);
            box-shadow: 
                0 20px 25px -5px rgba(0, 0, 0, 0.1), 
                0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border-color: rgba(79, 70, 229, 0.2);
        }}

        .card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 6px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            opacity: 0;
            transition: opacity 0.3s;
        }}
        
        .card:hover::before {{ opacity: 1; }}

        .card-icon {{
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            margin-bottom: 20px;
            font-size: 1.5rem;
        }}

        .card h3 {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.4rem;
            margin-bottom: 8px;
            color: #0f172a;
        }}

        .card-meta {{
            font-size: 0.85rem;
            color: #64748b;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .badge {{
            background: #f1f5f9;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 500;
            font-size: 0.75rem;
            color: #475569;
        }}

        .download-btn {{
            margin-top: auto;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: #0f172a;
            color: white;
            text-decoration: none;
            padding: 14px;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.2s;
        }}

        .download-btn:hover {{
            background: var(--primary);
            transform: scale(1.02);
        }}

        .download-btn svg {{ width: 18px; height: 18px; }}

        footer {{
            text-align: center;
            padding: 40px;
            color: var(--text-muted);
            font-size: 0.9rem;
            border-top: 1px solid rgba(0,0,0,0.05);
        }}
        
        footer a {{ color: var(--primary); text-decoration: none; }}

        /* Dark Mode Support */
        @media (prefers-color-scheme: dark) {{
            body {{ background-color: #0b1120; color: #f1f5f9; }}
            .card {{ background: rgba(30, 41, 59, 0.7); border-color: rgba(255,255,255,0.1); }}
            h1 {{ background: linear-gradient(135deg, #fff 0%, #a5b4fc 100%); -webkit-background-clip: text; }}
            .card h3 {{ color: white; }}
            .card-meta, .role {{ color: #94a3b8; }}
            .badge {{ background: rgba(255,255,255,0.1); color: #cbd5e1; }}
            .btn-social {{ background: rgba(255,255,255,0.05); color: white; border-color: rgba(255,255,255,0.1); }}
            .download-btn {{ background: white; color: #0f172a; }}
            .download-btn:hover {{ background: var(--primary-glow); }}
        }}
    </style>
</head>
<body>
    <div class="background-gradient"></div>

    <div class="container">
        <header>
            <img src="https://github.com/{github_user}.png" alt="Profile" class="avatar">
            
            <h1>Physics Notes Library</h1>
            <p class="role">{role}</p>
            
            <div class="social-links">
                <a href="{sheep_link}" class="btn-social" target="_blank">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
                    Sheep Tech
                </a>
                
                <a href="mailto:{email}" class="btn-social">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                    Contattami
                </a>

                <a href="{github_link}" class="btn-social" target="_blank">
                    <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    GitHub
                </a>
            </div>
        </header>

        <main class="grid">
            {cards}
        </main>

        <footer>
            <p>Designed with ⚛️ by {author} &bull; <a href="{sheep_link}" target="_blank">Sheep Technologies</a></p>
        </footer>
    </div>
</body>
</html>
"""

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
    size_bytes = os.path.getsize(file_path)
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.0f} KB"
    return f"{size_bytes / (1024 * 1024):.1f} MB"

def generate_index():
    pdf_dir = "public/pdfs"
    cards = ""
    
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir, exist_ok=True)

    files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    
    if not files:
        cards = """<div style="grid-column: 1/-1; text-align: center; padding: 60px; background: rgba(255,255,255,0.5); border-radius: 20px;">
                    <h3 style="color: var(--text-muted);">Nessun file PDF trovato...</h3>
                   </div>"""
    
    for filename in sorted(files):
        title = filename.replace("-", " ").replace("_", " ").replace(".pdf", "").title()
        file_path = os.path.join(pdf_dir, filename)
        
        mod_time = os.path.getmtime(file_path)
        date_str = datetime.datetime.fromtimestamp(mod_time).strftime('%d %b %Y')
        size_str = get_file_size(file_path)

        cards += card_template.format(
            title=title, 
            filename=filename, 
            date=date_str,
            size=size_str
        )
    
    output_html = html_template.format(
        author=AUTHOR_NAME,
        role=ROLE_DESC,
        github_user=GITHUB_USER,
        github_link=GITHUB_LINK,
        repo_link=REPO_LINK,
        sheep_link=SHEEP_LINK,
        email=EMAIL_LINK,
        cards=cards
    )
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(output_html)
    
    print("✨ Libreria aggiornata con contatti e link Sheep!")

if __name__ == "__main__":
    generate_index()
