// frontend/js/analytics.js
async function loadAnalytics() {

    const email =
    document.getElementById(
        "senderEmail"
    ).value;

    const response =
    await fetch(
       `${API_BASE}/analytics/sentiment-trend?sender=${email}`
    );

    const data =
    await response.json();

    document.getElementById(
       "analyticsResult"
    ).innerHTML =
    JSON.stringify(
        data,
        null,
        2
    );
}