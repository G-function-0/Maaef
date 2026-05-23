import re

with open('Maaef Direction A.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the tape array and map from line 776-808
OLD = """            {[
              { top: '15%', rot: -1.2, bg: '#dc2626', color: '#fff', a: 'left', h: 54, txt: ['LET\\u2019S TALK', 'START PROJECT'] },
              { top: '30%', rot: 0.8, bg: '#050505', color: '#dc2626', border: true, a: 'right', h: 50, txt: ['WAITING FOR YOU', 'GET IN TOUCH'] },
              { top: '45%', rot: -0.5, bg: '#dc2626', color: '#fff', a: 'right', h: 58, txt: ['LET\\u2019S TALK', 'LET\\u2019S TALK'] },
              { top: '60%', rot: 1.1, bg: '#050505', color: '#dc2626', border: true, a: 'left', h: 52, txt: ['WAITING FOR YOU', 'START PROJECT'] },
              { top: '75%', rot: -0.9, bg: '#dc2626', color: '#fff', a: 'left', h: 56, txt: ['LET\\u2019S TALK', 'GET IN TOUCH'] },
              { top: '90%', rot: 0.6, bg: '#050505', color: '#dc2626', border: true, a: 'right', h: 52, txt: ['WAITING FOR YOU', 'LET\\u2019S TALK'] },
            ].map((tape, i) => (
              <div key={i} style={{
                position: 'absolute', left: '-50%', right: '-50%', width: '200%', height: isMobile ? tape.h * 0.7 : tape.h, top: tape.top,
                background: tape.bg, border: tape.border ? '2px solid #c0251a' : 'none',
                boxShadow: tape.bg === '#dc2626' ? '0 0 50px rgba(196,30,58,0.6)' : '0 0 30px rgba(196,30,58,0.2)',
                opacity: showTapes ? 1 : 0,
                transform: `rotate(${tape.rot}deg) scaleX(${showTapes ? 1 : 0})`,
                transformOrigin: tape.a, transition: `all .7s cubic-bezier(.16,1,.3,1) ${i * 0.08}s`,
                display: 'flex', alignItems: 'center', overflow: 'hidden', zIndex: 10, pointerEvents: 'none',
              }}>
                <div className="serif" style={{
                  whiteSpace: 'nowrap', display: 'flex', gap: isMobile ? 18 : 28, color: tape.color,
                  fontWeight: 700, fontSize: isMobile ? 12 : 18, letterSpacing: '0.3em',
                  animation: `maaef-marquee 15s linear infinite ${i % 2 ? 'reverse' : 'normal'}`,
                }}>
                  {Array.from({ length: 16 }).map((_, k) => (
                    <React.Fragment key={k}>
                      <span>{tape.txt[0]}</span>
                      <span style={{ opacity: 0.5 }}>///</span>
                      <span>{tape.txt[1]}</span>
                      <span style={{ opacity: 0.5 }}>///</span>
                    </React.Fragment>
                  ))}
                </div>
              </div>
            ))}"""

NEW = """            {[
              { top: '15%', rot: -0.7, fromLeft: true,  bg: '#dc2626', color: '#fff',    border: false, h: 54, scrollLeft: true,  txt: ['LET\u2019S TALK', 'START PROJECT'] },
              { top: '30%', rot:  0.7, fromLeft: true,  bg: '#050505', color: '#dc2626', border: true,  h: 50, scrollLeft: false, txt: ['WAITING FOR YOU', 'GET IN TOUCH'] },
              { top: '45%', rot: -0.7, fromLeft: false, bg: '#dc2626', color: '#fff',    border: false, h: 58, scrollLeft: true,  txt: ['LET\u2019S TALK', 'START PROJECT'] },
              { top: '60%', rot:  0.7, fromLeft: false, bg: '#050505', color: '#dc2626', border: true,  h: 52, scrollLeft: false, txt: ['WAITING FOR YOU', 'GET IN TOUCH'] },
              { top: '75%', rot: -0.7, fromLeft: true,  bg: '#dc2626', color: '#fff',    border: false, h: 56, scrollLeft: true,  txt: ['LET\u2019S TALK', 'GET IN TOUCH'] },
              { top: '90%', rot:  0.7, fromLeft: false, bg: '#050505', color: '#dc2626', border: true,  h: 52, scrollLeft: false, txt: ['WAITING FOR YOU', 'LET\u2019S TALK'] },
            ].map((tape, i) => {
              const offX = tape.fromLeft ? '-110%' : '110%';
              return (
              <div key={i} style={{
                position: 'absolute', left: '-50%', right: '-50%', width: '200%',
                height: isMobile ? tape.h * 0.7 : tape.h, top: tape.top,
                background: tape.bg,
                border: tape.border ? '2px solid #c0251a' : 'none',
                boxShadow: tape.bg === '#dc2626' ? '0 0 50px rgba(196,30,58,0.6)' : '0 0 30px rgba(196,30,58,0.2)',
                opacity: showTapes ? 1 : 0,
                transform: showTapes
                  ? `translateX(0) rotate(${tape.rot}deg)`
                  : `translateX(${offX}) rotate(${tape.rot}deg)`,
                transition: `transform 0.7s cubic-bezier(0.16,1,0.3,1) ${i * 0.08}s, opacity 0.4s ease ${i * 0.08}s`,
                display: 'flex', alignItems: 'center', overflow: 'hidden', zIndex: 10, pointerEvents: 'none',
              }}>
                <div className="serif" style={{
                  whiteSpace: 'nowrap', display: 'flex', gap: isMobile ? 18 : 28, color: tape.color,
                  fontWeight: 700, fontSize: isMobile ? 12 : 18, letterSpacing: '0.3em',
                  animation: `maaef-marquee 15s linear infinite ${tape.scrollLeft ? 'normal' : 'reverse'}`,
                }}>
                  {Array.from({ length: 16 }).map((_, k) => (
                    <React.Fragment key={k}>
                      <span>{tape.txt[0]}</span>
                      <span style={{ opacity: 0.5 }}>///</span>
                      <span>{tape.txt[1]}</span>
                      <span style={{ opacity: 0.5 }}>///</span>
                    </React.Fragment>
                  ))}
                </div>
              </div>
            );})}"""

if OLD in content:
    content = content.replace(OLD, NEW)
    with open('Maaef Direction A.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK: Maaef Direction A.html')
else:
    print('WARNING: OLD block not found')
    # Try to find where it differs
    idx = content.find("{ top: '15%', rot: -1.2")
    print(f'Found tape config at pos: {idx}')
    if idx > 0:
        print(repr(content[idx:idx+200]))
