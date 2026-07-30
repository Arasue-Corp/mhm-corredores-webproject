import os, glob, re

css_override = """
/* ---- REDESIGN UX/UI LIQUID GLASS ---- */
.veh-type-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
    gap: 20px !important;
    margin-bottom: 40px !important;
    align-items: stretch !important;
    justify-content: center !important;
    max-width: 1200px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
.veh-type-card {
    background: rgba(255, 255, 255, 0.7) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 24px !important;
    padding: 16px !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    position: relative !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04), inset 0 1px 0 rgba(255, 255, 255, 1) !important;
    transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1), box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) !important;
    max-width: none !important;
    width: 100% !important;
    box-sizing: border-box !important;
}
.veh-type-card:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 1) !important;
}
.vt-image {
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 4 / 3 !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
    margin-bottom: 0 !important;
}
.vt-image img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    transition: transform 400ms ease !important;
    outline: 1px solid rgba(0, 0, 0, 0.05) !important;
    outline-offset: -1px !important;
}
.veh-type-card:hover .vt-image img {
    transform: scale(1.03) !important;
}
.vt-info {
    display: flex !important;
    flex-direction: column !important;
    flex: 1 !important;
    padding: 0 8px !important;
}
.vt-info h4 {
    color: #0F172A !important;
    font-size: 1.3rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em !important;
    text-wrap: balance !important;
    margin-bottom: 4px !important;
    text-align: left !important;
}
.plan-price {
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    margin-bottom: 12px !important;
    font-variant-numeric: tabular-nums !important;
    text-align: left !important;
}
.pet-feature-list {
    margin-top: 0 !important;
    margin-bottom: 16px !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 6px !important;
    flex: 1 !important;
}
.pet-feature-list li {
    align-items: flex-start !important;
    text-wrap: pretty !important;
    line-height: 1.3 !important;
}
.card-actions-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-top: auto;
    width: 100%;
}
.qty-controls {
    display: flex !important;
    align-items: center !important;
    background: #F1F5F9 !important;
    border-radius: 99px !important;
    padding: 2px !important;
    border: 1px solid #E2E8F0 !important;
    margin-top: 0 !important;
    width: auto !important;
}
.qty-btn {
    width: 34px !important;
    height: 34px !important;
    border-radius: 50% !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
    background: white !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.qty-btn:hover { background: #E2E8F0 !important; transform: scale(1.05) !important; }
.qty-btn:active { transform: scale(0.95) !important; }
.qty-value { 
    width: 32px !important; 
    font-size: 1rem !important;
    font-variant-numeric: tabular-nums !important;
    text-align: center !important;
}
.btn-outline-premium, .btn-primary-premium {
    flex: 1 !important;
    border-radius: 14px !important;
    padding: 12px 14px !important;
    margin-top: 0 !important;
    background: rgba(46, 217, 195, 0.1) !important;
    border: 1px solid rgba(46, 217, 195, 0.4) !important;
    color: #0F172A !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 8px !important;
    cursor: pointer !important;
    transition: all 150ms ease !important;
}
.btn-outline-premium:hover, .btn-primary-premium:hover {
    background: rgba(46, 217, 195, 0.2) !important;
    border-color: #2ED9C3 !important;
    transform: translateY(-2px) !important;
}
.btn-outline-premium:active, .btn-primary-premium:active { transform: scale(0.98) !important; }

.pro-card .btn-outline-premium, .pro-card .btn-primary-premium {
    border: 1px solid rgba(37, 99, 235, 0.3) !important;
    background: rgba(37, 99, 235, 0.05) !important;
    color: #2563EB !important;
}
.pro-card .btn-outline-premium:hover, .pro-card .btn-primary-premium:hover {
    background: rgba(37, 99, 235, 0.1) !important;
    border-color: #2563EB !important;
}
/* ---- END REDESIGN ---- */
"""

files = glob.glob('cotizacion/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Append CSS override right before </style>
    if '/* ---- REDESIGN UX/UI LIQUID GLASS ---- */' not in content:
        # Avoid appending multiple times if run repeatedly
        content = content.replace('</style>', css_override + '\n</style>', 1)
        
    # HTML modification for qty-controls and button
    # Find all occurrences of qty-controls followed by a button and wrap them in card-actions-row
    # Regex looks for <div class="qty-controls">...</div> followed by whitespace and <button ...>...</button>
    
    # We use a loop or re.sub. We must be careful not to wrap already wrapped ones.
    if 'card-actions-row' not in content:
        content = re.sub(
            r'(<div class="qty-controls">.*?</div>)\s*(<button[^>]+>.*?</button>)',
            r'<div class="card-actions-row">\n\1\n\2\n</div>',
            content,
            flags=re.DOTALL
        )
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {file}")
