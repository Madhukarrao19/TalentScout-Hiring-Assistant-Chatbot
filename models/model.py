from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Use Meta's LLaMA 2 model (requires access)
model_name = "meta-llama/Llama-2-7b-chat-hf"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Use float16 for memory efficiency
    device_map="auto"  # Automatically assigns GPU/CPU
)