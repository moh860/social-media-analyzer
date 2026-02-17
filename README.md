# 📊 Social Media Content Analyzer

A full-stack web application that analyzes social media content from PDFs and images, extracts text using OCR, and provides engagement improvement suggestions using a rule-based evaluation engine.

---

## 🚀 Live Demo

🌐 Frontend (Vercel):  
https://social-media-analyzer-sand.vercel.app

⚙️ Backend API (Render):  
https://social-media-analyzer-yh8b.onrender.com

---

## 📌 Project Overview

Social Media Content Analyzer is a web application designed to:

- Upload PDF documents
- Upload image files (scanned documents)
- Extract text from PDFs using PyMuPDF
- Extract text from images using Tesseract OCR
- Analyze content using rule-based engagement scoring
- Suggest improvements and relevant hashtags
- Provide a clean and modern UI experience

This project was built as part of a Software Engineering technical assessment focusing on practical problem-solving and production-quality implementation.

---

## 🛠 Tech Stack

### Frontend
- React.js
- React Router
- CSS (custom styling)
- Deployed on Vercel

### Backend
- FastAPI
- PyMuPDF (PDF parsing)
- Pytesseract (OCR)
- Pillow
- Uvicorn
- Deployed on Render

---

## 🏗 Architecture Overview

```
User Upload → React Frontend → FastAPI Backend → 
    → PDF Parser (PyMuPDF)
    → OCR Engine (Tesseract)
    → Rule-Based Analyzer
    → Engagement Score + Suggestions
```

---

## ✨ Features

### 1️⃣ Document Upload
- Supports PDF files
- Supports image files (JPG, PNG)
- File picker interface
- Connected to backend API

### 2️⃣ Text Extraction
- PDF Parsing using PyMuPDF
- OCR using Tesseract for scanned images
- Extracted text processed for analysis

### 3️⃣ Engagement Analysis
- Word count analysis
- Content type detection
- Basic engagement scoring logic
- Improvement suggestions
- Suggested hashtags

### 4️⃣ Clean UX
- Navigation (Home, Analyze, About)
- Loading states
- Result card display
- Modern UI design

---
📷 Screenshots



Then reference them like this:
🏠 Home Page
[Home](screenshots/home.png)

### 🔍 Analyze/result Page
[Analyze](screenshots/analyze.png)

---

## 🧪 How to Run Locally

### Backend

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on:
http://127.0.0.1:8000

---

### Frontend

```
cd frontend
npm install
npm start
```

Frontend runs on:
http://localhost:3000

---

## 📂 Project Structure

```
content-analyzer/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── styles.css
│
├── screenshots/
│
├── .gitignore
└── README.md
```

---

## 📊 Evaluation Logic (Rule-Based)

The engagement scoring system evaluates:

- Content length
- Use of call-to-action words
- Hiring or promotional keywords
- Presence of hashtags
- Content clarity indicators

Based on these factors, it generates:
- Engagement score (percentage)
- Summary
- Improvement suggestions
- Recommended hashtags

---

## 🔒 Error Handling

- File type validation
- Empty file checks
- Backend error responses
- CORS configured
- Basic frontend error display

---

## 📈 Future Improvements

- Advanced NLP-based sentiment analysis
- ML-based engagement prediction
- Social media platform optimization
- User authentication
- Save analysis history
- AI-generated caption rewriting

---

## 📝 Approach Summary (200 Words)

This project was designed as a full-stack solution to analyze and improve social media content performance. The backend was implemented using FastAPI due to its speed and simplicity for API development. For PDF parsing, PyMuPDF was used to accurately extract formatted text. For image-based documents, Tesseract OCR (via pytesseract) was integrated to extract textual content from scanned images.

A rule-based engagement engine was developed to simulate practical content evaluation without external AI APIs. The engine evaluates word count, promotional keywords, hiring indicators, and structural clarity to generate an engagement score, improvement suggestions, and relevant hashtags.

The frontend was built using React to ensure a clean, responsive user interface with page navigation and file upload capabilities. The application was deployed using Render (backend) and Vercel (frontend), following a production-ready setup.

The focus of this implementation was clean structure, clear separation of concerns, error handling, and delivering a fully working application within a constrained time frame.

---

## 👨‍💻 Author

Mohan Parashar  
Software Engineering Candidate  

---

## 📜 License

This project was created for technical assessment purposes.