from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    project_cost,
    debt_ratio,
    interest_rate,
    delay,
    inflation,
    gdp,
    sector,
    country,
    risk,
    confidence
):

    doc = SimpleDocTemplate("Infrastructure_Risk_Report.pdf")
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Infrastructure Finance Risk Report</b>", styles["Title"]))

    story.append(Paragraph(f"Project Cost: {project_cost} Million USD", styles["BodyText"]))
    story.append(Paragraph(f"Debt Ratio: {debt_ratio}", styles["BodyText"]))
    story.append(Paragraph(f"Interest Rate: {interest_rate}%", styles["BodyText"]))
    story.append(Paragraph(f"Construction Delay: {delay} Months", styles["BodyText"]))
    story.append(Paragraph(f"Inflation Rate: {inflation}%", styles["BodyText"]))
    story.append(Paragraph(f"GDP Growth: {gdp}%", styles["BodyText"]))
    story.append(Paragraph(f"Sector: {sector}", styles["BodyText"]))
    story.append(Paragraph(f"Country: {country}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Prediction Result</b>", styles["Heading2"]))

    story.append(Paragraph(f"Predicted Risk: {risk}", styles["BodyText"]))
    story.append(Paragraph(f"Confidence: {confidence:.2f}%", styles["BodyText"]))

    doc.build(story)