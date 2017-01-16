$(document).ready(function() {
    $.ajax({
        async: true,
        url:        "./charts_alumnos.json",
        dataType:   "json", // <== JSON-P request
        method: "GET",
        success:    function(datasets) {
            for (var i = 0; i < datasets.length; i++) {

                chart = document.getElementById("alumnos_chart_" + (i+1));
                var data = {
                    labels: ["NP/SC", "1", "2", "3", "4", "5"],
                    datasets: [datasets[i]]
                };

                var c = new Chart(chart, {
                    type: 'bar',
                    data: data,
                    options: {
                         legend: {
                            display: false
                         },
                         scales: {
                            yAxes: [{
                                display: true,
                                ticks: {
                                    beginAtZero: true   // minimum value will be 0.
                                }
                            }]
                        }
                     }
                });
            }
        }
    });
    $.ajax({
        async: true,
        url:        "./charts_profesores.json",
        dataType:   "json", // <== JSON-P request
        method: "GET",
        success:    function(datasets) {
            for (var i = 0; i < datasets.length; i++) {

                chart = document.getElementById("profesores_chart_" + (i+1));
                var data = {
                    labels: ["NP/SC", "1", "2", "3", "4", "5"],
                    datasets: [datasets[i]]
                };
                var c = new Chart(chart, {
                    type: 'bar',
                    data: data,
                    options: {
                         legend: {
                            display: false
                         },
                         scales: {
                            yAxes: [{
                                display: true,
                                ticks: {
                                    beginAtZero: true   // minimum value will be 0.
                                }
                            }]
                        }
                     }
                });
            }
        }
    });
});

