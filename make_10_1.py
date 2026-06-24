with open("cotizacion/cotizacion-9-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# Grab top part
top_part = content.split('<div class="page-wrapper">')[0]

# Grab bottom part
bottom_part = '<footer class="footer-aurora">' + content.split('<footer class="footer-aurora">')[1]

# Build new middle part
success_body = """
    <div class="page-wrapper" style="min-height: 80vh; display: flex; align-items: center; justify-content: center; padding: 40px 20px;">
        <div class="success-card-premium" style="max-width: 600px; width: 100%; background: white; border-radius: 24px; padding: 50px 40px; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.02); animation: slideUpFade 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;">
            
            <div class="success-icon-wrapper" style="width: 100px; height: 100px; background: #DCFCE7; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 30px; font-size: 3.5rem; color: #10B981; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.2);">
                <i class="fa-solid fa-check"></i>
            </div>
            
            <h1 class="text-gradient-corp" style="font-weight: 900; font-size: 1.8rem; margin-bottom: 25px; line-height: 1.3;">
                ¡FELICIDADES, TU NUEVO SEGURO YA SE ENCUENTRA ACTIVO!
            </h1>
            
            <div class="carrier-logo-box" style="margin-bottom: 20px;">
                <img src="../assets/img/logo-fid.webp" alt="FID Seguros" style="height: 60px; object-fit: contain;">
            </div>
            
            <h3 style="font-weight: 800; font-size: 1.4rem; color: #1E293B; margin-bottom: 15px;">
                ¡Genial! Te estábamos esperando
            </h3>
            
            <p style="color: #64748B; font-size: 1.05rem; line-height: 1.6; margin-bottom: 40px;">
                Nos pondremos en contacto contigo para brindarte detalles de tu póliza. 
                <strong>FID</strong> se encuentra emitiendo tu nuevo seguro, en los próximos minutos será enviado la póliza vía email y Whatsapp.
            </p>
            
            <a href="../index.html" class="btn-hero-gradient" style="padding: 16px 40px; font-size: 1.1rem; border-radius: 100px; display: inline-flex; align-items: center; gap: 10px; text-decoration: none;">
                <i class="fa-solid fa-house"></i> Volver a pantalla principal
            </a>
            
        </div>
    </div>
    
    <style>
        @keyframes slideUpFade {
            from { transform: translateY(40px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .success-card-premium {
            position: relative;
            overflow: hidden;
        }
        .success-card-premium::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 6px;
            background: linear-gradient(90deg, #10B981, #3B82F6);
        }
    </style>
"""

with open("cotizacion/cotizacion-10-1-fid.html", "w", encoding="utf-8") as f:
    f.write(top_part + success_body + bottom_part)

print("cotizacion-10-1-fid.html successfully generated!")
