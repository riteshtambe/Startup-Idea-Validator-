from utils.model_utils import call_llm

def generate_competitors(idea):
    prompt = f"""
You are a startup analyst. Identify **3 real or well-known** startups or companies that are similar to this idea:

\"\"\"{idea}\"\"\"

Provide the response in this format:

1. **[Startup Name]**  
   - What they do: ...  
   - Difference from our idea: ...

2. **[Startup Name]**  
   - What they do: ...  
   - Difference from our idea: ...

3. **[Startup Name]**  
   - What they do: ...  
   - Difference from our idea: ...
"""
    return call_llm(prompt)
