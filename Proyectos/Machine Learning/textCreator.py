from transformers import pipeline, set_seed

set_seed(42)

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

input_text = "Genera un texto que"

output = generator(input_text, max_length=50, num_return_sequences=1)

print("Texto generado:")
for result in output:
    print(result["generated_text"])
