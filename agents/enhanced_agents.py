from utils.model_utils import call_llm

def deep_market_analysis(idea):
    prompt = f"""You are a startup analyst. Given the startup idea:
\"\"\"{idea}\"\"\"

Perform a Deep Market Analysis:
- Estimate Total Addressable Market (TAM)
- Estimate Serviceable Available Market (SAM)
- Estimate Serviceable Obtainable Market (SOM)
- Identify key market trends
- Provide growth potential insights"""
    return call_llm(prompt)

def monetization_strategy(idea):
    prompt = f"""Suggest 3 viable monetization strategies for this startup:
\"\"\"{idea}\"\"\"

Explain each in 1-2 lines."""
    return call_llm(prompt)

def go_to_market_strategy(idea):
    prompt = f"""Create a Go-To-Market Strategy for the startup idea:
\"\"\"{idea}\"\"\"

Include:
- Target channels (ads, partnerships, etc.)
- Early customer acquisition tactics
- Brand positioning"""
    return call_llm(prompt)

def feasibility_check(idea):
    prompt = f"""Assess the technical and market feasibility of this startup idea:
\"\"\"{idea}\"\"\"

Include:
- Tech readiness
- Regulatory barriers (if any)
- Cost challenges
- Required team expertise"""
    return call_llm(prompt)

def target_audience(idea):
    prompt = f"""Define the ideal customer segment for this startup:
\"\"\"{idea}\"\"\"

Include:
- Demographics
- Behaviors
- Needs
- B2B/B2C classification"""
    return call_llm(prompt)

def funding_readiness(idea):
    prompt = f"""Evaluate what funding stage this startup is suitable for:
\"\"\"{idea}\"\"\"

Return:
- Suggested funding stage (idea, pre-seed, seed, series A...)
- Why
- Tips to prepare for it"""
    return call_llm(prompt)

def pitch_content_creator(idea):
    prompt = f"""Write the following for the startup idea:
\"\"\"{idea}\"\"\"

Return:
- 1-line tagline
- 30-second elevator pitch
- Vision statement"""
    return call_llm(prompt)

def lean_canvas_generator(idea):
    prompt = f"""Generate a Lean Canvas for the startup idea:
\"\"\"{idea}\"\"\"

Include:
- Problem
- Customer Segment
- Unique Value Proposition
- Solution
- Channels
- Revenue Streams
- Cost Structure
- Key Metrics
- Unfair Advantage"""
    return call_llm(prompt)

def real_startup_examples(idea):
    prompt = f"""List 3 real-world startups related to the following idea:
\"\"\"{idea}\"\"\"

For each:
- Name
- Website (if known)
- Similarity with idea"""
    return call_llm(prompt)

def investor_suggestions(idea):
    prompt = f"""Suggest potential investor types for this startup idea:
\"\"\"{idea}\"\"\"

Include:
- Angel investors
- VCs
- Government or grants
- What kind of pitch to give"""
    return call_llm(prompt)
