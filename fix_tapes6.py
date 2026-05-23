import re

NEW_STYLE_6 = """<style>
                    @keyframes tapeSlideLeft { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
                    @keyframes tapeSlideRight { 0% { transform: translateX(-50%); } 100% { transform: translateX(0); } }
                    .ftape {
                        position: absolute; left: -50%; right: -50%; width: 200%;
                        height: 38px; display: flex; align-items: center; overflow: hidden;
                        pointer-events: none; z-index: 10;
                        opacity: 0;
                        transition: transform 0.7s cubic-bezier(0.16,1,0.3,1), opacity 0.4s ease;
                    }
                    @media (min-width: 768px) { .ftape { height: 54px; } }
                    .ftape.from-left  { transform: translateX(-110%) rotate(-0.7deg); }
                    .ftape.from-right { transform: translateX(110%)  rotate(0.7deg);  }
                    .ftape.d1 { transition-delay: 0s;    }
                    .ftape.d2 { transition-delay: 0.08s; }
                    .ftape.d3 { transition-delay: 0.16s; }
                    .ftape.d4 { transition-delay: 0.24s; }
                    .ftape.d5 { transition-delay: 0.32s; }
                    .ftape.d6 { transition-delay: 0.40s; }
                    .footer-cta-hover:hover .ftape { opacity: 1; }
                    .footer-cta-hover:hover .ftape.from-left  { transform: translateX(0) rotate(-0.7deg); }
                    .footer-cta-hover:hover .ftape.from-right { transform: translateX(0) rotate(0.7deg);  }
                    @media (max-width: 1023px) {
                        .ftape { opacity: 1 !important; }
                        .ftape.from-left  { transform: translateX(0) rotate(-0.7deg) !important; }
                        .ftape.from-right { transform: translateX(0) rotate(0.7deg)  !important; }
                    }
                </style>"""

TAPES_6 = """
      <!-- Police Tape 1: from LEFT, scrolls LEFT -->
      <div class="ftape from-left d1" style="top: 15%; background: #dc2626; box-shadow: 0 0 50px rgba(196,30,58,0.6);">
        <div class="flex whitespace-nowrap gap-8 text-white font-bold serif text-[12px] md:text-xl tracking-[0.3em]" style="animation: tapeSlideLeft 15s linear infinite;">
          <span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span>
        </div>
      </div>

      <!-- Police Tape 2: from LEFT, scrolls RIGHT -->
      <div class="ftape from-left d2" style="top: 30%; background: #050505; border-top: 2px solid #c0251a; border-bottom: 2px solid #c0251a; box-shadow: 0 0 30px rgba(196,30,58,0.2);">
        <div class="flex whitespace-nowrap gap-8 font-bold serif text-[12px] md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: tapeSlideRight 15s linear infinite;">
          <span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span>
        </div>
      </div>

      <!-- Police Tape 3: from RIGHT, scrolls LEFT -->
      <div class="ftape from-right d3" style="top: 45%; background: #dc2626; box-shadow: 0 0 50px rgba(196,30,58,0.6);">
        <div class="flex whitespace-nowrap gap-8 text-white font-bold serif text-[12px] md:text-xl tracking-[0.3em]" style="animation: tapeSlideLeft 15s linear infinite;">
          <span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>START PROJECT</span>
        </div>
      </div>

      <!-- Police Tape 4: from RIGHT, scrolls RIGHT -->
      <div class="ftape from-right d4" style="top: 60%; background: #050505; border-top: 2px solid #c0251a; border-bottom: 2px solid #c0251a; box-shadow: 0 0 30px rgba(196,30,58,0.2);">
        <div class="flex whitespace-nowrap gap-8 font-bold serif text-[12px] md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: tapeSlideRight 15s linear infinite;">
          <span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>GET IN TOUCH</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span>
        </div>
      </div>

      <!-- Police Tape 5: from LEFT, scrolls LEFT -->
      <div class="ftape from-left d5" style="top: 75%; background: #dc2626; box-shadow: 0 0 50px rgba(196,30,58,0.6);">
        <div class="flex whitespace-nowrap gap-8 text-white font-bold serif text-[12px] md:text-xl tracking-[0.3em]" style="animation: tapeSlideLeft 15s linear infinite;">
          <span>LET'S TALK</span><span style="opacity:0.5">///</span><span>GET IN TOUCH</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>GET IN TOUCH</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>GET IN TOUCH</span><span style="opacity:0.5">///</span><span>LET'S TALK</span><span style="opacity:0.5">///</span><span>GET IN TOUCH</span>
        </div>
      </div>

      <!-- Police Tape 6: from RIGHT, scrolls RIGHT -->
      <div class="ftape from-right d6" style="top: 90%; background: #050505; border-top: 2px solid #c0251a; border-bottom: 2px solid #c0251a; box-shadow: 0 0 30px rgba(196,30,58,0.2);">
        <div class="flex whitespace-nowrap gap-8 font-bold serif text-[12px] md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: tapeSlideRight 15s linear infinite;">
          <span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>LET'S TALK</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>LET'S TALK</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span><span style="opacity:0.4">///</span><span>LET'S TALK</span><span style="opacity:0.4">///</span><span>WAITING FOR YOU</span>
        </div>
      </div>"""


def process_6tape_file(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Add footer-cta-hover to the group div (expertise/pinhole use a slightly different class string)
    # expertise uses: class="group relative w-full flex justify-center items-center min-h-[320px]...
    content = re.sub(
        r'(class=")(group relative w-full flex justify-center items-center)',
        r'\1footer-cta-hover \2',
        content
    )

    # 2. Remove old style blocks (tapeSlide keyframes + mobile-reveal styles)
    content = re.sub(
        r'\s*<style>\s*@keyframes tapeSlideLeft.*?</style>',
        '',
        content,
        flags=re.DOTALL
    )
    # Also remove the mobile-reveal style block
    content = re.sub(
        r'\s*<style>\s*@media \(max-width: 1023px\).*?\.mobile-reveal.*?</style>',
        '',
        content,
        flags=re.DOTALL
    )

    # 3. Replace old tape divs (Police Tape 1 through Police Tape 6)
    content = re.sub(
        r'\s*<!-- Police Tape 1 -->.*?<!-- Police Tape 6 -->.*?</div>(?=\s*\n\s*</div>)',
        '\n' + NEW_STYLE_6 + TAPES_6,
        content,
        flags=re.DOTALL
    )

    if content == original:
        print(f'WARNING: Nothing changed in {fname}')
    else:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'OK: {fname}')


process_6tape_file('expertise.html')
process_6tape_file('pinhole.html')
print('6-tape files done.')
