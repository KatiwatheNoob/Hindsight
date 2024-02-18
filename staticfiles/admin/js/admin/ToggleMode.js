function toggleDarkMode() {
    const styleSheet = document.getElementById("styleSheet");
    if (styleSheet.getAttribute("href") === "styles.css") {
        styleSheet.setAttribute("href", "dark-mode.css");
        document.body.classList.add("dark-mode");
        localStorage.setItem("theme", "dark");
    } else {
        styleSheet.setAttribute("href", "styles.css");
        document.body.classList.remove("dark-mode");
        localStorage.setItem("theme", "light");
    }
}

// Check for user's preferred theme in localStorage (if set)
const savedTheme = localStorage.getItem("theme");
if (savedTheme === "dark") {
    toggleDarkMode();
}
