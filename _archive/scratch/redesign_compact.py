import glob, os, re

css_compact = """
/* ---- REDESIGN UX/UI COMPACT & PREMIUM ---- */
.veh-type-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)) !important;
    gap: 20px !important;
    margin-bottom: 40px !important;
    align-items: stretch !important;
    justify-content: center !important;
    max-width: 1200px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
.veh-type-card {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 20px !important;
    padding: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    position: relative !important;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08), 0 4px 10px -3px rgba(15, 23, 42, 0.04) !important;
    transition: transform 300ms ease, box-shadow 300ms ease !important;
    max-width: none !important;
    width: 100% !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
}
.veh-type-card:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 20px 40px -8px rgba(15, 23, 42, 0.12), 0 8px 16px -6px rgba(15, 23, 42, 0.06) !important;
}
.vt-image {
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 4 / 5 !important;
    border-radius: 0 !important;
    margin-bottom: 0 !important;
    box-shadow: none !important;
    overflow: hidden !important;
}
.vt-image img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center 30% !important;
    transition: transform 500ms ease !important;
}
.veh-type-card:hover .vt-image img {
    transform: scale(1.05) !important;
}
.vt-info {
    display: flex !important;
    flex-direction: column !important;
    flex: 1 !important;
    padding: 16px 20px 20px 20px !important;
}
.vt-info h4 {
    color: #0F172A !important;
    font-size: 1.3rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em !important;
    margin-bottom: 6px !important;
    text-align: left !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 6px !important;
    line-height: 1.2 !important;
}
.vt-info h4 br {
    display: none !important;
}
.plan-price {
    font-size: 1.2rem !important;
    font-weight: 800 !important;
    color: #2563EB !important;
    margin-bottom: 12px !important;
    font-variant-numeric: tabular-nums !important;
    text-align: left !important;
}
.pet-feature-list {
    margin-top: 0 !important;
    margin-bottom: 20px !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    flex: 1 !important;
}
.pet-feature-list li {
    display: grid !important;
    grid-template-columns: 18px 1fr !important;
    gap: 8px !important;
    align-items: start !important;
    text-wrap: pretty !important;
    line-height: 1.3 !important;
    font-size: 0.9rem !important;
    color: #475569 !important;
    font-weight: 500 !important;
}
.pet-feature-list li i {
    margin-top: 3px !important;
    color: #10B981 !important;
    font-size: 0.85rem !important;
}
.card-actions-row {
    display: flex !important;
    flex-direction: row !important;
    gap: 8px !important;
    margin-top: auto !important;
    width: 100% !important;
    align-items: center !important;
}
.qty-controls {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    background: #F8FAFC !important;
    border-radius: 14px !important;
    padding: 4px !important;
    border: 1px solid #E2E8F0 !important;
    margin-top: 0 !important;
    width: auto !important;
    box-sizing: border-box !important;
    gap: 4px !important;
}
.qty-btn {
    width: 38px !important;
    height: 38px !important;
    border-radius: 10px !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.03) !important;
    background: #FFFFFF !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: #0F172A !important;
    font-size: 1rem !important;
    border: 1px solid #E2E8F0 !important;
    cursor: pointer !important;
    transition: all 150ms ease !important;
}
.qty-btn:hover { background: #F1F5F9 !important; transform: translateY(-1px) !important; box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important; }
.qty-btn:active { transform: scale(0.96) !important; }
.qty-value { 
    flex: none !important;
    width: 30px !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    color: #0F172A !important;
    font-variant-numeric: tabular-nums !important;
    text-align: center !important;
}
.btn-outline-premium, .btn-primary-premium {
    flex: 1 !important;
    width: auto !important;
    border-radius: 14px !important;
    padding: 12px 14px !important;
    margin-top: 0 !important;
    background: #FFFFFF !important;
    border: 2px solid #E2E8F0 !important;
    color: #0F172A !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 8px !important;
    cursor: pointer !important;
    transition: all 200ms ease !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
    text-align: center !important;
    line-height: 1.2 !important;
}
.btn-outline-premium:hover, .btn-primary-premium:hover {
    background: #F8FAFC !important;
    border-color: #CBD5E1 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.04) !important;
}
.btn-outline-premium:active, .btn-primary-premium:active { transform: translateY(0) scale(0.98) !important; }

.pro-card {
    border: 2px solid #3B82F6 !important;
}
.pro-card .vt-info {
    background: linear-gradient(180deg, rgba(59, 130, 246, 0.03) 0%, rgba(255, 255, 255, 0) 100%) !important;
}
.pro-card .btn-outline-premium, .pro-card .btn-primary-premium {
    border: 2px solid #3B82F6 !important;
    background: #3B82F6 !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2) !important;
}
.pro-card .btn-outline-premium:hover, .pro-card .btn-primary-premium:hover {
    background: #2563EB !important;
    border-color: #2563EB !important;
    box-shadow: 0 6px 16px rgba(59, 130, 246, 0.3) !important;
}
/* ---- END REDESIGN COMPACT ---- */
"""

files = glob.glob('cotizacion/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the previous robust redesign CSS block safely if it exists
    content = re.sub(r'/\* ---- REDESIGN UX/UI ROBUST & PREMIUM ---- \*/.*?/\* ---- END REDESIGN ROBUST ---- \*/', '', content, flags=re.DOTALL)
    content = re.sub(r'/\* ---- REDESIGN UX/UI LIQUID GLASS ---- \*/.*?/\* ---- END REDESIGN ---- \*/', '', content, flags=re.DOTALL)
    
    # If this compact block is already there, remove it too so we can inject a fresh one
    content = re.sub(r'/\* ---- REDESIGN UX/UI COMPACT & PREMIUM ---- \*/.*?/\* ---- END REDESIGN COMPACT ---- \*/', '', content, flags=re.DOTALL)

    # Append the compact CSS right before </style>
    content = content.replace('</style>', css_compact + '\n</style>', 1)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {file}")
