import re

# ── Read the canonical tape block from index.html ──────────────────────────
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Extract lines 1107-1159 (style block + 4 tapes, up to but not including the closing </div></div>)
CANONICAL_TAPES = """<style>
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
                </style>
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


def normalize_footer_cta(content):
    """Add footer-cta-hover class to the CTA group div if not already there."""
    # Match various CTA div patterns used across pages
    patterns = [
        # 4-tape pages
        r'(class=")(relative w-full flex justify-center items-center py-10 border-t border-b border-white/\[\.05\] mb-8 overflow-hidden group hover-trigger cursor-pointer")',
        # expertise / pinhole 6-tape pattern
        r'(class=")(group relative w-full flex justify-center items-center min-h-\[320px\] md:min-h-\[520px\] border-y border-white/5 mb-6 overflow-hidden cursor-pointer bg-black")',
    ]
    for pat in patterns:
        content = re.sub(pat, lambda m: m.group(1) + ('footer-cta-hover ' if 'footer-cta-hover' not in m.group(0) else '') + m.group(2), content)
    return content


def remove_old_tapes(content):
    """Remove any existing style block with tapeSlide keyframes + all old police tape divs."""
    # Remove old <style> blocks containing tapeSlide or mobile-reveal
    content = re.sub(r'\s*<style>\s*@keyframes tapeSlideLeft.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<style>\s*@media \(max-width: 1023px\).*?\.mobile-reveal.*?</style>', '', content, flags=re.DOTALL)
    # Remove old ftape style blocks (from previous fix run)
    content = re.sub(r'\s*<style>\s*@keyframes tapeSlideLeft.*?\.footer-cta-hover.*?</style>', '', content, flags=re.DOTALL)
    return content


def replace_tape_divs(content, new_tapes):
    """Replace the Police Tape divs (any number) with the canonical 4-tape block."""
    # Pattern: from first <!-- Police Tape to end of last tape's closing div
    replaced = re.sub(
        r'(?s)\s*<!-- Police Tape 1.*?<!-- Police Tape \d+ -->.*?</div>(?=\s*\n\s*(?:</div>|\n))',
        '\n' + new_tapes,
        content
    )
    return replaced


# ── Process each file ────────────────────────────────────────────────────────
files = ['about.html', 'contact.html', 'services.html', 'expertise.html', 'pinhole.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    content = normalize_footer_cta(content)
    content = remove_old_tapes(content)
    content = replace_tape_divs(content, CANONICAL_TAPES)

    if content == original:
        print(f'WARNING: No change in {fname}')
    else:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'OK: {fname}')

print('All pages updated.')
