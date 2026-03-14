const fs = require('fs');

fetch('https://raw.githubusercontent.com/PavelDoGreat/WebGL-Fluid-Simulation/master/script.js')
.then(res => res.text())
.then(text => {
    // Force entirely standard Unix line endings
    const fixed = text.replace(/\r\n|\r/g, '\n');
    fs.writeFileSync('pavel-fluid.js', fixed, 'utf8');
    console.log("SUCCESS. Lines: " + fixed.split('\n').length);
    console.log("Contains requestAnimationFrame: " + fixed.includes("requestAnimationFrame"));
})
.catch(err => console.error("DOWNLOAD ERROR: ", err));
