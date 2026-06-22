// frontend/js/emails.js
async function loadEmails() {

    const data =
        await getData(
            "/emails"
        );

    let html = "";

    data.forEach(email => {

        html += `
        <div class="result-card">

            <h3>
                ${email.subject}
            </h3>

            <p>
                ${email.sender}
            </p>

            <p>
                ${email.category}
            </p>

            <p>
                ${email.urgency}
            </p>

            <button
                onclick="viewThread(
                    '${email.sender}'
                )"
            >
                View Thread
            </button>

        </div>
        `;
    });

    document.getElementById(
        "emailResults"
    ).innerHTML = html;
}

function viewThread(email) {

    window.location =
        `thread.html?email=${email}`;
}