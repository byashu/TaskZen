document.addEventListener('DOMContentLoaded', () => {
    const authForm = document.querySelector('form');

    // 1. Simple validation to ensure passwords match in Registration
    if (authForm) {
        authForm.addEventListener('submit', (e) => {
            const password = document.querySelector('input[placeholder="Enter password"]')?.value;
            const confirmPassword = document.querySelector('input[placeholder="Confirm password"]')?.value;

            if (confirmPassword && password !== confirmPassword) {
                alert("Passwords do not match!");
                e.preventDefault();
            }
        });
    }
});