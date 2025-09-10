//show/hide password toggle
document.addEventListener("DOMContentLoaded", () => {
    const passwordInput = document.querySelector("#id_password");
    const toggle = document.createElement("span");

    toggle.textContent = "👁️";
    toggle.style.cursor = "pointer";
    toggle.style.marginLeft = "-30px";
    toggle.style.position = "relative";
    toggle.style.zIndex = "2";

    if (passwordInput) {
        passwordInput.parentElement.style.position = "relative";
        passwordInput.after(toggle);

        toggle.addEventListener("click", () => {
            const type = passwordInput.type === "password" ? "text" : "password";
            passwordInput.type = type;
        });
    }
});
