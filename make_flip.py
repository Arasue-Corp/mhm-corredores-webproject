from bs4 import BeautifulSoup
import re

with open("cotizacion/cotizacion.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

for card in soup.find_all(class_="hub-card"):
    # Remove popover handlers
    if "onmouseenter" in card.attrs:
        del card["onmouseenter"]
    if "onmouseleave" in card.attrs:
        del card["onmouseleave"]
    
    card["class"] = card.get("class", []) + ["flip-container"]
    
    # Get attributes for the back face
    tag = card.get("data-tag", "")
    desc = card.get("data-desc", "")
    
    # Extract current contents to put in front face
    front_content = []
    for child in list(card.children):
        front_content.append(child.extract())
        
    inner = soup.new_tag("div", **{"class": "flip-card-inner"})
    
    front = soup.new_tag("div", **{"class": "flip-card-front"})
    for child in front_content:
        front.append(child)
        
    back = soup.new_tag("div", **{"class": "flip-card-back"})
    # Fill back face
    tag_span = soup.new_tag("span", **{"class": "back-tag"})
    tag_span.string = tag
    
    desc_p = soup.new_tag("p", **{"class": "back-desc"})
    desc_p.string = desc
    
    icon = soup.new_tag("i", **{"class": "fa-solid fa-rotate back-icon"})
    
    back.append(tag_span)
    back.append(desc_p)
    back.append(icon)
    
    inner.append(front)
    inner.append(back)
    
    card.append(inner)

# Add CSS for flip
flip_css = """
<style id="flip-css">
/* 3D Flip Card Styles */
.flip-container {
    background-color: transparent !important;
    perspective: 1000px;
    height: 180px; /* Adjust height based on your original card */
    padding: 0 !important;
    border: none !important;
    box-shadow: none !important;
}

.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.6s cubic-bezier(0.4, 0.2, 0.2, 1);
    transform-style: preserve-3d;
    border-radius: 20px;
}

.flip-container:hover .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 20px;
    padding: 25px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
}

.flip-card-front {
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid rgba(226, 232, 240, 0.8);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
}

.flip-card-back {
    background: linear-gradient(135deg, #796bfc, #2ed9c3);
    color: white;
    transform: rotateY(180deg);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 15px 35px rgba(121, 107, 252, 0.3);
}

.back-tag {
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    background: rgba(255, 255, 255, 0.2);
    padding: 4px 10px;
    border-radius: 100px;
    margin-bottom: 12px;
}

.back-desc {
    font-size: 0.85rem;
    line-height: 1.4;
    margin: 0;
    opacity: 0.95;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.back-icon {
    margin-top: 15px;
    font-size: 1.2rem;
    opacity: 0.8;
}
</style>
"""

# Inject flip css
head = soup.find('head')
if head:
    head.append(BeautifulSoup(flip_css, 'html.parser'))

# Remove popover HTML
popover = soup.find(id="card-popover")
if popover:
    popover.decompose()

# Write output
with open("cotizacion/cotizacion.html", "w") as f:
    f.write(str(soup))

