// frontend/js/search.js
function searchEmails() {

    const query =
    document
    .getElementById(
        "searchInput"
    )
    .value
    .toLowerCase()
    .trim();

    if (!query) {

        renderEmails(
            allEmails
        );

        return;
    }

    const filtered =
    allEmails.filter(email => {

        return (

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

    });

    renderEmails(
        filtered
    );
}

document
.getElementById(
    "searchInput"
)
.addEventListener(
    "keyup",
    searchEmails
);