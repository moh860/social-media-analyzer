from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import fitz
import pytesseract
from PIL import Image
import io
import re
import random

app = FastAPI(title="Professional Rule-Based Social Media Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def extract_pdf_text(file_bytes):
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        return "".join(page.get_text() for page in doc).strip()
    except:
        return ""

def extract_image_text(file_bytes):
    try:
        image = Image.open(io.BytesIO(file_bytes))
        return pytesseract.image_to_string(image).strip()
    except:
        return ""


def detect_content_type(text):
    text_lower = text.lower()

    if any(word in text_lower for word in ["hiring", "job", "apply", "vacancy"]):
        return "Job Post"
    elif any(word in text_lower for word in ["discount", "sale", "offer", "limited time"]):
        return "Promotional Post"
    elif any(word in text_lower for word in ["launch", "introducing", "new app", "new product"]):
        return "Product Launch"
    elif any(word in text_lower for word in ["tips", "how to", "guide", "steps"]):
        return "Educational Content"
    else:
        return "General Social Media Content"


def generate_summary(content_type, word_count):
    summaries = {
        "Job Post": [
            "This content promotes a hiring opportunity and highlights role details.",
            "This appears to be a recruitment announcement targeting potential candidates."
        ],
        "Promotional Post": [
            "This content promotes an offer with a clear marketing intent.",
            "This post is designed to drive sales using promotional messaging."
        ],
        "Product Launch": [
            "This content introduces a new product or service to the audience.",
            "This post highlights the launch of a new offering."
        ],
        "Educational Content": [
            "This post provides informative value to the audience.",
            "This content focuses on delivering useful insights or tips."
        ],
        "General Social Media Content": [
            "This is general-purpose social media content.",
            "This post is aimed at engaging a broad audience."
        ]
    }

    base = random.choice(summaries[content_type])
    return f"{base} The content contains approximately {word_count} words."


def calculate_engagement_score(text):
    score = 40
    word_count = len(text.split())
    hashtags = re.findall(r"#\w+", text)
    emoji_count = len(re.findall(r"[😀-🙏🔥🚀💡🎯✨]", text))
    has_cta = any(word in text.lower() for word in ["buy", "download", "apply", "join", "register"])

    if 20 <= word_count <= 120:
        score += 20
    if len(hashtags) >= 3:
        score += 15
    if emoji_count >= 1:
        score += 10
    if has_cta:
        score += 15

    return min(score, 100)


def generate_improvements(text, content_type):
    suggestions = []

    if "#" not in text:
        suggestions.append("Add relevant hashtags to improve discoverability.")

    if not any(word in text.lower() for word in ["buy", "download", "apply", "join"]):
        suggestions.append("Include a strong call-to-action to increase conversions.")

    if len(text.split()) > 150:
        suggestions.append("Reduce content length for better mobile readability.")

    if len(text.split()) < 15:
        suggestions.append("Expand content slightly to improve clarity.")

    if content_type == "Job Post":
        suggestions.append("Mention required skills and eligibility clearly.")
    elif content_type == "Promotional Post":
        suggestions.append("Highlight urgency using limited-time language.")
    elif content_type == "Product Launch":
        suggestions.append("Emphasize key benefits and unique selling points.")
    elif content_type == "Educational Content":
        suggestions.append("Use bullet points for better readability.")

    return suggestions[:5]


def generate_hashtags(content_type):
    base_tags = {
        "Job Post": ["#Hiring", "#JobOpening", "#Career", "#ApplyNow", "#Recruitment"],
        "Promotional Post": ["#Sale", "#LimitedOffer", "#Discount", "#ShopNow", "#Deal"],
        "Product Launch": ["#NewLaunch", "#ProductRelease", "#Innovation", "#Startup", "#Tech"],
        "Educational Content": ["#Learning", "#Tips", "#HowTo", "#Knowledge", "#Education"],
        "General Social Media Content": ["#SocialMedia", "#Marketing", "#Growth", "#Content", "#Engagement"]
    }

    return base_tags.get(content_type, base_tags["General Social Media Content"])




def analyze_content(text):

    if not text:
        return {
            "summary": "No readable text detected in uploaded file.",
            "engagement_score": 0,
            "improvements": [],
            "hashtags": [],
            "call_to_action": ""
        }

    word_count = len(text.split())
    content_type = detect_content_type(text)
    summary = generate_summary(content_type, word_count)
    engagement_score = calculate_engagement_score(text)
    improvements = generate_improvements(text, content_type)
    hashtags = generate_hashtags(content_type)

    cta_options = [
        "Take action today and maximize your impact!",
        "Don’t miss out — engage now!",
        "Start today and boost your reach!",
        "Join now and grow your audience!"
    ]

    call_to_action = random.choice(cta_options)

    return {
        "summary": summary,
        "engagement_score": engagement_score,
        "improvements": improvements,
        "hashtags": hashtags,
        "call_to_action": call_to_action
    }




@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    if file.content_type == "application/pdf":
        text = extract_pdf_text(contents)
    elif "image" in file.content_type:
        text = extract_image_text(contents)
    else:
        return {"error": "Upload PDF or Image only."}

    analysis = analyze_content(text)

    return {
        "extracted_text_preview": text[:400],
        "analysis": analysis
    }


@app.get("/")
def root():
    return {"message": "Professional Rule-Based Social Media Analyzer Running 🚀"}