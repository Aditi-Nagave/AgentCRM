// frontend/js/polling.js

let pollingInterval =
10000;

let pollingEnabled =
true;

function startPolling(){

    setInterval(
        async () => {

            if(
                !pollingEnabled
            ){

                return;
            }

            console.log(
                "Refreshing Inbox..."
            );

            const emails =
            await apiGet(
                "/emails"
            );

            if(
                !emails.error
            ){

                allEmails =
                emails;

                renderEmails(
                    allEmails
                );
            }

        },

        pollingInterval
    );
}

function stopPolling(){

    pollingEnabled =
    false;
}

function resumePolling(){

    pollingEnabled =
    true;
}

startPolling();