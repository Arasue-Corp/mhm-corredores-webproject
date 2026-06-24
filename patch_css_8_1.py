with open("css/style-quote.css", "a", encoding="utf-8") as f:
    f.write("""

/* =========================================
   PANTALLA 8-1: FILE UPLOAD & DATE BOXES
   ========================================= */

/* Date Boxes */
.date-boxes-container {
    display: flex; align-items: center; gap: 15px; width: 100%;
}
.date-box { width: 100px; flex: none; }
.year-box { width: 130px; }
.date-separator { font-size: 1.5rem; font-weight: 300; color: #CBD5E1; }
.text-center { text-align: center; }

/* File Upload Zone */
.hidden-file-input { display: none; }
.upload-drop-zone {
    border: 2px dashed #CBD5E1; background: #F8FAFC;
    border-radius: 16px; padding: 40px 20px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    cursor: pointer; transition: all 0.3s ease; text-align: center;
}
.upload-drop-zone:hover {
    border-color: var(--quote-primary); background: #EFF6FF;
    box-shadow: 0 10px 25px rgba(46, 217, 195, 0.1);
}
.upload-icon-wrapper {
    width: 64px; height: 64px; border-radius: 50%;
    background: white; color: var(--quote-primary);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.8rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 15px; transition: transform 0.3s ease;
}
.upload-drop-zone:hover .upload-icon-wrapper { transform: scale(1.1); }
.upload-title { font-size: 1.2rem; font-weight: 700; color: var(--quote-dark); margin-bottom: 5px; }
.upload-desc { font-size: 0.9rem; color: #64748B; margin-bottom: 20px; }
.upload-btn-fake {
    background: white; border: 1px solid #E2E8F0; color: var(--quote-indigo);
    padding: 8px 24px; border-radius: 50px; font-weight: 600; font-size: 0.9rem;
    transition: all 0.2s ease;
}
.upload-drop-zone:hover .upload-btn-fake { border-color: var(--quote-primary); }

/* Document Preview Card */
.document-preview-card {
    display: flex; align-items: center; gap: 15px;
    background: white; border: 1px solid #E2E8F0; border-radius: 12px;
    padding: 15px 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    animation: slideInPanel 0.3s ease-out forwards;
}
.doc-icon { font-size: 2rem; color: #EF4444; }
.doc-info { flex: 1; text-align: left; }
.doc-name { font-weight: 600; color: var(--quote-dark); font-size: 0.95rem; margin-bottom: 2px; }
.doc-size { font-size: 0.75rem; color: #10B981; font-weight: 500; }
.doc-remove-btn {
    background: #FEF2F2; color: #EF4444; border: none;
    width: 32px; height: 32px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; transition: 0.2s;
}
.doc-remove-btn:hover { background: #FCA5A5; color: white; }
""")
print("CSS appended.")
