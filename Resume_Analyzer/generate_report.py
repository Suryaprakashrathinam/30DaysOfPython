from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import matplotlib.pyplot as plt
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register fonts
pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))

def create_pdf_report(candidate_name, job_role, report_data):
    # === PIE CHART SETUP ===
    total = report_data["keyword_score"] + len(report_data["missing_keywords"])
    matched = int((report_data["keyword_score"] / 100) * total)
    missing = total - matched if total else 0

    labels = ['Matched', 'Missing']
    sizes = [matched, missing]
    pie_colors = ['#00FFF7', '#FF00A8']

    fig, ax = plt.subplots(figsize=(3.5, 3.5), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=pie_colors,
        textprops=dict(color="black", fontsize=10)
    )
    ax.set_title("Keyword Match", color="black", fontsize=12, fontweight='bold')
    pie_path = "pie_chart_v2.png"
    plt.savefig(pie_path, bbox_inches='tight')
    plt.close()

    # === PDF GENERATION ===
    pdf_path = "resume_feedback_report_v2.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    # Set Title
    c.setFont("Arial-Bold", 22)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - 50, "Resume Feedback Report")

    # Candidate Info
    c.setFont("Arial", 12)
    c.drawString(50, height - 90, f"Candidate Name: {candidate_name}")
    c.drawString(50, height - 110, f"Target Role: {job_role}")
    c.drawString(50, height - 130, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Draw Pie Chart (Right side)
    c.drawImage(pie_path, width - 220, height - 300, width=160, preserveAspectRatio=True)

    # Scores Section
    y = height - 170
    c.setFont("Arial-Bold", 14)
    c.drawString(50, y, "Scores")
    y -= 20
    c.setFont("Arial", 12)

    ks = report_data["keyword_score"]
    fs = report_data["format_score"]
    oscore = report_data["overall_score"]

    c.setFillColor(colors.red if ks < 65 else colors.black)
    c.drawString(60, y, f"Keyword Score: {ks}%")
    y -= 20
    c.setFillColor(colors.black)
    c.drawString(60, y, f"Format Score: {fs:.1f}%")
    y -= 20
    c.setFillColor(colors.red if oscore < 65 else colors.black)
    c.drawString(60, y, f"Overall Score: {oscore}%")
    c.setFillColor(colors.black)

    # === MISSING KEYWORDS ===
    y -= 40
    c.setFont("Arial-Bold", 14)
    c.drawString(50, y, "Missing Keywords")
    y -= 20
    c.setFont("Arial", 12)
    for kw in report_data["missing_keywords"]:
        if y < 80:
            c.showPage()
            y = height - 50
        c.drawString(65, y, f"• {kw}")
        y -= 18

    # === SUGGESTIONS ===
    y -= 20
    c.setFont("Arial-Bold", 14)
    c.drawString(50, y, "Suggestions")
    y -= 20
    c.setFont("Arial", 12)
    for s in report_data["suggestions"]:
        if y < 80:
            c.showPage()
            y = height - 50
        c.drawString(65, y, f"- {s}")
        y -= 18
        y -= 18

    c.save()
    print(f"PDF report saved as: {pdf_path}")
    return pdf_path
