import re

JSX_FOOTER = """function MaaefFooter() {
      const ctaRef = useRef(null);

      useEffect(() => {
        const cta = ctaRef.current;
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
        position();
        window.addEventListener('resize', position);
        // Trigger a couple times to ensure font loaded metrics
        requestAnimationFrame(() => requestAnimationFrame(position));
        return () => window.removeEventListener('resize', position);
      }, []);

      return (
<footer id="main-footer" className="relative bg-[#050505] pt-20 pb-8 overflow-hidden border-t border-white/[.05]">

    <div className="absolute inset-0 opacity-[0.03] pointer-events-none z-0"
         style={{ backgroundImage: "url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 200 200%27%3E%3C/svg%3E')" }}></div>

    <div className="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 md:gap-8 mb-16">

            <div className="col-span-1 lg:col-span-2">
                <a href="/" className="inline-block hover-trigger mb-6">
                    <img src="logo.png" alt="Maaef Logo" className="h-10 w-auto opacity-90 hover:opacity-100 transition-opacity" />
                </a>
                <p className="text-gray-400 text-sm md:text-base max-w-sm font-light leading-relaxed border-l-2 border-red-600 pl-4">
                    We engineer attention.<br/>A new-era media house.
                </p>
            </div>

            <div>
                <h3 className="serif text-white text-lg mb-6 tracking-wide opacity-90">Navigation</h3>
                <ul className="space-y-4 text-xs tracking-[0.2em] uppercase">
                    <li><a href="/"              className="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Home</a></li>
                    <li><a href="/about.html"    className="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Clients</a></li>
                    <li><a href="/services.html" className="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Services</a></li>
                    <li><a href="/contact.html"  className="text-gray-500 hover:text-white transition duration-300 hover-trigger inline-block">Contact</a></li>
                </ul>
            </div>

            <div>
                <h3 className="serif text-white text-lg mb-6 tracking-wide opacity-90">Connect</h3>
                <ul className="space-y-4 text-xs tracking-[0.2em] uppercase">
                    <li><a href="https://www.instagram.com/maaef.media" target="_blank" rel="noopener noreferrer"
                           className="text-gray-500 hover:text-red-500 transition duration-300 hover-trigger inline-block">Instagram</a></li>
                    <li className="pt-2"><a href="/contact.html"
                           className="text-red-600 hover:text-red-500 transition duration-300 hover-trigger inline-block font-bold">Start Project</a></li>
                </ul>
            </div>

        </div>
    </div>

    {/* Big text CTA */}
    <div id="cta-block" ref={ctaRef} className="footer-cta-hover relative w-full flex justify-center items-center h-[30vh] md:h-[55vh] bg-[#030303] border-t border-b border-white/[.05] mb-8 overflow-hidden group cursor-pointer"
         onClick={() => window.location.href='/contact.html'}>

        <div className="absolute inset-0 pointer-events-none z-40 bg-[radial-gradient(circle_at_center,transparent_25%,rgba(3,3,3,0.95)_100%)]"></div>

        <h2 className="serif text-[18vw] md:text-[14vw] leading-none text-transparent tracking-tighter
                   transition-all duration-500 relative z-50
                   [-webkit-text-stroke:2px_#C41E3A]
                   group-hover:text-black group-hover:[-webkit-text-stroke:2px_#C41E3A]">
            Maaef.
        </h2>

        <style dangerouslySetInnerHTML={{ __html: `
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
        `}} />

        <div className="concept-tape ct-1" data-start="0,-7.5" data-end="74,105">
            <div className="w-full bg-[#dc2626] py-3 shadow-[0_0_40px_rgba(220,38,38,0.5)]">
                <div className="marquee-content gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style={{ animation: 'slideRight 30s linear infinite' }}>
                    <span>LET'S TALK</span><span className="opacity-50 text-black">///</span><span>START PROJECT</span><span className="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span className="opacity-50 text-black">///</span><span>START PROJECT</span><span className="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span className="opacity-50 text-black">///</span><span>START PROJECT</span><span className="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span className="opacity-50 text-black">///</span><span>START PROJECT</span><span className="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span className="opacity-50 text-black">///</span><span>START PROJECT</span><span className="opacity-50 text-black">///</span>
                    <span>LET'S TALK</span><span className="opacity-50 text-black">///</span><span>START PROJECT</span><span className="opacity-50 text-black">///</span>
                </div>
            </div>
        </div>

        <div className="concept-tape ct-2" data-start="2,45.5" data-end="86,-5.5">
            <div className="w-full bg-[#050505] py-2 border-y border-[#c0251a]">
                <div className="marquee-content gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style={{ color: '#dc2626', animation: 'slideLeft 35s linear infinite' }}>
                    <span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span>
                    <span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span><span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span>
                </div>
            </div>
        </div>

        <div className="concept-tape ct-3" data-start="2,56" data-end="96,80">
            <div className="w-full bg-[#dc2626] py-3 shadow-[0_0_40px_rgba(220,38,38,0.5)]">
                <div className="marquee-content gap-8 text-white font-bold serif text-sm md:text-xl tracking-[0.3em]" style={{ animation: 'slideRight 32s linear infinite' }}>
                    <span>START PROJECT</span><span className="opacity-50 text-black">///</span><span>LET'S TALK</span><span className="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span className="opacity-50 text-black">///</span><span>LET'S TALK</span><span className="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span className="opacity-50 text-black">///</span><span>LET'S TALK</span><span className="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span className="opacity-50 text-black">///</span><span>LET'S TALK</span><span className="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span className="opacity-50 text-black">///</span><span>LET'S TALK</span><span className="opacity-50 text-black">///</span>
                    <span>START PROJECT</span><span className="opacity-50 text-black">///</span><span>LET'S TALK</span><span className="opacity-50 text-black">///</span>
                </div>
            </div>
        </div>

        <div className="concept-tape ct-4" data-start="2,92" data-end="96,18">
            <div className="w-full bg-[#050505] py-2 border-y border-[#c0251a]">
                <div className="marquee-content gap-8 font-bold serif text-sm md:text-xl tracking-[0.3em]" style={{ color: '#dc2626', animation: 'slideLeft 28s linear infinite' }}>
                    <span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span>
                    <span>GET IN TOUCH</span><span className="opacity-30 text-white">///</span><span>WAITING FOR YOU</span><span className="opacity-30 text-white">///</span>
                </div>
            </div>
        </div>

    </div>

    <div className="max-w-[1400px] mx-auto px-6 md:px-12 relative z-10">
        <div className="flex flex-col md:flex-row justify-between items-center gap-6 pt-2">
            <span className="text-[10px] uppercase tracking-widest" style={{ color: 'rgba(255,255,255,.25)' }}>© 2026 Maaef Media House</span>

            <a href="https://dev-folio-wine.vercel.app/" target="_blank" rel="noopener noreferrer"
               className="text-[10px] uppercase tracking-widest hover:text-white transition duration-300 hover-trigger group flex items-center gap-2"
               style={{ color: 'rgba(255,255,255,.3)' }}>
                Made with <span className="text-red-600 group-hover:scale-125 transition-transform duration-300">&#10084;</span> &amp; Coffee by Humans
            </a>

            <div className="flex items-center gap-6">
                <span className="text-[10px] uppercase tracking-widest" style={{ color: 'rgba(255,255,255,.25)' }}>Lucknow, IN</span>
                <span onClick={() => window.scrollTo({top:0,behavior:'smooth'})}
                      className="text-[10px] uppercase tracking-widest hover:text-white transition cursor-pointer hover-trigger"
                      style={{ color: 'rgba(255,255,255,.25)' }}>&#8593; Top</span>
            </div>
        </div>
    </div>
</footer>
      );
    }
"""

with open('Maaef Direction A.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract from function MaaefFooter() { to the end of the function.
# We know the function ends before "function DirectionA("
match = re.search(r'function MaaefFooter\(\) \{.*?\}\n\s*function DirectionA\(', content, re.DOTALL)
if match:
    new_content = content[:match.start()] + JSX_FOOTER + "\n\n    function DirectionA(" + content[match.end()-20:]
    # Because of the overlap of "function DirectionA(", let's do it cleanly:
    
with open('Maaef Direction A.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
new_content = re.sub(r'function MaaefFooter\(\) \{.*?\}\n\s*function DirectionA\(', JSX_FOOTER + '\n\n    function DirectionA(', content, flags=re.DOTALL)

with open('Maaef Direction A.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated Maaef Direction A.html")
