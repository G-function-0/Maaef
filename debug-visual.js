const puppeteer = require('puppeteer');

(async () => {
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.setViewport({ width: 1200, height: 800 });
        
        console.log("Navigating...");
        await page.goto('file:///d:/Maef/Maaef/expertise.html', { waitUntil: 'networkidle0' });
        
        await new Promise(r => setTimeout(r, 2000));

        console.log("Simulating mouse moves over expertise block...");
        const expertise = await page.$('#expertise-section');
        if (expertise) {
            const box = await expertise.boundingBox();
            const startX = box.x + 100;
            const startY = box.y + 100;

            await page.mouse.move(startX, startY);
            
            // Perform a sweeping motion over a split-second
            for(let i=1; i<20; i++) {
                await page.mouse.move(startX + i * 20, startY + i * 15);
                await new Promise(r => setTimeout(r, 16)); // mimic 60fps frame delta
            }

            // Let the WebGL buffer draw
            await new Promise(r => setTimeout(r, 200)); 
            
            console.log("Snapping screenshot of expertise section...");
            await expertise.screenshot({ path: 'expertise_fluid_check.png' });
        }
        
        await browser.close();
        console.log("Check expertise_fluid_check.png");
    } catch(e) {
        console.error('ERROR:', e);
    }
})();
