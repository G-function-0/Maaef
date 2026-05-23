import re

CANONICAL = """
                <!-- Police Tape 1: slides from LEFT, text scrolls LEFT -->
                <div class="ftape from-left d1" style="top: 10%; background: #dc2626; box-shadow: 0 0 30px rgba(196,30,58,0.4);">
                    <div class="flex whitespace-nowrap gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style="animation: tapeSlideLeft 15s linear infinite;">
                        <span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span>
                    </div>
                </div>

                <!-- Police Tape 2: slides from LEFT, text scrolls RIGHT -->
                <div class="ftape from-left d2" style="top: 35%; background: #050505; border-top: 2px solid #c0251a; border-bottom: 2px solid #c0251a; box-shadow: 0 0 30px rgba(196,30,58,0.2);">
                    <div class="flex whitespace-nowrap gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: tapeSlideRight 15s linear infinite;">
                        <span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span>
                    </div>
                </div>

                <!-- Police Tape 3: slides from RIGHT, text scrolls LEFT -->
                <div class="ftape from-right d3" style="top: 62%; background: #dc2626; box-shadow: 0 0 30px rgba(196,30,58,0.4);">
                    <div class="flex whitespace-nowrap gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style="animation: tapeSlideLeft 15s linear infinite;">
                        <span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span>
                    </div>
                </div>

                <!-- Police Tape 4: slides from RIGHT, text scrolls RIGHT -->
                <div class="ftape from-right d4" style="top: 87%; background: #050505; border-top: 2px solid #c0251a; border-bottom: 2px solid #c0251a; box-shadow: 0 0 30px rgba(196,30,58,0.2);">
                    <div class="flex whitespace-nowrap gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: tapeSlideRight 15s linear infinite;">
                        <span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span>
                    </div>
                </div>"""

STYLE_BLOCK = """<style>
                    @keyframes tapeSlideLeft { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
                    @keyframes tapeSlideRight { 0% { transform: translateX(-50%); } 100% { transform: translateX(0); } }
                    .ftape {
                        position: absolute; left: -50%; right: -50%; width: 200%;
                        height: 42px; display: flex; align-items: center; overflow: hidden;
                        pointer-events: none; z-index: 10;
                        opacity: 0;
                        transition: transform 0.7s cubic-bezier(0.16,1,0.3,1), opacity 0.4s ease;
                    }
                    @media (min-width: 768px) { .ftape { height: 56px; } }
                    .ftape.from-left  { transform: translateX(-110%) rotate(-0.7deg); }
                    .ftape.from-right { transform: translateX(110%)  rotate(0.7deg);  }
                    .ftape.d1 { transition-delay: 0s;    }
                    .ftape.d2 { transition-delay: 0.09s; }
                    .ftape.d3 { transition-delay: 0.18s; }
                    .ftape.d4 { transition-delay: 0.27s; }
                    .footer-cta-hover:hover .ftape { opacity: 1; }
                    .footer-cta-hover:hover .ftape.from-left  { transform: translateX(0) rotate(-0.7deg); }
                    .footer-cta-hover:hover .ftape.from-right { transform: translateX(0) rotate(0.7deg);  }
                    @media (max-width: 1023px) {
                        .ftape { opacity: 1 !important; }
                        .ftape.from-left  { transform: translateX(0) rotate(-0.7deg) !important; }
                        .ftape.from-right { transform: translateX(0) rotate(0.7deg)  !important; }
                    }
                </style>"""

for fname in ['expertise.html', 'pinhole.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove ALL existing style blocks with tapeSlide or ftape
    content = re.sub(r'<style>[^<]*(?:tapeSlide|ftape|mobile-reveal)[^<]*(?:<[^>]+>[^<]*)*</style>', '', content, flags=re.DOTALL)

    # Remove all existing ftape divs
    content = re.sub(r'\s*<!-- Police Tape \d+ -->.*?</div>', '', content, flags=re.DOTALL)

    # Also remove any leftover ftape divs without the comment marker
    content = re.sub(r'\s*<div class="ftape[^"]*"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)

    # Now find the CTA group div's h2 and insert after it
    # The pattern: h2 tag closes, then we need to inject style + tapes before closing the group div
    # Find the closing </div> that ends the group (it's right before <div class="max-w-[1400px]...)
    replacement = STYLE_BLOCK + CANONICAL
    # Insert before </div> that is followed by the max-w container
    content = re.sub(
        r'(</h2>\s*)(\s*</div>\s*\n\s*(?:<div class="max-w-\[1400px\]|        <div class="max-w-\[1400px\]))' ,
        r'\1' + replacement + r'\2',
        content,
        flags=re.DOTALL
    )

    # Add footer-cta-hover class if missing
    content = re.sub(
        r'(class=")(group relative w-full flex justify-center)',
        r'\1footer-cta-hover \2',
        content
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Done: {fname}')
