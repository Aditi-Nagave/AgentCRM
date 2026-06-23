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

    if(currentEmailId){

        await loadRAG(
            currentEmailId
        );

        await loadMarket();
    }
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
                ${highlightEntities(email.body)}
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

        email.draft_reply ||

        email.draft ||

        "Thank you for contacting us. We are reviewing your request.";
}

async function loadContact(){

    const res =
        await fetch(
            `${API}/contacts/${email}`
        );

    const data =
        await res.json();

    if(!data){

        document.getElementById(
            "contactPane"
        ).innerHTML = `
            <p>No Contact Found</p>
        `;

        return;
    }

    document.getElementById(
        "contactPane"
    ).innerHTML = `
        <p><b>Email:</b> ${data.email || email}</p>
        <p><b>Name:</b> ${data.name || "N/A"}</p>
        <p><b>Company:</b> ${data.company || "N/A"}</p>
        <p><b>Status:</b> ${data.status || "Unknown"}</p>
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

    if(!logs.length){

    html =
    "<p>No Agent Activity Found</p>";
}

    logs.forEach(log => {

        (log.reasoning_trace || []).forEach(step => {

            html += `

             <details class="agent-step">

              <summary>${step.action}</summary>
              <p>Thought:${step.thought}</p>
              <p>Observation:${step.observation}</p>
              <p>Next:${step.next_step}</p>
            </details>
        `;
        });
    });

    document.getElementById(
        "agentPane"
    ).innerHTML = html;

}

async function loadRAG(
    emailId
){

    const results =
    await apiGet(
        `/workspace/rag/${emailId}`
    )

    if(results.error_code){

        document.getElementById(
            "ragPane"
        ).innerHTML =
        `<p>No RAG Context Found</p>`;

        return;
    }

    let html = ""

    results.forEach(item=>{

        html += `

        <div class="rag-card">

            <b>
                ${item.source}
            </b>

            <p>
                Score:
                ${item.similarity_score}
            </p>

            <p>
                ${item.chunk}
            </p>

        </div>

        `
    })

    document
    .getElementById(
        "ragPane"
    )
    .innerHTML = html
}

async function loadMarket(){

    const result =
    await apiGet(
        "/intelligence/reputation?company=SenAI"
    )

    const intel =
    result.market_intelligence

    document
    .getElementById(
        "intelPane"
    )
    .innerHTML = `

        <div class="intel-card">

            <h4>
                Market Summary
            </h4>

            <pre>

${JSON.stringify(
    intel.summary,
    null,
    2
)}

            </pre>

        </div>

    `
}

async function saveDraft(){

    const draft =
        document.getElementById(
            "draftText"
        ).value;

    const res =
        await fetch(
            `${API}/drafts/${currentEmailId}`,
            {
                method:"PATCH",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({
                    draft:draft
                })
            }
        );

    const data =
        await res.json();

    alert(
        data.status ||
        "Draft Saved"
    );
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


function renderWorkspaceAudit(
    audit
){

    let html = "";

    audit.forEach(item => {

        html += `

        <div>

            ${item.action}

        </div>

        `;
    });

    console.log(
        "Audit Logs:",
        audit
    );
}


function highlightEntities(
    text
){

    text = text.replace(

        /(ORD-\d+)/g,

        `<span class="entity order">
            $1
        </span>`
    )

    text = text.replace(

        /(\$[\d,]+)/g,

        `<span class="entity money">
            $1
        </span>`
    )

    text = text.replace(

        /(\d{1,2}\/\d{1,2}\/\d{4})/g,

        `<span class="entity deadline">
            $1
        </span>`
    )

    return text
}