import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
MODEL_NAME = "Qwen/Qwen2.5-Math-1.5B"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

def solve_equation(equation_text):
    # Format the prompt
    prompt = f"Return only the simplified equation. If it cannot be solved, return the equation as is. Equation: {equation_text}"

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    # Generate response
    with torch.no_grad():
        output = model.generate(**inputs, max_length=100)

    # Decode response
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract the answer from the model's response
    if "invalid" in generated_text.lower():
        return -1
    return generated_text.strip()
