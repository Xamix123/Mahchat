import { register } from '../services/auth.service.js';
import { showNotification } from '../utils/notification.js';
import { validateRegister } from '../utils/validators/registerValidator.js'
import { showErrors } from '../utils/showErrors.js'

const form = document.querySelector('#register-form');

form.addEventListener('submit', async e => {
     e.preventDefault()

    const data = {
        login: document.getElementById("login").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
        password_confirmation: document.getElementById("password_confirmation").value
    }

    const errors = validateRegister(data)

    if (Object.keys(errors).length > 0) {
        showErrors(errors)

        return
    }

    try {
        await register(data);
        showNotification('Registration successful. You can now log in.', 'success');
    } catch (err) {
        showNotification('Registration error', 'error');
    }
});