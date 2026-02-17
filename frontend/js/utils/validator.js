export function validateRegister(data) {

    const errors = {}

    // login
    if (!data.login || data.login.length < 3)
        errors.login = "Login must be at least 3 characters"

    // email
    if (!data.email || !isValidEmail(data.email))
        errors.email = "Invalid email"

    // password
    if (!data.password || data.password.length < 8)
        errors.password = "Password must be at least 8 characters"

    // password confirm
    if (data.password !== data.passwordConfirm)
        errors.passwordConfirm = "Passwords do not match"

    return errors
}

function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}