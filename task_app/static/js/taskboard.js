document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('.search-box');
    const taskCards = document.querySelectorAll('.col-6.col-md-4'); // Targets the task card columns

    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase();

            taskCards.forEach(column => {
                // Don't filter the "Add Task" card
                if (column.querySelector('.card.add')) return;

                const taskTitle = column.querySelector('h5').innerText.toLowerCase();
                if (taskTitle.includes(searchTerm)) {
                    column.style.display = "block";
                } else {
                    column.style.display = "none";
                }
            });
        });
    }
});