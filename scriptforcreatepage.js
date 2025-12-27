function downloadJSON(filename, dataObj) {
  const jsonStr = JSON.stringify(dataObj, null, 2);

  // Create a Blob with JSON MIME type
  const blob = new Blob([jsonStr], { type: "application/json" });

  // Create a temporary URL
  const url = URL.createObjectURL(blob);

  // Create a temporary <a> to trigger download
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;

  // Append, click, remove
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);

  // Cleanup
  URL.revokeObjectURL(url);
}

const button = document.getElementById("submit");

button.addEventListener("click", () => {
  const questions = [
    {
      question: document.getElementById("question1").value,
      answer: document.getElementById("answer1").value,
    },
    {
      question: document.getElementById("question2").value,
      answer: document.getElementById("answer2").value,
    },
  ];
  downloadJSON("jsonFile.json", questions);
});
