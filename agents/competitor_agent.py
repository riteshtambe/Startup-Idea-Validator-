from utils.model_utils import call_llm

def generate_competitors(idea):
    prompt = f"""
Identify 3 notable competitors or similar startups for the following idea:

\"\"\"{idea}\"\"\"

For each, provide:
- Name
- What they do
- How they are different
"""
    return call_llm(prompt)
