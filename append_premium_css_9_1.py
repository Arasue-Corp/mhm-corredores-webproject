with open("css/style-quote.css", "a", encoding="utf-8") as f:
    f.write("""

/* =========================================
   PREMIUM MODAL UPGRADE
   ========================================= */
.premium-modal-glass {
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    border-radius: 24px;
    padding: 40px 30px;
    max-width: 450px;
    width: 90%;
    margin: auto;
    text-align: center;
    position: relative;
    animation: scaleUpGlass 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes scaleUpGlass {
    from { transform: scale(0.95) translateY(20px); opacity: 0; }
    to { transform: scale(1) translateY(0); opacity: 1; }
}

.modal-floating-icon {
    width: 80px; height: 80px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 2rem; margin: -80px auto 20px;
    background: white; border: 4px solid white;
}
.modal-floating-icon.blue-glow {
    color: #3B82F6; box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
}
.modal-floating-icon.purple-glow {
    color: #8B5CF6; box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3);
}

.modal-premium-title { font-weight: 800; font-size: 1.5rem; color: #1E293B; margin-bottom: 10px; }
.modal-premium-desc { color: #64748B; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.5; }

.email-display-card {
    background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px;
    padding: 15px; display: flex; align-items: center; gap: 12px; margin-bottom: 30px;
}
.ed-icon { color: #94A3B8; font-size: 1.2rem; }
.ed-text { flex: 1; font-weight: 700; color: #334155; text-align: left; }
.ed-badge { background: #DCFCE7; color: #16A34A; font-size: 0.75rem; font-weight: 800; padding: 4px 8px; border-radius: 50px; }

.modal-action-stack { display: flex; flex-direction: column; gap: 12px; }
.btn-ghost-premium {
    background: transparent; border: 1px solid #CBD5E1; color: #475569;
    padding: 14px; border-radius: 12px; font-weight: 600; cursor: pointer; transition: 0.3s;
}
.btn-ghost-premium:hover { background: #F1F5F9; border-color: #94A3B8; }

.pin-box-premium {
    width: 55px; height: 65px; font-size: 2rem; font-weight: 800;
    text-align: center; border: 2px solid #E2E8F0; border-radius: 16px;
    background: #F8FAFC; color: #1E293B; outline: none; transition: 0.3s;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
}
.pin-box-premium:focus { border-color: #8B5CF6; background: white; box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.15); }
.resend-text { font-size: 0.85rem; color: #64748B; margin-bottom: 30px; }
.resend-text span { font-weight: 700; color: #8B5CF6; cursor: pointer; }


/* =========================================
   PREMIUM DASHBOARD CARDS (PLAN & PAGADOR)
   ========================================= */
.dashboard-grid-main {
    display: grid; grid-template-columns: 1fr 1fr; gap: 20px;
}
@media (max-width: 768px) { .dashboard-grid-main { grid-template-columns: 1fr; } }

.dashboard-card {
    background: white; border: 1px solid #E2E8F0; border-radius: 20px;
    padding: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.02);
}
.dc-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
.dc-icon {
    width: 40px; height: 40px; border-radius: 12px; background: #EFF6FF;
    color: #3B82F6; display: flex; align-items: center; justify-content: center; font-size: 1.1rem;
}
.dc-icon.purple { background: #F5F3FF; color: #8B5CF6; }
.dc-title { font-weight: 800; font-size: 1.1rem; color: #1E293B; }

.receipt-amount-big {
    font-size: 2.5rem; font-weight: 900; color: #0F172A; margin-bottom: 20px;
}
.receipt-amount-big .currency { font-size: 1.2rem; color: #64748B; vertical-align: super; font-weight: 700; }

.receipt-breakdown { display: flex; flex-direction: column; gap: 12px; }
.rb-row { display: flex; justify-content: space-between; font-size: 0.95rem; }
.rb-label { color: #64748B; }
.rb-value { font-weight: 700; color: #334155; }
.rb-divider { height: 1px; border-top: 1px dashed #CBD5E1; margin: 5px 0; }
.rb-row.highlight .rb-value { color: #3B82F6; font-size: 1.05rem; }

.payer-data-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
.pd-item { display: flex; flex-direction: column; gap: 4px; }
.pd-item.full-width { grid-column: span 2; }
.pd-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; color: #94A3B8; font-weight: 700; }
.pd-value { font-size: 0.95rem; font-weight: 600; color: #1E293B; }


/* =========================================
   MODERN TOGGLE BOXES & SEGMENTED CONTROL
   ========================================= */
.modern-toggle-box {
    display: flex; justify-content: space-between; align-items: center;
    background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 16px; padding: 15px 20px;
}
.modern-toggle-box.highlight-box { background: #F0FDF4; border-color: #BBF7D0; }
.mtb-info { display: flex; align-items: center; gap: 15px; }
.mtb-icon {
    width: 40px; height: 40px; border-radius: 50%; background: white;
    color: #64748B; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.mtb-icon.teal { color: #10B981; }
.mtb-title { font-weight: 800; color: #1E293B; font-size: 1rem; }
.mtb-desc { font-size: 0.8rem; color: #64748B; }

.ios-segmented-control {
    display: flex; position: relative; background: #E2E8F0; border-radius: 12px;
    padding: 4px; overflow: hidden;
}
.ios-segment {
    flex: 1; text-align: center; padding: 12px; font-weight: 700; color: #64748B;
    border: none; background: transparent; cursor: pointer; position: relative; z-index: 2;
    transition: color 0.3s;
}
.ios-segment.active { color: #1E293B; }
.ios-segment-pill {
    position: absolute; top: 4px; left: 4px; height: calc(100% - 8px); width: calc(50% - 4px);
    background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    z-index: 1; transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1);
}

""")
print("Premium CSS Appended")
