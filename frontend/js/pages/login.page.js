import { login } from '../services/auth.service.js';
import { showNotification } from '../utils/notification.js';
import { redirectTo } from '../utils/redirect.js';

const form = document.querySelector('#login-form');

form.addEventListener('submit', async e => {
    e.preventDefault();

    const loginValue = form.login.value;
    const password = form.password.value;

    try {
        await login(loginValue, password);
        redirectTo('main.html');
    } catch (err) {
        showNotification(err.message || 'Authorization failed', 'error');
    }
});