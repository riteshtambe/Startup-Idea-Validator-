from utils.model_utils import call_llm

def generate_swot(idea):
    prompt = f"""
You are a business analyst. Perform a SWOT analysis for this startup idea:

\"\"\"{idea}\"\"\"

Format:
Strengths:
- ...
Weaknesses:
- ...
Opportunities:
- ...
Threats:
- ...
"""
    return call_llm(prompt)
