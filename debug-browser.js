const puppeteer = require('puppeteer');

(async () => {
    try {
        console.log("Launching browser...");
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        
        page.on('console', msg => console.log('BROWSER_LOG [' + msg.type() + ']:', msg.text()));
        page.on('pageerror', err => console.log('BROWSER_ERROR:', err.toString()));
        page.on('requestfailed', request => console.log('NETWORK_ERROR:', request.url() + ' ' + request.failure().errorText));
        
        console.log("Navigating to services.html...");
        await page.goto('file:///d:/Maef/Maaef/services.html', { waitUntil: 'networkidle0' });
        
        console.log("Simulating mouse movements over expertise area...");
        const expertise = await page.$('#expertise-section');
        if (expertise) {
            const box = await expertise.boundingBox();
            console.log("Expertise box:", box);
            if (box) {
                await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
                await new Promise(r => setTimeout(r, 100));
                await page.mouse.move(box.x + box.width / 2 + 50, box.y + box.height / 2 + 50);
                await new Promise(r => setTimeout(r, 100));
                await page.mouse.move(box.x + box.width / 2 + 100, box.y + box.height / 2 + 100);
            }
        }
        
        await new Promise(r => setTimeout(r, 2000));
        await browser.close();
        console.log("Test complete.");
    } catch(e) {
        console.error('PUPPETEER_ERROR:', e);
    }
})();
