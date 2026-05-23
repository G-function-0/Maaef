import os, re

files = ['index.html', 'about.html', 'contact.html', 'services.html', 'expertise.html', 'pinhole.html']

correct_style = """<style>
            @keyframes slideLeft  { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
            @keyframes slideRight { 0% { transform: translateX(-50%); } 100% { transform: translateX(0); } }

            .concept-tape {
                position: absolute;
                display: flex;
                pointer-events: none;
                opacity: 0;
                transition: opacity 0.5s ease, filter 0.5s ease;
                filter: blur(4px);
            }
            .footer-cta-hover:hover .concept-tape {
                opacity: 0.95;
                filter: blur(0px);
            }

            .marquee-content {
                display: flex;
                width: max-content;
            }

            /* 1. TOP FRAME (Shallow angles hovering above text) */
            .ct-1 { top: 8%; left: -50vw; width: 200vw; transform: rotate(4deg); z-index: 10; }
            .ct-2 { top: 18%; left: -50vw; width: 200vw; transform: rotate(-2deg); z-index: 11; }
            
            /* 2. BOTTOM FRAME (Shallow angles hovering below text) */
            .ct-3 { top: 85%; left: -50vw; width: 200vw; transform: rotate(-3deg); z-index: 12; }
            .ct-4 { top: 75%; left: -50vw; width: 200vw; transform: rotate(2deg); z-index: 13; }

            /* 3. SIDE FRAMES (Steep angles locked to the extreme edges) */
            /* Far Left Wall */
            .ct-5 { top: -10%; left: -50vw; width: 120vw; transform: rotate(55deg); z-index: 14; }
            /* Far Right Wall */
            .ct-6 { top: -10%; right: -50vw; left: auto; width: 120vw; transform: rotate(-55deg); z-index: 15; }

            @media (max-width: 1023px) {
                .concept-tape {
                    opacity: 0.95 !important;
                    filter: blur(0px) !important;
                }
            }

            @media (max-width: 767px) {
                .ct-5 { display: flex !important; top: -35% !important; left: -20vw !important; width: 200vw !important; transform: rotate(45deg) !important; z-index: 15 !important; }
                .ct-6 { display: flex !important; top: auto !important; bottom: -35% !important; right: -20vw !important; width: 200vw !important; transform: rotate(45deg) !important; left: auto !important; z-index: 15 !important; }
                .marquee-content { font-size: 10px !important; }
                .concept-tape > div { padding-top: 6px !important; padding-bottom: 6px !important; }
            }
        </style>"""

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use re to replace the broken style block
    pattern = re.compile(r'(<svg[^>]*preserveAspectRatio="none"[^>]*>.*?</svg>)\s*<style>.*?</style>\s*(<div class="concept-tape ct-1)', re.DOTALL)
    
    new_content = pattern.sub(r'\1\n\n        ' + correct_style.replace('\\', '\\\\') + r'\n\n        \2', content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Updated static', filename)
