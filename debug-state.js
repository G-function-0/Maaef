const puppeteer = require('puppeteer');

(async () => {
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        
        await page.goto('file:///d:/Maef/Maaef/expertise.html', { waitUntil: 'load' });
        await new Promise(r => setTimeout(r, 1000));

        const diagnostics = await page.evaluate(() => {
            const cvs = document.getElementById('fluid-canvas');
            if(!cvs) return { error: "No canvas!" };
            
            // Assume pointers array is global in Pavel's code
            const p = typeof pointers !== 'undefined' ? pointers[0] : null;
            
            return {
                canvasId: cvs.id,
                clientWidth: cvs.clientWidth,
                clientHeight: cvs.clientHeight,
                renderedWidth: cvs.width,
                renderedHeight: cvs.height,
                pointerExists: !!p,
                pointerState: p ? { moved: p.moved, down: p.down, dx: p.deltaX, dy: p.deltaY, color: p.color } : null,
                isPaused: typeof config !== 'undefined' ? config.PAUSED : 'unknown',
                hasWebGL: !!cvs.getContext('webgl2') || !!cvs.getContext('webgl')
            };
        });

        console.log("DIAGNOSTICS:", JSON.stringify(diagnostics, null, 2));

        // Let's sweep the mouse and see if the variable changes
        if(diagnostics.clientWidth > 0) {
            await page.mouse.move(500, 500);
            await page.mouse.move(600, 600);
            await new Promise(r => setTimeout(r, 100));
            
            const postMove = await page.evaluate(() => {
                const p = typeof pointers !== 'undefined' ? pointers[0] : null;
                return p ? { moved: p.moved, down: p.down, dx: p.deltaX, dy: p.deltaY } : null;
            });
            console.log("POST MOVE POINTER:", JSON.stringify(postMove, null, 2));
        }

        await browser.close();
    } catch(e) {
        console.error(e);
    }
})();
