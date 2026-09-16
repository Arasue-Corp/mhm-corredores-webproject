/**
 * MHM Corredores - Lógica Interactiva de la Página de Contacto
 * Validación en tiempo real, manejo de envío, estados de confirmación,
 * copiado de datos y acordeón FAQ.
 */

document.addEventListener('DOMContentLoaded', () => {
    cleanFloatingElements();
    initContactForm();
    initFaqAccordion();
    initCopyButtons();
});

// Asegurar ejecución posterior al fix de script.js
window.addEventListener('load', () => {
    cleanFloatingElements();
});

function cleanFloatingElements() {
    const floatingMenu = document.getElementById('floating-menu-container');
    if (floatingMenu) {
        floatingMenu.style.setProperty('display', 'none', 'important');
    }
    const floatingChat = document.getElementById('floating-chat-container');
    if (floatingChat) {
        floatingChat.style.setProperty('bottom', '20px', 'important');
        floatingChat.style.setProperty('right', '20px', 'important');
    }
}

/* ==========================================================
   1. FORMULARIO DE CONTACTO
   ========================================================== */
function initContactForm() {
    const form = document.getElementById('main-contact-form');
    if (!form) return;

    const fnameInput = document.getElementById('fname');
    const lnameInput = document.getElementById('lname');
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const subjectSelect = document.getElementById('subject');
    const messageTextarea = document.getElementById('message');
    const charCounter = document.getElementById('char-count');
    const submitBtn = document.getElementById('btn-contact-submit');
    const formCard = document.getElementById('contact-form-container');
    const successCard = document.getElementById('contact-success-state');

    // Contador de caracteres para el mensaje
    if (messageTextarea && charCounter) {
        messageTextarea.addEventListener('input', () => {
            const length = messageTextarea.value.length;
            charCounter.textContent = `${length} / 500`;
            if (length > 500) {
                charCounter.style.color = '#EF4444';
            } else {
                charCounter.style.color = '#94A3B8';
            }
        });
    }

    // Formateo automático de teléfono chileno (+56 9 ...)
    if (phoneInput) {
        phoneInput.addEventListener('input', (e) => {
            let val = e.target.value.replace(/\D/g, '');
            if (val.startsWith('569')) {
                val = val.substring(3);
            } else if (val.startsWith('56')) {
                val = val.substring(2);
            } else if (val.startsWith('9')) {
                val = val.substring(1);
            }
            // Limitar a 8 dígitos locales (tras el 9)
            val = val.substring(0, 8);
            if (val.length > 0) {
                if (val.length > 4) {
                    e.target.value = `+56 9 ${val.substring(0, 4)} ${val.substring(4)}`;
                } else {
                    e.target.value = `+56 9 ${val}`;
                }
            } else {
                e.target.value = '';
            }
            if (e.target.value.trim() !== '') {
                validateField(phoneInput, isValidPhone(e.target.value));
            } else {
                phoneInput.classList.remove('is-valid', 'is-invalid');
            }
        });
    }

    // Validación interactiva en inputs individuales
    const fieldsToValidate = [
        { el: fnameInput, validator: val => val.trim().length >= 2 },
        { el: lnameInput, validator: val => val.trim().length >= 2 },
        { el: emailInput, validator: isValidEmail },
        { el: subjectSelect, validator: val => val && val.trim() !== '' },
        { el: messageTextarea, validator: val => val.trim().length >= 10 && val.length <= 500 }
    ];

    fieldsToValidate.forEach(({ el, validator }) => {
        if (!el) return;
        el.addEventListener('blur', () => {
            if (el.value.trim() !== '') {
                validateField(el, validator(el.value));
            }
        });
        el.addEventListener('input', () => {
            if (el.classList.contains('is-invalid')) {
                validateField(el, validator(el.value));
            }
        });
    });

    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
    }

    function isValidPhone(phone) {
        // Formato: +56 9 XXXX XXXX (9 dígitos locales)
        const digits = phone.replace(/\D/g, '');
        return digits.length === 11 && digits.startsWith('569');
    }

    function validateField(element, isValid) {
        if (!element) return;
        const parent = element.closest('.form-floating-field') || element.parentElement;
        if (isValid) {
            element.classList.remove('is-invalid');
            element.classList.add('is-valid');
            if (parent) {
                parent.classList.remove('has-error');
                parent.classList.add('has-success');
            }
        } else {
            element.classList.remove('is-valid');
            element.classList.add('is-invalid');
            if (parent) {
                parent.classList.remove('has-success');
                parent.classList.add('has-error');
            }
        }
    }

    // Envío del formulario
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Validar todos los campos obligatorios
        let isFormValid = true;

        fieldsToValidate.forEach(({ el, validator }) => {
            if (!el) return;
            const valid = validator(el.value);
            validateField(el, valid);
            if (!valid) isFormValid = false;
        });

        // Validar teléfono (si tiene contenido, debe ser válido)
        if (phoneInput && phoneInput.value.trim() !== '') {
            const validPhone = isValidPhone(phoneInput.value);
            validateField(phoneInput, validPhone);
            if (!validPhone) isFormValid = false;
        }

        const termsCheckbox = document.getElementById('terms-consent');
        if (termsCheckbox && !termsCheckbox.checked) {
            const row = termsCheckbox.closest('.terms-checkbox-row');
            if (row) {
                row.classList.add('shake-error');
                setTimeout(() => row.classList.remove('shake-error'), 600);
            }
            isFormValid = false;
        }

        if (!isFormValid) {
            const firstInvalid = form.querySelector('.is-invalid');
            if (firstInvalid) {
                firstInvalid.focus();
                firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
            showToast('Por favor, completa todos los campos requeridos correctamente.', 'warning');
            return;
        }

        // Estado de carga (Loading)
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.classList.add('is-submitting');
            submitBtn.innerHTML = `
                <div class="btn-loading-state">
                    <i class="fa-solid fa-circle-notch fa-spin"></i>
                    <span>Enviando mensaje...</span>
                </div>
            `;

            // Simulación de envío de red elegante (1.2 segundos)
            await new Promise(resolve => setTimeout(resolve, 1200));

            // Generar número de ticket único
            const ticketId = 'MHM-' + Math.floor(100000 + Math.random() * 900000);
            const userFname = fnameInput ? fnameInput.value.trim() : 'Estimado/a';
            const userEmail = emailInput ? emailInput.value.trim() : '';

            // Transición a la tarjeta de éxito
            if (formCard && successCard) {
                formCard.style.opacity = '0';
                formCard.style.transform = 'scale(0.96)';
                formCard.style.transition = 'opacity 0.3s ease, transform 0.3s ease';

                setTimeout(() => {
                    formCard.style.display = 'none';
                    
                    const ticketEl = document.getElementById('success-ticket-id');
                    const nameEl = document.getElementById('success-user-name');
                    const emailEl = document.getElementById('success-user-email');
                    
                    if (ticketEl) ticketEl.textContent = ticketId;
                    if (nameEl) nameEl.textContent = userFname;
                    if (emailEl) emailEl.textContent = userEmail;

                    successCard.style.display = 'block';
                    successCard.style.opacity = '0';
                    successCard.style.transform = 'scale(0.96)';
                    
                    requestAnimationFrame(() => {
                        successCard.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                        successCard.style.opacity = '1';
                        successCard.style.transform = 'scale(1)';
                    });
                }, 300);
            }

            showToast('¡Mensaje enviado con éxito! Nos pondremos en contacto a la brevedad.', 'success');
        }
    });

    // Botón para enviar otro mensaje desde la tarjeta de éxito
    const btnResetContact = document.getElementById('btn-send-another');
    if (btnResetContact) {
        btnResetContact.addEventListener('click', () => {
            form.reset();
            form.querySelectorAll('.is-valid, .is-invalid').forEach(el => {
                el.classList.remove('is-valid', 'is-invalid');
            });
            form.querySelectorAll('.has-success, .has-error').forEach(el => {
                el.classList.remove('has-success', 'has-error');
            });
            if (charCounter) charCounter.textContent = '0 / 500';

            if (successCard && formCard) {
                successCard.style.opacity = '0';
                setTimeout(() => {
                    successCard.style.display = 'none';
                    formCard.style.display = 'block';
                    formCard.style.opacity = '1';
                    formCard.style.transform = 'scale(1)';
                    if (submitBtn) {
                        submitBtn.disabled = false;
                        submitBtn.classList.remove('is-submitting');
                        submitBtn.innerHTML = `
                            <div class="btn-bg-layer"></div>
                            <div class="btn-glow-layer"></div>
                            <div class="btn-content-wrapper">
                                <span class="btn-text">Enviar Mensaje</span>
                                <span class="btn-icon"><i class="fa-solid fa-paper-plane"></i></span>
                            </div>
                        `;
                    }
                }, 250);
            }
        });
    }
}

