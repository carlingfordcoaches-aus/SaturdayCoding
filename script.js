const jsonFIle = document.getElementById("AddJSONFileInput");


const newFileInputWrapper = document.createElement('div');

const label = document.createElement('label');
const uniqueId = 'fileInput_' + date.Now();
label.setAttribute ('for', uniqueId);
label.textContext = 'Choose File: ';

const FileInput  = document.createElement('input');
  fileInput.setAttribute('type', 'file');
  fileInput.setAttribute('id', uniqueId);
  fileInput.setAttribute('name', 'uploadedFile[]');

  newFileInputWrapper.appendChild(label);
  newFileInputWrapper.appendChild(fileInput);

  document.getElementById('fileInputsContainer').appendChild(newFileInputWrapper);

// Show a message when the button is clicked
const clickTheButton = document.getElementById("upload JSON file")
const clickButton = document.getElementById("clickButton");
const message = document.getElementById("message");
const click = document.getElementById("takeToPage");

click.addEventListener("click", () => {
  message.textContent = "playPage"
  });

clickButton.addEventListener("click", () => {
  message.textContent = "🎉 You clicked the button! Great job!";
});

click.addEventListener("click", () => {
  message.textContent = "Start page";
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
