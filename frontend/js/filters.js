// frontend/js/filters.js
function filterEmails(
    filterType
){

    let filtered =
    [...allEmails];

    switch(
        filterType
    ){

        case "Needs Human":

            filtered =
            filtered.filter(
                email =>
                email.requires_human === true
            );

            break;

        case "Escalated":

            filtered =
            filtered.filter(
                email =>
                email.status ===
                "Escalated"
            );

            break;

        case "Spam":

            filtered =
            filtered.filter(
                email =>
                email.category ===
                "Spam"
            );

            break;

        case "Auto-Replied":

            filtered =
            filtered.filter(
                email =>
                email.status ===
                "Replied"
            );

            break;

        default:

            break;
    }

    renderEmails(
        filtered
    );
}

document
.querySelectorAll(
    ".tab"
)
.forEach(tab => {

    tab.addEventListener(
        "click",
        () => {

            document
            .querySelectorAll(
                ".tab"
            )
            .forEach(
                item =>
                item.classList.remove(
                    "active"
                )
            );

            tab.classList.add(
                "active"
            );

            filterEmails(
                tab.innerText.trim()
            );
        }
    );

});


document
.getElementById(
    "sortBy"
)
.addEventListener(
    "change",
    sortEmails
);

function sortEmails(){

    const sortType =
    document
    .getElementById(
        "sortBy"
    )
    .value;

    const emails =
    [...allEmails];

    switch(
        sortType
    ){

        case "urgency":

            emails.sort(
                (
                    a,
                    b
                ) => {

                    const priority = {

                        Critical:4,

                        High:3,

                        Medium:2,

                        Low:1

                    };

                    return (
                        priority[
                            b.urgency
                        ] || 0
                    ) -

                    (
                        priority[
                            a.urgency
                        ] || 0
                    );
                }
            );

            break;

        case "sentiment":

            emails.sort(
                (
                    a,
                    b
                ) =>

                (
                    b.sentiment_score || 0
                )

                -

                (
                    a.sentiment_score || 0
                )
            );

            break;

        case "date":

            emails.sort(
                (
                    a,
                    b
                ) =>

                new Date(
                    b.timestamp
                )

                -

                new Date(
                    a.timestamp
                )
            );

            break;
    }

    renderEmails(
        emails
    );
}