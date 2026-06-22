// frontend/js/audit.js
async function loadAudit() {

    const type =
        document.getElementById(
            "entityType"
        ).value;

    const id =
        document.getElementById(
            "entityId"
        ).value;

    const data =
        await getData(
            `/audit/${type}/${id}`
        );

    let html = "";

    if (data.error) {

        html =
        `<div class="result-card">
            ${data.error}
        </div>`;

    } else {

        data.forEach(log => {

            html += `
            <div class="result-card">
                <h4>${log.action}</h4>
                <p>${log.entity_type}</p>
                <p>${log.timestamp}</p>
            </div>
            `;
        });
    }

    document.getElementById(
        "auditResults"
    ).innerHTML = html;
}