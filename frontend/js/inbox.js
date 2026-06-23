// frontend/js/inbox.js
let allEmails = [];

async function loadEmails() {

    const emails =
        await apiGet(
            "/emails"
        );

    if (emails.error) {

        alert(emails.error);

        return;
    }

    allEmails = emails;

    renderEmails(
        allEmails
    );
}

function renderEmails(
    emails
) {

    let html = "";

    emails.forEach(email => {

        html += `

        <div class="email-card">

            <div class="email-header">

                <div>

                    <div class="email-subject">

                        ${email.subject || ""}

                    </div>

                    <div>

                        ${email.sender || ""}

                    </div>

                </div>

                <div>

                    <span class="badge badge-${(email.sentiment || "neutral").toLowerCase()}">

                        ${email.sentiment || "Neutral"}

                    </span>

                </div>

            </div>

            <p>

                ${(email.body || "").substring(0, 200)}

            </p>

            <div class="email-footer">

                <span class="badge badge-${(email.urgency || "low").toLowerCase()}">

                    ${email.urgency || "Low"}

                </span>

                <span>

                    ${email.category || "Other"}

                </span>

                <button
                    class="btn btn-primary"
                    onclick="openThread('${email.sender}')">

                    Open Thread

                </button>

                <button
                    class="btn btn-danger"
                    onclick="markSpam(${email.id})">

                    Spam

                </button>

            </div>

        </div>

        `;
    });

    document.getElementById(
        "emailList"
    ).innerHTML = html;
}

function openThread(
    sender
) {

    window.location =
        `thread.html?email=${sender}`;
}

async function markSpam(
    id
) {

    alert(
        `Spam Flagged: ${id}`
    );

    // Future API integration example:
    /*
    const result =
        await apiPatch(
            `/emails/${id}/spam`,
            {
                category: "Spam"
            }
        );

    console.log(result);
    */
}

document
.getElementById(
    "searchInput"
)
.addEventListener(
    "keyup",
    function () {

        const query =
            this.value.toLowerCase();

        const filtered =
            allEmails.filter(
                email =>

                    (email.subject || "")
                        .toLowerCase()
                        .includes(query)

                    ||

                    (email.body || "")
                        .toLowerCase()
                        .includes(query)

                    ||

                    (email.sender || "")
                        .toLowerCase()
                        .includes(query)

                    ||

                    (email.category || "")
                        .toLowerCase()
                        .includes(query)
            );

        renderEmails(
            filtered
        );
    }
);

loadEmails();