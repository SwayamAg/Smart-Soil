// Session management for access control
const PROTECTED_PAGES = ["login.html", "register.html", "dashboard.html", "research.html"]

const PUBLIC_PAGES = ["index.html", "shop.html", "about.html", "contact.html", "subscribe.html"]

// Check if current page requires authentication
function checkPageAccess() {
  const currentPage = window.location.pathname.split("/").pop()

  // If it's a protected page, verify payment
  if (PROTECTED_PAGES.includes(currentPage)) {
    if (!verifyPaymentStatus()) {
      redirectToSubscribe()
      return false
    }
    return true
  }
  return true
}

// Verify payment status
function verifyPaymentStatus() {
  const paymentVerified = localStorage.getItem("paymentVerified")
  const paymentTimestamp = localStorage.getItem("paymentTimestamp")
  const sessionId = localStorage.getItem("sessionId")

  // Check if all required session data exists
  if (!paymentVerified || !paymentTimestamp || !sessionId) {
    return false
  }

  // Check if payment is verified and not expired (1 minute)
  if (paymentVerified === "true" && paymentTimestamp) {
    const now = new Date().getTime()
    const paymentTime = Number.parseInt(paymentTimestamp)
    const minutesSincePayment = (now - paymentTime) / (1000 * 60)

    if (minutesSincePayment < 10) {
      return true
    } else {
      // Payment expired
      clearSession()
      return false
    }
  }
  return false
}

// Clear session data
function clearSession() {
  localStorage.removeItem("paymentVerified")
  localStorage.removeItem("paymentTimestamp")
  localStorage.removeItem("sessionId")
}

// Redirect to subscribe page
function redirectToSubscribe() {
  if (!window.location.pathname.includes("subscribe.html")) {
    window.location.href = "subscribe.html"
  }
}

// Initialize session
function initSession() {
  if (!localStorage.getItem("sessionId")) {
    localStorage.setItem("sessionId", Math.random().toString(36).substring(2, 15))
  }
}

// Run on page load
document.addEventListener("DOMContentLoaded", () => {
  initSession()
  if (!checkPageAccess()) {
    return // Stop further execution if access is denied
  }
})

