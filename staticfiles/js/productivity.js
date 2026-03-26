document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('chart-data-container');
    
    if (container) {
        // Extracting data from the HTML data-attributes
        const highVal = Number(container.getAttribute('data-high')) || 0;
        const medVal = Number(container.getAttribute('data-medium')) || 0;
        const lowVal = Number(container.getAttribute('data-low')) || 0;

        const ctx = document.getElementById('priorityChart').getContext('2d');
        if (ctx) {
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['High', 'Medium', 'Low'],
                    datasets: [{
                        data: [highVal, medVal, lowVal],
                        backgroundColor: ['#dc3545', '#fd7e14', '#198754'],
                        borderWidth: 0,
                        hoverOffset: 15
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: {
                        legend: { 
                            position: 'bottom', 
                            labels: { padding: 20, font: { size: 14 } } 
                        }
                    }
                }
            });
        }
    } else {
        console.error("Chart data container not found!");
    }
});