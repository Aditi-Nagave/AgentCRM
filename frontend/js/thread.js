// frontend/js/thread.js
const params =
    new URLSearchParams(
        window.location.search
    );

const email =
    params.get("email");

async function loadThread() {

    const data =
        await getData(
            `/threads/${email}`
        );

    let html = "";

    data.forEach(item => {

        html += `
        <div class="result-card">

            <h3>
                ${item.subject}
            </h3>

            <p>
                ${item.body}
            </p>

            <p>
                Sentiment:
                ${item.sentiment}
            </p>

            <p>
                Urgency:
                ${item.urgency}
            </p>

        </div>
        `;
    });

    document.getElementById(
        "threadData"
    ).innerHTML = html;
}

loadThread();