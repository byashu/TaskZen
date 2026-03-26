document.addEventListener('DOMContentLoaded', function () {
    // 1. Grab the bridge element that holds the data from Django
    const bridge = document.getElementById('summary-data-bridge');
    
    if (bridge) {
        // 2. Convert string attributes to Numbers, defaulting to 0 if empty
        const completedCount = Number(bridge.getAttribute('data-completed')) || 0;
        const pendingCount = Number(bridge.getAttribute('data-pending')) || 0;

        const canvas = document.getElementById('summaryChart');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            
            // 3. Initialize the Chart
            new Chart(ctx, {
                type: 'bar', // Professional bar chart for presentation
                data: {
                    labels: ['Completed', 'Pending'],
                    datasets: [{
                        label: 'Tasks Count',
                        data: [completedCount, pendingCount],
                        backgroundColor: ['#198754', '#ffc107'], // Success Green and Warning Yellow
                        borderRadius: 8,
                        barThickness: 50
                    }]
                },
                options: {
                    responsive: true,
                    // STOP CHART EXPANSION: This forces the chart to stay inside the container height
                    maintainAspectRatio: false, 
                    scales: {
                        y: { 
                            beginAtZero: true, 
                            ticks: { 
                                stepSize: 1 // Ensures we don't show "0.5 tasks"
                            } 
                        }
                    },
                    plugins: {
                        legend: {
                            display: false // Cleaner look for a single dataset
                        }
                    }
                }
            });
        }
    }
});