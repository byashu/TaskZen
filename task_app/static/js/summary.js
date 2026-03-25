document.addEventListener('DOMContentLoaded', function () {
    // 1. Find the bridge element
    const bridge = document.getElementById('summary-data-bridge');
    
    if (bridge) {
        // 2. Get the values safely from HTML attributes
        const completedCount = Number(bridge.getAttribute('data-completed')) || 0;
        const pendingCount = Number(bridge.getAttribute('data-pending')) || 0;

        // 3. Setup the Bar Chart
        const ctx = document.getElementById('summaryChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Completed', 'Pending'],
                datasets: [{
                    label: 'Number of Tasks',
                    data: [completedCount, pendingCount],
                    backgroundColor: ['#198754', '#ffc107'],
                    borderRadius: 8,
                    barThickness: 60
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { stepSize: 1 }
                    }
                }
            }
        });
    }
});