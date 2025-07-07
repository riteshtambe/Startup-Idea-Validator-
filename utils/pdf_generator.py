from fpdf import FPDF
from agents.enhanced_agents import (
    deep_market_analysis, monetization_strategy, go_to_market_strategy,
    feasibility_check, target_audience, funding_readiness,
    pitch_content_creator, lean_canvas_generator,
    real_startup_examples, investor_suggestions
)


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
    pdf.multi_cell(0, 10, "Deep Market Analysis")
    pdf.multi_cell(0, 10, deep_market_analysis(idea))

    pdf.multi_cell(0, 10, "Monetization Strategy")
    pdf.multi_cell(0, 10, monetization_strategy(idea))

    pdf.multi_cell(0, 10, "Go-To-Market Strategy")
    pdf.multi_cell(0, 10, go_to_market_strategy(idea))

    pdf.multi_cell(0, 10, "Feasibility Check")
    pdf.multi_cell(0, 10, feasibility_check(idea))

    pdf.multi_cell(0, 10, "Target Audience")
    pdf.multi_cell(0, 10, target_audience(idea))

    pdf.multi_cell(0, 10, "Funding Readiness")
    pdf.multi_cell(0, 10, funding_readiness(idea))

    pdf.multi_cell(0, 10, "Pitch Content")
    pdf.multi_cell(0, 10, pitch_content_creator(idea))

    pdf.multi_cell(0, 10, "Lean Canvas")
    pdf.multi_cell(0, 10, lean_canvas_generator(idea))

    pdf.multi_cell(0, 10, "Real Startup Examples")
    pdf.multi_cell(0, 10, real_startup_examples(idea))

    pdf.multi_cell(0, 10, "Investor Suggestions")
    pdf.multi_cell(0, 10, investor_suggestions(idea))


    return pdf.output(dest='S').encode('latin-1')
