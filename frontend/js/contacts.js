// frontend/js/contacts.js
async function getContact() {

    const email =
        document.getElementById(
            "contactEmail"
        ).value;

    const data =
        await getData(
            `/contacts/${email}`
        );

    if (!data) {

        document.getElementById(
            "contactResult"
        ).innerHTML =
        "Contact not found";

        return;
    }

    document.getElementById(
        "contactResult"
    ).innerHTML = `
        <div class="result-card">

            <h3>
                ${data.name || ""}
            </h3>

            <p>
                ${data.company || ""}
            </p>

            <p>
                ${data.status || ""}
            </p>

            <p>
                Account Value:
                ${data.account_value || 0}
            </p>

        </div>
    `;
}