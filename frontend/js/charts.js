// frontend/js/charts.js

function createSentimentChart(
    labels,
    values
){

    const ctx =
    document
    .getElementById(
        "sentimentChart"
    )

    new Chart(
        ctx,
        {
            type:"line",

            data:{

                labels:labels,

                datasets:[
                    {
                        label:
                        "Sentiment Score",

                        data:values,

                        borderWidth:2,

                        fill:false
                    }
                ]
            },

            options:{
                responsive:true
            }
        }
    )
}

function createCategoryChart(
    labels,
    values
){

    const ctx =
    document
    .getElementById(
        "categoryChart"
    )

    new Chart(
        ctx,
        {
            type:"pie",

            data:{

                labels:labels,

                datasets:[
                    {
                        data:values
                    }
                ]
            },

            options:{
                responsive:true
            }
        }
    )
}


function createHeatmapChart(
    labels,
    values
){

    new Chart(

        document.getElementById(
            "heatmapChart"
        ),

        {

            type:"bar",

            data:{

                labels:labels,

                datasets:[{

                    label:"Emails",

                    data:values

                }]
            }
        }
    )
}