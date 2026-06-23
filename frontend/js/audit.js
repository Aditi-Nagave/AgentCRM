// frontend/js/audit.js
async function loadAudit(){

    const entityType =
    document
    .getElementById(
        "entityType"
    )
    .value

    const entityId =
    document
    .getElementById(
        "entityId"
    )
    .value

    if(!entityId){

        alert(
            "Enter Entity ID"
        )

        return
    }

    const logs =
    await apiGet(

        `/audit/${entityType}/${entityId}`

    )

    if(
        logs.error
    ){

        alert(
            logs.error
        )

        return
    }

    renderAuditLogs(
        logs
    )
}

function renderAuditLogs(
    logs
){

    let html = ""

    if(
        logs.length === 0
    ){

        html = `

        <div class="card">

            No Audit Logs Found

        </div>

        `

        document
        .getElementById(
            "auditResults"
        )
        .innerHTML = html

        return
    }

    logs.forEach(log=>{

        html += `

        <div class="card">

            <h3>

                ${log.action}

            </h3>

            <p>

                <b>Entity Type:</b>

                ${log.entity_type}

            </p>

            <p>

                <b>Entity ID:</b>

                ${log.entity_id}

            </p>

            <p>

                <b>Performed By:</b>

                ${log.performed_by}

            </p>

            <p>

                <b>Timestamp:</b>

                ${log.timestamp}

            </p>

            <p>

                <b>Diff:</b>

            </p>

            <pre>

${JSON.stringify(
    log.diff,
    null,
    2
)}

            </pre>

        </div>

        `
    })

    document
    .getElementById(
        "auditResults"
    )
    .innerHTML = html
}