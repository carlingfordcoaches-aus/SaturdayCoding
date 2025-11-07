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
