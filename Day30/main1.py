from fpdf import FPDF

# Dictionary of role-specific roadmaps
ROLE_ROADMAPS = {
    "Data Analyst": """3-Month Roadmap:
---------------------
Month 1:
- Master advanced Excel functions and pivot tables.
- Practice writing SQL queries for data extraction and aggregation.

Month 2:
- Build interactive dashboards in Power BI.
- Complete a data cleaning project using Python (pandas).

Month 3:
- Work on a case study combining Excel, SQL, and Power BI.
- Prepare a presentation to showcase your analysis.""",

    "Data Scientist": """3-Month Roadmap:
---------------------
Month 1:
- Study supervised and unsupervised algorithms with scikit-learn.
- Review core statistics: probability, regression, distributions.

Month 2:
- Build a machine learning model using scikit-learn.
- Learn neural networks basics and experiment with simple deep learning.

Month 3:
- Complete an end-to-end data science project.
- Document your workflow and prepare to present your findings.""",

    "Data Engineer": """3-Month Roadmap:
---------------------
Month 1:
- Learn ETL concepts and create sample pipelines using SQL.
- Study cloud storage options like S3, BigQuery, or Azure Blob.

Month 2:
- Practice building data warehousing solutions.
- Explore Apache Spark for big data processing.

Month 3:
- Design and document a data engineering architecture.
- Set up a small cloud-based data pipeline as a project.""",

    "Machine Learning Engineer": """3-Month Roadmap:
---------------------
Month 1:
- Study end-to-end ML pipeline concepts in Python.
- Learn TensorFlow or PyTorch basics.

Month 2:
- Build and train a deep learning model.
- Explore model deployment with Flask or FastAPI.

Month 3:
- Containerize your model using Docker.
- Deploy your project and write documentation.""",

    "Cloud Engineer": """3-Month Roadmap:
---------------------
Month 1:
- Learn the basics of AWS/GCP/Azure services: compute, storage, IAM.
- Review Linux command-line and scripting.

Month 2:
- Practice Docker containerization for sample applications.
- Study CI/CD pipelines and automated deployments.

Month 3:
- Build a cloud infrastructure project combining compute, storage, and Docker.
- Set up a CI/CD workflow for deployments.""",

    "Backend Developer": """3-Month Roadmap:
---------------------
Month 1:
- Practice Python or Node.js for server-side development.
- Learn Django or Express fundamentals.

Month 2:
- Design REST APIs and practice CRUD operations.
- Explore authentication methods like OAuth2 and JWT.

Month 3:
- Build a full-stack backend project.
- Document your API endpoints and deploy your app.""",

    "Frontend Developer": """3-Month Roadmap:
---------------------
Month 1:
- Master HTML/CSS and responsive design principles.
- Practice JavaScript fundamentals.

Month 2:
- Learn React or Angular for building SPAs.
- Study state management with Redux or Context API.

Month 3:
- Build a frontend project and write tests with Jest or Cypress.
- Improve accessibility and performance.""",

    "Cybersecurity Analyst": """3-Month Roadmap:
---------------------
Month 1:
- Study network protocols like TCP/IP, HTTP, and DNS.
- Practice using security tools such as Wireshark and Nmap.

Month 2:
- Learn Linux hardening techniques and automate log analysis with Python.
- Explore threat detection using SIEM systems.

Month 3:
- Complete a security assessment project.
- Document findings and remediation steps.""",

    "UI/UX Designer": """3-Month Roadmap:
---------------------
Month 1:
- Practice wireframing and prototyping in Figma or XD.
- Study design systems and their importance.

Month 2:
- Conduct user testing and analyze feedback.
- Learn accessibility standards (WCAG).

Month 3:
- Build a complete design portfolio project.
- Refine UX writing and microcopy clarity.""",

    "Product Manager": """3-Month Roadmap:
---------------------
Month 1:
- Study Agile/Scrum frameworks and ceremonies.
- Practice creating basic wireframes.

Month 2:
- Learn stakeholder management techniques.
- Use analytics tools like GA or Mixpanel to gather insights.

Month 3:
- Develop a product roadmap and presentation.
- Prepare for cross-functional collaboration scenarios."""
}

