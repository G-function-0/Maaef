import re, os

NEW_STYLE = """<style>
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

TAPES_4 = """
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


def process_4tape_file(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Add 'footer-cta-hover' class to the CTA group div
    content = content.replace(
        'class="relative w-full flex justify-center items-center py-10 border-t border-b border-white/[.05] mb-8 overflow-hidden group hover-trigger cursor-pointer"',
        'class="footer-cta-hover relative w-full flex justify-center items-center py-10 border-t border-b border-white/[.05] mb-8 overflow-hidden group hover-trigger cursor-pointer"'
    )

    # 2. Remove old <style> block with tapeSlide keyframes
    content = re.sub(
        r'\s*<style>\s*@keyframes tapeSlideLeft.*?</style>',
        '',
        content,
        flags=re.DOTALL
    )

    # 3. Replace old tape divs (Police Tape 1 through Police Tape 4) with new ones
    content = re.sub(
        r'\s*<!-- Police Tape 1 -->.*?<!-- Police Tape 4 -->.*?</div>(?=\s*\n\s*</div>)',
        '\n' + NEW_STYLE + TAPES_4,
        content,
        flags=re.DOTALL
    )

    if content == original:
        print(f'WARNING: Nothing changed in {fname} - pattern not matched')
    else:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'OK: {fname}')


for fname in ['index.html', 'about.html', 'contact.html', 'services.html']:
    process_4tape_file(fname)

print('All done.')
