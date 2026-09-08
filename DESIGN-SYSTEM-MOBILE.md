# Guía de Diseño y Desarrollo Mobile-First - MHM Corredores

Este documento establece los **lineamientos arquitectónicos y de diseño obligatorios** para cualquier página, flujo o componente que se construya en la plataforma de MHM Seguros.

---

## 🎯 1. La Regla de Oro: Mobile-First Real

> **"Todo código CSS debe escribirse pensando primero en una pantalla de 320px a 390px (móvil). Las pantallas grandes son una mejora progresiva, no el punto de partida."**

### ❌ Lo que está PROHIBIDO (Desktop-First):
```css
/* INCORRECTO: Escribir para escritorio y parchar para móvil */
.mi-tarjeta {
    width: 600px; /* Ancho fijo rompe en móvil */
    display: flex;
}
@media (max-width: 768px) {
    .mi-tarjeta {
        width: 100%; /* Parche sobre parche */
        flex-direction: column;
    }
}
```

### ✅ Lo que se DEBE hacer (Mobile-First):
```css
/* CORRECTO: La regla base es móvil. Crece con min-width */
.mi-tarjeta {
    width: 100%;
    display: flex;
    flex-direction: column;
}
@media (min-width: 768px) {
    .mi-tarjeta {
        flex-direction: row;
    }
}
```

---

## 📐 2. Breakpoints Estándar Unificados

Solo existen **3 puntos de quiebre** oficiales en todo el proyecto:

| Dispositivo | Consulta Media | Comportamiento |
| :--- | :--- | :--- |
| **Móvil (Base)** | *(Sin media query)* | 1 columna, táctil, padding 16px, 100% ancho fluido |
| **Tablet** | `@media (min-width: 768px)` | 2 columnas, padding 24px, elementos expandidos |
| **Desktop** | `@media (min-width: 1024px)` | 3-4 columnas, max-width 1200px, barras laterales |

---

## 📱 3. Estándares Táctiles y Mobile UX Obligatorios

1. **Prevención de Zoom en iOS Safari:**
   * **Cualquier `input`, `select` o `textarea` DEBE tener `font-size: 16px` como mínimo.**
   * Si tiene un tamaño inferior a 16px, iOS hace zoom automático forzado sobre la pantalla al tocar el campo, arruinando la interfaz.

2. **Objetivo Táctil Mínimo (WCAG & Apple HIG):**
   * Todo botón o control táctil debe medir al menos **44x44px** (óptimo **48px** con `min-height: var(--touch-target)`).
   * Nunca poner botones diminutos pegados unos a otros sin espacio de separación.

3. **Cero Desbordamiento Horizontal:**
   * Prohibido fijar `width` en píxeles fijos mayores a `300px`.
   * Usar siempre `width: 100%` con `max-width` en su lugar.

4. **Soporte para Notch y Home Indicator (Safe Areas):**
   * Las barras flotantes o fijas al fondo deben respetar el notch inferior de iPhone/Android:
     ```css
     padding-bottom: calc(12px + var(--safe-bottom));
     ```

5. **Micro-feedback Táctil Háptico:**
   * Todo botón o tarjeta clickeable debe responder al toque con:
     ```css
     button:active, .m-btn:active {
         transform: scale(0.98);
     }
     ```

---

## 🧩 4. Catálogo de Componentes Globales (`mobile-first.css`)

### Contenedor Adaptativo
```html
<div class="m-container">
    <!-- En móvil tiene 16px de margen; en desktop centra a 1200px -->
</div>
```

### Rejilla Progresiva (1 col en móvil -> 2 en tablet -> 3 en desktop)
```html
<div class="m-grid m-grid-3">
    <div class="m-card">Opción 1</div>
    <div class="m-card">Opción 2</div>
    <div class="m-card">Opción 3</div>
</div>
```

### Botones Táctiles
```html
<!-- Botón primario degradado Aurora -->
<button class="m-btn m-btn-primary m-btn-block">
    <i class="fa-solid fa-arrow-right"></i> Continuar
</button>

<!-- Botón secundario Teal -->
<button class="m-btn m-btn-teal">
    Contratar
</button>
```

### Barra Fija Inferior para Acciones Móviles (Checkout / Resumen)
```html
<!-- Se muestra en móviles y se oculta automáticamente en Desktop (>=1024px) -->
<div class="m-sticky-bar">
    <div>
        <small class="text-muted">Total mensual</small>
        <div class="price-value font-bold">$12.990</div>
    </div>
    <button class="m-btn m-btn-primary">
        Continuar <i class="fa-solid fa-chevron-right"></i>
    </button>
</div>

<!-- Recuerda añadir al <main> o <body> la clase: -->
<main class="m-has-sticky-bar">
```

### Píldoras / Chips de Selección Horizontal
```html
<div class="m-chip-group">
    <button class="m-chip active">Básico</button>
    <button class="m-chip">Pro</button>
    <button class="m-chip">Senior</button>
</div>
```

---

## ✅ 5. Checklist de Verificación para Todo Nuevo Desarrollo

Antes de dar por terminada cualquier página o componente:

- [ ] ¿Se probó en resolución de **360px** (Samsung Galaxy) y **390px** (iPhone 14/15)?
- [ ] ¿Hay **cero scroll horizontal** accidental?
- [ ] ¿Al tocar un input en el teléfono la pantalla permanece quieta sin hacer auto-zoom molesto?
- [ ] ¿Todos los botones y enlaces se pueden presionar cómodamente con el pulgar?
- [ ] ¿Las acciones principales de compra/continuar están en la zona baja de la pantalla (zona del pulgar)?
- [ ] ¿Las tipografías y textos largos usan `text-wrap: balance` o `text-wrap: pretty`?
