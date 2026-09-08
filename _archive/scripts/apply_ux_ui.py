import glob, re

css_addition = """
/* ==========================================================
   UI/UX PREMIUM ENHANCEMENTS (V4.1)
   ========================================================== */

/* 1. Refinamiento Tipogrfico Global */
body {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
p {
    line-height: 1.65;
}
.badge-tech, .social-label, .cmd-badge, h5, h6 {
    letter-spacing: 0.05em;
}

/* 2. Scrollbar Personalizada (Webkit) */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #F8FAFC; 
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, var(--color-primary, #796bfc), var(--color-secondary, #cb6ce6));
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #6456f0, #b95bd5);
}

/* 3. Micro-Interacciones (Hover States) */
.offer-card, .plan-card {
    transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease;
}
.offer-card:hover, .plan-card:hover {
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 20px 40px rgba(121, 107, 252, 0.15) !important;
}

.icon-tile, .card-icon, .feature-icon {
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.dd-card:hover .icon-tile, .offer-card:hover .card-icon, .plan-card:hover .feature-icon {
    transform: scale(1.1) rotate(-3deg);
}

.btn-aurora-gradient, .lead-submit, .btn-hero-primary {
    transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.3s ease !important;
}
.btn-aurora-gradient:hover, .lead-submit:hover, .btn-hero-primary:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 12px 25px rgba(203, 108, 230, 0.35) !important;
}

/* 4. Inputs Premium (Focus Rings) */
input:not([type="checkbox"]):not([type="radio"]), select, textarea {
    transition: border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
}
input:not([type="checkbox"]):not([type="radio"]):focus, select:focus, textarea:focus, 
.lead-input:focus, .pd-input:focus, .native-premium-input:focus {
    border-color: #2ed9c3 !important;
    box-shadow: 0 0 0 4px rgba(46, 217, 195, 0.15) !important;
    outline: none !important;
}

/* 5. Glassmorphism Extra Polish */
.aurora-navbar, .hero-glass-card, .nav-command-center, .alex-chat-window, .dropdown-glass-panel, .glass-modal-content {
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.4), 0 20px 50px -10px rgba(15, 23, 42, 0.15) !important;
}

/* Intensificar saturacin del cristal en navbar y hero */
.aurora-navbar, .hero-glass-card {
    backdrop-filter: blur(20px) saturate(150%) !important;
    -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
}
"""

print("Appending UX/UI fixes...")
for css_file in ['css/style.css', 'css/style-quote.css']:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write('\n' + css_addition)

print("Updating cache buster...")
import time
new_v = str(int(time.time()))

html_files = glob.glob('**/*.html', recursive=True)
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'(\.css\?v=)\d+', r'\g<1>' + new_v, content)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("UX/UI Fixes applied and cache buster updated!")
