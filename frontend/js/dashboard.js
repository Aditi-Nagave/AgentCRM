// frontend/js/dashboard.js
async function loadDashboard() {

    const stats =
        await apiGet(
            "/dashboard/stats"
        );

    if(stats.error){

        alert(stats.error);

        return;
    }

    document.getElementById(
        "totalEmails"
    ).innerText =
    stats.total_emails || 0;

    document.getElementById(
        "criticalEmails"
    ).innerText =
    stats.critical || 0;

    document.getElementById(
        "spamEmails"
    ).innerText =
    stats.spam || 0;

    document.getElementById(
        "securityEmails"
    ).innerText =
    stats.security || 0;
}

loadDashboard();