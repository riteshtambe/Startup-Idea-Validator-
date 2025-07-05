from utils.model_utils import call_llm

def generate_persona_and_mvp(idea):
    prompt = f"""
For the startup idea below, generate:

1. Ideal customer persona (age, profession, pain point)
2. Suggested MVP features (3-5 features)

Startup Idea:
\"\"\"{idea}\"\"\"
"""
    return call_llm(prompt)
