const apiUrl = "https://backend-x-nine.vercel.app/api" // Adjust if necessary

// Handle OTP Request
const sendOtpBtn = document.getElementById("sendOtp")
if (sendOtpBtn) {
  sendOtpBtn.addEventListener("click", async () => {
    const email = document.getElementById("email").value

    if (!email) {
      alert("Please enter a valid email.")
      return
    }

    const res = await fetch(`${apiUrl}/send-otp`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    })

    const data = await res.json()
    if (res.ok) {
      alert(data.message)
      document.getElementById("otp-section").style.display = "block"
    } else {
      alert("Error sending OTP: " + data.error)
    }
  })
}

// Handle OTP Verification
const verifyOtpBtn = document.getElementById("verifyOtp")
if (verifyOtpBtn) {
  verifyOtpBtn.addEventListener("click", async () => {
    const email = document.getElementById("email").value
    const otp = document.getElementById("otp").value

    if (!otp) {
      alert("Please enter the OTP sent to your email.")
      return
    }

    const res = await fetch(`${apiUrl}/verify-otp`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, otp }),
    })

    const data = await res.json()
    if (res.ok) {
      alert("OTP Verified! You can now register.")
      document.getElementById("password").disabled = false
      document.getElementById("registerBtn").disabled = false
    } else {
      alert("Invalid OTP! Please try again.")
    }
  })
}

// Handle Registration After OTP Verification
const registerForm = document.getElementById("registerForm")
if (registerForm) {
  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault()
    const username = document.getElementById("username").value
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    if (document.getElementById("password").disabled) {
      alert("Please verify OTP before registering.")
      return
    }

    const res = await fetch(`${apiUrl}/auth/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password }),
    })

    const data = await res.json()
    if (res.ok) {
      localStorage.setItem("token", data.token)

      // Fetch user details after registration
      fetch(`${apiUrl}/auth/user`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${data.token}`,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((userData) => {
          localStorage.setItem("username", userData.username)
          window.location.href = "dashboard.html"
        })
        .catch((error) => console.error("Error fetching user details:", error))
    } else {
      alert(data.message || "Registration failed")
    }
  })
}

// Handle Login
const loginForm = document.getElementById("loginForm")
if (loginForm) {
  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault()
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const res = await fetch(`${apiUrl}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    })

    const data = await res.json()
    if (res.ok) {
      localStorage.setItem("token", data.token)

      // Fetch user details after login
      fetch(`${apiUrl}/auth/user`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${data.token}`,
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((userData) => {
          localStorage.setItem("username", userData.username)
          window.location.href = "dashboard.html"
        })
        .catch((error) => console.error("Error fetching user details:", error))
    } else {
      alert(data.message || "Login failed")
    }
  })
}

// Check if user is logged in and display username
document.addEventListener("DOMContentLoaded", () => {
  const username = localStorage.getItem("username")
  if (username) {
    const usernameSpan = document.getElementById("username")
    if (usernameSpan) {
      usernameSpan.textContent = username
    }
  }
})