/* ==========================================================
   2. ACORDEÓN DE PREGUNTAS FRECUENTES (FAQ)
   ========================================================== */
function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-contact-item');
    if (!faqItems.length) return;

    faqItems.forEach(item => {
        const header = item.querySelector('.faq-contact-header');
        const body = item.querySelector('.faq-contact-body');
        if (!header || !body) return;

        header.addEventListener('click', () => {
            const isOpen = item.classList.contains('is-open');

            // Cerrar otros acordeones para mantener orden
            faqItems.forEach(otherItem => {
                if (otherItem !== item && otherItem.classList.contains('is-open')) {
                    otherItem.classList.remove('is-open');
                    const otherHeader = otherItem.querySelector('.faq-contact-header');
                    const otherBody = otherItem.querySelector('.faq-contact-body');
                    if (otherHeader) otherHeader.setAttribute('aria-expanded', 'false');
                    if (otherBody) otherBody.style.maxHeight = null;
                }
            });

            if (isOpen) {
                item.classList.remove('is-open');
                header.setAttribute('aria-expanded', 'false');
                body.style.maxHeight = null;
            } else {
                item.classList.add('is-open');
                header.setAttribute('aria-expanded', 'true');
                body.style.maxHeight = body.scrollHeight + 'px';
            }
        });
    });
}

