# app.py
import streamlit as st
from agents.swot_agent import generate_swot
from agents.competitor_agent import generate_competitors
from agents.persona_agent import generate_persona_and_mvp
from utils.model_utils import call_llm
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="Startup Idea Validator \U0001f4bc", layout="centered")
st.title("\U0001f4bc Startup Idea Validator")
st.markdown("Enter your startup idea below and receive a complete validation report using AI-powered agents! \U0001f916")

idea = st.text_area("Enter your startup idea:", height=200)

if st.button("Validate My Idea \U0001f680") and idea:
    with st.spinner("Running agentic workflow..."):
        industry_summary = call_llm(f"Describe the industry and market potential for: {idea}")
        competitors = generate_competitors(idea)
        swot = generate_swot(idea)
        persona_mvp = generate_persona_and_mvp(idea)

        st.subheader("\U0001f4c8 Industry Overview")
        st.write(industry_summary)

        st.subheader("\U0001f465 Competitors")
        st.write(competitors)

        st.subheader("\U0001f6e0 SWOT Analysis")
        st.write(swot)

        st.subheader("\U0001f4a1 MVP & Target Persona")
        st.write(persona_mvp)

        pdf_bytes = generate_pdf(idea, industry_summary, competitors, swot, persona_mvp)
        st.download_button("Download Report as PDF \U0001f4c4", pdf_bytes, file_name="Startup_Validation_Report.pdf", mime="application/pdf")
