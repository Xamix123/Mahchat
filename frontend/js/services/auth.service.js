import { saveToken } from '../utils/storage.js';

/* стоит посмотреть можно ли url вынести в какую нить конфигурацию */
export async function login(email, password, checker) {
    const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password, checker}),
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
        throw new Error(data.detail || data.message || 'Login failed');
    }

    if (data.token) {
        saveToken(data.token);
    }

    return data;
}

export async function register(formData) {
    const response = await fetch('http://localhost:8000/registation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });

    if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        throw new Error(error.message || 'Login failed');
    }


    return response.json();
}