function toggleForm(formType) {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('forgot-password-form').classList.add('hidden');
    document.getElementById(formType).classList.remove('hidden');
}
