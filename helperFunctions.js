// This is a simple helper function that lets you download a generated JSON file.
// In the filename parameter, you type in the file name obviously, but in the
// dataObj parameter, you pass in the json file that you want!
export function downloadJSON(filename, dataObj) {
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

// This reads a JSON file and parses it out. You can use a function like this for your quiz webstite! Make sure you use this in an event handler tho!
function sampleFileReader(event) {
  const file = event.target.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const rawContent = e.target.result;

      // In this case you dont need a try and catch block!

      try {
        // 1. Parse the string into a real JavaScript Object
        const jsonObject = JSON.parse(rawContent);

        // 2. Convert it back to a string with "Pretty Printing"
        // The '2' argument adds 2 spaces of indentation per level
        const prettyString = JSON.stringify(jsonObject, null, 2);

        outputDiv.textContent = prettyString;
      } catch (error) {
        // If the file wasn't valid JSON, show an error
        outputDiv.textContent =
          "Error: The file is not valid JSON.\n\n" + error.message;
        outputDiv.style.color = "red"; // Make text red for errors
      }
    };

    reader.readAsText(file);
  }
}
