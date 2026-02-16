import { useState } from "react";

function Analyze() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data.analysis);
    } catch (error) {
      alert("Backend not running!");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1 className="page-title">ANALYZE CONTENT</h1>

      <div className="upload-box">
        <input
          type="file"
          accept=".pdf,image/*"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </div>

      <button className="primary-btn" onClick={handleUpload}>
        {loading ? "Analyzing..." : "ANALYZE NOW"}
      </button>

      {result && (
        <div className="result-box">
          <h2>Engagement Score: {result.engagement_score}%</h2>

          <h3>Summary</h3>
          <p>{result.summary}</p>

          <h3>Improvements</h3>
          <ul>
            {result.improvements.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>

          <h3>Suggested Hashtags</h3>
          <div className="hashtags">
            {result.hashtags.map((tag, i) => (
              <span key={i} className="tag">{tag}</span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default Analyze;