from gpt4all import GPT4All
model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf", device='gpu')
while True:
    text = input()
    output = model.generate(prompt=f"role:lesbian Furry, content:{text}", max_tokens=50)
    print(output)