/* ==========================================================
   3. BOTONES DE COPIADO RÁPIDO Y TOAST FEEDBACK
   ========================================================== */
function initCopyButtons() {
    const copyBtns = document.querySelectorAll('.js-copy-text');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const textToCopy = btn.getAttribute('data-copy') || btn.textContent.trim();
            if (!textToCopy) return;

            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalHtml = btn.innerHTML;
                btn.classList.add('copied');
                btn.innerHTML = '<i class="fa-solid fa-check"></i>';
                showToast(`"${textToCopy}" copiado al portapapeles.`, 'info');

                setTimeout(() => {
                    btn.classList.remove('copied');
                    btn.innerHTML = originalHtml;
                }, 2000);
            }).catch(() => {
                showToast('No se pudo copiar el texto.', 'warning');
            });
        });
    });
}

/* ==========================================================
   4. TOAST NOTIFIER HELPER
   ========================================================== */
function showToast(message, type = 'info') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `aurora-toast toast-${type}`;
    
    let iconClass = 'fa-solid fa-circle-info';
    if (type === 'success') iconClass = 'fa-solid fa-circle-check';
    if (type === 'warning') iconClass = 'fa-solid fa-triangle-exclamation';

    toast.innerHTML = `
        <i class="${iconClass}"></i>
        <span>${message}</span>
        <button type="button" class="toast-close" onclick="this.parentElement.remove()">&times;</button>
    `;

    container.appendChild(toast);

    requestAnimationFrame(() => {
        toast.classList.add('show');
    });

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 400);
    }, 4500);
}
