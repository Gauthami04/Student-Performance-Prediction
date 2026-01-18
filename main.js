function showSection(id) {
    document.querySelectorAll(".section").forEach(section => {
        section.classList.remove("active");
    });
    document.getElementById(id).classList.add("active");
}

function toggleSidebarAndDashboard() {
    const sidebar = document.getElementById("sidebar");

    // toggle sidebar open / close
    sidebar.classList.toggle("closed");

    // open dashboard
    showSection("dashboard");
}

/* dummy functions if not created yet */
function saveData() {
    alert("Data saved (demo)");
}

function logout() {
    alert("Logged out");
}
function openDashboard() {
    window.location.href = "dashboard.html";
}
