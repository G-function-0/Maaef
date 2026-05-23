import os
import re

NEW_CTA = """<div class="footer-cta-hover relative w-full flex justify-center items-center h-[75vh] md:h-[90vh] bg-[#030303]
                border-t border-b border-white/[.05] mb-8 overflow-hidden group cursor-pointer"
         onclick="window.location.href='/contact'">

        <div class="absolute inset-0 pointer-events-none z-40 bg-[radial-gradient(circle_at_center,transparent_25%,rgba(3,3,3,0.95)_100%)]"></div>

        <h2 class="serif text-[18vw] md:text-[14vw] leading-none text-transparent tracking-tighter
                   transition-all duration-500 relative z-50
                   [-webkit-text-stroke:2px_#C41E3A]
                   group-hover:text-black group-hover:[-webkit-text-stroke:2px_#C41E3A]">
            Maaef.
        </h2>

        <svg class="absolute inset-0 w-full h-full z-0 opacity-30 pointer-events-none" viewBox="0 0 1000 500" preserveAspectRatio="none">
            <path d="M-100,100 Q200,200 400,50 T700,150 T1100,50" 
                  stroke="#dc2626" stroke-width="2" fill="none" 
                  style="filter: drop-shadow(0px 0px 10px rgba(220,38,38,1));" />
            <path d="M-100,400 Q250,300 500,450 T800,350 T1100,450" 
                  stroke="#dc2626" stroke-width="3" fill="none" 
                  style="filter: drop-shadow(0px 0px 15px rgba(220,38,38,0.8));" />
        </svg>

        <style>
            @keyframes slideLeft  { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
            @keyframes slideRight { 0% { transform: translateX(-50%); } 100% { transform: translateX(0); } }

            .concept-tape {
                position: absolute;
                display: flex;
                pointer-events: none;
                opacity: 0.95;
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
        </style>

        <div class="concept-tape ct-1">
            <div class="w-full bg-[#dc2626] py-3 shadow-[0_0_40px_rgba(220,38,38,0.5)]">
                <div class="marquee-content gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style="animation: slideRight 30s linear infinite;">
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                </div>
            </div>
        </div>

        <div class="concept-tape ct-2">
            <div class="w-full bg-[#050505] py-2 border-y border-[#c0251a]">
                <div class="marquee-content gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: slideLeft 35s linear infinite;">
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                </div>
            </div>
        </div>

        <div class="concept-tape ct-3">
            <div class="w-full bg-[#dc2626] py-3 shadow-[0_0_40px_rgba(220,38,38,0.5)]">
                <div class="marquee-content gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style="animation: slideRight 32s linear infinite;">
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span class="opacity-50 text-black">///</span><span>START PROJECT</span><span class="opacity-50 text-black">///</span>
                </div>
            </div>
        </div>

        <div class="concept-tape ct-4">
            <div class="w-full bg-[#050505] py-2 border-y border-[#c0251a]">
                <div class="marquee-content gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: slideLeft 28s linear infinite;">
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                </div>
            </div>
        </div>

        <div class="concept-tape ct-5">
            <div class="w-full bg-[#050505] py-2 md:py-3 border-y border-[#c0251a]">
                <div class="marquee-content gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style="color: #dc2626; animation: slideRight 26s linear infinite;">
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                </div>
            </div>
        </div>

        <div class="concept-tape ct-6">
            <div class="w-full bg-[#dc2626] py-2 md:py-3 shadow-[0_0_30px_rgba(220,38,38,0.5)]">
                <div class="marquee-content gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style="animation: slideLeft 24s linear infinite;">
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                </div>
            </div>
        </div>

    </div>"""

files = ['index.html', 'about.html', 'contact.html', 'services.html', 'expertise.html', 'pinhole.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace the whole footer-cta-hover block with the NEW_CTA
    # It starts with <div class="footer-cta-hover... and ends just before <div class="max-w-[1400px]... Bottom bar -->
    # Since I've seen it earlier, the block is closed by </div></div> before the bottom bar wrapper.
    
    pattern = re.compile(r'<div class="footer-cta-hover [^>]*>.*?</div>\s*</div>', re.DOTALL)
    
    # But wait, in the previous script it was matching until the end of tapes. 
    # Let's write a smarter regex: from <div class="footer-cta-hover ... to the </div> right before <div class="max-w-[1400px]
    
    new_content = re.sub(r'<div\s+class="footer-cta-hover[^>]*>.*?(?=\s*<div\s+class="max-w-\[1400px\]\s+mx-auto)', NEW_CTA, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced in", filename)
