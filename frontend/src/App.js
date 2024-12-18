import { useState } from "react";

function App() {
  const [docFile, setDocFile] = useState(null);
  const [jobBookNumber, setJobBookNumber] = useState("");
  const [message, setMessage] = useState()

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!docFile || !jobBookNumber) {
      setMessage("Please provide a file and job book number.");
      return;
    }

    const jobNumber = jobBookNumber.replace(/[-_]/g, "");

    if (isNaN(jobNumber)) {
      setMessage("Please insert a valid job book format.");
      return;
    } else {
      if (jobNumber.length !== 10 && jobNumber.length !== 12) {
        setMessage("Job book number must have 10 or 12 digits.");
        return;
      }
    }

    const formData = new FormData();
    formData.append("doc_file", docFile);
    formData.append("job_book_number", jobNumber);

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      // const result = await response.json();
      if (response.ok) {

        // Handle download zip
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'output_' + jobBookNumber + '.zip'; // Name of the downloaded file
        a.click();
        window.URL.revokeObjectURL(url);
        setMessage("File processed succesfully. Download started.");
      } else {
        const result = await response.json();
        setMessage(result.error || "An error occurred.");
      }
    } catch (error) {
      setMessage("An error occurred. Please try again.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Data Generator - Creative Spark</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="doc_file">Upload project info file:</label>
          <input
            type="file"
            accept=".doc,.docx"
            name="doc_file"
            onChange={(e) => setDocFile(e.target.files[0])}
            required
          />
        </div>
        <div>
          <label htmlFor="job-book-number">Job book number:</label>
          <input
            type="text"
            value={jobBookNumber}
            id="job-book-number"
            name="job_book_number"
            onChange={(e) => setJobBookNumber(e.target.value)}
            required
          />
        </div>
        <button type="submit">Generate</button>
      </form>
      <p>{message}</p>
    </div>
  );
}

export default App;