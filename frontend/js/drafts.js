// frontend/js/drafts.js
async function saveDraft() {

    const id =
    document.getElementById(
        "emailId"
    ).value;

    const draft =
    document.getElementById(
        "draftText"
    ).value;

    const response =
    await fetch(
        `${API_BASE}/drafts/${id}`,
        {
            method: "PATCH",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
                draft: draft
            })
        }
    );

    const data =
    await response.json();

    document.getElementById(
        "result"
    ).innerText =
    JSON.stringify(data);
}


async function approveDraft() {

    const id =
    document.getElementById(
        "emailId"
    ).value;

    const response =
    await fetch(
        `${API_BASE}/drafts/${id}/approve`,
        {
            method: "POST"
        }
    );

    const data =
    await response.json();

    document.getElementById(
        "result"
    ).innerText =
    JSON.stringify(data);
}