document.addEventListener('DOMContentLoaded', () => {
    const deleteBtn = document.querySelector('.btn-delete');
    const completeBtn = document.querySelector('.btn-complete');

    // 1. Delete Confirmation
    if (deleteBtn) {
        deleteBtn.addEventListener('click', (e) => {
            if (!confirm("Are you sure you want to delete this task permanently?")) {
                e.preventDefault();
            } else {
                // In Django, you'd typically redirect to the delete URL
                const taskId = window.location.pathname.split('/')[2];
                window.location.href = `/delete/${taskId}/`;
            }
        });
    }

    // 2. Mark Done Visual Feedback
    if (completeBtn) {
        completeBtn.addEventListener('click', function () {
            alert("Task marked as completed!");
            this.style.background = "grey";
            this.innerText = "Completed";
            this.disabled = true;
        });
    }
});