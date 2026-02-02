import { login } from '../services/auth.service.js';
import { showNotification } from '../utils/notification.js';
import { redirectTo } from '../utils/redirect.js';

const form = document.querySelector('#login-form');

form.addEventListener('submit', async e => {
    e.preventDefault();

    const email = form.email.value;
    const password = form.password.value;
    /* remove this field after finish validation checking */
    const checker = form.checker.checked;

    try {
        await login(email, password, checker);
        redirectTo('main.html');
    } catch (err) {
        showNotification(err.message || 'Authorization failed', 'error');
    }
});