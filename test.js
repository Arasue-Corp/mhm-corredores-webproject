
    const plans = {
        'basico': { name: 'Asistencia Mascota', price: 5555, qty: 0 },
        'pro': { name: 'Asistencia Mascota Pro', price: 5555, qty: 0 },
        'senior': { name: 'Asistencia Senior', price: 5555, qty: 0 }
    };

    
    function toggleDetails(listId, btn) {
        const list = document.getElementById(listId);
        if (!list) return;
        
        if (list.classList.contains('show-details') || list.style.display === 'block') {
            list.classList.remove('show-details');
            list.style.setProperty('display', 'none', 'important');
            btn.innerHTML = 'Ver detalles <i class="fa-solid fa-chevron-down"></i>';
        } else {
            list.classList.add('show-details');
            list.style.setProperty('display', 'block', 'important');
            btn.innerHTML = 'Ocultar detalles <i class="fa-solid fa-chevron-up"></i>';
        }
    }

    function updateQty(id, delta) {
        plans[id].qty += delta;
        if(plans[id].qty < 0) plans[id].qty = 0;
        if(plans[id].qty > 10) plans[id].qty = 10;
        
        document.getElementById('qty-' + id).innerText = plans[id].qty;
        
        renderSummary();
        validateForm();
    }

    function renderSummary() {
        const summaryDiv = document.getElementById('cart-summary');
        if(!summaryDiv) return;
        
        let html = '';
        let total = 0;
        let itemsCount = 0;

        for(let id in plans) {
            if(plans[id].qty > 0) {
                itemsCount += plans[id].qty;
                const subtotal = plans[id].qty * plans[id].price;
                total += subtotal;
                html += `<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 1.05rem; color: #334155;">
                    <span><i class="fa-solid fa-paw" style="color: #CBD5E1; margin-right: 8px;"></i> ${plans[id].name} <strong style="color: #0F172A;">x ${plans[id].qty}</strong></span>
                    <strong style="color: #0F172A;">$${subtotal.toLocaleString('es-CL')}</strong>
                </div>`;
            }
        }

        if(itemsCount === 0) {
            html = '<div style="color: #94A3B8; font-size: 1rem; text-align: center; padding: 20px 0;"><i class="fa-solid fa-basket-shopping" style="font-size: 2.5rem; margin-bottom: 15px; opacity: 0.3;"></i><br>Aún no has seleccionado ningún plan.</div>';
        } else {
            html += `<div style="border-top: 2px dashed #E2E8F0; margin-top: 15px; padding-top: 20px; display: flex; justify-content: space-between; font-size: 1.3rem; color: #0F172A;">
                <strong>Total Estimado:</strong>
                <strong style="color: #2ED9C3;">$${total.toLocaleString('es-CL')}</strong>
            </div>`;
        }
        summaryDiv.innerHTML = html;
    }

    function validateForm() {
        const chkTerms = document.getElementById('chk-terms').checked;
        const chkLegal = document.getElementById('chk-legal').checked;
        const btn = document.getElementById('btn-continue');
        
        let hasItems = false;
        for(let id in plans) {
            if(plans[id].qty > 0) hasItems = true;
        }

        if(chkTerms && chkLegal && hasItems) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
            btn.style.transform = 'translateY(0)';
        } else {
            btn.style.opacity = '0.5';
            btn.style.pointerEvents = 'none';
            btn.style.transform = 'translateY(0)';
        }
    }

    function goToNextStep() {
        sessionStorage.setItem('mhmPetCart', JSON.stringify(plans));
        
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.3s ease';
        setTimeout(() => {
            window.location.href = 'cotizacion-mascota-2.html';
        }, 300);
    }
    
    document.addEventListener('DOMContentLoaded', () => {
        renderSummary();
    });