# Helper function for suggestions
def get_suggestion_message(rating):
    if 1 <= rating <= 3:
        return "A lot of improvement is needed but nothing is impossible."
    elif 4 <= rating <= 7:
        return "You are almost there... Just need a little more practice."
    elif 8 <= rating <= 10:
        return "Woohoo! You're almost a legend here. You are all good to go but remember, there's always room for improvement."
    else:
        return "Invalid rating."

# The main function to generate the PDF
def generate_pdf_report(user_data):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "SKILL GAP ROADMAP", ln=True, align="C")

    # User info
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"NAME: {user_data['name']}", ln=True)
    pdf.cell(0, 10, f"STATUS: {user_data['status']}", ln=True)
    pdf.cell(0, 10, f"ASPIRING ROLE: {user_data['aspiring_role']}", ln=True)

    # Table headers
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(60, 10, "Skill", border=1)
    pdf.cell(20, 10, "Self", border=1)
    pdf.cell(20, 10, "Target", border=1)
    pdf.cell(20, 10, "Gap", border=1)
    pdf.cell(70, 10, "Suggestion", border=1)
    pdf.ln()

    # Table rows
    pdf.set_font("Arial", "", 12)
    for skill, rating in user_data["skills"].items():
        target = 8
        gap = max(0, target - rating)
        suggestion = get_suggestion_message(rating)

        x_left = pdf.get_x()
        y_top = pdf.get_y()

        # Measure suggestion height
        pdf.set_xy(x_left + 120, y_top)
        pdf.multi_cell(70, 10, suggestion, border=1)
        y_after = pdf.get_y()
        row_height = y_after - y_top

        # Reset cursor
        pdf.set_xy(x_left, y_top)
        pdf.cell(60, row_height, skill, border=1)
        pdf.cell(20, row_height, str(rating), border=1)
        pdf.cell(20, row_height, str(target), border=1)
        pdf.cell(20, row_height, str(gap), border=1)

        pdf.set_y(y_top + row_height)

    # Summary
    avg_rating = sum(user_data["skills"].values()) / len(user_data["skills"])
    skills_below_target = [s for s, r in user_data["skills"].items() if r < 8]
    skills_at_or_above = [s for s, r in user_data["skills"].items() if r >= 8]

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Overall summary and recommendations", ln=True)

    focus_text = ", ".join(skills_below_target) if skills_below_target else "all skills"

    pdf.set_font("Arial", "", 12)
    summary_text = (
        "Summary of skills:\n"
        f"- Average self-rating: {avg_rating:.2f}\n"
        f"- Skills below target: {len(skills_below_target)} ({', '.join(skills_below_target) if skills_below_target else 'None'})\n"
        f"- Skills at or above target: {len(skills_at_or_above)} ({', '.join(skills_at_or_above) if skills_at_or_above else 'None'})\n\n"
        "Recommended next steps:\n"
        f"- Focus on improving {focus_text} first.\n"
        "- Complete at least 2 practice projects in these areas within the next month.\n"
        "- Re-assess your skill levels after completing these steps."
    )
    pdf.multi_cell(0, 8, summary_text)

    # Personalized roadmap
    role = user_data.get("aspiring_role")
    roadmap_text = ROLE_ROADMAPS.get(role, "No roadmap available for this role.")

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Personalized 3-Month Roadmap:", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, roadmap_text)

    # Footer
    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 10, "Generated by Skill Gap Analyzer v1.0", ln=True, align="C")

    # Output
    pdf.output("Skill_Roadmap_Test.pdf")

# Example user data
sample_user = {
    "name": "Surya",
    "status": "Working professional",
    "aspiring_role": "Data Scientist",
    "skills": {
        "Python (Pandas/Numpy etc)": 6,
        "Machine Learning (Scikit-learn)": 1,
        "Statistics": 5,
        "Deep Learning": 9
    }
}

# Generate
generate_pdf_report(sample_user)

print("PDF generated successfully! Check 'Skill_Roadmap_Test.pdf'.")
