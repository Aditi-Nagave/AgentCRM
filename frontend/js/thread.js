// frontend/js/thread.js

const params =
new URLSearchParams(
    window.location.search
)

const sender =
params.get("email")

let currentEmailId = 1

async function loadWorkspace(){

    const thread =
    await apiGet(
        `/threads/${sender}`
    )

    renderTimeline(
        thread
    )

    const contact =
    await apiGet(
        `/contacts/${sender}`
    )

    renderContact(
        contact
    )

    loadAgentLogs()

}

function renderTimeline(
    emails
){

    let html = ""

    emails.forEach(email=>{

        currentEmailId =
        email.id

        html += `

        <div class="timeline-email">

            <h3>
                ${email.subject}
            </h3>

            <p>
                ${email.body}
            </p>

            <span class="
                badge
                badge-${(
                    email.sentiment ||
                    "neutral"
                ).toLowerCase()}
            ">

                ${email.sentiment}

            </span>

            <span class="
                badge
                badge-${(
                    email.urgency ||
                    "low"
                ).toLowerCase()}
            ">

                ${email.urgency}

            </span>

        </div>

        `
    })

    document
    .getElementById(
        "timelinePane"
    )
    .innerHTML = html
}

function renderContact(
    contact
){

    document
    .getElementById(
        "contactPane"
    )
    .innerHTML = `

        <div class="contact-card">

            <p>
                <b>Name:</b>
                ${contact.name || ""}
            </p>

            <p>
                <b>Company:</b>
                ${contact.company || ""}
            </p>

            <p>
                <b>Status:</b>
                ${contact.status || ""}
            </p>

            <p>
                <b>Account Value:</b>
                ${contact.account_value || 0}
            </p>

            <p>
                <b>Churn Risk:</b>
                ${contact.churn_risk_score || 0}
            </p>

        </div>

    `
}

async function loadAgentLogs(){

    const logs =
    await apiGet(
        `/agent/logs/${currentEmailId}`
    )

    let html = ""

    logs.forEach(log=>{

        html += `

        <div class="agent-step">

            <p>

                <b>Action:</b>

                ${log.action_type}

            </p>

        </div>

        `
    })

    document
    .getElementById(
        "agentPane"
    )
    .innerHTML = html
}

async function saveDraft(){

    const draft =
    document
    .getElementById(
        "draftText"
    )
    .value

    const result =
    await apiPatch(

        `/drafts/${currentEmailId}`,

        {
            draft:draft
        }
    )

    alert(
        JSON.stringify(
            result
        )
    )
}

async function approveDraft(){

    const result =
    await apiPost(
        `/drafts/${currentEmailId}/approve`
    )

    alert(
        JSON.stringify(
            result
        )
    )
}

loadWorkspace()