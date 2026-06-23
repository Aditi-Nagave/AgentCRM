// frontend/js/thread.js

const API =
    "http://127.0.0.1:8000";

const params =
    new URLSearchParams(
        window.location.search
    );

const email =
    params.get("email");

let currentEmailId = null;

async function loadWorkspace() {

    await loadThread();

    await loadContact();

}

async function loadThread() {

    const res =
        await fetch(
            `${API}/threads/${email}`
        );

    const data =
        await res.json();

    if(!data.length)
        return;

    currentEmailId =
        data[0].id;

    renderTimeline(data);

    renderDraft(
        data[0]
    );

    await loadAgentLogs(
        currentEmailId
    );
}

function renderTimeline(
    emails
){

    let html = "";

    emails.forEach(email => {

        html += `

        <div class="email-card">

            <h3>
                ${email.subject}
            </h3>

            <p>
                ${email.body}
            </p>

            <span class="badge badge-negative">
                ${email.sentiment}
            </span>

            <span class="badge badge-low">
                ${email.urgency}
            </span>

        </div>

        `;
    });

    document.getElementById(
        "timelinePane"
    ).innerHTML = html;
}

function renderDraft(
    email
){

    document.getElementById(
        "draftText"
    ).value =
        email.draft_reply || "";
}

async function loadContact() {

    const res =
        await fetch(
            `${API}/contacts/${email}`
        );

    const data =
        await res.json();

    document.getElementById(
        "contactPane"
    ).innerHTML = `

        <p>
            <b>Email:</b>
            ${data.email}
        </p>

        <p>
            <b>Name:</b>
            ${data.name || "N/A"}
        </p>

        <p>
            <b>Company:</b>
            ${data.company || "N/A"}
        </p>

        <p>
            <b>Status:</b>
            ${data.status}
        </p>

        <p>
            <b>Account Value:</b>
            ${data.account_value}
        </p>

        <p>
            <b>Churn Risk:</b>
            ${data.churn_risk_score}
        </p>

    `;
}

async function loadAgentLogs(
    emailId
){

    const res =
        await fetch(
            `${API}/agent/logs/${emailId}`
        );

    const logs =
        await res.json();

    let html = "";

    logs.forEach(log => {

        log.reasoning_trace.forEach(step => {

            html += `

            <div>

                <b>Thought:</b>

                ${step.thought}

                <br>

                <b>Action:</b>

                ${step.action}

                <br>

                <b>Observation:</b>

                ${step.observation}

                <br>

                <b>Next:</b>

                ${step.next_step}

                <hr>

            </div>

            `;
        });
    });

    document.getElementById(
        "agentPane"
    ).innerHTML = html;

    loadDemoRAG();

    loadDemoMarket();
}

function loadDemoRAG(){

    document.getElementById(
        "ragPane"
    ).innerHTML = `

        <b>Complaint Handling Policy</b>

        <p>
        Customers threatening
        public reviews should
        be escalated immediately.
        </p>

        <p>
        Source:
        retention_playbook.md
        </p>

    `;
}

function loadDemoMarket(){

    document.getElementById(
        "intelPane"
    ).innerHTML = `

        <p>
        Trustpilot Risk:
        High
        </p>

        <p>
        Recent complaints:
        Slow support,
        refund delays
        </p>

    `;
}

async function approveDraft(){

    await fetch(
        `${API}/drafts/${currentEmailId}/approve`,
        {
            method:"POST"
        }
    );

    alert(
        "Draft Approved"
    );
}


loadWorkspace();