document.addEventListener("DOMContentLoaded", () => {
  // Check for token to handle login state
  const token = localStorage.getItem("token")

  // Redirect from login/register if already logged in
  if (
    (window.location.pathname.endsWith("login.html") || window.location.pathname.endsWith("register.html")) &&
    token
  ) {
    window.location.href = "dashboard.html"
  }

  // Logout functionality
  const logoutBtn = document.getElementById("logoutBtn")
  if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      localStorage.removeItem("token")
      window.location.href = "login.html"
    })
  }
})

