
async function vulnScan() {
    
    console.log("Vulnerability Scan Start");
    
    const response = await fetch('http://127.0.0.1:1337/vulnerability');
    const vulnScanJson = await response.json();
    // vulnScanJson = vulnScanJson.replace(/(\r\n|\n|\r)/gm, `" 
    
    // "`);
    console.log(vulnScanJson);
    console.log("Vulnerability Scan End");

    let results = document.querySelector("#results");
    results.innerHTML = `<span>` + String(vulnScanJson) + `</span>`;

}

document.getElementById('vuln-scan').addEventListener('click', () => {
    vulnScan();
});


// Quick Scan

async function quickScan() {
    
    console.log("Quick Scan Start");
    
    const response = await fetch('http://127.0.0.1:1337/quick');
    const vulnScanJson = await response.json();    
    console.log(vulnScanJson);
    console.log("Quick Scan End");

    let results = document.querySelector("#results");
    results.innerHTML = `<span>` + String(vulnScanJson) + `</span>`;

}

document.getElementById('quick-scan').addEventListener('click', () => {
    quickScan();
});