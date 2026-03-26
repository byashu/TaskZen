document.addEventListener('DOMContentLoaded', function () {
    const bridge = document.getElementById('summary-data-bridge');
    
    if (bridge) {
        const completedCount = Number(bridge.getAttribute('data-completed')) || 0;
        const pendingCount = Number(bridge.getAttribute('data-pending')) || 0;

        const canvas = document.getElementById('summaryChart');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Completed', 'Pending'],
                    datasets: [{
                        label: 'Tasks',
                        data: [completedCount, pendingCount],
                        backgroundColor: ['#198754', '#ffc107'],
                        borderRadius: 8,
                        barThickness: 50
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: { beginAtZero: true, ticks: { stepSize: 1 } }
                    }
                }
            });
        }
    }
});