# app.py
import streamlit as st
from agents.swot_agent import generate_swot
from agents.competitor_agent import generate_competitors
from agents.persona_agent import generate_persona_and_mvp
from utils.model_utils import call_llm
from utils.pdf_generator import generate_pdf
from agents.enhanced_agents import (
    deep_market_analysis, monetization_strategy, go_to_market_strategy,
    feasibility_check, target_audience, funding_readiness,
    pitch_content_creator, lean_canvas_generator,
    real_startup_examples, investor_suggestions
)


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
        deep_m_a = deep_market_analysis(idea) 
        mont_str = monetization_strategy(idea)
        go_to_m_s = go_to_market_strategy(idea)
        fes_chk = feasibility_check(idea)
        tgt_aud = target_audience(idea)
        fund_read = funding_readiness(idea)
        pitch_con_creator = pitch_content_creator(idea)
        lean_can_gene = lean_canvas_generator(idea)
        real_start_exam = real_startup_examples(idea)
        investor_sugg = investor_suggestions(idea)


        st.subheader(" Industry Overview")
        st.write(industry_summary)

        st.subheader("Competitors")
        st.write(competitors)

        st.subheader("SWOT Analysis")
        st.write(swot)

        st.subheader("MVP & Target Persona") 
        st.write(persona_mvp)

        st.subheader("Deep Market Analysis")
        st.write(deep_market_analysis(deep_m_a))

        st.subheader("Monetization Strategy")
        st.write(monetization_strategy(mont_str))

        st.subheader("Go-To-Market Strategy")
        st.write(go_to_market_strategy(go_to_m_s))

        st.subheader("Feasibility Check")
        st.write(feasibility_check(fes_chk))

        st.subheader("Target Audience")
        st.write(target_audience(tgt_aud))

        st.subheader("Funding Readiness")
        st.write(funding_readiness(fund_read))

        st.subheader("Pitch Content")
        st.write(pitch_content_creator(pitch_con_creator))

        st.subheader("Lean Canvas")
        st.write(lean_canvas_generator(lean_can_gene))

        st.subheader("Real Startup Examples")
        st.write(real_startup_examples(real_start_exam))

        st.subheader("Investor Suggestions")
        st.write(investor_suggestions(investor_sugg))
        

        pdf_bytes = generate_pdf(idea, industry_summary, competitors, swot, persona_mvp)
        pdf_bytes = generate_pdf(deep_m_a,mont_str,go_to_m_s,fes_chk,tgt_aud,fund_read)
        pdf_bytes = generate_pdf(pitch_con_creator,lean_can_gene,real_start_exam,investor_sugg)
        pdf_bytes = generate_pdf(fund_read) 
        st.download_button("Download Report as PDF ", pdf_bytes, file_name="Startup_Validation_Report.pdf", mime="application/pdf")
