// frontend/js/dashboard.js
async function loadDashboard() {

    const response =
    await fetch(
      `${API_BASE}/dashboard/stats`
    );

    const data =
    await response.json();

    document.getElementById(
        "totalEmails"
    ).innerText =
    data.total_emails;

    document.getElementById(
        "spamEmails"
    ).innerText =
    data.spam;

    document.getElementById(
        "criticalEmails"
    ).innerText =
    data.critical;

    document.getElementById(
        "securityEmails"
    ).innerText =
    data.security;
}

loadDashboard();