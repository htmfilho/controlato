$(document).ready(function () {
    let canvas = $('div.card-columns').find('canvas');

    for (let i = 0;i < canvas.length;i++) {
        let canvasId = canvas[i].id;
        let ctx = document.getElementById(canvasId).getContext('2d');
        let contextId = canvasId.substring(canvasId.lastIndexOf("-") + 1);

        $.get("/contexts/"+ contextId +"/chart", function (data) {
            new Chart(ctx, {
                type: data.chart,
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: data.scale.concat(" - ", data.unit) ,
                        data: data.dataset,
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        xAxes: [{
                            type: 'time',
                            distribution: 'series',
                            time: {
                                unit: data.interval,
                                displayFormats: {
                                    minute: "h:mm a"
                                }
                            },
                            z: 1
                        }]
                    }
                }
            });
        })
    }
});
