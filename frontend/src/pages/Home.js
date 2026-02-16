import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="container">
      <h1 className="hero-title">YOUR CONTENT MATTERS.</h1>

      <p className="hero-text">
        In the crowded world of social media, standing out is everything.
        Upload PDFs or images and get instant engagement insights,
        hashtag suggestions, and improvement tips.
      </p>

      <button className="primary-btn" onClick={() => navigate("/analyze")}>
        START ANALYZING
      </button>

      <div className="feature-boxes">
        <div className="feature-card">
          <h3>PDF ANALYSIS</h3>
          <p>Extract and analyze text from PDF documents.</p>
        </div>

        <div className="feature-card">
          <h3>IMAGE OCR</h3>
          <p>Read text from images using OCR technology.</p>
        </div>

        <div className="feature-card">
          <h3>RULE-BASED AI</h3>
          <p>Get engagement score, hashtags and improvement tips instantly.</p>
        </div>
      </div>
    </div>
  );
}

export default Home;