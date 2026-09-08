(function(window) {
    'use strict';

    const MHM_PRODUCTS = {
        ciclista: {
            category: 'Asistencias',
            title: 'Asistencia al Ciclista',
            plans: {
                'ciclista': {
                    id: 'ciclista',
                    name: 'Asistencia al Ciclista',
                    badge: 'Recomendado',
                    priceCLP: 7990,
                    priceUF: 0.22,
                    billing: 'mensual',
                    coverages: [
                        'Transporte de bicicleta por avería o accidente (hasta 3 eventos/año)',
                        'Reparación in situ por pinchazo o cadena suelta',
                        'Orientación médica telefónica en caso de accidente 24/7',
                        'Gastos médicos menores de emergencia hasta $150.000'
                    ]
                },
                'ciclista-pro': {
                    id: 'ciclista-pro',
                    name: 'Asistencia al Ciclista Pro',
                    badge: 'Full Cobertura',
                    priceCLP: 12990,
                    priceUF: 0.35,
                    billing: 'mensual',
                    coverages: [
                        'Transporte ilimitado de bicicleta por avería o accidente',
                        'Reparación in situ express 24/7 en toda la Región Metropolitana',
                        'Reembolso de gastos médicos de urgencia hasta $500.000',
                        'Responsabilidad civil ciclista frente a terceros hasta $2.000.000',
                        'Reemplazo temporal de bicicleta por robo hasta 15 días'
                    ]
                }
            }
        },
        mascota: {
            category: 'Asistencias',
            title: 'Asistencia para Mascotas',
            plans: {
                'basico': {
                    id: 'basico',
                    name: 'Asistencia Mascota Esencial',
                    badge: 'Básico',
                    priceCLP: 5555,
                    billing: 'mensual',
                    coverages: [
                        'Orientación veterinaria telefónica 24/7',
                        'Consulta veterinaria de emergencia presencial (2 al año)',
                        'Vacuna antirrábica anual y desparasitación',
                        'Hotel para mascotas en caso de hospitalización del titular'
                    ]
                },
                'pro': {
                    id: 'pro',
                    name: 'Asistencia Mascota Pro',
                    badge: 'Más Popular',
                    priceCLP: 9990,
                    billing: 'mensual',
                    coverages: [
                        'Todas las coberturas del plan Esencial',
                        'Consultas presenciales ilimitadas en red asociada con copago $0',
                        'Exámenes de laboratorio básicos incluidos (hasta $80.000/año)',
                        'Procedimientos quirúggicos menores de urgencia',
                        'Asistencia en entierro / cremación de la mascota'
                    ]
                },
                'senior': {
                    id: 'senior',
                    name: 'Asistencia Mascota Senior',
                    badge: 'Especializado',
                    priceCLP: 12990,
                    billing: 'mensual',
                    coverages: [
                        'Diseñado especialmente para perros y gatos mayores a 7 años',
                        'Chequeo geriátrico anual preventivo completo (ecografía, sangre)',
                        'Medicamentos de urgencia cubiertos hasta $60.000 por evento',
                        'Atención a domicilio preferencial sin recargo'
                    ]
                }
            }
        },
        hogar: {
            category: 'Hogar',
            title: 'Asistencia Hogar Inteligente',
            plans: {
                'hogar-standard': {
                    id: 'hogar-standard',
                    name: 'Hogar Protegido Estándar',
                    badge: 'Básico',
                    priceCLP: 8990,
                    billing: 'mensual',
                    coverages: [
                        'Cerrajería de urgencia 24/7 (hasta 3 eventos/año)',
                        'Gasfitería de emergencia (fugas visibles e inundación)',
                        'Electricidad de emergencia (cortocircuitos generales)',
                        'Vidriería por rotura imprevista en accesos exteriores'
                    ]
                },
                'hogar-pro': {
                    id: 'hogar-pro',
                    name: 'Hogar Protegido Premium',
                    badge: 'Full',
                    priceCLP: 14990,
                    billing: 'mensual',
                    coverages: [
                        'Eventos ilimitados en cerrajería, gasfitería y electricidad',
                        'Asistencia de línea blanca (refrigerador, lavadora, cocina)',
                        'Instalación de cortinas, cuadros, lámparas y cerraduras inteligentes',
                        'Guarda de muebles y mudanza de emergencia en siniestros graves'
                    ]
                }
            }
        },
        vehicular: {
            category: 'Vehicular',
            title: 'Seguro Automotriz con IA',
            deductibles: [
                { id: 'ded-0', name: 'Deducible 0 UF', multiplier: 1.25 },
                { id: 'ded-3', name: 'Deducible 3 UF', multiplier: 1.00, default: true },
                { id: 'ded-5', name: 'Deducible 5 UF', multiplier: 0.88 },
                { id: 'ded-10', name: 'Deducible 10 UF', multiplier: 0.75 }
            ],
            vehicleTypes: ['Auto', 'Camioneta', 'Station Wagon', 'Jeep', 'Furgón']
        }
    };

    const MHM_HELPERS = {
        formatCLP: function(num) {
            if (num === null || num === undefined || isNaN(num)) return '$0';
            return '$' + Math.round(num).toLocaleString('es-CL');
        },
        formatUF: function(num, decimals = 2) {
            if (num === null || num === undefined || isNaN(num)) return 'UF 0,00';
            return 'UF ' + Number(num).toFixed(decimals).replace('.', ',');
        },
        showToast: function(msg, type = 'success') {
            let container = document.getElementById('toast-container');
            if (!container) {
                container = document.createElement('div');
                container.id = 'toast-container';
                document.body.appendChild(container);
            }
            const toast = document.createElement('div');
            let iconHtml = '<i class="fa-solid fa-check"></i>';
            if (type === 'warning') iconHtml = '<i class="fa-solid fa-triangle-exclamation"></i>';
            if (type === 'danger') iconHtml = '<i class="fa-solid fa-circle-xmark"></i>';
            if (type === 'info') iconHtml = '<i class="fa-solid fa-circle-info"></i>';
            toast.className = 'alex-toast ' + type;
            toast.innerHTML = '<div class="toast-icon-box">' + iconHtml + '</div><div class="toast-content"><span class="toast-title">MHM Seguros</span><span class="toast-sub">' + msg + '</span></div>';
            container.appendChild(toast);
            requestAnimationFrame(() => toast.classList.add('show'));
            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => toast.remove(), 400);
            }, 3500);
        }
    };

    window.MHM_PRODUCTS = MHM_PRODUCTS;
    window.MHM_HELPERS = MHM_HELPERS;
})(typeof window !== 'undefined' ? window : this);
