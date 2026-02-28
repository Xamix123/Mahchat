export function showErrors(errors) {
    document.querySelectorAll('.input-error')
        .forEach(el => el.classList.remove('input-error'))

    document.querySelectorAll('.error-message')
        .forEach(el => el.remove())

    for (const key in errors) {
        const el = document.getElementById(key)

        el.classList.add("input-error")

        const message = document.createElement("div")
        message.className = "error-message"
        message.innerText = errors[key]

        el.after(message)
    }
}