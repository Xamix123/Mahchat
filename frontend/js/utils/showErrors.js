export function showErrors(errors) {

    for (const key in errors) {

        const el = document.getElementById(key)

        el.classList.add("input-error")

        console.log(errors[key])
    }
}