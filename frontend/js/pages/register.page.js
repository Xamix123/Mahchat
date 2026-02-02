import { register } from '../services/auth.service.js';
import { showNotification } from '../utils/notification.js';

const form = document.querySelector('#register-form');

form.addEventListener('submit', async e => {
    e.preventDefault();

    const data = {
        nickname: form.nickname.value,
        email: form.email.value,
        password: form.password.value,
        checker: form.checker.checked
    };

    try {
        await register(data);
        showNotification('Registration successful. You can now log in.', 'success');
    } catch (err) {
        showNotification('Registration error', 'error');
    }
});