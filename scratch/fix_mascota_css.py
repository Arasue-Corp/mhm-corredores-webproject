import re

css_to_add = """
        /* VEH TYPE CARD STYLES */
        .veh-type-card {
            height: 100%; box-sizing: border-box;
            background: #ffffff;
            border-radius: 24px;
            padding: 32px;
            overflow: hidden;
            position: relative;
            display: flex; flex-direction: column; align-items: stretch; text-align: left; gap: 20px;
            border: 1px solid rgba(226, 232, 240, 0.8);
            box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.04), 0 4px 10px -5px rgba(15, 23, 42, 0.02);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .veh-type-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.12), 0 0 0 1px rgba(121, 107, 252, 0.15);
            border-color: transparent;
        }

        .vt-image {
            width: 100%; aspect-ratio: 16 / 9; border-radius: 16px;
            overflow: hidden; margin-bottom: 5px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.06);
            background: #F8FAFC;
            position: relative;
        }
        .vt-image img {
            width: 100%; height: 100%; object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .veh-type-card:hover .vt-image img { transform: scale(1.08); }

        .vt-info { width: 100%; display: flex; flex-direction: column; flex-grow: 1; }
        .vt-info-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; }
        .vt-info h4 { margin: 0; color: #0F172A; font-size: 1.5rem; font-weight: 800; letter-spacing: -0.5px; line-height: 1.2; }

        .badge-recomendado {
            font-size: 0.65rem;
            line-height: 1;
            background: linear-gradient(135deg, #796bfc, #4F46E5);
            color: #ffffff;
            padding: 6px 12px;
            border-radius: 30px;
            font-weight: 800;
            display: inline-flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(121, 107, 252, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }

        .pro-card {
            border: 1px solid rgba(121, 107, 252, 0.3);
            box-shadow: 0 10px 30px -5px rgba(121, 107, 252, 0.1);
        }
        .pro-card .card-aurora-top {
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 6px;
            z-index: 10;
            background: linear-gradient(90deg, #796bfc, #2ED9C3, #796bfc);
            background-size: 200% 100%;
            animation: gradientMove 3s linear infinite;
        }
        @keyframes gradientMove {
            0% { background-position: 100% 0; }
            100% { background-position: -100% 0; }
        }
        
        .plan-price-wrapper { display: flex; align-items: baseline; gap: 6px; margin-bottom: 10px; }
        .plan-price-label { font-size: 0.9rem; color: #64748B; font-weight: 600; }
        .plan-price { font-size: 1.8rem; font-weight: 800; color: #796bfc; letter-spacing: -0.5px; }
        .plan-price-period { font-size: 1rem; color: #94A3B8; font-weight: 500; }

        .card-actions {
            display: flex; gap: 12px; flex-direction: column; margin-top: auto; padding-top: 24px;
        }
        
        .btn-primary-premium {
            width: 100%; border-radius: 12px; padding: 14px; font-weight: 700; 
            cursor: pointer; border: none; background: #2ED9C3; color: white;
            font-size: 1rem; transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(46, 217, 195, 0.3);
            display: flex; justify-content: center; align-items: center; gap: 8px;
        }
        .btn-primary-premium:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(46, 217, 195, 0.4);
            background: #25C7B3;
        }
        
        .btn-primary-premium.familiar {
            background: #796bfc;
            box-shadow: 0 4px 12px rgba(121, 107, 252, 0.3);
        }
        .btn-primary-premium.familiar:hover {
            background: #6355E0;
            box-shadow: 0 6px 16px rgba(121, 107, 252, 0.4);
        }

        .split-btn-container {
            display: grid; grid-template-columns: 1fr 1fr; gap: 12px; width: 100%;
        }
        .split-btn {
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            border-radius: 12px; padding: 10px 5px; font-weight: 700; cursor: pointer; border: none; 
            color: white; font-size: 0.95rem; line-height: 1.3; transition: all 0.3s ease;
        }
        .split-btn span {
            font-size: 0.8em; font-weight: 500; opacity: 0.9;
        }
"""

with open('cotizacion/cotizacion-mascota-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Only add if not already there
if '.veh-type-card {' not in content:
    new_content = content.replace('</style>', css_to_add + '\n</style>')
    with open('cotizacion/cotizacion-mascota-1.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("CSS added to mascota successfully.")
else:
    print("CSS already present.")
