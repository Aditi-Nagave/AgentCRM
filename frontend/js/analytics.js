// frontend/js/analytics.js
async function loadSentimentTrend(){

    const sender =
    "angry@test.com"

    const data =
    await apiGet(
        `/analytics/sentiment-trend?sender=${sender}`
    )

    if(
        data.error
    ){
        return
    }

    const labels = []

    const values = []

    data.forEach(item=>{

        labels.push(
            item.date ||
            item.timestamp
        )

        values.push(
            item.score ||
            item.sentiment_score
        )

    })

    createSentimentChart(
        labels,
        values
    )
}

async function loadCategoryBreakdown(){

    const data =
    await apiGet(
        "/analytics/category-breakdown"
    )

    if(
        data.error
    ){
        return
    }

    const labels = []
    const values = []

    Object.entries(data)
.forEach(([category,count])=>{

    labels.push(category)

    values.push(count)

})

    createCategoryChart(
        labels,
        values
    )
}

async function loadRiskAccounts(){

    const emails =
    await apiGet(
        "/emails"
    )

    let html = ""

    emails.forEach(email=>{

        if(
            email.sentiment ===
            "Negative"
        ){

            html += `

            <div class="risk-card">

                <b>
                    ${email.sender}
                </b>

                <p>
                    ${email.subject}
                </p>

            </div>

            `
        }

    })

    document
    .getElementById(
        "riskAccounts"
    )
    .innerHTML = html
}

async function loadAgentMetrics(){

    const stats =
    await apiGet(
        "/dashboard/stats"
    )

    document
    .getElementById(
        "agentMetrics"
    )
    .innerHTML = `

        <div class="metric">

            Total Emails:

            ${stats.total_emails}

        </div>

        <div class="metric">

            Critical:

            ${stats.critical}

        </div>

        <div class="metric">

            Spam:

            ${stats.spam}

        </div>

        <div class="metric">

            Security:

            ${stats.security}

        </div>

    `
}

loadSentimentTrend()

loadCategoryBreakdown()

loadRiskAccounts()

loadAgentMetrics()


async function loadHeatmap(){

    const data =
    await apiGet(
        "/analytics/response-heatmap"
    )

    createHeatmapChart(

        Object.keys(data),

        Object.values(data)
    )
}

loadHeatmap()