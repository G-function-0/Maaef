import re
import glob

NEW_FOOTER = """<footer id="main-footer" class="relative bg-[#050505] pt-20 pb-8 overflow-hidden border-t border-white/[.05]">

    <div class="absolute inset-0 opacity-[0.03] pointer-events-none z-0"
         style="background-image: url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 200 200%27%3E%3C/svg%3E')"></div>

    <div class="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 md:gap-8 mb-16">

            <div class="col-span-1 lg:col-span-2">
                <a href="/" class="inline-block hover-trigger mb-6">
                    <img src="logo.png" alt="Maaef Logo" class="h-10 w-auto opacity-90 hover:opacity-100 transition-opacity">
                </a>
                <p class="text-gray-400 text-sm md:text-base max-w-sm font-light leading-relaxed border-l-2 border-red-600 pl-4">
                    We engineer attention.<br>A new-era media house.
                </p>
            </div>

            <div>
                <h3 class="serif text-white text-lg mb-6 tracking-wide opacity-90">Navigation</h3>
                <ul class="space-y-4 text-xs tracking-[0.2em] uppercase">
                    <li><a href="/"              class="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Home</a></li>
                    <li><a href="/about.html"    class="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Clients</a></li>
                    <li><a href="/services.html" class="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Services</a></li>
                    <li><a href="/contact.html"  class="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Contact</a></li>
                </ul>
            </div>

            <div>
                <h3 class="serif text-white text-lg mb-6 tracking-wide opacity-90">Connect</h3>
                <ul class="space-y-4 text-xs tracking-[0.2em] uppercase">
                    <li><a href="https://www.instagram.com/maaef.media" target="_blank" rel="noopener noreferrer"
                           class="text-gray-500 hover:text-red-500 transition duration-300 hover-trigger inline-block">Instagram</a></li>
                    <li class="pt-2"><a href="/contact.html"
                           class="text-red-600 hover:text-red-500 transition duration-300 hover-trigger inline-block font-bold">Start Project</a></li>
                </ul>
            </div>

        </div>
    </div>

    <!-- Big text CTA -->
    <div id="cta-block" class="footer-cta-hover relative w-full flex justify-center items-center h-[30vh] md:h-[55vh] bg-[#030303]
                border-t border-b border-white/[.05] mb-8 overflow-hidden group cursor-pointer"
         onclick="window.location.href='/contact.html'">

        <div class="absolute inset-0 pointer-events-none z-40 bg-[radial-gradient(circle_at_center,transparent_25%,rgba(3,3,3,0.95)_100%)]"></div>

        <h2 class="serif text-[18vw] md:text-[14vw] leading-none text-transparent tracking-tighter
                   transition-all duration-500 relative z-50
                   [-webkit-text-stroke:2px_#C41E3A]
                   group-hover:text-black group-hover:[-webkit-text-stroke:2px_#C41E3A]">
            Maaef.
        </h2>

        <style>
            @keyframes slideRight { 0% { transform: translateX(-50%); } 100% { transform: translateX(0); } }
            @keyframes slideLeft  { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

            .concept-tape {
                position: absolute;
                display: flex;
                pointer-events: none;
                opacity: 0;
                transition: opacity 0.6s ease, filter 0.6s ease, clip-path 0.8s cubic-bezier(0.7, 0, 0.3, 1);
                filter: blur(4px);
                transform-origin: 0% 50%;
                overflow: hidden;
                will-change: transform, clip-path;
            }
            .footer-cta-hover:hover .concept-tape {
                opacity: 0.95;
                filter: blur(0px);
                clip-path: inset(0 0 0 0);
            }
            .marquee-content { display: flex; width: max-content; }

            .ct-1 { z-index: 13; clip-path: inset(0 100% 0 0); }
            .ct-2 { z-index: 11; clip-path: inset(0 0 0 100%); }
            .ct-3 { z-index: 12; clip-path: inset(0 100% 0 0); }
            .ct-4 { z-index: 10; clip-path: inset(0 0 0 100%); }

            @media (max-width: 1023px) {
                .concept-tape { opacity: 0.95 !important; filter: blur(0px) !important; }
            }
            @media (max-width: 767px) {
                .marquee-content { font-size: 10px !important; }
                .concept-tape > div { padding-top: 6px !important; padding-bottom: 6px !important; }
            }
        </style>

        <div class="concept-tape ct-1" data-start="0,-7.5" data-end="74,105">
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

        <div class="concept-tape ct-2" data-start="2,45.5" data-end="86,-5.5">
            <div class="w-full bg-[#050505] py-2 border-y border-[#c0251a]">
                <div class="marquee-content gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style="color:#dc2626; animation: slideLeft 35s linear infinite;">
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span>
                </div>
            </div>
        </div>

        <div class="concept-tape ct-3" data-start="2,56" data-end="96,80">
            <div class="w-full bg-[#dc2626] py-3 shadow-[0_0_40px_rgba(220,38,38,0.5)]">
                <div class="marquee-content gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style="animation: slideRight 32s linear infinite;">
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span class="opacity-50 text-black">///</span><span>LET'S TALK</span><span class="opacity-50 text-black">///</span>
                </div>
            </div>
        </div>

        <div class="concept-tape ct-4" data-start="2,92" data-end="96,18">
            <div class="w-full bg-[#050505] py-2 border-y border-[#c0251a]">
                <div class="marquee-content gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style="color:#dc2626; animation: slideLeft 28s linear infinite;">
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span class="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span class="opacity-30 text-white">///</span>
                </div>
            </div>
        </div>

    </div>

    <div class="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">
        <div class="flex flex-col md:flex-row justify-between items-center gap-6 pt-2">
            <span class="text-[10px] uppercase tracking-widest" style="color:rgba(255,255,255,.25)">© 2026 Maaef Media House</span>

            <a href="https://dev-folio-wine.vercel.app/" target="_blank" rel="noopener noreferrer"
               class="text-[10px] uppercase tracking-widest hover:text-white transition duration-300 hover-trigger group flex items-center gap-2"
               style="color:rgba(255,255,255,.3)">
                Made with <span class="text-red-600 group-hover:scale-125 transition-transform duration-300">&#10084;</span> &amp; Coffee by Humans
            </a>

            <div class="flex items-center gap-6">
                <span class="text-[10px] uppercase tracking-widest" style="color:rgba(255,255,255,.25)">Lucknow, IN</span>
                <span onclick="window.scrollTo({top:0,behavior:'smooth'})"
                      class="text-[10px] uppercase tracking-widest hover:text-white transition cursor-pointer hover-trigger"
                      style="color:rgba(255,255,255,.25)">&#8593; Top</span>
            </div>
        </div>
    </div>

    <script>
    (function () {
        const cta = document.getElementById('cta-block');
        if (!cta) return;
        const tapes = cta.querySelectorAll('.concept-tape[data-start]');
        function position() {
            const W = cta.clientWidth, H = cta.clientHeight;
            tapes.forEach(el => {
                const [x1, y1] = el.dataset.start.split(',').map(Number);
                const [x2, y2] = el.dataset.end.split(',').map(Number);
                const dx = (x2 - x1) / 100 * W;
                const dy = (y2 - y1) / 100 * H;
                el.style.left  = (x1 / 100 * W) + 'px';
                el.style.top   = (y1 / 100 * H - el.offsetHeight / 2) + 'px';
                el.style.width = Math.hypot(dx, dy) + 'px';
                el.style.transform = 'rotate(' + (Math.atan2(dy, dx) * 180 / Math.PI) + 'deg)';
            });
        }
        window.positionMaaefStripes = position;
        requestAnimationFrame(() => requestAnimationFrame(position));
        window.addEventListener('resize', position);
    })();
    </script>

</footer>"""

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    match = re.search(r'<footer id="main-footer".*?</footer>', content, re.DOTALL)
    if match:
        new_content = content[:match.start()] + NEW_FOOTER + content[match.end():]
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated', f)
