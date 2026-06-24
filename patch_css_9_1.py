with open("css/style-quote.css", "a", encoding="utf-8") as f:
    f.write("""

/* =========================================
   PANTALLA 9-1: PAYMENTS & EMAIL MODAL
   ========================================= */

/* PIN Code Inputs for Email Modal */
.pin-box {
    width: 50px;
    height: 60px;
    font-size: 1.5rem;
    font-weight: 800;
    text-align: center;
    border: 2px solid #E2E8F0;
    border-radius: 12px;
    background: white;
    color: var(--quote-dark);
    outline: none;
    transition: all 0.2s ease;
}
.pin-box:focus {
    border-color: var(--quote-primary);
    box-shadow: 0 0 0 4px rgba(46, 217, 195, 0.15);
}

/* Payment Tabs */
.payment-tabs-container {
    display: flex;
    background: #F8FAFC;
    border-radius: 50px;
    padding: 6px;
    gap: 5px;
    border: 1px solid #E2E8F0;
}
.payment-tab {
    flex: 1;
    border: none;
    background: transparent;
    padding: 12px;
    border-radius: 50px;
    font-weight: 700;
    color: #64748b;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}
.payment-tab.active {
    background: white;
    color: var(--quote-indigo);
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}
.payment-form-box {
    animation: fadeInForm 0.4s ease-out forwards;
}

@keyframes fadeInForm {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

""")
print("CSS for 9-1 appended.")
