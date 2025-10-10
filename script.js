// Show a message when the button is clicked
const clickButton = document.getElementById("clickButton");
const message = document.getElementById("message");

clickButton.addEventListener("click", () => {
  message.textContent = "🎉 You clicked the button! Great job!";
});

// === Contact Form Logic ===
const contactForm = document.getElementById("contactForm");
const nameInput = document.getElementById("nameInput");
const messageInput = document.getElementById("messageInput");
const feedback = document.getElementById("formFeedback");

contactForm.addEventListener("submit", (event) => {
  event.preventDefault(); // stop page reload

  const name = nameInput.value.trim();
  const msg = messageInput.value.trim();

  // This checks to see if they have anything in the text fields

  if (name === "" || msg === "") {
    feedback.textContent = "⚠️ Please fill in both fields.";
    feedback.style.color = "red";
  } else {
    feedback.textContent = `✅ Thanks, ${name}! Your message has been sent.`;
    feedback.style.color = "green";
    contactForm.reset();
  }
});
