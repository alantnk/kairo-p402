function toggleForm(formType) {
    document.getElementById('login-form').classList.add('d-none');
    document.getElementById('forgot-password-form').classList.add('d-none');
    document.getElementById(formType).classList.remove('d-none');
}
