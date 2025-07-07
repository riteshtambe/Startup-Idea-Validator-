from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# Optional: Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def call_llm(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)

    with torch.no_grad():
        output = model.generate(
            inputs["input_ids"],
            max_new_tokens=256,
            temperature=0.9,             # More randomness
            top_p=0.95,                  # Nucleus sampling
            top_k=50,                    # Top-k sampling
            repetition_penalty=1.3,      # Penalize repetition
            no_repeat_ngram_size=3,      # No repeating 3-grams
            do_sample=True               # Use sampling instead of greedy decoding
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)
