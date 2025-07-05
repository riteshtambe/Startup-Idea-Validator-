from fpdf import FPDF

def generate_pdf(idea, industry, competitors, swot, persona):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Startup Idea Validation Report", ln=True)

    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"Idea: {idea}\n")
    pdf.multi_cell(0, 10, f"Industry & Market Overview:\n{industry}\n")
    pdf.multi_cell(0, 10, f"Competitor Overview:\n{competitors}\n")
    pdf.multi_cell(0, 10, f"SWOT Analysis:\n{swot}\n")
    pdf.multi_cell(0, 10, f"Persona & MVP Suggestions:\n{persona}\n")

    return pdf.output(dest='S').encode('latin-1')
