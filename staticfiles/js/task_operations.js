document.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.getElementById('due');

    // 1. Prevent selecting past dates for tasks
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }

    // 2. Character counter for Description
    const descTextarea = document.getElementById('desc');
    if (descTextarea) {
        descTextarea.addEventListener('input', function () {
            if (this.value.length > 500) {
                alert("Description is too long (Max 500 chars)");
                this.value = this.value.substring(0, 500);
            }
        });
    }
});