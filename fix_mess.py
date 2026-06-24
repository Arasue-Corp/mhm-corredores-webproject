import re

with open("cotizacion/cotizacion-9-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# I will find '<div id="tourFocusRing">' which is safe, and replace everything after it.
safe_marker = '<div id="tourFocusRing">'
if safe_marker in content:
    top_part = content.split(safe_marker)[0]
    
    bottom_part = """<div id="tourFocusRing">
        <div class="scan-line"></div>
        <div class="focus-label" id="focusLabel">SCANNING</div>
    </div>

    <div id="tourCard" class="tour-card-holo">
        <div class="holo-header">
            <span class="holo-badge">CONTINUITY <span id="tcCurrent">1</span>/<span id="tcTotal">2</span></span>
            <button class="holo-skip" onclick="endHistoryTour()">Skip Guide</button>
        </div>

        <div class="holo-body">
            <div class="graphic-stage" id="graphicStage"></div>
            <h3 class="holo-title" id="tcTitle">Title</h3>
            <p class="holo-desc" id="tcDesc">Desc</p>
        </div>

        <div class="holo-footer">
            <button class="btn-holo-prev" id="btnHistPrev" onclick="prevHistoryStep()">
                <i class="fa-solid fa-arrow-left"></i> Back
            </button>
            <button class="btn-holo-next" id="btnHistNext" onclick="nextHistoryStep()">
                Next <i class="fa-solid fa-arrow-right"></i>
            </button>
        </div>
    </div>

<script>
    // Modal Logic
    function goToModalStep2() {
        document.getElementById('emailStep1').style.display = 'none';
        document.getElementById('emailStep2').style.display = 'block';
        setTimeout(() => { document.querySelector('.pin-box-premium').focus(); }, 100);
    }
    
    function moveNext(elem, nextId) {
        if(elem.value.length >= 1) {
            const nextElem = document.getElementById(nextId);
            if(nextElem) {
                nextElem.focus();
            } else {
                verifyCode();
            }
        }
    }
    
    function verifyCode() {
        const p1 = document.querySelector('.pin-box-premium').value;
        const p2 = document.getElementById('pin2').value;
        const p3 = document.getElementById('pin3').value;
        const p4 = document.getElementById('pin4').value;
        
        if (p1 && p2 && p3 && p4) {
            const btn = document.getElementById('btnVerifyPin');
            btn.disabled = false;
            btn.style.opacity = '1';
            btn.style.cursor = 'pointer';
        }
    }
    
    function closeEmailModal() {
        document.getElementById('emailVerifyModal').style.display = 'none';
        document.body.style.overflow = 'auto'; // restore scroll
    }

    // PAC/PAT Form logic
    function togglePACPATForm() {
        const isYes = document.getElementById('dc_yes').checked;
        const section = document.getElementById('paymentOptionsSection');
        const btnNext = document.getElementById('btnNext');
        
        if (isYes) {
            section.style.display = 'block';
            setTimeout(() => { section.style.opacity = '1'; }, 10);
            
            // Enable next button when they confirm
            btnNext.disabled = false;
            btnNext.classList.remove('disabled');
            btnNext.style.cursor = 'pointer';
            btnNext.style.opacity = '1';
        } else {
            section.style.opacity = '0';
            setTimeout(() => { section.style.display = 'none'; }, 400);
            
            btnNext.disabled = true;
            btnNext.classList.add('disabled');
            btnNext.style.cursor = 'not-allowed';
            btnNext.style.opacity = '0.5';
        }
    }
    
    function switchPaymentTab(type) {
        const tabPAC = document.getElementById('tabPAC');
        const tabPAT = document.getElementById('tabPAT');
        const formPAC = document.getElementById('formPAC');
        const formPAT = document.getElementById('formPAT');
        const pill = document.getElementById('iosPill');
        
        if (type === 'PAC') {
            tabPAC.classList.add('active');
            tabPAT.classList.remove('active');
            if(pill) pill.style.transform = 'translateX(0)';
            
            formPAC.style.display = 'block';
            formPAT.style.display = 'none';
        } else {
            tabPAT.classList.add('active');
            tabPAC.classList.remove('active');
            if(pill) pill.style.transform = 'translateX(100%)';
            
            formPAT.style.display = 'block';
            formPAC.style.display = 'none';
        }
    }
    
    // On load, disable body scroll until modal is closed
    document.addEventListener("DOMContentLoaded", () => {
        document.body.style.overflow = 'hidden';
    });
</script>
</body>
</html>
"""
    with open("cotizacion/cotizacion-9-1.html", "w", encoding="utf-8") as f:
        f.write(top_part + bottom_part)
    print("Fixed syntax error and mangled bottom section.")
