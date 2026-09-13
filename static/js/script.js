// ========================================
// AI PROJECT EVALUATOR
// Theme Toggle
// ========================================

const themeToggle = document.getElementById("theme-toggle");


// Load saved theme
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
}


// Update theme icon
function updateThemeIcon() {
    if (document.body.classList.contains("dark-mode")) {
        themeToggle.textContent = "☀️";
    } else {
        themeToggle.textContent = "🌙";
    }
}


// Set initial icon
updateThemeIcon();


// Toggle theme
themeToggle.addEventListener("click", function () {

    document.body.classList.toggle("dark-mode");

    const isDark = document.body.classList.contains("dark-mode");

    if (isDark) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }

    updateThemeIcon();
});