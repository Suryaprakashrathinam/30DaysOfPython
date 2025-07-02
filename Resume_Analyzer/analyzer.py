import re

# ✅ Clean the resume text
def clean_text(raw_text):
    raw_text = raw_text.lower()
    raw_text = re.sub(r"[^a-z0-9\s.,;:()/\u2013\-/]", "", raw_text)  # keep / and – (en dash)
    raw_text = re.sub(r"\s+", " ", raw_text).strip()
    return raw_text

# ✅ Split into logical sections (optional for scoring)
def split_into_sections(cleaned_text):
    section_patterns = {
        'summary': r'(summary|profile|objective)',
        'skills': r'(skills|technical skills)',
        'education': r'(education|academic background)',
        'work_experience': r'(work experience|professional experience)',
        'certifications': r'(certifications|licenses|awards)'
    }

    section_positions = {}
    for key, pattern in section_patterns.items():
        match = re.search(rf'{pattern}\s*[:\-]', cleaned_text, re.IGNORECASE)
        if match:
            section_positions[key] = match.start()

    sorted_sections = sorted(section_positions.items(), key=lambda x: x[1])
    sections = {}

    for i, (section, start) in enumerate(sorted_sections):
        end = sorted_sections[i + 1][1] if i + 1 < len(sorted_sections) else len(cleaned_text)
        sections[section] = cleaned_text[start:end].strip()

    return sections

# ✅ Analyze cleaned resume vs job description
def analyze_against_jd(cleaned_resume, job_description):
    job_description = job_description.lower()
    resume_text = cleaned_resume.lower()

    # 🎯 Valid skills list (lowercase comparison used)
    valid_skills = {
        "excel", "sql", "mysql", "postgresql", "sqlite", "mongodb", "power bi", "tableau", "looker",
        "superset", "aws", "azure", "gcp", "databricks", "snowflake", "bigquery", "google sheets",
        "python", "r", "sas", "julia", "shell", "bash", "java", "scala", "javascript",
        "pandas", "numpy", "matplotlib", "seaborn", "plotly", "scikit-learn", "tensorflow", "keras",
        "pytorch", "statsmodels", "xgboost", "lightgbm", "nltk", "spacy", "opencv", "pyspark",
        "beautifulsoup", "requests", "fastapi", "flask",
        "data cleaning", "data preprocessing", "data wrangling", "data mining", "data visualization",
        "data modeling", "feature engineering", "feature selection", "dimensionality reduction", "data structures",
        "eda", "etl", "elt", "dashboarding", "a/b testing", "data pipelines", "data governance", "data quality",
        "data lake", "data warehouse", "machine learning", "supervised learning", "unsupervised learning",
        "reinforcement learning", "regression", "classification", "clustering", "decision trees", "random forest",
        "svm", "neural networks", "deep learning", "nlp", "time series", "forecasting", "recommendation system",
        "model deployment", "hyperparameter tuning", "model evaluation", "cross validation",
        "business intelligence", "storytelling", "communication", "problem solving", "presentation", "agile",
        "scrum", "jira", "business acumen", "critical thinking", "stakeholder management", "collaboration"
    }

    # ✅ Extract JD keywords and filter with valid skills
    jd_keywords = set(re.findall(r'\b[a-z]{3,}\b', job_description))  # only words with 3+ chars
    keywords = [kw for kw in jd_keywords if kw in valid_skills]

    # ✅ Match keywords in resume
    matched_keywords = [kw for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', resume_text)]
    keyword_score = int((len(matched_keywords) / len(keywords)) * 100) if keywords else 0

    # ✅ Formatting score based on sections
    section_count = len(re.findall(r'(summary|skills|education|work experience|certifications)', resume_text))
    format_score = min(section_count / 5 * 100, 100)

    # ✅ Combine for overall score
    overall_score = int((keyword_score * 0.6) + (format_score * 0.4))

    # ✅ Missing keywords
    missing_keywords = sorted(set(keywords) - set(matched_keywords))

    # ✅ Suggestions
    suggestions = []
    if missing_keywords:
        suggestions.append("Add missing keywords: " + ", ".join(missing_keywords))
    if section_count < 3:
        suggestions.append("Add more resume sections (e.g., Skills, Work Experience).")

    # ✅ Return final report
    return {
        "keyword_score": keyword_score,
        "format_score": format_score,
        "overall_score": overall_score,
        "missing_keywords": missing_keywords,
        "suggestions": suggestions
    }
