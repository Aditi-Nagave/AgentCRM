// frontend/js/contacts.js
async function loadContact(){

    const email =
    document
    .getElementById(
        "contactEmail"
    )
    .value

    if(!email){

        alert(
            "Enter Email"
        )

        return
    }

    const contact =
    await apiGet(
        `/contacts/${email}`
    )

    if(
        contact.error
    ){

        alert(
            contact.error
        )

        return
    }

    renderContact(
        contact
    )
}

function renderContact(
    contact
){

    document
    .getElementById(
        "contactResult"
    )
    .innerHTML = `

    <div class="card">

        <h2>
            Contact Profile
        </h2>

        <p>

            <b>Name:</b>

            ${contact.name || ""}

        </p>

        <p>

            <b>Email:</b>

            ${contact.email || ""}

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

        <br>

        <select
            id="newStatus">

            <option>
                Active
            </option>

            <option>
                VIP
            </option>

            <option>
                Blocked
            </option>

            <option>
                Churned
            </option>

        </select>

        <button
            class="btn btn-primary"
            onclick="updateStatus(
                '${contact.email}'
            )">

            Update Status

        </button>

    </div>

    `
}

async function updateStatus(
    email
){

    const status =
    document
    .getElementById(
        "newStatus"
    )
    .value

    const result =
    await apiPatch(

        `/contacts/${email}/status`,

        {
            status:status
        }
    )

    alert(
        JSON.stringify(
            result
        )
    )
}